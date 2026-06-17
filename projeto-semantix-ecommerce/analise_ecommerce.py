"""
Projeto de Parceria Semantix — Análise de Dados em E-commerce

Este script realiza a análise exploratória da base ecommerce_estatistica.csv,
tratando os dados, gerando gráficos, arquivos de resultados e uma base tratada
para uso no Looker Studio.

Como executar:
1. Coloque este arquivo na mesma pasta do arquivo ecommerce_estatistica.csv.
2. No terminal, execute:
   python analise_ecommerce.py
3. Os arquivos serão gerados nas pastas resultados/ e imagens/.
"""

from pathlib import Path
import unicodedata
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")


# -----------------------------------------------------------------------------
# 1. Configurações iniciais
# -----------------------------------------------------------------------------

PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_RESULTADOS = PASTA_PROJETO / "resultados"
PASTA_IMAGENS = PASTA_PROJETO / "imagens"

PASTA_RESULTADOS.mkdir(exist_ok=True)
PASTA_IMAGENS.mkdir(exist_ok=True)

POSSIVEIS_ARQUIVOS = [
    PASTA_PROJETO / "ecommerce_estatistica.csv",
    PASTA_PROJETO / "ecommerce_estatistica(2).csv",
]


# -----------------------------------------------------------------------------
# 2. Funções auxiliares
# -----------------------------------------------------------------------------

def localizar_arquivo_csv() -> Path:
    """Localiza o arquivo CSV principal do projeto."""
    for arquivo in POSSIVEIS_ARQUIVOS:
        if arquivo.exists():
            return arquivo

    arquivos_csv = list(PASTA_PROJETO.glob("*.csv"))
    if arquivos_csv:
        return arquivos_csv[0]

    raise FileNotFoundError(
        "Nenhum arquivo CSV foi encontrado. "
        "Coloque o arquivo ecommerce_estatistica.csv na mesma pasta deste script."
    )


def remover_acentos(texto: str) -> str:
    """Remove acentos de uma string."""
    texto_normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(caractere for caractere in texto_normalizado if not unicodedata.combining(caractere))


def padronizar_nome_coluna(nome: str) -> str:
    """Padroniza nomes de colunas para facilitar análises em Python e Looker Studio."""
    nome = remover_acentos(str(nome))
    nome = nome.strip().lower()
    nome = nome.replace(" ", "_")
    nome = nome.replace("/", "_")
    nome = nome.replace("-", "_")
    nome = nome.replace("__", "_")
    return nome


def salvar_grafico(nome_arquivo: str) -> None:
    """Salva o gráfico atual na pasta de imagens."""
    caminho = PASTA_IMAGENS / nome_arquivo
    plt.tight_layout()
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Gráfico salvo: {caminho}")


def confirmar_colunas(df: pd.DataFrame, colunas: list[str]) -> None:
    """Valida se as colunas necessárias existem na base."""
    faltantes = [coluna for coluna in colunas if coluna not in df.columns]
    if faltantes:
        raise KeyError(
            "As seguintes colunas não foram encontradas na base: "
            + ", ".join(faltantes)
            + "\nColunas disponíveis: "
            + ", ".join(df.columns)
        )


# -----------------------------------------------------------------------------
# 3. Leitura da base de dados
# -----------------------------------------------------------------------------

arquivo_csv = localizar_arquivo_csv()
print(f"Arquivo localizado: {arquivo_csv}")

try:
    df = pd.read_csv(arquivo_csv)
except UnicodeDecodeError:
    df = pd.read_csv(arquivo_csv, encoding="latin1")

print("\nPrimeiras linhas da base original:")
print(df.head())

print("\nDimensão da base original:")
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")


# -----------------------------------------------------------------------------
# 4. Padronização e tratamento dos dados
# -----------------------------------------------------------------------------

# Padroniza nomes das colunas.
df.columns = [padronizar_nome_coluna(coluna) for coluna in df.columns]

# Remove coluna de índice criada automaticamente, se existir.
if "unnamed:_0" in df.columns:
    df = df.drop(columns=["unnamed:_0"])

# Padroniza textos em colunas categóricas.
colunas_categoricas = ["marca", "material", "genero", "temporada"]
for coluna in colunas_categoricas:
    if coluna in df.columns:
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.strip()
            .str.lower()
            .replace({"nan": "nao informado", "não definido": "nao definido"})
        )

# Valida colunas essenciais para a análise.
colunas_necessarias = [
    "nota",
    "n_avaliacoes",
    "desconto",
    "marca",
    "material",
    "genero",
    "temporada",
    "preco",
    "qtd_vendidos_cod",
]
confirmar_colunas(df, colunas_necessarias)

# Converte colunas numéricas.
colunas_numericas = ["nota", "n_avaliacoes", "desconto", "preco", "qtd_vendidos_cod"]
for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

# Remove duplicidades.
duplicados_antes = df.duplicated().sum()
df = df.drop_duplicates()

# Trata valores nulos.
# Numéricos: mediana. Categóricos: "nao informado".
for coluna in colunas_numericas:
    df[coluna] = df[coluna].fillna(df[coluna].median())

for coluna in colunas_categoricas:
    if coluna in df.columns:
        df[coluna] = df[coluna].fillna("nao informado")

print("\nTratamento concluído.")
print(f"Duplicados removidos: {duplicados_antes}")
print("Valores nulos após tratamento:")
print(df[colunas_necessarias].isna().sum())


# -----------------------------------------------------------------------------
# 5. Análise descritiva
# -----------------------------------------------------------------------------

indicadores = {
    "total_produtos": len(df),
    "total_vendas_codificado": df["qtd_vendidos_cod"].sum(),
    "preco_medio": df["preco"].mean(),
    "desconto_medio": df["desconto"].mean(),
    "nota_media": df["nota"].mean(),
    "total_avaliacoes": df["n_avaliacoes"].sum(),
}

print("\nIndicadores principais:")
for indicador, valor in indicadores.items():
    print(f"{indicador}: {valor:,.2f}")

indicadores_df = pd.DataFrame(
    list(indicadores.items()), columns=["indicador", "valor"]
)
indicadores_df.to_csv(PASTA_RESULTADOS / "indicadores_principais.csv", index=False, encoding="utf-8-sig")

print("\nEstatísticas descritivas:")
print(df[colunas_numericas].describe())


# -----------------------------------------------------------------------------
# 6. Agrupamentos para análise
# -----------------------------------------------------------------------------

vendas_por_marca = (
    df.groupby("marca", as_index=False)["qtd_vendidos_cod"]
    .sum()
    .sort_values("qtd_vendidos_cod", ascending=False)
)

vendas_por_material = (
    df.groupby("material", as_index=False)["qtd_vendidos_cod"]
    .sum()
    .sort_values("qtd_vendidos_cod", ascending=False)
)

vendas_por_temporada = (
    df.groupby("temporada", as_index=False)["qtd_vendidos_cod"]
    .sum()
    .sort_values("qtd_vendidos_cod", ascending=False)
)

vendas_por_genero = (
    df.groupby("genero", as_index=False)["qtd_vendidos_cod"]
    .sum()
    .sort_values("qtd_vendidos_cod", ascending=False)
)

vendas_por_marca.to_csv(PASTA_RESULTADOS / "vendas_por_marca.csv", index=False, encoding="utf-8-sig")
vendas_por_material.to_csv(PASTA_RESULTADOS / "vendas_por_material.csv", index=False, encoding="utf-8-sig")
vendas_por_temporada.to_csv(PASTA_RESULTADOS / "vendas_por_temporada.csv", index=False, encoding="utf-8-sig")
vendas_por_genero.to_csv(PASTA_RESULTADOS / "vendas_por_genero.csv", index=False, encoding="utf-8-sig")

print("\nTop 10 marcas por quantidade vendida:")
print(vendas_por_marca.head(10))

print("\nTop 10 materiais por quantidade vendida:")
print(vendas_por_material.head(10))


# -----------------------------------------------------------------------------
# 7. Correlação entre variáveis numéricas
# -----------------------------------------------------------------------------

correlacao = df.select_dtypes(include=[np.number]).corr()
correlacoes_com_vendas = (
    correlacao[["qtd_vendidos_cod"]]
    .sort_values("qtd_vendidos_cod", ascending=False)
    .reset_index()
    .rename(columns={"index": "variavel", "qtd_vendidos_cod": "correlacao_com_qtd_vendidos_cod"})
)

correlacao.to_csv(PASTA_RESULTADOS / "matriz_correlacao.csv", encoding="utf-8-sig")
correlacoes_com_vendas.to_csv(PASTA_RESULTADOS / "correlacoes_com_vendas.csv", index=False, encoding="utf-8-sig")

print("\nCorrelação com quantidade vendida codificada:")
print(correlacoes_com_vendas)


# -----------------------------------------------------------------------------
# 8. Visualizações
# -----------------------------------------------------------------------------

# Histograma de preços.
plt.figure(figsize=(10, 5))
plt.hist(df["preco"], bins=20)
plt.title("Distribuição dos preços dos produtos")
plt.xlabel("Preço")
plt.ylabel("Frequência")
salvar_grafico("histograma_precos.png")

# Top 10 marcas.
top_marcas = vendas_por_marca.head(10).sort_values("qtd_vendidos_cod")
plt.figure(figsize=(10, 6))
plt.barh(top_marcas["marca"], top_marcas["qtd_vendidos_cod"])
plt.title("Top 10 marcas por quantidade vendida")
plt.xlabel("Quantidade vendida codificada")
plt.ylabel("Marca")
salvar_grafico("grafico_vendas_marca.png")

# Top 10 materiais.
top_materiais = vendas_por_material.head(10).sort_values("qtd_vendidos_cod")
plt.figure(figsize=(10, 6))
plt.barh(top_materiais["material"], top_materiais["qtd_vendidos_cod"])
plt.title("Top 10 materiais por quantidade vendida")
plt.xlabel("Quantidade vendida codificada")
plt.ylabel("Material")
salvar_grafico("grafico_vendas_material.png")

# Vendas por temporada.
plt.figure(figsize=(10, 5))
plt.bar(vendas_por_temporada["temporada"], vendas_por_temporada["qtd_vendidos_cod"])
plt.title("Quantidade vendida por temporada")
plt.xlabel("Temporada")
plt.ylabel("Quantidade vendida codificada")
plt.xticks(rotation=45, ha="right")
salvar_grafico("grafico_vendas_temporada.png")

# Vendas por gênero.
plt.figure(figsize=(10, 5))
plt.bar(vendas_por_genero["genero"], vendas_por_genero["qtd_vendidos_cod"])
plt.title("Quantidade vendida por gênero")
plt.xlabel("Gênero")
plt.ylabel("Quantidade vendida codificada")
plt.xticks(rotation=45, ha="right")
salvar_grafico("grafico_vendas_genero.png")

# Dispersão preço x vendas.
plt.figure(figsize=(8, 5))
plt.scatter(df["preco"], df["qtd_vendidos_cod"], alpha=0.7)
plt.title("Relação entre preço e quantidade vendida")
plt.xlabel("Preço")
plt.ylabel("Quantidade vendida codificada")
salvar_grafico("grafico_preco_vendas.png")

# Dispersão desconto x vendas.
plt.figure(figsize=(8, 5))
plt.scatter(df["desconto"], df["qtd_vendidos_cod"], alpha=0.7)
plt.title("Relação entre desconto e quantidade vendida")
plt.xlabel("Desconto")
plt.ylabel("Quantidade vendida codificada")
salvar_grafico("grafico_desconto_vendas.png")

# Dispersão avaliações x vendas.
plt.figure(figsize=(8, 5))
plt.scatter(df["n_avaliacoes"], df["qtd_vendidos_cod"], alpha=0.7)
plt.title("Relação entre número de avaliações e quantidade vendida")
plt.xlabel("Número de avaliações")
plt.ylabel("Quantidade vendida codificada")
salvar_grafico("grafico_avaliacoes_vendas.png")

# Mapa de calor de correlação usando matplotlib.
plt.figure(figsize=(12, 8))
plt.imshow(correlacao, aspect="auto")
plt.colorbar(label="Correlação")
plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation=90)
plt.yticks(range(len(correlacao.index)), correlacao.index)
plt.title("Mapa de calor da matriz de correlação")
salvar_grafico("mapa_calor_correlacao.png")


# -----------------------------------------------------------------------------
# 9. Relatório de insights
# -----------------------------------------------------------------------------

maior_marca = vendas_por_marca.iloc[0]["marca"]
maior_material = vendas_por_material.iloc[0]["material"]
maior_temporada = vendas_por_temporada.iloc[0]["temporada"]
maior_genero = vendas_por_genero.iloc[0]["genero"]

corr_preco = df["preco"].corr(df["qtd_vendidos_cod"])
corr_desconto = df["desconto"].corr(df["qtd_vendidos_cod"])
corr_avaliacoes = df["n_avaliacoes"].corr(df["qtd_vendidos_cod"])
corr_nota = df["nota"].corr(df["qtd_vendidos_cod"])

insights = pd.DataFrame(
    {
        "insight": [
            f"A marca com maior quantidade vendida codificada foi {maior_marca}.",
            f"O material com maior quantidade vendida codificada foi {maior_material}.",
            f"A temporada com maior quantidade vendida codificada foi {maior_temporada}.",
            f"O gênero com maior quantidade vendida codificada foi {maior_genero}.",
            f"A correlação entre preço e vendas foi de {corr_preco:.3f}.",
            f"A correlação entre desconto e vendas foi de {corr_desconto:.3f}.",
            f"A correlação entre avaliações e vendas foi de {corr_avaliacoes:.3f}.",
            f"A correlação entre nota e vendas foi de {corr_nota:.3f}.",
        ],
        "sugestao": [
            "Avaliar campanhas, estoque e destaque para marcas com maior desempenho.",
            "Priorizar materiais com maior aceitação comercial.",
            "Planejar campanhas considerando a sazonalidade dos produtos.",
            "Usar a segmentação por gênero para orientar comunicação e sortimento.",
            "Avaliar faixas de preço mais competitivas antes de definir estratégias comerciais.",
            "Analisar se os descontos realmente geram aumento proporcional no volume vendido.",
            "Destacar produtos com maior número de avaliações para aumentar confiança do consumidor.",
            "Monitorar a relação entre qualidade percebida e desempenho comercial.",
        ],
    }
)

insights.to_csv(PASTA_RESULTADOS / "insights_ecommerce.csv", index=False, encoding="utf-8-sig")

print("\nInsights gerados:")
print(insights)


# -----------------------------------------------------------------------------
# 10. Exportação da base tratada
# -----------------------------------------------------------------------------

caminho_base_tratada = PASTA_RESULTADOS / "base_tratada.csv"
df.to_csv(caminho_base_tratada, index=False, encoding="utf-8-sig")

# Também salva uma cópia na raiz do projeto para facilitar o upload no Looker Studio.
df.to_csv(PASTA_PROJETO / "base_tratada.csv", index=False, encoding="utf-8-sig")

print("\nProcesso concluído com sucesso!")
print(f"Base tratada salva em: {caminho_base_tratada}")
print(f"Cópia da base tratada salva em: {PASTA_PROJETO / 'base_tratada.csv'}")
print(f"Arquivos de resultado salvos em: {PASTA_RESULTADOS}")
print(f"Gráficos salvos em: {PASTA_IMAGENS}")

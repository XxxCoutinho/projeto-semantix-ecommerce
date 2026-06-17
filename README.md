# projeto-semantix-ecommerce
Projeto de análise de dados em e-commerce desenvolvido para a parceria Semantix. O objetivo é identificar fatores que influenciam o volume de vendas de produtos, utilizando análise exploratória, tratamento de dados, geração de insights e dashboard no Looker Studio.

# Projeto de Parceria Semantix — Análise de Dados em E-commerce

## 1. Problema escolhido

O problema escolhido para este projeto é a dificuldade que empresas de e-commerce enfrentam para entender quais fatores mais influenciam o volume de vendas de seus produtos.

Em um ambiente digital competitivo, uma loja virtual precisa tomar decisões rápidas sobre preço, desconto, divulgação, estoque, categorias de produtos e relacionamento com o cliente. No entanto, muitas dessas decisões ainda são tomadas com base em intuição ou experiência individual, sem uma análise estruturada dos dados disponíveis.

A problemática central deste projeto é:

**Como identificar os fatores que mais influenciam as vendas de produtos em um e-commerce?**

Essa pergunta é relevante porque o desempenho de vendas pode ser afetado por diferentes variáveis, como preço, desconto aplicado, quantidade de avaliações, nota média dos produtos, marca, material, gênero, temporada e categoria. Ao analisar esses dados, é possível identificar padrões que ajudam a empresa a melhorar sua estratégia comercial.

## 2. Importância do problema

O e-commerce tem grande importância econômica e social, pois permite que empresas vendam produtos para diferentes regiões, ampliem seu alcance e melhorem a experiência dos consumidores. Porém, a grande quantidade de dados gerados diariamente pode se tornar um desafio caso não seja analisada corretamente.

A ausência de análise de dados pode gerar problemas como:

* produtos com bom potencial de venda recebendo pouca atenção;
* aplicação de descontos sem impacto real no volume vendido;
* dificuldade em identificar marcas ou categorias mais rentáveis;
* baixa compreensão sobre o comportamento dos consumidores;
* decisões comerciais baseadas em achismos.

Dessa forma, o uso de dados ajuda a transformar informações brutas em conhecimento útil para o negócio. Com a análise correta, a empresa pode direcionar melhor suas campanhas, ajustar preços, melhorar a exposição de produtos e priorizar itens com maior potencial de venda.

## 3. Como a análise de dados pode ajudar

A análise de dados pode ajudar a solucionar ou mitigar esse problema por meio da identificação de padrões, tendências e relações entre variáveis.

Neste projeto, a análise busca responder perguntas como:

* Quais marcas apresentam maior quantidade de vendas?
* Produtos com desconto vendem mais?
* Existe relação entre preço e quantidade vendida?
* Produtos com mais avaliações apresentam maior volume de vendas?
* A nota média influencia o desempenho comercial?
* Determinados materiais, gêneros ou temporadas possuem melhor desempenho?

Com essas respostas, é possível gerar insights para apoiar decisões estratégicas, como:

* priorizar produtos com maior aceitação;
* ajustar descontos de forma mais eficiente;
* identificar marcas e categorias com melhor desempenho;
* melhorar campanhas promocionais;
* apoiar decisões de estoque e reposição;
* criar dashboards para acompanhamento contínuo dos indicadores.

## 4. Fontes de dados

### 4.1 Base principal utilizada

A base principal utilizada no projeto é o arquivo `ecommerce_estatistica.csv`, contendo informações sobre produtos de e-commerce.

Essa base contém dados estruturados em formato CSV, permitindo análise com ferramentas como Google Planilhas, Python, SQL e Looker Studio.

Principais variáveis utilizadas:

* `Nota`: avaliação média do produto;
* `N_Avaliações`: quantidade de avaliações recebidas;
* `Desconto`: percentual ou valor de desconto aplicado;
* `Preço`: preço do produto;
* `Marca`: marca do produto;
* `Material`: material do produto;
* `Gênero`: público ou categoria do produto;
* `Temporada`: período ou sazonalidade do produto;
* `Qtd_Vendidos_Cod`: quantidade vendida codificada.

### 4.2 Fonte pública de referência

Como fonte pública de referência, foi considerado o dataset Brazilian E-Commerce Public Dataset by Olist, disponível publicamente no Kaggle.

Essa base possui dados reais e anonimizados de pedidos de e-commerce no Brasil, contendo informações sobre pedidos, produtos, vendedores, clientes, pagamentos, frete e avaliações.

Tipo de dados:

* Dados estruturados;
* Arquivos em formato CSV;
* Dados relacionais distribuídos em múltiplas tabelas.

Método de acesso:

* Download direto pela plataforma Kaggle;
* Possibilidade de uso via notebook Python;
* Possibilidade de importação para Google Planilhas, BigQuery ou Looker Studio após tratamento.

## 5. Coleta de dados

A coleta dos dados foi realizada por meio do arquivo CSV utilizado no projeto. O arquivo foi carregado no ambiente de análise para exploração, limpeza e geração de visualizações.

Etapas realizadas:

1. Importação do arquivo CSV no Python;
2. Verificação das colunas disponíveis;
3. Identificação dos tipos de dados;
4. Verificação de valores nulos;
5. Análise de duplicidades;
6. Padronização dos nomes das colunas;
7. Preparação da base para visualização no Looker Studio.

## 6. Modelagem e tratamento dos dados

Durante a etapa de modelagem, os dados foram organizados para facilitar a análise exploratória e a criação do dashboard.

Foram realizadas as seguintes etapas:

* remoção ou tratamento de valores ausentes;
* verificação de inconsistências em campos numéricos;
* padronização de campos categóricos;
* criação de métricas agregadas;
* análise de variáveis como preço, desconto, nota, avaliações e quantidade vendida;
* preparação da base final para visualização.

As principais métricas analisadas foram:

* total de produtos analisados;
* média de preço;
* média de desconto;
* média de nota;
* soma da quantidade vendida;
* quantidade vendida por marca;
* quantidade vendida por material;
* quantidade vendida por temporada;
* relação entre preço e vendas;
* relação entre desconto e vendas;
* relação entre avaliações e vendas.

## 7. Análise exploratória de dados

A análise exploratória foi realizada para compreender o comportamento geral da base.

Foram avaliadas distribuições, tendências e possíveis relações entre as variáveis. A análise buscou identificar quais características estão mais associadas ao aumento ou redução da quantidade vendida.

Principais análises realizadas:

### 7.1 Distribuição dos preços

Foi analisada a distribuição dos preços dos produtos para identificar a presença de produtos mais baratos, intermediários e mais caros.

Essa análise ajuda a compreender a faixa de preço predominante no e-commerce.

### 7.2 Relação entre preço e quantidade vendida

Foi criado um gráfico de dispersão para avaliar se produtos mais baratos tendem a vender mais ou se há produtos de preço elevado com bom desempenho.

### 7.3 Relação entre desconto e vendas

Foi analisado se produtos com maiores descontos apresentam aumento relevante na quantidade vendida.

Essa análise é importante para avaliar se os descontos realmente contribuem para o crescimento das vendas ou se estão sendo aplicados sem retorno proporcional.

### 7.4 Relação entre avaliações e vendas

Foi verificado se produtos com maior número de avaliações possuem maior volume de vendas.

Essa análise é relevante porque a quantidade de avaliações pode indicar confiança do consumidor e popularidade do produto.

### 7.5 Desempenho por marca, material e temporada

Foram analisadas as vendas por marca, material e temporada, permitindo identificar quais grupos apresentam melhor desempenho comercial.

## 8. Relatório de insights

Com base na análise exploratória, foram identificados alguns insights importantes:

### Insight 1 — Avaliações podem indicar maior confiança do consumidor

Produtos com maior número de avaliações tendem a demonstrar maior engajamento dos consumidores. Isso pode indicar que avaliações funcionam como prova social, influenciando novos compradores.

### Insight 2 — Descontos precisam ser avaliados com cuidado

Nem sempre um desconto maior significa maior quantidade vendida. Por isso, é importante analisar a efetividade dos descontos por produto, marca ou categoria antes de aplicar promoções generalizadas.

### Insight 3 — Preço influencia o comportamento de compra

A análise de preço permite identificar faixas mais competitivas. Produtos muito caros podem ter menor volume de vendas, enquanto produtos com preço intermediário podem apresentar melhor equilíbrio entre atratividade e rentabilidade.

### Insight 4 — Algumas marcas concentram maior volume de vendas

A análise por marca permite identificar quais marcas possuem melhor desempenho. Essas marcas podem receber maior investimento em campanhas, estoque e destaque no site.

### Insight 5 — Sazonalidade pode impactar as vendas

A variável temporada ajuda a entender se determinados produtos vendem melhor em períodos específicos. Isso pode apoiar decisões de estoque e planejamento de campanhas promocionais.

## 9. Dashboard no Looker Studio

O dashboard foi desenvolvido no Looker Studio com o objetivo de apresentar os principais resultados de forma visual e interativa.

Foram incluídos os seguintes elementos:

* cartões de indicadores principais;
* gráfico de barras com vendas por marca;
* gráfico de barras com vendas por material;
* gráfico de barras com vendas por temporada;
* gráfico de pizza para distribuição por gênero;
* gráfico de dispersão entre preço e quantidade vendida;
* gráfico de dispersão entre desconto e quantidade vendida;
* gráfico de dispersão entre avaliações e quantidade vendida;
* tabela com os produtos ou categorias de maior desempenho;
* filtros interativos por marca, material, gênero e temporada.

### Indicadores principais do dashboard

* Total de produtos analisados;
* Total de vendas;
* Preço médio;
* Desconto médio;
* Nota média;
* Total de avaliações.

## 10. Conclusões

A análise de dados mostrou que o desempenho de vendas em um e-commerce pode ser influenciado por diferentes fatores, como preço, desconto, avaliações, marca, material e temporada.

O projeto demonstrou que a análise exploratória permite transformar dados brutos em informações úteis para a tomada de decisão. A partir dos insights gerados, uma empresa pode melhorar suas estratégias comerciais, otimizar campanhas promocionais, priorizar produtos com maior potencial e acompanhar indicadores por meio de dashboards.

Portanto, o uso de dados é fundamental para reduzir decisões baseadas em achismo e aumentar a eficiência das ações comerciais em ambientes digitais.

## 11. Sugestões de ações

Com base nos resultados obtidos, recomenda-se:

* investir em produtos e marcas com maior volume de vendas;
* revisar descontos que não geram aumento significativo nas vendas;
* destacar produtos com boas notas e muitas avaliações;
* analisar sazonalidade antes de planejar campanhas;
* acompanhar os indicadores em um dashboard atualizado;
* utilizar os insights para apoiar decisões de estoque, preço e marketing.

## 12. Estrutura sugerida do repositório

```text
projeto-semantix-ecommerce/
│
├── README.md
├── ecommerce_estatistica.csv
├── notebook_eda_ecommerce.ipynb
├── analise_ecommerce.py
├── dashboard/
│   └── link_dashboard_looker_studio.txt
├── imagens/
│   ├── 1_dashboard_visao_garal.png
│   ├── 2_dashboard_desempenho_por_categoria
│   ├── 3_dashboard_relacoes_insights_e_conclusoes
│   └──Análise_de_Vendas_em_E-commerce_dashboard.pdf
└── resultados/
    ├── base_tratada.csv
    └── insights_ecommerce.csv
```

## 13. Link do dashboard

O dashboard final foi desenvolvido no Looker Studio e disponibilizado no link abaixo:

https://datastudio.google.com/reporting/664bc65f-3a6b-4413-a287-e7308c338ca9

## 14. Link do repositório

O projeto completo foi disponibilizado no GitHub no link abaixo:

https://github.com/XxxCoutinho/projeto-semantix-ecommerce

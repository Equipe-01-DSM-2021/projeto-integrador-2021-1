<br id="topo">

<h1 align="center"> Análise de Dados Eleitorais </h1>

<p align="center"> 
    <a href="#dados">Os dados</a> &nbsp | &nbsp 
    <a href="#analise">Gráficos interessantes</a> &nbsp | &nbsp
    <a href="#equipe">Responsáveis</a>
</p>
   
A análise de dados se faz importante para descobrir padrões ou relações entre certos aspectos para tirar conclusões, e como o objetivo deste projeto é, sobre tudo, exibir estatísticas sobre o eleitorado contido na cobertura da [TV Vanguarda](http://vanguarda.tv/), esta técnica foi utilizada para evidenciar características (como o estado civil, escolaridade e faixa etária), bem como informações sobre renda e evolução na quantidade de eleitores, além do candidato eleito em um determinado ano, resultando na geração de alguns gráficos interessantes...

<span id="dados">

## :open_file_folder: Os dados

Foi utilizado como base de dados alguns CSVs públicos disponibilizados pelo TSE e IBGE, onde as fontes podem ser conferidas pelos links abaixo:

- [TSE - Tribunal Superior Eleitoral](https://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais): Características do eleitorado e dos candidatos eleitos.
- [IBGE - Instituto Brasileiro de Geografia e Estatística](https://cidades.ibge.gov.br/brasil/sp/sao-jose-dos-campos/pesquisa/19/29765?localidade1=355410&localidade2=355030): Dados sobre renda da população

→ [Voltar ao topo](#topo)

<span id="analise">

## :bar_chart: Gráficos interessantes

A análise de dados foi feita através do Jupyter Notebook, onde focamos em atender os requisitos que o cliente declarou, e com isso, obtivemos alguns resultados interessantes quanto à renda dos eleitores mas também sobre a evolução da quantidade de eleitores em cada cidade conforme os anos e as cidades com as maiores percentagens de eleitores jovens e idosos em cada região. Nas demonstrações abaixo, a cidade principal da análise foi "São José dos Campos", no ano de 2020, mas também, para comparações, foram usadas cidades como "Taubaté" e "Jacareí".

<br>

### Verificação das cidades com mais jovens e mais idosos na região

<div align="center">
  <img src="./img/idoso-jovem.jpg" alt="Cidades 'mais velhas' e 'mais novas'">
</div>

<br>

### Verificação da renda média do eleitorado

<div align="center">
  <img src="./img/renda.jpg" alt="Gráfico de renda média">
</div>

<br>

### Verificação da evolução na quantidade de eleitores

<div align="center">
  <img src="./img/evolucao.jpg" alt="Evolução de eleitores">
</div>

<br>

Para interagir com o Jupyter Notebook desenvolvido, tem-se 2 opções:

- Use [este link](https://nbviewer.jupyter.org/github/Equipe-01-DSM-2021/projeto-integrador-2021-1/blob/a44edcce3a86c0f1c070d5b6c52d683010af94cd/jupyter-notebooks/AnaliseDadosEleitorais.ipynb) para ver as análises, mas sem poder alterar as variáveis (como cidade ou ano), pois o GitHub não suporta a visualização devido à biblioteca Python que usamos para gerar os gráficos;
- Baixe este repositório e siga o passo a passo descrito no tópico "Rodando o Jupyter Notebook" [deste link](https://github.com/Equipe-01-DSM-2021/projeto-integrador-2021-1/blob/trunk/planejamento/sprint-2/README.md#analise) para abrir o Notebook localmente em seu dispositivo.

→ [Voltar ao topo](#topo)

<span id="equipe">
	
## :busts_in_silhouette: Responsáveis
Nossa equipe é composta por 6 integrantes, onde todos colaboraram com o desenvolvimento do Jupyter Notebook, mas 3 tomaram a frente nestas tarefas e merecem destaque. São eles:

- Adriano Andrade Almeida
  - Responsável pela viabilidade de algumas análises e desenvolvimento da análise sobre as cidades com mais eleitores jovens e idosos de cada região;
- Ana Carolina dos Santos
  - Responsável pela manipulação da biblioteca Plotly para geração de gráficos e desenvolvimento da análise sobre a renda do eleitorado;
- Caio Vitor Dias
  - Responsável pelo desenvolvimento da análise sobre a evolução na quantidade de eleitores e manipulação da biblioteca Plotly para geração de gráficos.

Outras pessoas deram suporte na geração de gráficos, manipulação de dados e ajustes no Markdown.

→ [Voltar ao topo](#topo)

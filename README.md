<br id="topo">

<h1 align="center"> FATEC Profº Jessen Vidal, SJC - 1º Semestre DSM </h1>

<h4 align="center"> 
	🚧  Projeto em desenvolvimento  🚧
</h4>

<p align="center">
    <a href="#sobre">Sobre</a> | 
    <a href="#backlogs">Backlogs</a> | 
    <a href="#user-stories">User Stories</a> | 
    <a href="#prototipo">Protótipo</a> | 
    <a href="#tecnologias">Tecnologias</a>
    <a href="#equipe">Equipe</a> | 
    <a href="#final">Apresentação Final</a> | 
    <a href="#licenca">Licença</a>
</p>
   
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

Tem por objetivo proporcionar à "TV Vanguarda" um site de análise de dados com a exibição de estatísticas do eleitorado localizado dentro de sua cobertura no Estado de São Paulo, podendo obter diversas características, como gráficos e tabelas de estado civil, escolaridade e faixa etária, além de informações sobre renda e evolução na quantidade de eleitores, tanto no âmbito municipal (de cada cidade) quanto macro-regiões, como o Vale do Paraíba.

_Projeto integrador baseado em metodologia ágil (SCRUM), procurando desenvolver Proatividade, Autonomia, Colaboração e Entrega de resultados_

> Status do Projeto: Em andamento

### Entregas de Sprints

Cada entrega será realizada a partir da criação de uma **tag**. Observe a relação a seguir:
| Sprint| Tag | Lançamento | Status | Histórico |
|:-----:|:-------------:|:----------:|:---------:|:---------:|
| 01 | [sprint-01](https://github.com/Equipe-01-DSM-2021/projeto-integrador-2021-1/releases/tag/sprint-01) | 28/03/2021 | Entregue | [Entrega parcial 1](/planejamento/sprint-1) |
| 02 | [sprint-02](https://github.com/Equipe-01-DSM-2021/projeto-integrador-2021-1/releases/tag/sprint-02) | 18/04/2021 | Entregue | [Entrega parcial 2](/planejamento/sprint-2) |
| 03 | [sprint-03](https://github.com/Equipe-01-DSM-2021/projeto-integrador-2021-1/releases/tag/sprint-03) | 16/05/2021 | Entregue | [Entrega parcial 3](/planejamento/sprint-3) |
| 04 | Em breve... | 05/06/2021 | Planejada | Em breve... |

→ [Voltar ao topo](#topo)

<span id="backlogs">

## :dart: Backlogs

### Backlog do Produto

#### Requisitos Funcionais

| Código | Item                                                                           | User Story |
| :----: | :----------------------------------------------------------------------------- | :--------: |
| RF 01  | Geração de estatísticas sobre eleitorado                                       |    #01     |
| RF 02  | Verificação características do eleitorado de acordo com o representante eleito |    #02     |
| RF 03  | Verificação das cidades com mais jovens e mais idosos na região                |    #04     |
| RF 04  | Exportação dos resultados da busca                                             |    #06     |
| RF 05  | Verificação da renda média do eleitorado                                       |    #03     |
| RF 06  | Comparação renda média do Vale do Paraíba com outras regiões                   |    #05     |
| RF 07  | Geração de estatísticas sobre comparecimento e ausência às urnas               | #11 e #12  |
| RF 08  | Geração de estatísticas sobre a evolução da quantidade de eleitores            |    #13     |

#### Requisitos Não Funcionais

| Código | Item                                 | User Story |
| :----: | :----------------------------------- | :--------: |
| RFN 01 | Passível de atualizações             |    #07     |
| RFN 02 | Implementação do back-end em Python  |    #09     |
| RFN 03 | Codificação de fácil compreensão     |    #08     |
| RFN 04 | Documentação                         |    #10     |
| RFN 05 | Análise de dados em Jupyter Notebook |    #14     |

→ [Voltar ao topo](#topo)

### Backlog das Sprints

#### Sprint 1

| Item | Descrição                  |
| :--: | :------------------------- |
|  01  | Wireframe                  |
|  02  | Levantamento de Requisitos |
|  03  | Protótipo Dinâmico         |
|  04  | Organização da equipe      |
|  05  | Organização do repositório |

#### Sprint 2

| Item do Backlog do Produto | Descrição                                                                      | User Story |
| :------------------------: | :----------------------------------------------------------------------------- | :--------: |
|           RF 01            | Geração de estatísticas sobre eleitorado                                       |    #01     |
|           RF 02            | Verificação características do eleitorado de acordo com o representante eleito |    #02     |
|           RF 07            | Geração de estatísticas sobre comparecimento e ausência às urnas               | #11 e #12  |

#### Sprint 3

| Item do Backlog do Produto | Descrição                                                       | User Story |
| :------------------------: | :-------------------------------------------------------------- | :--------: |
|           RF 03            | Verificação das cidades com mais jovens e mais idosos na região |    #04     |
|           RF 05            | Verificação da renda média do eleitorado                        |    #03     |
|           RF 06            | Comparação da renda média do Vale do Paraíba com outras regiões |    #05     |
|           RF 08            | Verificação da evolução na quantidade de eleitores              |    #13     |

#### Sprint 4

| Item do Backlog do Produto | Descrição                          | User Story |
| :------------------------: | :--------------------------------- | :--------: |
|           RF 04            | Exportação dos resultados da busca |    #06     |

- **OBS:** Para a quarta sprint, os maiores esforços estarão no desenvolvimento do site e aplicação de melhorias na análise de dados (Jupyter Notebook).

:round_pushpin: Para ver o planejamento completo das sprints, como entregas, tarefas e prazos, assim como estatísticas do time, [clique aqui](/planejamento).

→ [Voltar ao topo](#topo)

<span id="user-stories">

## :mag: User Stories

Informações informais sobre as funções do sistema (como uma única tarefa pode oferecer determinado valor)

| Código | Quem       | O que?                                                                                                                                                   | Para                                                |
| :----: | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
|  #01   | Jornalista | Quer saber a classificação do eleitorado a partir do estado civil, escolaridade e faixa etária, além da quantidade de eleitores que utilizam nome social | Obter conteúdo para sua matéria                     |
|  #02   | Jornalista | Quer relacionar as características do eleitorado de acordo com o representante eleito em determinada região                                              | Obter conteúdo para sua matéria                     |
|  #03   | Jornalista | Quer saber a renda média do eleitorado de determinada região                                                                                             | Obter conteúdo para sua matéria                     |
|  #04   | Jornalista | Quer saber, daquela região, a cidade com mais eleitores jovem e mais eleitores idosos                                                                    | Obter conteúdo para sua matéria                     |
|  #05   | Jornalista | Quer comparar a renda média de eleitores do Vale do Paraíba com a de outras regiões do Estado                                                            | Obter conteúdo para sua matéria                     |
|  #06   | Jornalista | Quer automatizar a exportação das estatísticas                                                                                                           | Publicar gráficos e dados em diferentes plataformas |
|  #07   | Jornalista | Quer poder relacionar características do eleitorado de acordo com o representante eleito em determinada região de eleições futuras                       | Continuar obtendo conteúdo para sua matéria         |
|  #08   | Jornalista | Quer entender o código                                                                                                                                   | Fazer customizações                                 |
|  #09   | Jornalista | Quer que o back-end seja feito em Python                                                                                                                 | Fazer customizações                                 |
|  #10   | Jornalista | Quer ler uma documentação simples                                                                                                                        | Saber usar a aplicação                              |
|  #11   | Jornalista | Quer saber a percentagem de eleitores justificados da última eleição                                                                                     | Obter conteúdo para sua matéria                     |
|  #12   | Jornalista | Quer saber a percentagem de eleitores ausentes da última eleição                                                                                         | Obter conteúdo para sua matéria                     |
|  #13   | Jornalista | Quer saber a evolução do número de eleitores                                                                                                             | Obter conteúdo para sua matéria                     |
|  #14   | Jornalista | Quer a análise de dados feita em Jupyter Notebook                                                                                                        | Obter visualização prévia das estatísticas          |

→ [Voltar ao topo](#topo)

<span id="prototipo">

## :desktop_computer: Protótipo

Antes de realmente desenvolver o projeto, foi idealizado um layout específico, aplicado em um wireframe e validado com o cliente. Depois, foi criado um protótipo em HTML, CSS e Javascript (que possibilitava algumas interações na interface e também a exibição de gráficos com dados fictícios), onde é possível observar o resultado gerado pelos códigos na demonstração abaixo:

![](/prototipo/demo.gif)

Depois de alguns feedbacks, o time desenvolveu um novo protótipo e layout para o site, contando com mais páginas em sua navegação, além de novos estilos e ícones. Observe o resultado da atualização do protótipo:

![](/prototipo/demo-2.gif)

→ [Voltar ao topo](#topo)

<span id="tecnologias">

## 🛠️ Tecnologias

As seguintes ferramentas, linguagens, bibliotecas e tecnologias foram usadas na construção do projeto:

- [Figma](http://www.figma.com): Prototipagem
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML): Estrutura das páginas do site
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS): Estilização do site
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript): Interações do site
- [Python](https://www.python.org/): Back-end
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): Servidor
- [Jupyter Notebook](https://jupyter.org/): Análise de dados
- [Pandas](https://pandas.pydata.org/docs/): Análise de dados
- [NumPy](https://numpy.org/doc/stable/): Análise de dados
- [Plotly](https://plotly.com/python/): Geração de gráficos (Jupyter Notebook)
- [Chart.js](https://www.chartjs.org/): Geração de gráficos (site)
- [Visual Studio Code](https://code.visualstudio.com/): Codificação
- [Discord](https://discord.com/): Comunicação
- [GitHub](https://github.com/): Versionamento
- [Google Sheets](https://www.google.com/sheets/about/): Acompanhamento do gráfico de burndown

→ [Voltar ao topo](#topo)

<span id="equipe">

## :busts_in_silhouette: Equipe

|    Função    | Nome                     |                               LinkedIn                                |                     GitHub                     |
| :----------: | :----------------------- | :-------------------------------------------------------------------: | :--------------------------------------------: |
| Scrum Master | Maria Gabriela G.S. Reis |      [LinkedIn](https://www.linkedin.com/in/mariagabrielareis/)       | [GitHub](https://github.com/MariaGabrielaReis) |
|   Dev Team   | Adriano Andrade Almeida  |         [LinkedIn](https://www.linkedin.com/in/aeroadriano/)          |    [GitHub](https://github.com/aeroadriano)    |
|   Dev Team   | Ana Carolina dos Santos  |     [LinkedIn](https://www.linkedin.com/in/ana-santos-856436145/)     |      [GitHub](https://github.com/annakks)      |
|   Dev Team   | Antônio A.R. Nepomuceno  | [LinkedIn](https://www.linkedin.com/in/antonio-nepomuceno-04943720a/) |      [GitHub](https://github.com/Nepoun)       |
|   Dev Team   | Caio Vitor Dias          |         [LinkedIn](https://www.linkedin.com/in/caio-vitor-c1)         |  [GitHub](https://github.com/CaioVitorDias1)   |
|   Dev Team   | Giovana Thaís O. Silva   |         [LinkedIn](https://www.linkedin.com/in/gioliveirass)          |   [GitHub](https://github.com/gioliveirass)    |

→ [Voltar ao topo](#topo)

<span id="final">

## :clapper: Apresentação Final do Projeto

Clique no link abaixo para visualizar o vídeo final do projeto:

> Vídeo (Em breve)

→ [Voltar ao topo](#topo)

<span id="licenca">

## :page_with_curl: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

→ [Voltar ao topo](#topo)

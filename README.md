<br id="topo">

<h1 align="center"> FATEC Profº Jessen Vidal, SJC - 1º Semestre DSM </h1>

<h4 align="center"> 
	🚧  Projeto em desenvolvimento  🚧
</h4>

<p align="center">
    <a href="#sobre">Sobre</a> | 
    <a href="#metodologias">Metodologia e Princípios</a> | 
    <a href="#backlogs">Backlogs</a> | 
    <a href="#user-stories">User Stories</a> | 
    <a href="#prototipo">Protótipo</a> | 
    <a href="#tecnologias">Tecnologias</a>
    <br>
    <a href="#manual">Manual do Usuário</a> | 
    <a href="#equipe">Equipe</a> | 
    <a href="#final">Apresentação Final</a> | 
    <a href="#licenca">Licença</a>
</p>
   
<span id="sobre">

## :bookmark_tabs: Sobre o projeto
Tem por objetivo proporcionar à "TV Vanguarda" um site de busca por informações do eleitorado atual localizado dentro de sua cobertura no Estado de São Paulo, podendo obter características como relações de estado civil, escolaridade, gênero, entre outras variáveis em regiões macro (como o Vale do Paraíba) ou micro (as cidades que compões o Vale do Paraíba).

*Projeto integrador baseado em metodologia ágil, procurando desenvolver Proatividade, Autonomia, Colaboração e Entrega de resultados*

> Status do Projeto: Em andamento

#### Entregas de Sprints
Cada entrega será realizada a partir da criação de uma **tag**, onde a relação de nomes pode ser observada a seguir:
| Sprint| Tag           | Lançamento | Status    |
|:-----:|:-------------:|:----------:|:---------:|
| 01    | **sprint-01** | 28/03/2021 | Entregue  |
| 02    | em breve...   | 18/04/2021 | Planejada |
| 03    | em breve...   | 16/05/2021 | Planejada |
| 04    | em breve...   | 05/06/2021 | Planejada |

→ [Voltar ao topo](#topo)

<span id="metodologias">

## :pushpin: Metodologias e Princípios
- **Metodologia Ágil:** Framework [Scrum](https://www.desenvolvimentoagil.com.br/scrum/), prática que consiste em dividir o desenvolvimento do projeto em blocos de trabalho chamados de Sprints, com duração de, neste caso, 3 semanas cada. Ao final de cada ciclo há algum tipo de entrega ao cliente, que avaliará o trabalho e então dará um feedback sobre o andamento do projeto.
- **KISS** (Keep It Simple, Stupid) e **DRY** (Don't Repeat Yourself), princípios da programação que defendem a criação de códigos simples e intuitivos quanto a nomenclatura e funcionalidades, e sem repetições (ocorrência única de uma função).

→ [Voltar ao topo](#topo)

<span id="backlogs">

## :dart: Backlogs

### Backlog do Produto
#### Requisitos Funcionais
| Código | Item                                                                           | User Story     |
|:------:|:-------------------------------------------------------------------------------|:--------------:|
| RF 01  | Geração de estatísticas sobre eleitorado                                       | #01 e #02      |
| RF 02  | Verificação características do eleitorado de acordo com o representante eleito | #03            |
| RF 03  | Verificação da cidade com média mais alta e mais baixa de idade na região      | #05            |
| RF 04  | Exportação dos resultados da busca                                             | #07            |
| RF 05  | Verificação da renda média do eleitorado                                       | #04            |
| RF 06  | Comparação renda média do Vale do Paraíba com outras regiões                   | #06            |
| RF 07  | Geração de estatísticas sobre comparecimento e quantidade de eleitores         | #11, #12 e #13 |

#### Requisitos Não Funcionais
| Código | Item                                | User Story |
|:------:|:------------------------------------|:----------:|
| RFN 01 | Passível de atualizações            | #08        |
| RFN 02 | Implementação do back-end em Python | #09        |
| RFN 03 | Codificação de fácil compreensão    | #09        |
| RFN 04 | Documentação                        | #10        |

→ [Voltar ao topo](#topo)


### Backlog das Sprints
#### Sprint 1
| Item  | Descrição                   | 
|:-----:|:----------------------------|
| 01    | Wireframe                   |
| 02    | Levantamento de Requisitos  |
| 03    | Protótipo Dinâmico          |
| 04    | Organização da equipe       |
| 05    | Organização do repósitório  |

#### Sprint 2
| Item do Backlog do Produto | Descrição                                                                      | User Story     |
|:--------------------------:|:-------------------------------------------------------------------------------|:--------------:|
| RF 01                      | Geração de estatísticas sobre eleitorado                                       | #01 e #02      |
| RF 02                      | Verificação características do eleitorado de acordo com o representante eleito | #03            |


#### Sprint 3
| Item do Backlog do Produto | Descrição                                                                      | User Story     |
|:--------------------------:|:-------------------------------------------------------------------------------|:--------------:|
| RF 03                      | Verificação da cidade com média mais alta e mais baixa de idade na região      | #05            |
| RF 04                      | Exportação dos resultados da busca                                             | #07            |

#### Sprint 4
| Item do Backlog do Produto | Descrição                                                                      | User Story     |
|:--------------------------:|:-------------------------------------------------------------------------------|:--------------:|
| RF 05                      | Verificação da renda média do eleitorado                                       | #04            |
| RF 06                      | Comparação renda média do Vale do Paraíba com outras regiões                   | #06            |
| RF 07                      | Geração de estatísticas sobre comparecimento e quantidade de eleitores         | #11, #12 e #13 |

:round_pushpin: Para ver o planejamento completo das sprints, entregas, tarefas e prazos, assim como estatísticas do time, [clique aqui](/planejamento).

→ [Voltar ao topo](#topo)

<span id="user-stories">

## :mag: User Stories
Informações informais sobre as funções do sistema (como uma única tarefa pode oferecer determinado valor)

| Código | Quem       | O que?                                                                                               | Para                                        |
|:------:|:-----------|:-----------------------------------------------------------------------------------------------------|:--------------------------------------------|
| #01    | Jornalista | Quer saber a classificação do eleitorado a partir do estado civil, esolaridade e gênero              | Obter conteúdo para sua matéria             |
| #02    | Jornalista | Quer saber a porcentagem de eleitores que utilizam nome social ou que possuem deficiência            | Obter conteúdo para sua matéria             |
| #03    | Jornalista | Quer relacionar as características do eleitorado de acordo com o representante eleito em determinada região | Obter conteúdo para sua matéria      |
| #04    | Jornalista | Quer saber a renda média do eleitorado de determinada região                                         | Obter conteúdo para sua matéria             |
| #05    | Jornalista | Quer sabe, daquela região, a cidade com o eleitorado mais jovem e mais velho                         | Obter conteúdo para sua matéria             |
| #06    | Jornalista | Quer saber comparar a renda média de eleitores do Vale do Paraíb com a de outras regiões do Estado   | Obter conteúdo para sua matéria             |
| #07    | Jornalista | Quer automatizar a publicação de gráficos e dados em diferentes plataformas                          | Continuar obtendo conteúdo para sua matéria |
| #08    | Jornalista | Quer poder relacionar características do eleitorado de acordo com o representante eleito em determinada região de eleições futuras | Obter conteúdo para sua matéria |
| #09    | Jornalista | Quer entender o código                                                                               | Fazer customizações                         |
| #10    | Jornalista | Quer ler uma documentação simples                                                                    | Saber usar a aplicação                      |
| #11    | Jornalista | Quer saber a porcentagem de eleitores justificados na última eleição                                 | Obter conteúdo para sua matéria             |
| #12    | Jornalista | Quer saber a porcentagem de eleitores faltosos na última eleição                                     | Obter conteúdo para sua matéria             |
| #13    | Jornalista | Quer saber a evolução do número de eleitores                                                         | Obter conteúdo para sua matéria             |

→ [Voltar ao topo](#topo)

<span id="prototipo">

## :desktop_computer: Protótipo
Antes de colocar a mão na massa e construir o projeto, idealizamos um layout específico, aplicando em um wireframe e validando com o cliente. Logo após, foi iniciado o desenvolvimento de um protótipo, exemplificando funcionalidades, cores, tipografia e a experiência que o usuário terá ao manipular o produto final. 

OBS.: Tanto a confecção do wireframe quanto a do protótipo navegável foram possíveis através da utilização de uma ferramenta gratuita própria para prototipagem chamada "[Figma](http://www.figma.com)". É possível acessar o protótipo por meio [deste link](https://www.figma.com/file/bgsXLk2bXJIwo5SOnUhylt/API-2021%2F1?node-id=1%3A886).

Assim que o protótipo estava pronto no Figma, começamos o desenvolvimento do projeto em HTML e CSS, utilizando também o JavaScript para algumas interações na interface e para a exibição de gráficos com dados fictícios, onde é possível observar o resultado gerado pelos códigos na demonstração abaixo:

### Demonstração
![](/prototipo/demo.gif)

→ [Voltar ao topo](#topo)

<span id="tecnologias">

## 🛠️ Tecnologias
As seguintes ferramentas, linguagens, bibliotecas e tecnologias serão e estão sendo usadas na construção do projeto:

- [Figma](http://www.figma.com)
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [Python](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/)
- [Chart.js](https://www.chartjs.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Discord](https://discord.com/)
- [WhatsApp](https://www.whatsapp.com/?lang=pt_br)
- [GitHub](https://github.com/)

→ [Voltar ao topo](#topo)

<span id="manual">

## :open_book: Manual do Usuário
> Em breve

→ [Voltar ao topo](#topo)

<span id="equipe">

## :busts_in_silhouette: Equipe

| Função       | Nome                     | LinkedIn                                                             | GitHub                                         |
|:------------:|:-------------------------|:--------------------------------------------------------------------:|:----------------------------------------------:|
| Scrum Master | Maria Gabriela G.S. Reis | [LinkedIn](https://www.linkedin.com/in/mariagabrielareis/)           | [GitHub](https://github.com/MariaGabrielaReis) |
| Dev Team     | Adriano Andrade Almeida  | [LinkedIn](https://www.linkedin.com/in/aeroadriano/)                 | [GitHub](https://github.com/aeroadriano)       |
| Dev Team     | Ana Carolina dos Santos  | [LinkedIn](https://www.linkedin.com/in/ana-santos-856436145/)        | [GitHub](https://github.com/annakks)           |
| Dev Team     | Antônio A.R. Nepomuceno  | [LinkedIn](https://www.linkedin.com/in/antonio-nepomuceno-04943720a/)| [GitHub](https://github.com/Nepoun)            |
| Dev Team     | Caio Vitor Dias          | [LinkedIn](https://www.linkedin.com/in/caio-vitor-c1)                | [GitHub](https://github.com/CaioVitorDias1)    |
| Dev Team     | Giovana Thaís O. Silva   | [LinkedIn](https://www.linkedin.com/in/gioliveirass)                 | [GitHub](https://github.com/gioliveirass)      |


→ [Voltar ao topo](#topo)

<span id="final">

## :clapper: **Apresentação Final do Projeto**
**Clique no link abaixo para visualizar o vídeo final do projeto:**
> Vídeo (Em breve)

→ [Voltar ao topo](#topo)

<span id="licenca">

## :page_with_curl: Licença
Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

→ [Voltar ao topo](#topo)

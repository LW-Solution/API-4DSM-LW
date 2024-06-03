# DEVOPS

<p align="center">
 <a href="#versionamento">Versionamento</a> •
 <a href="#rastreabilidade">Rastreabilidade</a> • 
 <a href="#teste">Testes</a> • 
 <a href="#ci">CI</a> •
 <a href="#da">Deploy Automático</a>
</p>


# Documentação <a id="doc"></a>


### Versionamento: <a id="versionamento"></a>

VER

### Rastreabilidade: <a id="rastreabilidade"></a>

Rastreabilidade

### Testes: <a id="teste"></a>

Para a realização dos testes foram elaborados diferentes estratégias de processos de acordo com a necessidade de cada tipo de serviço. O projeto possui vários serviços ativos que são divididos, basicamente, em serviços Node e Python, há também um repositório em código C de modelo para dispositivos IOT.
Tendo isso em vista, se faz necessário, ocasionalmente, divergir nas estratégias dos processos de testes entre os serviços.
Os processos foram divididos da seguinte forma:
- Serviços Node backend (estações métricas e autenticação);
- Serviço Node frontend;
- Serviços Python backend (tratamento e recepção de dados);

#### Processo de teste Node backend:

O processo começa com o ínicio de alguma feature, logo deve-se respeitar os padrões estabelecidos de commits e etc. Assim que o desenvolvedor terminar a adição, ele deve ir na pasta "test" presente na raiz dos repositórios, e seguir ou estipular o caminho dos arquivos alterados na pasta "src", porém nesta pasta "test". Após isso, ele deve fazer o teste unitário ou de integração referente às adições realizadas. Terminando o teste, deve-se rodar o seguinte comando na raiz do projeto: "npm run test"; E então será iniciado um script que rodará todos os testes disponíveis. Se tudo der "OK" então o dev poderá fazer o merge de suas alterações com a branch "develop". Ao final da sprint, antes de juntar a "develop" com a "prod" os testes devem ser rodados novamente para garantir que de fato não há problemas e só então deverá ser feito o merge com a branch de produção.

#### Bibliotecas utilizadas:
- jest;
- supertest;
- ts-jest;
- @types do jest e supertest;

Essas libs foram escolhidas pois o Jest é um framework simples que, dentre outras coisas, providencia métodos para organizar os testes a serem criados, já o Supertest é uma biblioteca que simula a aplicação REST inteira, permitindo que sejam feitas requisições e etc, sem que seja preciso rodar a aplicação tornando muito útil para o ambiente de teste.

#### Especificações:

Cada teste possui um escopo que deve ser respeitado e cada escopo é definido pela função "describe(" ", () => {})" que possuirá uma string explicando esse escopo. Cada teste deve ser feito dentro do "describe(" ", () => {})" numa função "it(" ", () => {})" que também terá uma string para descrever seu escopo. No caso de um teste abrir um novo escopo, deve-se criar uma nova função "describe(" ", () => {})" para ele. Vale ressaltar que toda função de teste deve possuir uma asserção de um valor esperado.

#### Processo de teste Node frontend:

O processo de teste para o frontend segue exatamente os mesmos passos que o Node backend, exceto por um fator determinante; Após a criação da feature e a criação dos testes estipulados para ela, antes de rodar o comando para iniciar os testes, deve-se ir ao arquivo "package.json" na raiz do projeto e alterar a linha 4: "type: module"; para "type: commonjs", ao fazer isso, deve-se rodar o comando de testes normalmente (npm run test) e se tudo der "OK", é preciso voltar ao arquivo "package.json" e desfazer as alterações para só então realizar o merge das branches.

#### Bibliotecas utilizadas:
- jest;
- ts-jest;
- @types do jest;

Foi escolhido o Jest pois ele é um framework que cria um ambiente de testes virtual para rodar os scripts descritos pelos testes e providencia métodos para organizar os testes a serem criados. O que o torna muito útil especialmente para testes de integração.

#### Especificações:

Cada teste possui um escopo que deve ser respeitado e cada escopo é definido pela função "describe(" ", () => {})" que possuirá uma string explicando esse escopo. Cada teste deve ser feito dentro do "describe(" ", () => {})" numa função "it(" ", () => {})" que também terá uma string para descrever seu escopo. No caso de um teste abrir um novo escopo, deve-se criar uma nova função "describe(" ", () => {})" para ele. Vale ressaltar que toda função de teste deve possuir uma asserção de um valor esperado.

#### Processo de teste Python backend:

Para o processo dos serviços em python é necessário gerar um arquivo de teste seguindo a nomenclatura (test_ + nome arquivo) para que esse arquivo marque o escopo de todos os testes referentes às funções nele presentes. O arquivo deve, também, ser criado seguindo o mesmo endereço do arquivo em teste da pasta "src" ou raiz porém na pasta "test". Após desenvolvido os testes, deve-se abrir o terminal dentro da pasta "test" e rodar o seguinte comando: "python -m unittest". Se tudo der "OK" então já é possível fazer o merge com a branch develop. Antes de mergear com a branch prod é necessário rodar os testes novamente para garantir que está tudo okay.

#### Bibliotecas utilizadas:
- unittest (padrão do python);

O motivo da escolha dessa lib é por sua simplicidade e eficiencia já que não é necessário instalar dependências pois ela já vem com o python e sua estruturação de testes é bastante intuitiva e rápida.

#### Especificações:

O escopo de cada teste é definido pelo arquivo criado, ou seja, se há um arquivo "app.py" que precisa ter seus métodos testados, todos os testes referentes a eles devem ficar no arquivo "test_app.py". Dentro de cada arquivo de teste deve haver uma classe "TestApp(unittet.TestCase)", e cada teste deve representar uma função dentro da classe. O nome dessas funções deve descrever o escopo daquele teste específico. Vale ressaltar que toda função de teste deve possuir uma asserção de um valor esperado.

## CI: <a id="ci"></a>

## Processo de CI

Este documento descreve o processo de Integração Contínua (CI) e Deploy Contínuo (CD) para o nosso projeto. Ele inclui a organização das branches, as regras de merge, e o pipeline de CI/CD configurado para builds, testes e deploys automáticos.

## Estrutura das Branches

### `develop`

- **Objetivo**: Integrar mudanças diárias dos desenvolvedores.
- **Regras de Merge**:
  - Pull Requests (PRs) podem ser aprovadas pelo próprio criador.
  - Deve haver commits diários para manter a branch atualizada.
- **Builds e Testes**:
  - Builds automáticos a cada PR.
  - Execução de testes unitários.
  - Atualização das imagens Docker.

### `staging`

- **Objetivo**: Validar tarefas concluídas por um desenvolvedor.
- **Regras de Merge**:
  - PRs devem ser revisadas e aprovadas por alguém que não trabalhou na tarefa.
  - A tarefa deve ser testada para garantir que os requisitos foram atendidos.
  - Feedback deve ser fornecido em caso de falha na build ou reprovação do PR.
- **Builds e Testes**:
  - Builds automáticos a cada PR.
  - Execução de testes unitários.
  - Atualização das imagens Docker.

### `prod`

- **Objetivo**: Contém o código que será entregue ao cliente.
- **Regras de Merge**:
  - PRs do `staging` para `prod` devem ser feitas ao final de cada sprint.
  - Tagging das entregas após a aprovação do PR.
- **Builds e Testes**:
  - Builds automáticos a cada PR.
  - Execução de testes unitários.
  - Atualização das imagens Docker.

## Fluxo de Trabalho

### 1. Desenvolvimento Diário

- Os desenvolvedores criam branches a partir da `develop` para trabalhar em suas tarefas.
- Realizam commits frequentes em suas branches de tarefa.
- Ao final do dia (ou de cada sessão de trabalho), fazem merges dessas branches de tarefa na `develop` via PRs, que podem ser aprovadas por eles mesmos.

### 2. Validação de Tarefas

- Quando uma tarefa é concluída, o desenvolvedor abre um PR da sua branch de tarefa para a `staging`.
- Outro membro da equipe, que não esteve envolvido na tarefa, revisa o PR.
  - Verifica se a tarefa foi cumprida conforme os requisitos.
  - Não é necessário revisar o código detalhadamente, mas garantir que a funcionalidade está conforme o esperado.
- Se o PR é aprovado, a tarefa é mergeada na `staging`.
- Caso contrário, feedback é fornecido, e o desenvolvedor faz as correções necessárias antes de tentar novamente.

### 3. Entrega da Sprint

- Ao final de cada sprint, um PR é aberto da `staging` para a `prod`.
- Este PR deve ser revisado para garantir que todas as funcionalidades planejadas estão corretamente implementadas.
- Após a aprovação, o merge é realizado e a entrega é tagueada na `prod`.

## Pipeline CI/CD

### Builds Automáticos

- A cada PR aberto ou merge em qualquer uma das branches (`develop`, `staging`, `prod`), o projeto é automaticamente buildado.
- Testes unitários são executados para garantir que nada foi quebrado.
- As imagens Docker são atualizadas para refletir as mudanças.

### Deploy Automático

1. **Commit e Push**:
   - Desenvolvedores fazem commits e push do código para o repositório.

2. **Build e Testes**:
   - Pipeline é acionado automaticamente.
   - Código é compilado.
   - Testes unitários, de integração e de aceitação são executados.

3. **Criação de Imagem Docker**:
   - Uma imagem Docker é criada a partir do código atualizado.
   - A imagem é testada para garantir que ela funciona conforme o esperado.

4. **Push da Imagem Docker**:
   - A imagem Docker é enviada para um repositório de contêiner (Docker Hub).



## Conteiner Público e Separação de Serviços

### Documentação

- Forneça documentação clara sobre como usar os contêineres, incluindo comandos para executar partes separadas do contêiner, se aplicável.

### Versatilidade de Conteinerização

-

#### Exemplo de `docker-compose.yml`

```yaml
version: '3.8'

networks:
  rede_microsservicos:
    external: true

services:
  db:
    container_name: postgres-container
    image: postgres
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=test_db
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.2

  pgadmin:
    container_name: pgadmin-container
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=doxito007@gmail.com
      - PGADMIN_DEFAULT_PASSWORD=postgres
    ports:
      - "5050:80"
    restart: always
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.3
    depends_on:
      - db

  controller-cadastro-autenticacao:
    image: jonasrsribeiro/lw-controller-cadastro-autenticacao:develop
    ports:
      - "3000:3000"
    restart: always
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.4
    depends_on:
      - pgadmin

  mysql:
    build: .
    image: mysql:8.0
    container_name: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: estacoes_parametros_db
      MYSQL_USER: username
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.5

  controller-gerenciamento-estacoes-metricas:
    image: jonasrsribeiro/lw-controller-gerenciamento-estacoes-metricas:develop
    ports:
      - "3001:3001"
    restart: always
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.6
    depends_on:
      - mysql

  frontend:
    image: jonasrsribeiro/lw-frontend:develop
    ports:
      - "5000:5000"
    volumes:
      - front-data:/app
    environment:
      - NODE_ENV=development
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.7
    depends_on:
      - db
      - mysql
      - controller-cadastro-autenticacao
      - controller-gerenciamento-estacoes-metricas

  controller-recepcao-dados:
    image: jonasrsribeiro/lw-controller-recepcao-dados:develop
    ports:
      - "3002:3002"
    restart: always
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.8
    depends_on:
      - db
      - mysql
      - controller-cadastro-autenticacao
      - controller-gerenciamento-estacoes-metricas
      - frontend

  controller-tratamento-dados:
    image: jonasrsribeiro/lw-controller-tratamento-dados:develop
    ports:
      - "3003:3003"
    restart: always
    networks:
      rede_microsservicos:
        ipv4_address: 172.18.0.9
    depends_on:
      - db
      - mysql
      - controller-cadastro-autenticacao
      - controller-gerenciamento-estacoes-metricas
      - frontend
      - controller-recepcao-dados

volumes:
  postgres-data:
  mysql-data:
  front-data:
```

### Deploy Automático: <a id="da"></a>

Deploy automático
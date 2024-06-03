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

testes

### CI: <a id="ci"></a>

# Processo de CI/CD

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

- Utilize Docker Compose ou Kubernetes para definir serviços individuais. Isso facilita a execução de diferentes partes do seu aplicativo independentemente.

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
# DEVOPS

<p align="center">
 <a href="#versionamento">Versionamento</a> •
 <a href="#rastreabilidade">Rastreabilidade</a> • 
 <a href="#teste">Testes</a> • 
 <a href="#ci">CI</a>
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

### CI: <a id="ci"></a>

CI

### Deploy Automático: <a id="da"></a>

Deploy automático



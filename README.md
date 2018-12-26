# Desafio

### Problema
Criar uma Estrutura de Dados para armazenar nomes de pacientes, que deverá prover uma função de busca, e essa busca deverá fazer _Autocomplete_, ou seja, dado uma query a consulta deverá retornar todos os nomes que tenham a query como seu prefixo.

Disponibilizar uma API Rest para fazer a consulta na Estrutura de Dados.

### Solução
A Estrutura de Dados utilizada para a solução foi a [**Ternary Search Tree**](https://www.geeksforgeeks.org/ternary-search-tree/), que provê uma solução simples e direta para armazenar os nomes. Para fazer a API Rest, foi utilizado [**Flask**](http://flask.pocoo.org).

![Exemplo - Ternary Search Tree](https://raw.githubusercontent.com/phakiller/autocomplete_restapi/master/images/ternary_search_tree.png "Exemplo - Ternary Search Tree")

## Sistema

### Tecnologias Utilizadas

* [**Python**](https://www.python.org)
    * [**Flask**](http://flask.pocoo.org)
    * [**Flask RESTFul**](https://flask-restful.readthedocs.io/en/latest/)
    * [**Flask Testing**](https://pythonhosted.org/Flask-Testing/)
    * [**Flasgger**](https://github.com/rochacbruno/flasgger)
* [**Docker**](https://www.docker.com)

### Como rodar o projeto?

**Clone ou faça o download deste repositório.**

É possivel rodar o **Projeto** de duas formas:

* Utilizando o seu próprio ambiente:
    1. Instale as dependencias do projeto utilizando o comando, `make installdependencies`.
    2. Suba o servidor de testes com o comando, `make runapplocal`.
* Utilizando Docker:
    1. Faça o _build_ da imagem: `make build`
    2. Existem duas maneiras de subir o _App_:
        * Modo Normal: `make runapp`
        * Modo Background: `make runappd`
    3. Para parar o container execute: `make stop`

Depois que subir o projeto:
* A API estará disponivel em: [**http://localhost:6606/**](http://localhost:6606/)
* A Documentação estará disponivel em: [**http://localhost:6606/docs/**](http://localhost:6606/docs/)

##### Rodando os Testes
Para rodar os testes, temos duas opções:
* Rodar localmente: `make runtestslocal`
* Rodar dentro do _Container_: `make runtests`

### Interagindo com o sistema(Swagger)

Acesse a documentação: [**http://localhost:6606/docs/**](http://localhost:6606/docs/)

1. Clique na rota `/patients/search`
![Rota de Pesquisa - Desabilitada](https://raw.githubusercontent.com/phakiller/autocomplete_restapi/master/images/step_1-system_interaction.png "Rota de Pesquisa - Desabilitada")

2. Clique em `Try it out`, para habilitar a caixa de texto.
![Rota de Pesquisa - Habilitada](https://raw.githubusercontent.com/phakiller/autocomplete_restapi/master/images/step_2-system_interaction.png "Rota de Pesquisa - Habilitada")

3. Preencha a caixa de texto com um nome, ou o começo de um. Em seguida clique em `Execute` para fazer a pesquisa. _Exemplo de Pesquisa: Marco_
![Rota de Pesquisa - Caixa de Pesquisa](https://raw.githubusercontent.com/phakiller/autocomplete_restapi/master/images/step_3-system_interaction.png "Rota de Pesquisa - Caixa de Pesquisa")

4. Aqui podemos ver o resultado da pesquisa. Nos retornou quatro nomes que contém a `query`, que enviamos na requisição, como seus prefixo.
![Rota de Pesquisa - Caixa de Pesquisa](https://raw.githubusercontent.com/phakiller/autocomplete_restapi/master/images/step_4-system_interaction.png "Rota de Pesquisa - Caixa de Pesquisa")

### Interagindo com o sistema(curl, Postman e etc.)

Para interagir com o sistema, basta mandar um requisição para, `http://localhost:6606//patients/search`, passando **q** como _query parameter_, sendo obrigatório a passagem desse parâmetro.
Exemplos:
* `http://localhost:6606/patients/search?q=marco`

* `curl -X GET "http://localhost:6606/patients/search?q=marco" -H "accept: application/json"`


### Retorno da requisição
* `query`: Pesquisa enviada na requisição.
* `patients`: Um _array_ com todos os nomes encontrados.
* `patients_count`: Quantidade de nomes encontrados.
```json
{
    "query": "marco",
    "patients": [
        "Marco Lorenzo",
        "Marco Rodriguez",
        "Marcos Martins",
        "Marcos Montero"
    ],
    "patients_count": 4
}
```
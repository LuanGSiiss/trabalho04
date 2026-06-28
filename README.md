PROJETO ESTOQUE GERBER

## Descrição
O seguinte documento apresenta o Sistema de Estoque Gerber, sendo uma API RESTFUL feita com Python com o microframework Flask. 

O projeto utiliza práticas de desenvolvimento de software com a cultura DevOps, simulando uma base de dados através de um arquivo JSON externo e garantindo a qualidade do código com um pipeline de Integração Contínua configurado via GitHub Actions. 

## Como rodar

### Requisitos

- Pyhton instalado na versão > 3.10  ;

### Passos
*no Windows

1. Abrir o terminal na pasta principal do projeto e criar um ambiente virtual utilizando o comando "python -m venv venv", ativando-o de seguida com ".\venv\Scripts\activate".
2. Rode o comando "pip install -r api/requirements.txt" para baixar as dependencias.
3. Para rodar, basta utilizar o comando "python api/app.py";
4. Teste se as rotas estão funcionando.
5. Para rodar os testes unitarios, basta utilizar o comando "python -m pytest api/tests/".
6. Para rodar a verificação de formatação e boas práticas no código, rode o comando "python -m flake8 api/ --max-line-length=120";
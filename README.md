# Projeto Full Stack de Métricas

Aplicação web full-stack que permite os usuários carregarem uma planilha de dados de assinantes e visualizar métricas chave de negócios: Monthly Recurring Revenue (MRR) e Churn Rate em gráficos interativos.

## Resumo sobre o Frontend
O frontend deste projeto foi desenvolvido utilizando Vue.js, uma estrutura progressiva de JavaScript. Ele oferece uma interface de usuário para fazer upload de planilhas de dados de assinantes. Após o processamento dos dados no backend, exibe gráficos interativos de Monthly Recurring Revenue (MRR) e Churn Rate, permitindo uma visualização clara das métricas de negócios.

## Resumo sobre o Backend
O backend é construído em Python utilizando o framework Flask. Ele fornece uma API RESTful para processar os dados das planilhas de assinantes. Calcula o MRR e Churn Rate com base nos dados fornecidos, retornando as informações necessárias para a exibição dos gráficos no frontend.

## Passo a Passo para Instalação e Execução

Passo 1: Clonar o Repositório

```sh
git clone https://github.com/decoesp/projeto_full_stack.git
cd projeto_full_stack
```
Passo 2: Ative o ambiente virtual para o backend: 

```sh
source ambiente_backend/bin/activate 
```

Passo 3: No diretório backend, instale as dependências do Python:

```sh
pip install -r requirements.txt
```

Passo 4: No diretório backend, inicie o servidor Flask:

```sh
python app.py
```
Passo 5: No diretório frontend, instale as dependências do Node.js e Inicie o servidor Vue.js:

```sh
npm install
npm run serve
```

## Considerações Finais
Certifique-se de ter os requisitos necessários instalados (Node.js, Python, etc.). Caso encontre problemas, verifique se as portas especificadas nos arquivos de configuração (Vue.js e Flask) não estão em uso por outras aplicações. Ao acessar a aplicação no navegador, o frontend estará disponível em http://localhost:8080 e o backend em http://localhost:5000. Aqui está o arquivo de exemplo para teste: [modelo-teste-full-stack.xlsx](https://github.com/decoesp/projeto_full_stack/files/13892838/modelo-teste-full-stack.xlsx)


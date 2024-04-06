# Documentação da API

Teste Arariwe. Esta API é construída usando Django Rest Framework e fornece endpoints para gerenciar tarefas.

## Endpoints

### Autenticação

- `POST /token/`: Obtém um token JWT para autenticação.

#### Parâmetros da solicitação

| Parâmetro | Descrição         |
|-----------|-------------------|
| username  | O nome de usuário que voce criar|
| password  | senha |

### Tarefas

- `GET /tasks/`: Lista todas as tarefas.
- `POST /tasks/`: Cria uma nova tarefa.
- `GET /tasks/{id}/`: Obtém detalhes de uma tarefa específica.
- `PUT /tasks/{id}/`: Atualiza uma tarefa existente.
- `DELETE /tasks/{id}/`: Exclui uma tarefa existente.

#### Parâmetros da solicitação (para criação e atualização de tarefas)

| Parâmetro | Descrição                       |
|-----------|---------------------------------|
| titulo    | Título da tarefa                |
| prazo     | Prazo da tarefa (opcional)      |
| descricao | Descrição da tarefa (opcional)  |
| finalizada| Indica se a tarefa está finalizada (true/false) |

#### Parâmetros da resposta

| Parâmetro | Descrição                         |
|-----------|-----------------------------------|
| id        | ID da tarefa                      |
| titulo    | Título da tarefa                  |
| prazo     | Prazo da tarefa                   |
| descricao | Descrição da tarefa               |
| finalizada| Indica se a tarefa está finalizada|

## Autenticação JWT

Nao inseri endpoints protegidos para poupar o tempo, porem para acessar os endpoints protegidos, basta configurar em urls.py e os passos são: incluir o token JWT no cabeçalho `Authorization` com o valor `Bearer <seu_token_jwt>`, onde `<seu_token_jwt>` é o token JWT obtido na rota `/token/`. Basicamente é isso 


---------------------------------------------------------------------------------------------------------------------------
## Configuração do PostgreSQL

Esta aplicação requer o PostgreSQL como banco de dados. Siga estas etapas para configurar o PostgreSQL em seu ambiente de desenvolvimento:

1. **Instale o PostgreSQL**: Faça o download e instale o PostgreSQL em seu sistema a partir do [site oficial do PostgreSQL](https://www.postgresql.org/download/).

2. **Instale o adaptador PostgreSQL para Python (Psycopg2)**: Você pode instalar o Psycopg2 usando o pip:

    ```
    pip install psycopg2-binary
    ```

3. **Configuração no Django**:
   - No arquivo `settings.py` do seu projeto Django, configure as informações de conexão com o PostgreSQL no dicionário `DATABASES`. Aqui está um exemplo de configuração:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nome_do_seu_banco_de_dados',
            'USER': 'seu_usuario_do_postgresql',
            'PASSWORD': 'sua_senha_do_postgresql',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Certifique-se de substituir `'nome_do_seu_banco_de_dados'`, `'seu_usuario_do_postgresql'` e `'sua_senha_do_postgresql'` pelos valores corretos para o seu ambiente.

4. **Crie o banco de dados**: Após configurar as informações de conexão, você pode criar o banco de dados PostgreSQL executando o comando `python manage.py migrate`.

    ```bash
    python manage.py migrate
    ```

5. **Verifique a conexão**: Você pode verificar se a conexão com o PostgreSQL está funcionando corretamente executando o comando `python manage.py check`.

    ```bash
    python manage.py check
    ```

Certifique-se de revisar e adaptar as configurações conforme necessário para o seu ambiente específico.

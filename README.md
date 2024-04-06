Teste arariwe
Esta API é construída usando Django Rest Framework e fornece endpoints para gerenciar tarefas.


Endpoints
Autenticação
POST /token/: Obtém um token JWT para autenticação.
Parâmetros da solicitação
Parâmetro	Descrição
username	O nome de usuário
password	A senha do usuário
Tarefas
GET /tasks/: Lista todas as tarefas.
POST /tasks/: Cria uma nova tarefa.
GET /tasks/{id}/: Obtém detalhes de uma tarefa específica.
PUT /tasks/{id}/: Atualiza uma tarefa existente.
DELETE /tasks/{id}/: Exclui uma tarefa existente.
Parâmetros da solicitação (para criação e atualização de tarefas)
Parâmetro	Descrição
titulo	Título da tarefa
prazo	Prazo da tarefa (opcional)
descricao	Descrição da tarefa (opcional)
finalizada	Indica se a tarefa está finalizada (true/false)
Parâmetros da resposta
Parâmetro	Descrição
id	ID da tarefa
titulo	Título da tarefa
prazo	Prazo da tarefa
descricao	Descrição da tarefa
finalizada	Indica se a tarefa está finalizada
Autenticação JWT
Para acessar os endpoints protegidos, inclua o token JWT no cabeçalho Authorization com o valor Bearer <seu_token_jwt>, onde <seu_token_jwt> é o token JWT obtido na rota /token/.

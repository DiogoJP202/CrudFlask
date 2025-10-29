# CRUD Flask (Usuários)

Aplicação simples em Flask para gerenciar usuários (CRUD) com páginas HTML e endpoints REST.

## Tecnologias / Linguagens
- Python (Flask)
- HTML + CSS (templates em `templates/`)

## Estrutura do Projeto
- `app.py` – App Flask e rotas da API e páginas
- `Usuario.py` – Classe de domínio `Usuario`
- `templates/` – Páginas HTML (Home, Criar, Ver, Procurar, Atualizar, Excluir)
- `venv/` – Ambiente virtual (opcional/local)

## Pré‑requisitos
- Python 3.10+ (testado com 3.13)

## Como iniciar
1) Criar e ativar o ambiente virtual (opcional, recomendado)

Windows (PowerShell):
```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
```

macOS/Linux (bash/zsh):
```bash
python3 -m venv venv
source venv/bin/activate
```

2) Instalar dependências
```bash
pip install Flask
```

3) Executar o servidor
```bash
python app.py
```
O app sobe por padrão em `http://127.0.0.1:5000`.

## Páginas (UI)
- Home: `GET /`
- Criar usuário: `GET /criarUsuarios`
- Ver usuários: `GET /verUsuarios`
- Procurar usuário: `GET /procurarUsuario`
- Atualizar usuário: `GET /atualizarUsuario`
- Excluir usuário: `GET /excluirUsuario`

Os HTMLs ficam em `templates/` e consomem os endpoints abaixo.

## Endpoints REST
Base: `http://127.0.0.1:5000`

- Criar usuário
  - `POST /users`
  - Body JSON: `{ "nome": "Fulano", "email": "fulano@email.com" }`
  - Retornos: `201 Created` em sucesso; `400` se inválido

- Listar usuários
  - `GET /users`
  - Retorna lista de usuários: `[ { "id": 1, "nome": "...", "email": "..." }, ... ]`

- Obter usuário por id
  - `GET /users/{id}`
  - Retornos: `200` com usuário; `404` se não encontrado

- Atualizar usuário
  - `PUT /users`
  - Body esperado (conforme implementação atual): `{ "id": <id>, "nome": "...", "email": "..." }`
  - Obs.: A lógica atual cria um novo usuário ao invés de atualizar. Ajuste pode ser necessário dependendo do objetivo.

- Excluir usuário
  - `DELETE /users/{id}`
  - Retornos: `200` em sucesso; `404` se não encontrado

### Exemplos com curl
```bash
# Criar
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"nome":"Ana","email":"ana@example.com"}'

# Listar
curl http://127.0.0.1:5000/users

# Buscar por id
curl http://127.0.0.1:5000/users/1

# (Ver nota) Atualizar (conforme implementação atual)
curl -X PUT http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"id":1,"nome":"Ana Silva","email":"ana.silva@example.com"}'

# Excluir
curl -X DELETE http://127.0.0.1:5000/users/1
```

## Observações Importantes
- Os dados são mantidos apenas em memória (lista em `app.py`), e são perdidos ao reiniciar o servidor.
- Alguns textos de resposta podem exibir caracteres estranhos caso o terminal não esteja em UTF‑8.
- Para produção, considere adicionar `requirements.txt`, validações adicionais e persistência em banco de dados.

## Licença
Uso acadêmico/educacional.

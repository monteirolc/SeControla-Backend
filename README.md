###💰 Backend - Controle de Gastos
Este projeto é um backend desenvolvido em Python/Django para um sistema de controle de gastos pessoais.
Ele permite que usuários cadastrem, editem e acompanhem suas receitas e despesas, com autenticação e API REST.

###🚀 Tecnologias utilizadas
Linguagem: Python 3.11+

Framework web: Django 5+

API REST: Django REST Framework (DRF)

Banco de Dados: PostgreSQL (pode ser substituído por SQLite/MySQL)

Autenticação: JWT (via djangorestframework-simplejwt)

Outros: Django ORM, Django Environ, etc.

###⚙️ Configuração do Ambiente
#1. Clonar o repositório

```text
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

#2. Criar e ativar ambiente virtual

```text
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

#3. Instalar dependências

```text
pip install -r requirements.txt
```

#4. Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto (use .env.example como base):

```text
DEBUG=True
SECRET_KEY=sua_chave_aqui
DATABASE_URL=postgres://usuario:senha@localhost:5432/controle_gastos
ALLOWED_HOSTS=127.0.0.1,localhost
```

#5. Rodar migrações e iniciar servidor

```text
python manage.py migrate
python manage.py runserver
```

### Estrutura

backend/

├── balance/ # app principal -> "conta geral"

│ ├── models.py # saldo consolidado

│ └── ...

├── expenses/ # gastos eventuais

│ ├── models.py

│ └── ...

├── fixed_expenses/ # gastos recorrentes

│ ├── models.py

│ └── ...

├── incomes/ # ganhos eventuais

│ ├── models.py

│ └── ...

├── shared_accounts/ # vínculo entre usuários

│ ├── models.py

│ └── ...

└── login/ # seu CustomUser

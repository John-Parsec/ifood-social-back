# ifood-social-back
# ifood-social-back
Repositório para a criação do módulo Cliente para o projeto da disciplina Engenharia de Software

## Dependências
Para executar este projeto, você precisará das seguintes dependências:

- Python 3
- Django
- Django REST framework

## Instalação
Siga estes passos para instalar o projeto:

1. Clone o repositório:
    ```bash
    git clone https://github.com/John-Parsec/ifood-social-back.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd ifood-social-back
    ```

3. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

6. O servidor estará rodando em `http://localhost:8000`.

Certifique-se de ter o Python 3 e o Django instalados antes de prosseguir com os passos de instalação.
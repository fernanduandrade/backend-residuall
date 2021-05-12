# backend-residuall  

Backend para realizar validação de emails, utilizando django como servidor e MySQl para salvar os emails!

## :heart: Pode usar tanto uma virtual environment ou docker

### :computer: Com virtual environment:

Tenha o python e pip instalado na sua máquina e execute os seguintes comandos para criar e ativar o virtual environment.

<li>No Linux

   ```sh
   python -m venv nome_da_virtualenv
   source nome_da_virtualenv/bin/activate
   ```

</li>

<li>No Windows

   ```sh
   python -m venv nome_da_virtualenv
   nome_da_virtualenv\Scripts\activate.bat
   ```

</li>

<li>No Mac
   
   ```sh
   python -m venv nome_da_virtualenv
   source nome_da_virtualenv/bin/activate
   ```

</li>

<li>Por fim dentro do diretório onde contém o arquivo requirements.txt

```sh
(nome_da_virtualenv)pip install -r requirements.txt
```
    
</li>

**Realize o migrate para que o banco de dados crie as tabelas**

```sh
(nome_da_virtualenv) python manage.py migrate
```
**Inicie o servidor**

```sh
python manage.py runserver 8080
```


### :computer: Com docker:

<li>Dentro do diretório onde contém o arquivo docker-compose.yml execute o seguinte comando

```sh
docker-compose up
```
    
</li>


## Entendendo a API

Os endpoints da API são:

|Rotas| Método | Descrição |
|---|---|---|
|`http://localhost:8080/`| `GET` | Retorna uma array vazia . |
|`http://localhost:8080/health`| `GET` | Retorna um json informando que o servidor está rodando . |
|`http://localhost:8080/mail/v1`| `GET` | Retorna todos registros para o primeiro tipo de validação . |
|`http://localhost:8080/mail/v1?`| `GET` | Retorna o todos match da query string para o primeiro tipo de validação. |
|`http://localhost:8080/mail/validation/v1`| `POST` | Cadastra um novo email para o primeiro tipo de validação. |
|`http://localhost:8080/mail/v3`| `GET` | Retorna todos registros para o segundo tipo de validação . |
|`http://localhost:8080/mail/v3?`| `GET` | Retorna o todos match da query string para o segundo tipo de validação. |
|`http://localhost:8080/mail/validation/v3`| `POST` | Cadastra um novo email para o segundo tipo de validação. |

+ Exemplo da Resquest/POST (application/json) para rota /mail/validation/v1

+ Body 
    ```text
    {
        "email_address": "user@gmail.com",
        "domain": "gmail.com"
    }
    ```
+ Response 

    ```text
    {
        "status": "ok",
        "code": 200,
        "results": [{
            "email_address": "user@gmail.com",
            "domain": "gmail.com",
            "valid_syntax": true
        }]
    }
    ```

+ Exemplo da Resquest/POST (application/json) para rota /mail/validation/v3
+ Body 
    ```text
    {
        "email_address": "user@gmail.com"
    }
    ```
+ Response 

    ```text
    {
        "status": "ok",
        "code": 200,
        "results": [{
            "data": {
                "email_address": "user@gmail.com",
                "domain": "gmail.com",
                "valid_syntax": true,
                "disposable": false,
                "webmail": false,
                "deliverable": false,
                "catch_all": false,
                "gibberish": false,
                "spam": false
            }
        }]
    }
    ```

## :notebook: Notas
<ol>

<li>
Você deve configurar a conexão com banco de dados, caso você esteja usando virtual environment, se estiver utilizando docker já estará pré configurado

Configure o banco de dados no `settings.py` no diretório `eva/`

```text
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DOBANCODEDADOS',
            'USER': 'USUARIO',
            'PASSWORD': 'SUASENHA',
            'HOST': 'localhost',
            'PORT': '3306'
    }
}
```
</li>
<li>Não consegui implementar o envio de arrays</li>
<li>Docker não foi testado no sistema operacional windows</li>
</ol>


## :mailbox_with_mail: License
Feel free to try it out.

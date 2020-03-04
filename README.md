##Teste Consultoria - Synergia 

- Criar a modelagem relacional a partir da planilha (arquivo excel)
- Normalizar os dados da maneira que achar adequada
- Criar um importador que faça o processamento da planilha
- Faça as validações que achar necessário
- Faça o processamento ocorrer em segundo plano (usando celery)
- Criar um endpoint (django-rest) dos dados importados
- Faça a autenticação do endpoint que retorne um token para acesso
- Uma vez logado, faça uma paginação para disponibilizar a listagem de demandas cadastradas
- Criar um template para apresentar as demandas cadastradas
- Criar uma tabela usando bootstrap que apresente os dados
- Criar fixture das categorias

##Instalação

```
pip install -r requirements.txt
python manager.py migrate
python manager.py loaddata category 
```

###Criar as variaveis de ambiente, segue exemplo 

```
export DB_USER=postgres
export DB_NAME=test007
export DB_PASS=1234
export DB_HOST=localhost

export USER_NAME=carlos
export USER_EMAIL=carlos@gmail.com
export USER_PASS=1234

export CELERY_USER=user
export CELERY_PASS=bitnami
export CELERY_SERVER=localhost
```

###Rodar o Projeto

```
python manager.py runserver 0.0.0.0:8000
```
###Observações

Utilizei docker para rodar o banco de dados  e RabbitMQ

####docker-compose.yml  banco 

```
version: '2'

services:
  postgresql:
    image: 'bitnami/postgresql:11'
    ports:
      - '5432:5432'
    volumes:
      - 'postgresql_data:/bitnami/postgresql'
    environment:
      - POSTGRESQL_PASSWORD=1234

volumes:
  postgresql_data:
    driver: local
```

#### docker-compose.yml  RabbitMQ 
```
version: '2'

services:
  rabbitmq:
    image: 'bitnami/rabbitmq:3.8'
    ports:
      - '4369:4369'
      - '5672:5672'
      - '25672:25672'
      - '15672:15672'
    volumes:
      - 'rabbitmq_data:/bitnami'
volumes:
  rabbitmq_data:
    driver: local
```


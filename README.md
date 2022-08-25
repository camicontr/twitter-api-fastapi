# Twitter-Api

## Introduction 
This application is the final project of the [**Curso de FastAPI: Modularización, Datos Avanzados y Errores**](https://platzi.com/cursos/fastapi-modularizacion-datos/) course of platzi. This app simulates the basic functions of twitter as well as adding tweet updates

## Depedencies
Dependencies for Docker:
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Installation
### Clone the repository
First you need to clone the repository.

```bash
git clone https://github.com/camicontr/twitter-api-fastapi.git
```

### Docker Installation
To install twitter-api-fastapi on a docker container, run the following command:

```bash
docker compose --env-file .env up
```

## Usage
### Running the API
To run the API in the Docker container, run the following command:

Configure the server in pgadmin
1. Go into pgadmin localhost:80, with user: admin@admin.com and password: admin
2. Register a new server with name: DockerConnect, hostname: db, user and password: postgres
3. Use
```bash
docker start twitter-api-fastapi_app
```

At this moment the app can already connect to the database

4. Go into 
```bash
http://localhost:8000/docs
```

here you will find all the documentation and you can use the api.

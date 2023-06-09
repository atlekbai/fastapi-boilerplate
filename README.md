# FastAPI + MongoDB Boilerplate

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/WleFVe?referralCode=UBd_g_)

This is a FastAPI boilerplate, which includes includes:

- MongoDB as database
- Bcrypt for password hashing
- JWT for user token management and verification
- Dockerfile and docker-compose files for easy deployment
- CORS Middleware configuration

## 📚 Features

1. User registration.
2. User authentication and token creation.
3. User verification and token validation.
4. Encrypted password management.

## 🚀 Quick Start

You'll need Docker and Docker Compose to run this application.

1. Clone the repository

```bash
git clone https://github.com/atlekbai/fastapi-boilerplate.git
```

2. Navigate to the directory

```bash
cd fastapi-boilerplate
```

3. Run the application

```bash
docker-compose up -d
```

Copy environment configurations and edit the file.

```bash
cp .env.example .env
```

Export environmental configurations.

```bash
export $(cat .env)
```

Start the FastAPI server.

```bash
poetry install
poetry shell
sh ./scripts/launch.sh
```

This command will start the FastAPI server on port 8000 and the MongoDB service on port 27017. You can navigate to `http://localhost:8000/docs` in your browser to access the automatically generated API documentation.

## 📚 Project Structure

The main sections of the project are:

- `app/main.py`: This is the entry point of the application.
- `app/config.py`: This file contains the global configuration of the application.
- `app/auth`: This folder contains the logic related to the authentication system.
- `app/auth/service.py`: Contains the service layer logic for the authentication system.
- `app/auth/repository`: Contains the logic for interacting with the MongoDB database.
- `app/auth/router`: Contains the routing logic for the authentication API.
- `app/auth/adapters`: Contains the JWT management logic.
- `app/auth/utils`: Contains utility functions, such as password hashing.

## 🛠️ Development

### Install Dependencies

This project uses poetry for dependency management. To install the dependencies, run:

```bash
poetry install
```

### Launch the Application

This project includes a script to launch the application, which can be started with:

```bash
sh ./scripts/launch.sh
```

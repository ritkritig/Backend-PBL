# Backend Development PBL – FastAPI with Docker & CI/CD

## Project Overview

This project demonstrates the containerization and automated deployment of a FastAPI application using Docker, Docker Compose, automated API testing, GitHub Actions, and Docker Hub.

The application provides a simple Student API with endpoints to check the application status, health status, and retrieve student information.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub
- Python Requests

## Project Structure

```text
Backend-PBL/
├── .github/
│   └── workflows/
│       └── docker-publish.yml
├── .dockerignore
├── Dockerfile
├── automationTesting.py
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns application name, framework, and status |
| GET | `/health` | Returns application health status |
| GET | `/students` | Returns the list of students |

## Run Using Docker

Build the Docker image:

```bash
docker build -t student-api-fastapi:1.0 .
```

Run the container:

```bash
docker run --name student-fastapi -p 8000:8000 student-api-fastapi:1.0
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

## Run Using Docker Compose

Build and start the application:

```bash
docker compose up --build
```

To run it in the background:

```bash
docker compose up -d
```

To stop and remove the Compose containers:

```bash
docker compose down
```

## Automated Testing

The `automationTesting.py` script automatically tests the following routes:

- `/`
- `/health`
- `/students`

Run the tests using:

```bash
python automationTesting.py
```

Successful execution produces:

```text
Root route test passed
Health route test passed
Students route test passed
All automated tests passed!
```

## CI/CD Using GitHub Actions

A GitHub Actions workflow is configured to run automatically when code is pushed to the `main` branch.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Starts the FastAPI application.
5. Executes the automated API tests.
6. Logs in to Docker Hub securely using GitHub Secrets.
7. Builds the Docker image.
8. Pushes the image to Docker Hub.

This ensures that the application is tested before the Docker image is published.

## Docker Hub

The Docker image is published as:

```text
ritkriti/backend-pbl:latest
```

It can be pulled using:

```bash
docker pull ritkriti/backend-pbl:latest
```

It can then be run using:

```bash
docker run -p 8000:8000 ritkriti/backend-pbl:latest
```

## PBL Requirements Implemented

- FastAPI application
- Application containerized using Dockerfile
- Docker Compose configuration
- Automated route testing
- GitHub Actions CI/CD workflow
- Automatic Docker image build
- Automatic image push to Docker Hub

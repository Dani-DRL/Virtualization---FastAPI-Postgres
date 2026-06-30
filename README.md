# Task Management API

REST API built with FastAPI and PostgreSQL, containerized with Docker Compose.

## Requirements

- Docker + Docker Compose

## Running the project

```bash
docker compose up --build
```

API available at `http://localhost:8080`

```bash
docker compose down      # stop
docker compose down -v   # stop and clear the database
```

## Endpoints

### HTTP methods and routes

- `GET /tasks/` - Hello from the FastAPI
- `POST /tasks/create/` - Creates a task with a JSON as the payload
- `GET /tasks/{id}` - Retrieves info from a task by id
- `PUT /tasks/{id}/complete` - Mark a task as completed
- `DELETE /tasks/{id}/delete` - Delete a task by id
- `GET /tasks/overdue` - List of overdue tasks

### Create task — request body

```json
{
  "name": "Example 1",
  "content": "Description of the task",
  "deadline": "2030-09-30"
}
```

Deadlines in the past are rejected with `400 Bad Request`. Tasks not found return `404 Not Found`.

## Documentation

Once the containers are running, you can access the documentation:
- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`

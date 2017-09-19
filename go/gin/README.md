# structure of Todo object
```json
{
    "title": "<string>",
    "completed": "<int>"
}
```

# Behavior
| method | path       | behavior         |
|--------|------------|------------------|
| POST   | /todos/    | create new todo  |
| GET    | /todos/    | List all todos   |
| GET    | /todos/:id | Show single todo |
| PUT    | /todos/:id | Update todo      |
| DELETE | /todos/:id | Remove a todo    |

## POST new todo
```
curl -X POST -F "title=PostNewTodo" -F "completed=0" http://localhost:8080/todos/
```

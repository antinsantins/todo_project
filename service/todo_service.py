from entity.todo_task import TodoTask


class TodoService:
    todos: list[TodoTask]

    def __init__(self) -> None:
        super().__init__()
        self.todos = list()

    def get_todos(self, completed: bool = None) -> list[TodoTask]:
        not_deleted = [todo for todo in self.todos if todo.deleted is False]
        if completed is None:
            return not_deleted
        return [todo for todo in self.todos if todo.completed is completed]

    def add_todo(self, title: str) -> TodoTask:
        todo = TodoTask(len(self.todos), title)
        self.todos.append(todo)
        return todo

    def update_completed(self, id: int, title: str, completed: bool) -> TodoTask:
        for todo in self.todos:
            if todo.id == id:
                todo.title = title
                todo.completed = completed
                return todo
        return 404

    def delete(self, id: int):
        for todo in self.todos:
            if todo.id == id:
                todo.deleted = True

    def delete_all(self):
        self.todos = [todo for todo in self.todos if todo.completed is False]

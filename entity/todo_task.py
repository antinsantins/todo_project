from dataclasses import dataclass


@dataclass
class TodoTask:
    id: int
    title: str
    completed: bool
    deleted: bool

    def __init__(self, id: int, title: str, completed=False, deleted=False) -> None:
        super().__init__()
        self.id = id
        self.title = title
        self.completed = completed
        self.deleted = deleted


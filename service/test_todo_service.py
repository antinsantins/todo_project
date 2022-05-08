from unittest import TestCase
from entity.todo_task import TodoTask
from service.todo_service import TodoService


class TestTodoService(TestCase):
    todo_service: TodoService

    def setUp(self):
        self.todo_service = TodoService()

    def test_get_todos(self):
        self.todo_service.add_todo("asd")
        actual_list = self.todo_service.get_todos()
        expected_list = [
            TodoTask(0, "asd")
        ]
        self.assertListEqual(actual_list, expected_list)

    def test_update_completed(self):
        self.todo_service.add_todo("Поездка")
        self.todo_service.update_completed(0, "Поездка в Санкт-Петербург", completed=False)
        actual_list = self.todo_service.get_todos()
        expected_list = [
            TodoTask(0, "Поездка в Санкт-Петербург")
        ]
        self.assertListEqual(actual_list, expected_list)

    def test_deleted(self):
        self.todo_service.add_todo("Сходить в магазин")
        self.todo_service.delete(0)
        actual_list = self.todo_service.get_todos()
        expected_list = [

        ]
        self.assertListEqual(actual_list, expected_list)

    def test_deleted_all(self):
        self.todo_service.add_todo("Сходить погулять")
        # self.todo_service.add_todo("Позаниматься спортом")
        self.todo_service.update_completed(0, "Сходить погулять", completed=True)
        # self.todo_service.update_completed(1, "Позаниматься спортом", completed=True)
        self.todo_service.delete_all()
        actual_list = self.todo_service.get_todos()
        expected_list = [

        ]
        self.assertListEqual(actual_list, expected_list)

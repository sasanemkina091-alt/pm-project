"""Тесты для TaskService (изолированные)."""
from tasks import Task, TaskService

class FakeTaskRepository:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)

def test_create_task():
    repo = FakeTaskRepository()
    service = TaskService(repo)
    service.create_task("Сделать отчет")
    assert len(repo.tasks) == 1

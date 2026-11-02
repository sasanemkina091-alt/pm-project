"""Модель задачи."""

class Task:
    def __init__(self, title: str, status: str = "Новая"):
        self.title = title
        self.status = status

    def __repr__(self):
        return f"Task({self.title}, {self.status})"

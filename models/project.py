"""Модель проекта."""

class Project:
    def __init__(self, title: str, deadline: str):
        self.title = title
        self.deadline = deadline

    def __repr__(self):
        return f"Project({self.title})"

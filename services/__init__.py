
"""Сервис проектов."""

class ProjectService:
    """Класс для управления проектами."""
    
    def __init__(self, repo):
        self.repo = repo

    def create_project(self, title: str, deadline: str):
        """Создает новый проект."""
        # TODO: добавить валидацию и сохранение в БД
        return f"Проект {title} создан с дедлайном {deadline}"

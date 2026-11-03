"""Модуль работы с задачами."""
from .models import Task
from .service import TaskService

__all__ = ["Task", "TaskService"]

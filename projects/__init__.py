"""Модуль работы с проектами."""
from .models import Project
from .service import ProjectService

__all__ = ["Project", "ProjectService"]

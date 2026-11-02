# Модель проекта
class Project:
    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return f"Project({self.title})"

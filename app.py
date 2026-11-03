
"""Точка входа приложения «ProjectFlow»."""
from flask import Flask

def create_app() -> Flask:
    """Создает и настраивает приложение."""
    app = Flask(__name__)
    
    @app.route("/")
    def index():
        return "<h1>Система управления проектами ProjectFlow</h1>"
        
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

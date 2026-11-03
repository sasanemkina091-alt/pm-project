"""Проверка, что приложение запускается."""

def test_index_page(client):
    """Главная страница возвращает 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "ProjectFlow" in response.data.decode("utf-8")

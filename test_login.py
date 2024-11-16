import requests

BASE_URL = "https://dev.admin.sum-up.online/api"

def test_login():
    response = requests.post(f"{BASE_URL}/auth/token", json={"clientId": "test1","clientSecret": "WGEdJR9VpVnxmk0R0D4G7EFYWjb2WYZy"})

    data = response.json()

    assert response.status_code == 201
    assert "accessToken" in data
    assert "expiresIn" in data, "Поле 'expiresIn' отсутствует в ответе"
    assert data["expiresIn"] == 36000, f"Ожидалось значение '36000', но получено: {data['expiresIn']}"
import requests

BASE_URL = "http://localhost:8000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    print("Root route test passed")

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("Health route test passed")

def test_students():
    response = requests.get(f"{BASE_URL}/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print("Students route test passed")

if __name__ == "__main__":
    test_root()
    test_health()
    test_students()
    print("All automated tests passed!")
import requests

class APIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url

    def get_question(self, question_id: int):
        response = requests.get(f"{self.base_url}/api/{question_id}")
        if response.status_code == 200:
            return response.json()
        return None

    def create_question(self, question_data: dict):
        response = requests.post(f"{self.base_url}/api/", json=question_data)
        if response.status_code == 200:
            return response.json()
        return None

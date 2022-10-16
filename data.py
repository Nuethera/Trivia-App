import requests

PARAMETER = {
    "amount": 10,
    "type": "boolean",
    "difficulty": None
}

class QuestionBank:
    def __init__(self):
        response = requests.get("https://opentdb.com/api.php", params=PARAMETER)
        response.raise_for_status()
        data = response.json()
        self.question_data = data["results"]



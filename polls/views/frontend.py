import requests
from django.shortcuts import render

FASTAPI_URL = "http://127.0.0.1:40069"

# Displays all questoins
def index(request):
    response = requests.get(f"{FASTAPI_URL}/questions/") 
    questions = response.json()
    return render(request, "polls/index.html", {"questions": questions})

# Display a single question and its choices
def detail(request, question_id):
    question_response = requests.get(f"{FASTAPI_URL}/questions/{question_id}")
    choice_response = requests.get(f"{FASTAPI_URL}/questions/{question_id}/choices/")
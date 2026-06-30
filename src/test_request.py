from datetime import datetime
from datetime import date
import requests
from datetime import datetime

# Landing Page for Testing Purposes
print("\n\n\n" + 20*"*" + "\nLETS TRY THIS API\n" + 20*"*")
response = requests.get("http://localhost:8000/tasks/")
print(response.status_code, response.content)
assert response.status_code == 200, "The landing page in the up should be working"



# Create some tasks and add them, one will fail
print("\n\n\n" + 20*"*" + "\nCREATE TASKS\n" + 20*"*")

task_a = {
    "name": "Study for the exam",
    "content": "Catch up with the AWS SAA cert by viewing Cantrill course",
    "deadline": "2026-08-30"
  }

task_b = {
    "name": "Assignment PontIA",
    "content": "Complete the advanced programming FastAPI challenge",
    "deadline": "2026-06-29"
  }

task_c = {
    "name": "Mock task with a deadline in the past",
    "content": "Fails when you try to create this task",
    "deadline": "2024-01-01"
  }

response = requests.post("http://localhost:8000/tasks/create/", json=task_a)
print(response.status_code, "\n",response.content)
assert response.status_code == 201, "expected 201 when creating a valid task"
task_a_id = response.json()["id"]
assert response.json()["name"] == task_a["name"]
assert response.json()["content"] == task_a["content"]
assert response.json()["deadline"] == task_a["deadline"]




response = requests.post("http://localhost:8000/tasks/create/", json=task_b)
print(response.status_code, "\n",response.content)
assert response.status_code == 201, "expected 201 when creating a valid task"
task_b_id = response.json()["id"]
assert response.json()["name"] == task_b["name"]
assert response.json()["content"] == task_b["content"]
assert response.json()["deadline"] == task_b["deadline"]

response = requests.post("http://localhost:8000/tasks/create/", json=task_c)
print(response.status_code, "\n",response.content)
assert response.status_code == 400, "expected 400 when creating a task with an invalid deadline"
# No id since this task won't be created since its deadline is overdue



# For the created tasks, lets retrieve them
print("\n\n\n" + 20*"*" + "\nGET TASKS\n" + 20*"*")

response = requests.get(f"http://localhost:8000/tasks/{task_a_id}")
print(response.status_code, "\n",response.content)
assert response.status_code == 200, "expected 200 when retrieving a valid task"
assert response.json()["id"] == task_a_id
assert response.json()["name"] == task_a["name"]
assert response.json()["content"] == task_a["content"]
assert response.json()["deadline"] == task_a["deadline"]


response = requests.get(f"http://localhost:8000/tasks/{task_b_id}")
print(response.status_code, "\n",response.content)
assert response.status_code == 200, "expected 200 when retrieving a valid task"
assert response.json()["id"] == task_b_id
assert response.json()["name"] == task_b["name"]
assert response.json()["content"] == task_b["content"]
assert response.json()["deadline"] == task_b["deadline"]



# Completing one of those tasks
print("\n\n\n" + 20*"*" + "\nCOMPLETE TASK\n" + 20*"*")

response = requests.put(f"http://localhost:8000/tasks/{task_a_id}/complete")
print(response.status_code, "\n",response.content)
assert response.status_code == 200, "expected 200 when completing a valid task"
assert response.json()["is_completed"] is True, "task should be marked as complete"


# Get overduetasks
print("\n\n\n" + 20*"*" + "\nOVERDUE TASKS\n" + 20*"*")
response = requests.get("http://localhost:8000/tasks/overdue")
print(response.status_code, "\n",response.content)
assert response.status_code == 200, "expected 200 when retrieving overdue tasks, even if its empty"

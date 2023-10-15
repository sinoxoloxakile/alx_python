import json

# Assuming you have a dictionary called 'all_tasks' that contains all tasks from all employees
# with the structure: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

# Convert the dictionary to a JSON string
json_data = json.dumps(all_tasks)

# Write the JSON string to a file
with open('todo_all_employees.json', 'w') as json_file:
    json_file.write(json_data)
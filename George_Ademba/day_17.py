task=[
    {"activity":"cleaning","supervisor":"John","status":"incomplete"},
    {"activity":"cooking","supervisor":"Sam","status":"incomplete"},
    {"activity":"washing","Supervisor":"Mary","status":"incomplete"}
]
for tasks in task:
    tasks["status"]=["complete"]
print(task)
new_task=[{"activity":"shopping","supervisor":"Jane","status":"incomplete"}]
task.append(new_task)

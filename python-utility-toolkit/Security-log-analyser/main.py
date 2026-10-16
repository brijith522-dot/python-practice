#Security log analyser
logs=[
    "alice SUCCESSFUL LOGIN",
    "bob SUCCESSFUL LOGIN",
    "bob SUCCESSFUL LOGIN",
    "charlie SUCCESSFUL LOGIN",
    "bob SUCCESSFUL LOGIN"
]
success_count=0
failed_count=0
for log in logs:
    if "SUCCESSFUL LOGIN" in log:
        success_count+=1
    elif "FAILED LOGIN" in log:
        failed_count+=1
    if failed_count>2:
        print("ALERT: More than 2 failed login attempts detected!")

total_attempts=success_count+failed_count
print("Total login attempts:", total_attempts)
print("Successful logins:", success_count)
print("Failed logins:", failed_count)
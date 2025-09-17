task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: You have a high-priority task '{task}'. Please address it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: You have a medium-priority task '{task}' that is time-bound. Please plan to complete it soon.")
        else:
            print(f"Reminder: You have a medium-priority task '{task}'. Consider scheduling time for it.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' that is time-bound. Try to complete it when you can.")
        else:
            print(f"Note: '{task}'is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
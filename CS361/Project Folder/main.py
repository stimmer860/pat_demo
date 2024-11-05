reminders = []

def create_full():
    task = input("\nTask: ")
    date = input("Date (MM/DD/YYYY): ")
    time = input("Time (HR:MIN): ")
    reminders.append({"task": task, "date": date, "time": time})
    print("Reminder successfully created.\n")

def create_quick():
    time = input("Set an alarm for later today (HR:MIN): ")
    reminders.append({"task": "Alarm", "date": "Today", "time": time})
    print("Reminder successfully created.\n")

def create():
    print("\n1. Create a full reminder")
    print("2. Create a quick reminder")
    create_choice = input("Please select an option (1/2): ")
    match create_choice:
        case "1":
            create_full()
        case "2":
            create_quick()

def view():

    if (reminders == []):
        print("\nNo reminders to show!\nReturning to menu...\n")
        return
    else:
        print("\n----------------------")
        i = 1
        for reminder in reminders:
            print("Reminder " + str(i) + ":")
            print("  - Task: " + reminder["task"])
            print("  - Date: " + reminder["date"])
            print("  - Time: " + reminder["time"] + " o'clock")
            print("----------------------")
            i += 1

    print("1. Delete a reminder\n2. Sort by Date\n3. Return to Menu")
    view_choice = input("Please select an option (1/2/3): ")

    match view_choice:
        case "1":
            delete()
        case "3":
            return

def delete():
    index = int(input("Please select a reminder to delete: ")) - 1
    delete_choice = input("Are you sure you would like to delete this reminder? Changes are permanent. (Y/N): ")

    if (delete_choice == "Y"):
        reminders.pop(index)
        print("Reminder successfully deleted.")
    else:
        print("Reminder not deleted.")

    delete_choice = input("Would you like to delete another reminder? (Y/N): ")
    match delete_choice:
        case "Y":
            delete()
        case "N":
            view()

def help():
    print("\nThe Create a Reminder menu option lets you create reminders with a task description, a date, and a time you will be notified at.")
    print("The View Reminders menu option lets you view a numerical list of reminders you've created.")
    print("Within the View Reminders screen, the Delete menu option will allow you to permanently remove a reminder you've made.")
    print("Meanwhile, the Return to Menu option will take you back to the main menu.")
    print("From the main menu, the Quit menu option will exit the program.\n")
    return


while True:
    print("Welcome! Use this app to create and view reminders so you never have to worry about forgetting something again!")
    print("1. Create a Reminder\n2. View Reminders\n3. Help\n4. Quit")
    choice = input("Please select an option (1/2/3/4): ")

    match choice:
        case "1":
            create()
        case "2":
            view()
        case "3":
            help()
        case "4":
            break
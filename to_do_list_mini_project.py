to_do_list = []
completed_task = []
flag = True

while flag:
        user_input = int(input('''What would you like to do?
    1 - Add a task
    2 - View task
    3 - Mark task as complete
    4 - Delete task
    5 - Quit
    '''))
        if user_input == 1:
            add = input("What would you like to add?")
            to_do_list.append(add)
            done = input("add another task or back to options: ")
            if done == 'add':
                add_more = input("What else?: ")
                to_do_list.append(add_more)
            elif done == 'back':
                continue
        elif user_input == 2:
            print(to_do_list)
            print(f"Complete: {completed_task}")
        elif user_input == 3:
             print(to_do_list)
             is_complete = input("What would you like to mark as complete?")
             completed_task.append(is_complete)
             to_do_list.remove(is_complete)
             for i in range(len(completed_task)):
                  if completed_task[i] == is_complete:
                       completed_task[i] += " [X]"
                       print(completed_task)
        elif user_input == 4:
            print(to_do_list)
            remove = input("What would you like to remove?")
            to_do_list.remove(remove)
        elif user_input == 5:       # was number 4
            flag = False
            print(f"This is your to do list: {to_do_list}")
            print(f"Your completed task: {completed_task}")
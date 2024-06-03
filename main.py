import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos_list = functions.get_todos()

        todos_list.append(todo + '\n')

        functions.write_todos(todos_list)

    elif user_action.startswith("show"):
        todos_list = functions.get_todos()

        for index, item in enumerate(todos_list):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            num = int(user_action[5:])
            number = num - 1

            todos_list = functions.get_todos()

            new_todo = input("Enter new to-do: ")
            todos_list[number] = new_todo + '\n'

            functions.write_todos(todos_list)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos_list = functions.get_todos()

            index = number - 1
            todo_toRemove = todos_list[index].strip('\n')
            todos_list.pop(index)

            functions.write_todos(todos_list)

            message = f"To-do {todo_toRemove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")

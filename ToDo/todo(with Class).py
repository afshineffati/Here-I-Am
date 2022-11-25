import json

todo_list = []

class Task:
    type = "todo"
    def __init__(self, title, priority, date):
        self.title = title
        self.priority = priority
        self.date = date


# def save():
#     with open("data.json", 'w') as datafile:
#         json.dump(todo_list, datafile)


def add_task(title, priority):
    from datetime import date
    task = Task(title, priority, date.today())
    todo_list.append(task)


def show_all():
    for i in todo_list:
        print(f'\nTitle: {i.title}')
        print(f'Priority: {i.priority}')
        print(f'Create: {i.date}\n')


def main():

    add_task("book dr appointment", "high")
    add_task("send tax bill", "low") 
    show_all()
    # save()


if __name__ == '__main__':
    main()
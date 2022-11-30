import json

data = {}

# class Task:
#     type = "todo"
#     def __init__(self, title, priority, date):
#         self.title = title
#         self.priority = priority
#         self.date = date


# def save():
#     with open("data.json", 'w') as datafile:
#         json.dump(todo_list, datafile)


def new_list(name):
    with open('data.json', mode='wt', encoding='utf-8') as df:
        data[name] = {}
        json.dump(data, df)


# def add_task(title, priority):
#     from datetime import date
#     todo_list = Task(title, priority, date.today())


# def show_all():
#     for i in todo_list:
#         print(f'\nTitle: {i.title}')
#         print(f'Priority: {i.priority}')
#         print(f'Create: {i.date}\n')


def main():
    new_list("todo list")
    # new_list("todo_list")
    # add_task("book dr appointment", "high")
    # add_task("send tax bill", "low") 
    # show_all()
    # save()


if __name__ == '__main__':
    main()
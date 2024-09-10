from dataclasses import dataclass as dc
from random import randint as rnd
from msvcrt import getch as any_key


def resave_tasks():
    all_tasks_string = ""
    names = []
    for i in all_tasks:
        all_tasks_string += str("{0};{1};{2};;".format(i.name, i.description, i.prior))
    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.write(all_tasks_string)

def save_new_task():
    all_tasks_string = ""
    names = []
    for i in all_tasks:
        all_tasks_string += str("{0};{1};{2};;".format(i.name, i.description, i.prior))
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(all_tasks_string)

def load_tasks():  #Считывание всех существующих задач из текстового файла
    try:
        with open('tasks.txt', encoding="utf-8") as file:
            tasks_list = file.read().split(sep=";;")
            tasks_list = tasks_list[:-1]
            taskss_lisst = []
            for i in tasks_list:
                taskss_lisst.append(i.__str__().split(';'))
            return taskss_lisst
    except FileNotFoundError:
        print("Не нашёл файл")
        with open("tasks.txt", "w", encoding="utf-8") as file:
            file.write("")


def input_task():  ##Ввод новой задачи
    print("\n --- ",pool_string[1]," ---\n")
    name = input("Введите имя:")
    description = input("Описание:")
    prior = 1
    return Task(name, description, prior)


def get_random_task():  #Вывод рандомной задачи
    got_task = (all_tasks[rnd(0, (len(all_tasks))) - 1])
    # print(got_task.__dict__)
    #
    name, discr, prior = got_task.name, got_task.description, got_task.prior
    print("\n--- Твоя задача на сегодня ---:\n\n{0}\n{1}".format(name, discr))

def print_task(a):
    task_list = load_tasks() #task_list существует для того, чтобы заполнить список задач all_tasks
    all_tasks.clear()
    for i, b, c in task_list: #Вот здесь происходит заполнение списка
        names.append(str(i).upper())
        all_tasks.append(Task(i, b, c))
    if a != 2:
        print("\n --- ",pool_string[a]," ---\n")
        #2 - 'Имеющиеся задачи',
        #3 - 'Выберите задачу:',
        #4 - 'Меняем задачу:',
        index = 0
        for i in all_tasks:
            index += 1
            print("{0}. {1}".format(index, i.name))
        print()

def doing_list_func(): #Функция отображения возможных действий
    for i in doing_list:
        f = doing_list.index(i)
        print(str(f) + ".", i) if f != 0 else print('\n ---', i, '---\n')
    print()

names = []
pool_string = ['Выберите задачу', #0
               'Создайте задачу', #1
               'Изменяемая задача:',                #2
               'Имеющиеся задачи',#3
               'Какую задачу хотите изменить?',#4
               'Какую задачу удалить?']#5
doing_list = ['Что будем делать?',
              'Добавить задачу',
              'Вывести задачу на день',
              'Показать задачи',
              'Изменить задачу',
              'Удалить задачу']

def rename_task(num_num):
    tusk_tusk = all_tasks[num_num].name, all_tasks[num_num].description
    print("\n{1} {0}\n".format(tusk_tusk[0], pool_string[2]))
    name = input("Введите имя:")
    if name == "":
        print("Имя задачи без изменений: {0}".format(tusk_tusk[0]))
        name = tusk_tusk[0]
    description = input("Описание:")
    if description == "":
        print("Описание без изменений: {0}".format(tusk_tusk[1]))
        description = tusk_tusk[1]
    prior = 1
    new_task = name, description, prior
    all_tasks[num_num].name, all_tasks[num_num].description, all_tasks[num_num].prior = new_task
    print("Задача изменена\n")
    print(all_tasks[num_num])

def delete_task(num_num):
    tusk_tusk = all_tasks[num_num].name, all_tasks[num_num].description
    print("\n{1} {2}. {0}\n".format(tusk_tusk[0], pool_string[5], num_num+1))
    all_tasks.pop(num_num)
    print("Задача удалена\n")

def what_to_do():  #Выбор, что делаем
    z = 1
    task_list = load_tasks()
    while z == 1:
        doing_list_func()
        try:

            doing = input()
            case_ind = int(doing)
        except:
            doing = 0
        match doing:
            case 0:
                print("\n!!! Пока не умею такое распознавать, извини !!!")
            case "1":
                all_tasks.clear()
                task_list.clear()
                all_tasks.append(input_task())
                save_new_task()
            case "2":
                print_task(case_ind)
                get_random_task()
                z = 0
            case "3":
                print_task(case_ind)
            case "4":
                print_task(case_ind)

                try:
                    task_choose_input = input()
                    task_choose = int(task_choose_input)
                except:
                    task_choose = str(task_choose_input)

                # print(isinstance(task_choose,int))
                if isinstance(task_choose, int):
                    if task_choose >= 0 and task_choose <= len(all_tasks):
                        task_num = task_choose - 1
                        rename_task(task_num)
                        resave_tasks()
                        all_tasks.clear()
                        task_list.clear()
                elif isinstance(task_choose, str) and task_choose.upper() in names:
                    print('\nЕБАТЬ!!!!')
                    task_num = names.index(task_choose.upper())
                    rename_task(task_num)
                    resave_tasks()
                    all_tasks.clear()
                    task_list.clear()

                else:
                    print("\n !!! Такой задачи не найдено !!!\n")
            case "5":
                print_task(case_ind)
                try:
                    task_choose_input = input()
                    task_choose = int(task_choose_input)
                except:
                    task_choose = str(task_choose_input)
                if isinstance(task_choose, int):
                    if task_choose >= 0 and task_choose <= len(all_tasks):
                        task_num = task_choose - 1
                        delete_task(task_num)
                        resave_tasks()
                        all_tasks.clear()
                        task_list.clear()

                elif isinstance(task_choose, str) and task_choose.upper() in names:
                    print('\nЕБАТЬ!!!!')
                    task_num = names.index(task_choose.upper())
                    task_num = names.index(task_choose.upper())
                    delete_task(task_num)
                    resave_tasks()
                    all_tasks.clear()
                    task_list.clear()
                else:
                    print("\n !!! Такой задачи не найдено !!!\n")

            case _:
                print("\n !!! Нет такого, давай ещё раз !!!\n")




@dc
class Task:
    name: str
    description: str
    prior: float


all_tasks = []
what_to_do()
print('\n--- Теперь нажми любую клавишу и иди выполнять ---\n')
any_key()
# for i in range(4):
#     all_tasks.append(Task('Задача {0}'.format(i),'Описание {0}'.format(i),5))

# for i in range(4):
#     all_tasks.append(input_task())

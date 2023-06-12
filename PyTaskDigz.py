import os
import time
from termcolor import cprint

task_list = []

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def alert():
    cprint('[!] Nenhuma Tarefa a ser apagada ou modificada!','red')
    time.sleep(1)


def add_todo():
    cprint('Digite a tarefa:\t[V]oltar','green')
    task = input('-> ')

    if task == 'V':
        time.sleep(0.5);clear()
        return


    cprint('Tarefa adicionada com sucesso!','green')
    task_list.append(task);time.sleep(1);clear()


def list_todo():
    time.sleep(0.5)
    print(f'\033[1;32mTarefas Pendentes: \033[m{len(task_list)}')

    for index,task in enumerate(task_list):
        print(f'[{index+1}] {task}')



def delete_todo():
    print('\033[1;32mQual Tarefa Deseja Apagar?    [V]oltar\033[m\n')
    list_todo()
    choice = input('-> ')

    if choice.upper() == 'V':
        time.sleep(0.5);clear()
        return
    
    try:
        choice = int(choice)
    except IndexError:
        cprint('Tarefa Nao Existe','red')
        time.sleep(1)
        clear()

    if 0 < choice <= len(task_list):
        print('\033[1;32mTarefa Apagada Com Sucesso\033[m')
        task_list.pop(choice-1)
        time.sleep(1)
        clear()
    else:
        cprint('Tarefa Nao Existe','red')
        time.sleep(1)
        clear()


def update():
    print('\033[1;32mQual Tarefa Deseja Alterar?    [V]oltar\033[m\n')
    list_todo()
    index = input('-> ')

    if index.upper() == 'V':
        time.sleep(0.5)
        clear()
        return

    try:
        index = int(index)
    except ValueError:
        cprint('Tarefa Nao Existe','red')
        time.sleep(0.5)
        clear()
        return update()

    if 0 < index <= len(task_list):
        new_value = input('\033[33mSobrescrever com -> \033[m')
        task_list[int(index)-1] = new_value
        cprint(f'Tarefa Alterada -> [{index}]','cyan')
    else:
        cprint('Tarefa Nao Existe','red')

    time.sleep(1);clear()




clear()
while True:
    cprint('\nDigz Todo-List', 'green', attrs=['blink'])
    
    MENU = f"""\n\033[1;32m Gerenciador de Tarefas:\033[m\r \033[33m
    [1] Adicionar Tarefa
    [2] Alterar Tarefa
    [3] Ver Tarefas
    [4] Deletar Tarefa
    [5] Encerrar
    \r-> \033[m"""

    try:
        option = input(MENU);clear()

        match option:
            case '1':
                add_todo()
            case '2':
                if len(task_list) == 0:
                    alert()
                else:
                    update()
            case '3':
                list_todo()
                # input()
            case '4':
                if len(task_list) == 0:
                    alert()
                else:
                    delete_todo()
            case '5':
                time.sleep(0.5)
                cprint('Exited','red')
                break
            case _:
                cprint('Invalid Option!','red',attrs=['bold'])

    except KeyboardInterrupt:
        cprint('\nExiting...','red')
        time.sleep(1)
        clear()
        break
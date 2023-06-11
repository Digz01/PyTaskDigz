import os
import time
import termcolor as t

list_user = []

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def alert():
    print('\033[1;31m[!] Nenhuma Tarefa a ser apagada ou modificada!\033[m')
    time.sleep(1)


def add_todo():
    print('\033[1;32mDigite a tarefa\033[m')
    task = input('-> ')
    print('\033[1;32mTarefa adicionada com sucesso!\033[m')
    list_user.append(task);time.sleep(1);clear()


def list_todo():
    time.sleep(0.5)
    print(f'\033[1;32mTarefas Pendentes: \033[m{len(list_user)}')
    
    for index,task in enumerate(list_user):
        print(f'[{index+1}] {"".join(task)}')


def delete_todo():
    print('\033[1;32mQual Tarefa Deseja Apagar?\033[m\n')
    
    list_todo()
    
    choice = int(input('-> '))
    print('\033[1;32mTarefa Apagada Com Sucesso\033[m')
    
    list_user.pop(choice-1);time.sleep(1)
    clear()
    

def update():
    print('\033[1;32mQual Tarefa Deseja Alterar?\033[m\n')
    list_todo()
    
    index = int(input('-> '))
    new_value = input('\033[33mSobrescrever com -> \033[m')
    list_user[index-1] = new_value
    
    t.cprint(f'\nTareda Alterada -> [{index}]','cyan')

    time.sleep(0.5)



t.cprint('Digz Todo-List', 'green', attrs=['blink'])

while True:
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
                if len(list_user) == 0:
                    alert()
                else:
                    update()
            case '3':
                list_todo()
            case '4':
                if len(list_user) == 0:
                    alert()
                else:
                    delete_todo()
            case '5':
                time.sleep(0.5)
                t.cprint('Exited','red')
                break
            case _:
                t.cprint('Invalid Option!','red',attrs=['bold'])
                    
    except KeyboardInterrupt:
        t.cprint('\nExiting...','red');time.sleep(1)
        break
import os
import time
from termcolor import cprint, colored
import json


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def alert():
    cprint('[!] Nenhuma tarefa a ser apagada ou modificada!', 'red')
    time.sleep(1.5)
    clear()


def add_todo():
    cprint('Digite a tarefa:\t[V]oltar','green')
    task = input(colored('-> ','green'))

    if task.upper() == 'V':
        time.sleep(0.5)
        clear()
        return

    task_list[len(task_list)+1] = task
    save(task_list)
    cprint('Tarefa adicionada com sucesso!','green')
    time.sleep(1)
    clear()


def list_todo():
    time.sleep(0.5)
    cprint(f'Tarefas pendentes: {len(task_list)}','green')

    for key, value in task_list.items():
        print(f'[{key}] {value}')

    time.sleep(1)



def delete_todo():

    cprint('Qual tarefa deseja apagar?\t[V]oltar\n','green')
    list_todo()
    choice = input(colored('-> ','red'))

    if choice.upper() == 'V':
        time.sleep(0.5)
        clear()
        return

    try:
        choice = int(choice)
    except ValueError:
        cprint('Tarefa não existe', 'red')
        time.sleep(0.5)
        clear()
        return delete_todo()

    if 0 < choice <= len(task_list):
        del(task_list[choice])
        save(task_list)
        cprint('Tarefa apagada com sucesso!','yellow')
        time.sleep(1)
        clear()
    else:
        cprint('Tarefa não existe', 'red')
        time.sleep(0.5)
        clear()
        return delete_todo()


def update():
    cprint('Qual tarefa deseja alterar?\t[V]oltar\n','green')
    list_todo()
    index = input(colored('-> ','yellow'))

    if index.upper() == 'V':
        time.sleep(0.5)
        clear()
        return

    try:
        index = int(index)
    except ValueError:
        cprint('Tarefa não existe', 'red')
        time.sleep(0.5)
        clear()
        return update()

    if index in task_list.keys():
        new_value = input(colored('Sobrescrever com -> ','yellow'))
        task_list[index] = new_value
        
        save(task_list)
        
        cprint(f'Tarefa alterada -> [{index}]', 'cyan')
        time.sleep(0.5)
        clear()
    else:
        cprint('Tarefa não existe', 'red')

    time.sleep(1)


def save(tl: dict):
    try:
        jd = json.dumps(task_list, indent=4, ensure_ascii=False, separators=(',', ':'))
        with open(os.path.join(path,'db_tasks.json'), 'w', encoding='CP850') as f:
            f.write(jd)

    except Exception as error:
        print(error)


def load() -> dict:
    global task_list
    try:
        with open(os.path.join(path,'db_tasks.json'), 'r', encoding='CP850') as f:
            task_list = json.load(f)

        task_list = {int(i):j for i,j in task_list.items()}

        return task_list

    except Exception as error:
        print(error)
        return False


def begin():

    clear()

    while True:
        cprint("""\n
    .-,--.              ,--,--'    .
    ' |   \ . ,-. ,_,   `- | ,-. ,-| ,-.
    , |   / | | |  /     , | | | | | | |
    `-^--'  ' `-| '"'    `-' `-' `-' `-'
            ,|          v1
            `'
            """\
            ,'red', attrs=['bold','blink'])


        MENU = f"""\n \033[1;32mGerenciador de Tarefas:\033[m\r
        \033[33m
    [1] Adicionar Tarefa\t[0] Encerrar
    [2] Alterar Tarefa
    [3] Ver Tarefas
    [4] Deletar Tarefa
    [5] Reiniciar Programa
        \r-> \033[m"""

        try:
            option = input(MENU)
            clear()

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

                case '4':
                    if len(task_list) == 0:
                        alert()
                    else:
                        delete_todo()

                case '5':
                    begin()

                case '0':
                    time.sleep(0.5)
                    cprint('Encerrado', 'red')
                    exit(0)

                case _:
                    cprint('Opcao Invalida!', 'red', attrs=['bold'])

        except KeyboardInterrupt:
            cprint('\nEncerrado...', 'red')
            time.sleep(1)
            clear()
            break


if __name__ == '__main__':

    if os.name == 'nt':
        home_user = os.getenv('USERPROFILE')
    elif os.name == 'posix':
        home_user = os.getenv('HOME')

    directory = '.pytaskdigz/db'
    
    path = os.path.join(home_user,directory)
    existing_dirs = os.listdir(home_user)

    if '.pytaskdigz' in existing_dirs:
        cprint('[!] Seja Bem Vindo De Volta :)','yellow', attrs=['bold'])
        time.sleep(2)
    else:
        cprint('[!] Criando Banco de Dados...','yellow', attrs=['bold'])
        time.sleep(2)
        os.makedirs(path)


    if 'db_tasks.json' in os.listdir(path):
        task_list = load()
    else:
        task_list = {}

    begin()


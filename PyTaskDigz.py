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
	time.sleep(1)
	

def add_todo():
	cprint('Digite a tarefa:\t[V]oltar')
	task = input('-> ')
	
	if task.upper() == 'V':
		time.sleep(0.5)
		clear()
		return
	
	task_list[len(task_list)+1] = task
	save(task_list)
	cprint('Tarefa adicionada com sucesso!')
	clear()


def list_todo():
	time.sleep(0.5)
	cprint(f'Tarefas pendentes: {len(task_list)}')
	
	for key, value in task_list.items():
		print(f'[{key}] {value}')
		

def delete_todo():
	cprint('Qual tarefa deseja apagar?\t[V]oltar')
	list_todo()
	choice = input('-> ')
	
	if choice.upper() == 'V':
		time.sleep(0.5)
		clear()
		return
	
	try:
		choice = int(choice)
	except ValueError:
		cprint('Tarefa não existe', 'red')
		time.sleep(1)
		clear()

	if 0 < choice <= len(task_list):
		del(task_list[choice])
		save(task_list)
		cprint('Tarefa apagada com sucesso!')
		time.sleep(1)
		clear()
	else:
		cprint('Tarefa não existe', 'red')
		time.sleep(1)
		clear()


def update():
	cprint('Qual tarefa deseja alterar?\t[V]oltar')
	list_todo()
	index = input('-> ')

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
		new_value = input(colored('Sobrescrever com -> '))
		task_list[index] = new_value
		save(task_list)
		cprint(f'Tarefa alterada -> [{index}]', 'cyan')
	else:
		cprint('Tarefa não existe', 'red')
		
	time.sleep(1)


def save(tl: dict):
	try:
		jd = json.dumps(task_list, indent=4, ensure_ascii=False, separators=(',', ':'))
		with open('db_tasks.json', 'w', encoding='CP850') as f:
			f.write(jd)

	except Exception as error:
		print(error)


def load() -> dict:
	global task_list
	try:
		with open('db_tasks.json', 'r', encoding='CP850') as f:
			task_list = json.load(f)

		task_list = {int(i):j for i,j in task_list.items()}
  
		return task_list

	except Exception as error:
		print(error)
		return False


def begin():
		
	clear()

	while True:
		cprint('\nDigz Todo-List ', 'green', attrs=['blink'])

		MENU = f'''\n\033[1;32mGerenciador de tarefas:
[1] Adicionar tarefa
[2] Alterar tarefa
[3] Ver tarefas
[4] Deletar tarefa
[5] Encerrar
\r-> \033[m'''.strip()

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
					time.sleep(0.5)
					cprint('Exited', 'red')
					break

				case _:
					cprint('Invalid option!', 'red', attrs=['bold'])

		except KeyboardInterrupt:
			cprint('\nExiting...', 'red')
			time.sleep(1)
			clear()
			break


if __name__ == '__main__':

	if 'db_tasks.json' in os.listdir():
		task_list = load()
	else:
		task_list = {}

	begin()

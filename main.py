import os
import io
from cursesmenu import *
from cursesmenu.items import *

# linux command to run
cmd = 'ps h -do pid:1,command'
# store tasks in a dictionary
tasks = {}


def generatemenu(tasks):
    # Create the menu
    menu = CursesMenu("Select something to kill him!")

    # older
    # os.system('clear')
    # for pid, name in tasks.items():
    #     print("[{}]\t - {}".format(pid, name[:30]))

    # kpid = input('Digito o numero do processo para matar: ')
    # os.system('kill {}'.format(kpid))

    # A CommandItem runs a console command
    for pid, name in tasks.items():
        # print("[{}]\t - {}".format(pid, name[:30]))
        label = "{:<8} - {}".format('[' + str(pid) + ']', name[:40])
        command = "kill {}".format(pid)

        # add item
        menu.append_item(CommandItem(label, command))

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()


# processos rodando na maquina
# get all processes in a list
data = [(int(p), c) for p, c in
        [x.rstrip('\n').split(' ', 1) for x in os.popen(cmd)]]

# filter
for p, n in data:
    # skip kernel threads
    if (n[0] == '['):
        continue

    # add to dictionary
    tasks[p] = n

if __name__ == '__main__':
    # interface para fechar qualquer processo que esteja executando
    generatemenu(tasks)

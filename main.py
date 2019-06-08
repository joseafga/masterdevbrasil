#! /usr/bin/env python3
import os
from cursesmenu import CursesMenu, items as cmitems


def get_processes():
    """ get all processes in a list """
    cmd = 'ps -do pid:1,cmd'  # linux command to run
    processes = {}

    with os.popen(cmd) as out:
        # see https://stackoverflow.com/questions/24362007/
        next(out.__iter__())  # skip header (first line)

        for line in out:
            # sepate pid and command in a tuple
            p = line.rstrip('\n').split(' ', 2)

            # skip kernel threads
            if p[1][0] == '[':
                continue

            processes[p[0]] = p[1]

    return processes


def generate_menu(tasks):
    """ Create menu for process selection """
    menu = CursesMenu("Select something to kill him!")

    # a CommandItem runs a console command
    for pid, name in tasks.items():
        label = "{:<8} - {}".format('[' + str(pid) + ']', name[:40])
        command = "kill {}".format(pid)

        menu.append_item(cmitems.CommandItem(label, command))

    # show the menu and allow the user to interact
    menu.show()


if __name__ == '__main__':
    generate_menu(get_processes())

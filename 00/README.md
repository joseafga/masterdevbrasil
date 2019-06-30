System Tasks
==========
Simple processes viewer and killer, made for *Master Dev Brasil*

About
----------
Display processes using `ps -do pid:1,cmd`. The `ps` is the command, option `-d` display all processes except session leaders, `-o` allow user format in this case used for display only PID (with `:1` for no left spaces) and CMD columns.
All results are parsed in a python dictionary and finally displayed with [`curses-menu`](https://github.com/pmbarrett314/curses-menu) help.

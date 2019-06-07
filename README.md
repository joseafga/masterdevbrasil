System Tasks
==========
Simple processes viewer and killer, made for first *Master Dev Brasil*

Fist commit is the code presented in the live stream after this some improvements have be done.

About
----------
Display processes using `ps -do pid:1,cmd`. The `ps` is the command, option `-d` display all processes except session leaders, `-o` allow user format in this case used for display only PID (with `:1` for no left spaces) and CMD columns.
All results are parsed in a python dictionary and finally displayed with [`curses-menu`](https://github.com/pmbarrett314/curses-menu) help.

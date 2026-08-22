A programming language I made for the fun of it. It runs Python in the backend.

Has no name right now

Completely useless and will probably be slow, so don't actually program in it unless ur insane or me.

To run, make sure both compiler.py and input.txt are in the same folder on your device. Input the code into input.txt and run compiler.py; you should see the output on your terminal
Syntax/Instructions/Explanation of inner workings:
The interpreter compiles line by line. It ignores trailing and leading whitespace.

Each line must be separated into chunks spaced apart by the | symbol.

The first chunk of each line must tell the interpreter what you intend to do.

Ex: call|print|1

(Here, call is telling the interpreter to call a function. The rest of the chunks tell it to print 1)

NOTE: the interpreter only looks for the number of chunks needed for the command and ignores the rest. This allows you to add comments by adding more chunks than necessary to a line and typing whatever you want, since the extra chunks will be ignored

Here are all the commands and their respective info.

Command 1: var


This command allows you to create a variable. The first chunk is the variable name, and the second chunk is the value.

variable names cannot begin with | or ".

if the second chunk is a parameter of a custom function or variable, the variable will be set to the value of the parameter/other variable. 

Note: if a parameter and variable have the same name and are passed into the second chunk, the parameter takes priority. Likewise if a parameter/variable has the name of a number (Ex: 1, and yes parameters/variables can be numbers), the parameter/variable take priority (parameter first, then variable, then number).

if the second chunk is not a variable, it can either be a string or an int. Strings always begin with a " symbol (THEY DO NOT END WITH THAT SYMBOL). 

TODO: 
1. put syntax into the readme
2. lists and some more useful built in functions
3. make some fractal in ur own language. 

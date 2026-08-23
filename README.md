A programming language I made for the fun of it. It runs Python in the backend.

Called Dumbass346, cause every error message insults you and it was done in 346 lines of python code. (1/2 of which is just built in functions).

I winged this shit in 5 days, took a 2 week break, then finished it in like 2 more days. No ai or research on how good interpreters actually work (very smart of me).

Completely useless and will probably be slow, so don't actually program in it unless ur insane or me.

To run, make sure both compiler.py and input.txt are in the same folder on your device. Input the code into input.txt and run compiler.py; you should see the output on your terminal

Syntax/Instructions/Explanation of inner workings:

(Look at input.txt for some example code, which makes the Mandelbrot set).

The interpreter compiles line by line. It ignores trailing and leading whitespace.

Each line must be separated into chunks spaced apart by the | symbol. If you wish to put this symbol in a string, variable name, parameter name or function name, put 2 next to each other (ex: ||) and the interpreter will read it as a | symbol rather than a divider. Note that this will not work if you want to put this symbol at the beginning of a variable name, parameter name or function name, as the interpreter will believe the symbol is part of an earlier chunk.

The first chunk of each line must tell the interpreter what you intend to do.

Ex: call|print|1

(Here, call is telling the interpreter to call a function. The rest of the chunks tell it to print 1)

NOTE: the interpreter only looks for the number of chunks needed for the command and ignores the rest. This allows you to add comments by adding more chunks than necessary to a line and typing whatever you want, since the extra chunks will be ignored

Here are all the commands and their respective info.

Command 1: var


This command allows you to create a variable. The first chunk is the variable name, and the second chunk is the value.

Variable names cannot begin with " (or |).
if the variable name is a parameter of a custom function, the parameter's value will be changed.

if the second chunk is a parameter of a custom function or variable, the variable will be set to the value of the parameter/other variable. 

Note: if a parameter and variable have the same name and are passed into the second chunk, the parameter takes priority. Likewise if a parameter/variable has the name of a number (Ex: 1, and yes parameters/variables can be numbers), the parameter/variable take priority (parameter first, then variable, then number).

if the second chunk is not a variable, it can either be a string or a number. Strings always begin with a " symbol (THEY DO NOT END WITH THAT SYMBOL). Numbers are either ints or floats, which you write in their standard decimal notation. (ex: var|test|3.14 or var|test|3).

There is one special variable called last. This variable stores the return value of the last function call. If the last function returns nothing, then it stores the value 1. Be careful when accessing it.

Notes: 
All variables have global domain, so try to keep parameter names different from variables. 
if a variable/parameter name is a number that does not equal itself. (ex: var|12|11), it is very hard to reset and locks you out of using that value (in this example: 12) since variables/parameters take priority. To reset it, call any math function to set last equal to the value, then assign it to the variable.

Ex:

call|mult|4|3

var|12|last

If a variable gets set to a float, but the float equals an int, the interpreter will set it equal to an int in the backend automatically (this is true for all commands). This is probably a stupid idea since there are good reasons to keep ints and floats separate, but all my built-in functions do algebraic manipulation, and I think Python can handle those between ints and floats well, so we are just going to roll with it.
End notes.


Command 2: return


EX: return|"Yes

returns a value. Can be a parameter, variable, string or number, with that priority order. If used outside a custom function, the program will merely exit (or you can use the built-in exit function).

Note: From here on I will just say string and int, just know that you can pass in a parameter or variable in their place too and remember the priority order.

Command 3: done

used to end an if, while or def statement. if, while or def statements can be nested so long as each statement has a corresponding done. ALL OF THESE STATEMENTS MUST HAVE A CORRESPONDING done STATEMENT.


Command 4: if


EX: if|1|<|2

Conditional statements. Chunks 2 and 4 must either be both strings or both ints.

The operator in chunk 3 can either be 

 (= : same as pythons ==)
 
 (< : same as python)
 
 (> : same as python)

 (<= : same as python)
 
 (>= : same as python)

The comparisons work just like how python does it so go look that up Im too lazy to write this documentation.

This STATEMENT MUST HAVE A DONE STATEMENT CORRESPONDING TO IT.

Works like a conditional statement. if the condition in the if statement is false, then the interpreter will disable all lines up until the corresponding done statement.

Note: Since the interpreter ignores disabled lines, you can put multi line comments by having an if statement that is always disabled, then put whatever you want inside it.


Command 5: while


Only difference between if and while is that once the interpretor reaches the corresponding done, it goes back to the while statements and reevaluates the lines until the while statement is false. Other than that it works EXACTLY THE SAME.

Command 6: def


Ex: def|function name| parameter 1| parameter 2

Used to define a custom function. The first chunk after def is the function's name, and all other chunks will be set as the parameters. The rest of the lines are disabled until the function's corresponding done statement. (MUST HAVE A CORRESPONDING DONE STATEMENT)

Notes: Parameters cannot begin with " or |. You also cant put comments on def statements since the interpretor will consider them as parameters.

Since all variables are global, it is better to have parameter names be unique to variable names.

Extra restrictions/notes to parameters can be found in previous instructions.

Functions are only defined once the parameter reaches the def statement for the first time. So if you define a function in another function/ conditional, it can only be used if the other function is called/ conditional turns true.

All functions have global domain, and once defined cannot be reset. The only way to have 2 functions defined with the same name is if one is in a conditional/function that is never called.

The recursion limit for functions is 467. I dunno why its this number but after this many calls my custom recursion depth error message stops printing so yeah. 


Command 7: call


Ex: call|print|"YES!!!

Calls a function. The function can either be a built-in function or custom function. The first chunk after call must be the function names, and you must provide all the parameters. The variable last will take in the return value of the function, and if the function has none then last will be set equal to one. Parameters can be either strings or ints.

Here are all the built-in functions. Most are pretty obvious in what they do, and will error if provided the wrong type of parameter or for other reasons (ex: divide by zero). There are also no operators in my language (like + or *), you have to use functions which is why this language sucks and why the interpreter is so small).

add: adds 2 numbers

subtract: subtracts 2 numbers

mult: multiply 2 numbers

div: divides 2 numbers (numerator then denominator)

pow: takes the power of 2 numbers (first is base, second is exponent)

log: takes the logarithm of the 2 numbers (first is the base)

sin: takes the sine of a number

cos: takes the cosine of a number

tan: takes the tangent of a number

floor: rounds the number down

ceil: rounds the number up

num: converts a string into a number

str: converts a number into a string

substring: takes a substring of a string. (first is the string, next 2 are the start and end indices) (works just like Python).

contains: checks if the first string is in the second string (case-sensitive)

append: concatenates the second string onto the first



Should an error occur, the error message will include the line number, the text on that line and the reason for the error. There is also a traceback stack in case the error happenend in a custom function. It will also call you a dumbass.

Explanation of inner workings

Used python so I dont need to do any low level stuff or make a compiler for every single hardware architecture. I made a custom split function to handle my notation, made 2 stacks (that are actually lists) to handle nested statements and errors, had a couple dictionaries to handle storing variables and functions, and put all the interpretor logic in a function so that I could recall it for custom functions. Also had to edit python built-in functions to handle my notation and put a gazillion try-excepts and if-elif-else chains to handle errors. Rest is obvious stuff go figure it out.

TODO: 
1. lists and some more useful built-in functions (only if I have to I dont wanna change the title name)>
2. make some fractal in ur own language. 

# this language shall pride itself as being conveniant for the developer only.
#no putting | at the beggining of variables/ functions
#last is a special variable that equals the return value of the last function called. If no return value then it will equals 1. Be careful when referencing it.
#variables that are numbers are hard to reset if they do not equal their value


from os import _exit
import math
path = "input.txt "
count = 0
i = 0
ifwhilecount = 0
disable = -1
enable = []
def check_is_string(string):
    if(not check_is_num(string)):
        return string[0] == "\""
    return False
def check_is_num(string):
    try:
        float(string)
        return True
    except:
        return False
def p(list):
    if(check_is_num(list[0])):
        print(list[0])
    else:
        print(list[0][1:])
    return 1.0

def length(list):
    if(check_is_string(list[0])):
        return len(list[0][1:])
    else:
        traceback("You didnt put a string variable in here dumbass")
def add(list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            return list[0]+list[1]
        else:
            traceback("A parameter aint a number dumbass")
    except:
        traceback("Number out of bounds")
def subtract(list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            return list[0]-list[1]
        else:
            traceback("A parameter aint a number dumbass")
    except:
        traceback("Number out of bounds")
def multiply(list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            return list[0]*list[1]
        else:
            traceback("A parameter aint a number dumbass")
    except:
        traceback("Number out of bounds")
def divide(list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            if(list[1] != 0):
                return list[0] / list[1]
            else:
                traceback("Divde by zero error dumbass")
        else:
            traceback("A parameter aint a number dumbass")
    except:
        traceback("Number out of bounds")
def power(list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            if(list[0] == 0 and list[1] < 0):
                traceback("No negative exponents if base = 0 dumbass")
            if(list[0] < 0 and list[1] != int(list[1])):
                    traceback("No fractional exponents if base < 0 dumbass")
            else:
                return list[0]**list[1]
        else:
            traceback("A parameter aint a number dumbass")
    except:
        traceback("Number out of bounds")
def log(list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            if(list[1] <= 0):
                traceback("Argument for log must be positive dumbass")
            if(list[0] <= 0 or list[0] == 1):
                    traceback("Base must be positive and unequal to 1 dumbass")
            else:
                return math.log(list[1],list[0])
        else:
            traceback("A parameter aint a number dumbass")
    except:
        traceback("Number out of bounds")
def sin(list):
    if(check_is_num(list[0])):
        return math.sin(list[0])
    else:
        traceback("Must be a number in here dumbass")
def cos(list):
    if(check_is_num(list[0])):
        return math.cos(list[0])
    else:
        traceback("Must be a number in here dumbass")
def tan(list):
    if(check_is_num(list[0])):
        try:
            return math.tan(list[0])
        except:
            traceback("Number out of bounds")
    else:
        traceback("Must be a number in here dumbass")
def num(list):
    if(check_is_num(list[0])):
        return list[0]
    else:
        try:
            return float(list[0][1:])
        except:
            traceback("Must be a number in here dumbass")
def string(list):
    if(check_is_num(list[0])):
        return "\""+str(list[0])
    else:
        return list[0]
def floor(list):
    if(check_is_num(list[0])):
        return math.floor(list[0])
    else:
        traceback("Must be a number in here dumbass")
def ceil(list):
    if(check_is_num(list[0])):
        return math.ceil(list[0])
    else:
        traceback("Must be a number in here dumbass")
def substring(list):
    if(check_is_string(list[0]) and check_is_num(list[1]) and check_is_num(list[2])):
        try:
            return "\""+list[0][1:][int(list[1]):int(list[2])]
        except:
            traceback("Your not using integer indexes you dumbass")
    else:
        traceback(" First parameter must be string. Rest are integers dumbass")
def contains(list):
    if(check_is_string(list[0]) and check_is_string(list[1])):
        if(list[0][1:] in list[1][1:]):
            return 1.0
        else:
            return 0.0
    else:
        traceback("You didnt put string variables in here dumbass")
def append(list):
    if(check_is_string(list[0]) and check_is_string(list[1])):
        return "\""+list[0][1:]+list[1][1:]
    else:
        traceback("Parameters must be strings dumbass")
built_in_functions = {
    "print":(1,p),
    "len":(1,length),
    "add":(2,add),
    "subtract":(2,subtract),
    "mult":(2,multiply),
    "div":(2,divide),
    "pow":(2,power),
    "log":(2,log),
    "sin":(1,sin),
    "cos":(1,cos),
    "tan":(1,tan),
    "floor":(1,floor),
    "ceil":(1,ceil),
    "num":(1,num),
    "str":(1,string),
    "substring":(3,substring),
    "contains":(2,contains),
    "append":(2,append)
}

variables = {
    "last": 1.0
}
functions = {}
def better_split(line):
    output = []
    i = 0
    word = ""
    disable = False
    while(i< len(line)):
        if(line[i] == "|"):
            if(i!=0 and line[i-1] == "|" and not disable):
                word = output.pop()
                word+="|"
                disable = True
                i+=1
                continue
            else:
                output.append(word)
                word = ""
        else:
            word+=line[i]
        disable = False
        i+=1
    output.append(word)
    return output
def traceback(message):
    print("On line " +str(i+1)+": "+message)
    _exit(0)
with open(path, "r") as file:
    lines = file.readlines()
    while  i < len(lines):
        line =better_split(lines[i].strip())
        #print(line)
        # things to do with each line
        # var - variable assignment
        # def - function definition
        # end - ends function definition
        # return - returns value.
        # if - conditional statement
        # while - loop statement
        # done - ends if statement
        # final - ends while statement
        # exit - exits
        if(line[0] == "var" and disable == -1):
            # variable assignment
            try:
                if("\"" in line[1]):
                    traceback("No quotations. dumbass")
                else:
                    try:
                        if(line[2] in variables):
                            variables[line[1]] = variables[line[2]]
                        elif(check_is_string(line[2])):
                            variables[line[1]] = line[2]
                        elif(check_is_num(line[2])):
                            variables[line[1]] = float(line[2])
                        else:
                            traceback("Dont recognize your value dumbass")
                    except:
                        traceback("Need a value dumbass")
            except:
                traceback("Messed up variable syntax. dumbass")
        elif(line[0] == "def"and disable == -1):
            # function definition
            pass
        elif(line[0] == "if"):
            # conditional statement
            if(disable != -1):
                ifwhilecount+=1
            elif(len(line)-1 < 3):
                traceback("Too few arguments for conditional dumbass")
            else:
                if(line[1] not in variables or line[3] not in variables):
                    traceback("DONT SEE THE ARGUMENTS IN VARIABLES DUMBASS!")
                else:
                    if((not check_is_num(variables[line[1]])) or (not check_is_num(variables[line[3]]))):
                        traceback("Arguments must be numbers dumbass")
                    else:
                        if(line[2] == "="):
                            if(not (variables[line[1]] == variables[line[3]])):
                                disable = -2
                        elif(line[2] == "<"):
                            if(not (variables[line[1]] < variables[line[3]])):
                                disable = -2
                        elif(line[2] == ">"):
                           if(not (variables[line[1]] > variables[line[3]])):
                                disable = -2
                        elif(line[2] == "<="):
                            if(not (variables[line[1]] <= variables[line[3]])):
                                disable = -2
                        elif(line[2] == ">="):
                            if(not (variables[line[1]] >= variables[line[3]])):
                                disable = -2
                        elif(line[2] == "!="):
                            if(not (variables[line[1]] != variables[line[3]])):
                                disable = -2
                        else:
                            traceback("UNRECOGNIZED OPERATOR DUMBASS")
        elif(line[0] == "while"):
            # loop statement
            if(disable != -1):
                ifwhilecount+=1
            elif(len(line)-1 < 3):
                traceback("Too few arguments for conditional dumbass")
            else:
                if(line[1] not in variables or line[3] not in variables):
                    traceback("DONT SEE THE ARGUMENTS IN VARIABLES DUMBASS!")
                else:
                    if((not check_is_num(variables[line[1]])) or (not check_is_num(variables[line[3]]))):
                        traceback("Arguments must be numbers dumbass")
                    else:
                        if(line[2] == "="):
                            if(not (variables[line[1]] == variables[line[3]])):
                                disable = i
                        elif(line[2] == "<"):
                            if(not (variables[line[1]] < variables[line[3]])):
                                disable = i
                        elif(line[2] == ">"):
                            if(not (variables[line[1]] > variables[line[3]])):
                                disable = i
                        elif(line[2] == "<="):
                            if(not (variables[line[1]] <= variables[line[3]])):
                                disable = i
                        elif(line[2] == ">="):
                            if(not (variables[line[1]] >= variables[line[3]])):
                                disable = i
                        elif(line[2] == "!="):
                            if(not (variables[line[1]] != variables[line[3]])):
                                disable = i
                        else:
                            traceback("UNRECOGNIZED OPERATOR DUMBASS")
                        if(disable == -1):
                            enable.append(i)
        elif(line[0] == "done"):
            if(disable!=-1):
                if(ifwhilecount == 0):
                    disable = -1
                else:
                    ifwhilecount-=1
            else:
                if(len(enable) != 0):
                    i = enable.pop()
        elif(line[0] == "exit"and disable == -1):
            _exit(0)
        elif(line[0] == "call"and disable == -1):
            try:
                if(line[1] in built_in_functions):
                    if(len(line)-2 < built_in_functions[line[1]][0]):
                        traceback("Too few parameters dumbass")
                    else:
                        inp = []
                        for j in range(2,2+built_in_functions[line[1]][0]):
                            if(line[j] not in variables):
                                traceback("Parameter "+str(j-1)+" is not a recognized variable")
                            else:
                                inp.append(variables[line[j]])
                        variables["last"] = built_in_functions[line[1]][1](inp)
                else:
                    traceback("UNRECOGNIZED FUNCTION DUMBASS")
            except:
                traceback("Didnt find your function dumbass")
        else:
            if(disable == -1 and line != ['']):
                traceback("You didnt put a command we recognize (You cant have lines at the beginning of variables or functions)")
        i+=1

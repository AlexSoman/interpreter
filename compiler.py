# this language shall pride itself as being conveniant for the developer only.
#no putting | at the beggining of variables/ functions
#last is a special variable that equals the return value of the last function called. If no return value then it will equals 1. Be careful when referencing it.
#variables that are numbers are hard to reset if they do not equal their value
# variables/functions that are only made of whitespace in them should have a | at the end to prevent being cutoff.
# all variables are global

from os import _exit
import math
def check_is_string(string):
    if(not check_is_num(string)):
        return string[0] == "\""
    return False
def check_is_num(string):
    if(string == "inf" or string == "-inf" or string == "nan"):
        return False
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
def get_val(value,trace,parameters):
    val = 0
    if(value in parameters):
        val = parameters[value]
    elif(value in variables):
        val = variables[value]
    elif(check_is_string(value)):
        val = value
    elif(check_is_num(value)):
        if(int(value) == float(value)):
            val = int(value)
        else:
            val= float(value)
    else:
        traceback("Dont recognize your value dumbass")
    return val
built_in_functions = {"print":(1,p),"len":(1,length),"add":(2,add),"subtract":(2,subtract),"mult":(2,multiply),"div":(2,divide),"pow":(2,power),"log":(2,log),"sin":(1,sin),"cos":(1,cos),"tan":(1,tan),"floor":(1,floor),"ceil":(1,ceil),"num":(1,num),"str":(1,string),"substring":(3,substring),"contains":(2,contains),"append":(2,append)}
functions = {}
functions_start = {}
path = "input.txt "
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
    print("On line " +str(traceback_i+1)+": "+message)
    _exit(0)
traceback_i = 0 #make this better later im way too lazy to think rn
variables = {
    "last": 1.0
}
def logic(in_function = True,count = 0,parameters = {}):
    global traceback_i
    i = count
    disable = -1
    disable_stack = []
    with open(path, "r") as file:
        lines = file.readlines()
        while  i < len(lines):
            traceback_i = i
            line =better_split(lines[i].strip().lstrip())
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
                    if("\"" == line[1][0]):
                        traceback("No quotations. dumbass")
                    else:
                        try:
                            if(line[1] in parameters):
                                parameters[line[1]] = get_val(line[2],"Dont Recognize your value dumbass",parameters)
                            else:
                                variables[line[1]] = get_val(line[2],"Dont Recognize your value dumbass",parameters)
                        except:
                            traceback("Need a value dumbass")
                except:
                    traceback("Messed up variable syntax. dumbass")
            elif(line[0] == "def"):
                # function definition
                disable_stack.append(i)
                if(disable == -1):
                    try:
                        if(len(line) == 0):
                            traceback("give ur function a name dumbass")
                        elif(line[1] in functions):
                            traceback("function already defined dumbass")
                        elif(len(line[2:]) != len(set(line[2:]))):
                            traceback("Parameters should be unique dumbass")
                        else:
                            for j in line[2:]:
                                if(j[0] == "\""):
                                    traceback("No quotations. dumbass")
                            functions[line[1]] = line[2:]
                            functions_start[line[1]] = i+1
                            disable = i
                    except:
                        traceback("Messed up Function syntax dumbass ")
            elif(line[0] == "if" or line[0] == "while"):
                # conditional statement
                disable_stack.append(i)
                if (disable == -1):
                    if(len(line)-1 < 3):
                        traceback("Too few arguments for conditional dumbass")
                    else:
                        lazy = []
                        for j in [1,3]:
                            lazy.append(get_val(line[j],"Token "+str(j)+" is not a recognized variable, number, or int dumbass",parameters))
                        if((check_is_string(lazy[0]) and check_is_num(lazy[1])) or (check_is_string(lazy[1]) and check_is_num(lazy[0]))):
                            traceback("arguments are opposite types dumbass")
                        if(line[2] == "="):
                            if(not (lazy[0] == lazy[1])):
                                disable = i
                        elif(line[2] == "<"):
                            if(not (lazy[0]  < lazy[1])):
                                disable = i
                        elif(line[2] == ">"):
                            if(not (lazy[0]  > lazy[1])):
                                disable = i
                        elif(line[2] == "<="):
                            if(not (lazy[0]  <= lazy[1])):
                                disable = i
                        elif(line[2] == ">="):
                            if(not (lazy[0]  >= lazy[1])):
                                disable = i
                        elif(line[2] == "!="):
                            if(not (lazy[0]  != lazy[1])):
                                disable = i
                        else:
                            traceback("UNRECOGNIZED OPERATOR DUMBASS")
            elif(line[0] == "done"):
                try:
                    temp =  disable_stack.pop() #stores what conditional done is referencing
                except:
                    if(in_function):
                        return 1
                    else:
                        traceback("Done statement has no corresponding conditional dumbass")
                if(disable!=-1):
                    if(disable == temp): #checks if the done is part of the conditional that is disabled (will be false if part of a nested conditional)
                        disable = -1
                else:
                    if(better_split(lines[temp].strip().lstrip())[0] == "while"):
                        i = temp
                        continue
            elif(line[0] == "exit"and disable == -1):
                _exit(0)
            elif(line[0] == "return"):
                try:
                    return get_val(line[1],"DONT RECOGNIZE YOUR VALUE DUMBASS",parameters)
                except:
                    traceback("Need a value dumbass")
            elif(line[0] == "call"and disable == -1):
                try:
                    if(line[1] in built_in_functions):
                        if(len(line)-2 < built_in_functions[line[1]][0]):
                            traceback("Too few parameters dumbass")
                        else:
                            inp = []
                            for j in range(2,2+built_in_functions[line[1]][0]):
                                inp.append(get_val(line[j],"Parameter "+str(j-1)+" is not a recognized variable, string or number dumbass",parameters))
                            variables["last"] = built_in_functions[line[1]][1](inp)
                            if(check_is_num(variables["last"]) and int(variables["last"]) == float(variables["last"])):
                                variables["last"] = int(variables["last"])
                    elif(line[1] in functions):
                        if(len(line)-2 < len(functions[line[1]])):
                            traceback("too few parameters dumbass")
                        else:
                            inp = {}
                            for j in range(2,2+len(functions[line[1]])):
                                inp[functions[line[1]][j-2]] = get_val(line[j],"Parameter "+str(j-1)+" is not a recognized variable, string or number dumbass",parameters)
                            variables["last"] = logic(count = functions_start[line[1]],parameters=inp)
                            if(check_is_num(variables["last"]) and int(variables["last"]) == float(variables["last"])):
                                variables["last"] = int(variables["last"])
                            
                    else:
                        traceback("UNRECOGNIZED FUNCTION DUMBASS")
                except Exception as e:
                    traceback("Didnt find your function dumbass")
            else:
                if(disable == -1 and line != ['']):
                    traceback("You didnt put a command we recognize (You cant have lines at the beginning of variables or functions)")
            i+=1
logic(False)

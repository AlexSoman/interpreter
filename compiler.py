from os import _exit
import math
def check_is_string(string):
    if(not check_is_num(string) and string != ""):
        return string[0] == "\""
    return False
def check_is_num(string):
    if(string == "inf" or string == "-inf" or string == "nan" or string == ""):
        return False
    try:
        float(string)
        return True
    except:
        return False
def p(traceback_i,lines,list):
    if(check_is_num(list[0])):
        print(list[0])
    else:
        print(list[0][1:])
    return 1.0

def length(traceback_i,lines,list):
    if(check_is_string(list[0])):
        return len(list[0][1:])
    else:
        traceback(traceback_i,lines,"You didnt put a string variable in here dumbass")
def log(traceback_i,lines,list):
    try:
        if(check_is_num(list[0]) and check_is_num(list[1])):
            if(list[1] <= 0):
                traceback(traceback_i,lines,"Argument for log must be positive dumbass")
            if(list[0] <= 0 or list[0] == 1):
                    traceback(traceback_i,lines,"Base must be positive and unequal to 1 dumbass")
            else:
                return math.log(list[1],list[0])
        else:
            traceback(traceback_i,lines,"A parameter aint a number dumbass")
    except:
        traceback(traceback_i,lines,"Number out of bounds dumbass")
def sin(traceback_i,lines,list):
    if(check_is_num(list[0])):
        return math.sin(list[0])
    else:
        traceback(traceback_i,lines,"Must be a number in here dumbass")
def cos(traceback_i,lines,list):
    if(check_is_num(list[0])):
        return math.cos(list[0])
    else:
        traceback(traceback_i,lines,"Must be a number in here dumbass")
def tan(traceback_i,lines,list):
    if(check_is_num(list[0])):
        try:
            return math.tan(list[0])
        except:
            traceback(traceback_i,lines,"Number out of bounds dumbass")
    else:
        traceback(traceback_i,lines,"Must be a number in here dumbass")
def num(traceback_i,lines,list):
    if(check_is_num(list[0])):
        return list[0]
    else:
        try:
            return float(list[0][1:])
        except:
            traceback(traceback_i,lines,"Must be a number in here dumbass")
def string(traceback_i,lines,list):
    if(check_is_num(list[0])):
        return "\""+str(list[0])
    else:
        return list[0]
def floor(traceback_i,lines,list):
    if(check_is_num(list[0])):
        return math.floor(list[0])
    else:
        traceback(traceback_i,lines,"Must be a number in here dumbass")
def ceil(traceback_i,lines,list):
    if(check_is_num(list[0])):
        return math.ceil(list[0])
    else:
        traceback(traceback_i,lines,"Must be a number in here dumbass")
def substring(traceback_i,lines,list):
    if(check_is_string(list[0]) and check_is_num(list[1]) and check_is_num(list[2])):
        try:
            return "\""+list[0][1:][int(list[1]):int(list[2])]
        except:
            traceback(traceback_i,lines,"Your not using integer indexes you dumbass")
    else:
        traceback(traceback_i,lines," First parameter must be string. Rest are integers dumbass")
def contains(traceback_i,lines,list):
    if(check_is_string(list[0]) and check_is_string(list[1])):
        if(list[0][1:] in list[1][1:]):
            return 1.0
        else:
            return 0.0
    else:
        traceback(traceback_i,lines,"You didnt put string variables in here dumbass")
def append(traceback_i,lines,list):
    if(check_is_string(list[0]) and check_is_string(list[1])):
        return "\""+list[0][1:]+list[1][1:]
    else:
        traceback(traceback_i,lines,"Parameters must be strings dumbass")
def exits(traceback_i,lines,list):
    _exit(0)
def get_val(traceback_i,lines,value,trace,parameters):
    if(value in parameters):
        return parameters[value]
    if(value in variables):
        return variables[value]
    if(check_is_string(value)):
        return value
    if(check_is_num(value)):
        if(int(float(value)) == float(value)):
            return int(value)
        return float(value)
    try:
        order_of_operations = {"+":0,"-":0,"*":1,"/":1,"^":2}
        operations = {"+":(lambda first,second: first+second),"-":(lambda first,second: first-second),"*":(lambda first,second: first*second),"/":(lambda first,second: first/second),"^":(lambda first,second: first**second)}
        for i in range(max(order_of_operations.values())+1):
            parantheses_stack = 0
            for j in range(len(value)-1,-1,-1):
                if(value[j] == ")"):
                    parantheses_stack+=1
                if(value[j] == "("):
                    parantheses_stack =  max(parantheses_stack-1,0)
                if(value[j] in order_of_operations and order_of_operations[value[j]] == i and parantheses_stack == 0):
                    first,second = get_val(traceback_i,lines,value[0:j],"",parameters),get_val(traceback_i,lines,value[j+1:len(value)],"",parameters)
                    if(check_is_string(second)):
                        traceback(traceback_i,lines,"Value: "+second+" operates "+value[j]+" on a string dumbass")
                    if(value[j] == "/" and second == 0):
                        traceback(traceback_i,lines,"At value " +value+": Division by zero dumbass")
                    if(value[j] == "^" and first == 0 and second < 0):
                        traceback(traceback_i,lines,"At value " +value+": No negative exponents if base = 0 dumbass")
                    if(value[j] == "^" and first < 0 and second != int(second)):
                        traceback(traceback_i,lines,"At value " +value+": No fractional exponents if base < 0 dumbass")
                    val = operations[value[j]](first,second)
                    if(int(float(val)) == float(val)):
                        return int(val)
                    return float(val)
    except Exception as e:
        print(e)
        traceback(traceback_i,lines,"Expression yielded number too large dumbass")
    if(value != "" and value[0] == "(" and value[len(value)-1] == ")"):
        return get_val(traceback,lines,value[1:len(value)-1],"",parameters)
    if(trace == ""):
        traceback(traceback_i,lines,"Dont recognize value "+value+" dumbass")
    traceback(traceback_i,lines,trace)
built_in_functions = {"exit":(0,exits),"print":(1,p),"len":(1,length),"log":(2,log),"sin":(1,sin),"cos":(1,cos),"tan":(1,tan),"floor":(1,floor),"ceil":(1,ceil),"num":(1,num),"str":(1,string),"substring":(3,substring),"contains":(2,contains),"append":(2,append)}
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
def traceback(traceback_i,lines,message):
    output = ""
    for i in range(len(traceback_i)-1):
        output+="From line "+str(traceback_i[i]+1)+": "+lines[traceback_i[i]].strip().lstrip()+"\n"
    output+="On line " +str(traceback_i[len(traceback_i)-1]+1)+": "+lines[traceback_i[len(traceback_i)-1]].strip().lstrip()+"\n"+message
    print(output)
    _exit(0)
variables = {"last": 1.0}
def logic(count = 0,parameters = {},traceback_i = [0]):
    i = count
    disable = -1
    disable_stack = []
    with open(path, "r") as file:
        lines = file.readlines()
        while  i < len(lines):
            traceback_i[len(traceback_i)-1] = i
            line =better_split(lines[i].strip().lstrip())
            if(line[0] == "var" and disable == -1):# variable assignment
                try:
                    if("\"" == line[1][0]):
                        traceback(traceback_i,lines,"No quotations. dumbass")
                    else:
                        try:
                            if(line[1] in parameters):
                                parameters[line[1]] = get_val(traceback_i,lines,line[2],"Dont Recognize your value dumbass",parameters)
                            else:
                                variables[line[1]] = get_val(traceback_i,lines,line[2],"Dont Recognize your value dumbass",parameters)
                        except:
                            traceback(traceback_i,lines,"Need a value dumbass")
                except:
                    traceback(traceback_i,lines,"Messed up variable syntax. dumbass")
            elif(line[0] == "def"):# function definition
                disable_stack.append(i)
                if(disable == -1):
                    try:
                        if(len(line) == 0):
                            traceback(traceback_i,lines,"give ur function a name dumbass")
                        elif(line[1] in functions and functions_start[line[1]]-1 != i):
                            traceback(traceback_i,lines,"function already defined dumbass")
                        elif(len(line[2:]) != len(set(line[2:]))):
                            traceback(traceback_i,lines,"Parameters should be unique dumbass")
                        else:
                            for j in line[2:]:
                                if(j[0] == "\""):
                                    traceback(traceback_i,lines,"No quotations. dumbass")
                            functions[line[1]] = line[2:]
                            functions_start[line[1]] = i+1
                            disable = i
                    except:
                        traceback(traceback_i,lines,"Messed up Function syntax dumbass ")
            elif(line[0] == "if" or line[0] == "while"):# conditional statement
                disable_stack.append(i)
                if (disable == -1):
                    if(len(line)-1 < 3):
                        traceback(traceback_i,lines,"Too few arguments for conditional dumbass")
                    else:
                        lazy = []
                        for j in [1,3]:
                            lazy.append(get_val(traceback_i,lines,line[j],"Token "+str(j)+" is not a recognized variable, number, or int dumbass",parameters))
                        if((check_is_string(lazy[0]) and check_is_num(lazy[1])) or (check_is_string(lazy[1]) and check_is_num(lazy[0]))):
                            traceback(traceback_i,lines,"arguments are opposite types dumbass")
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
                            traceback(traceback_i,lines,"UNRECOGNIZED OPERATOR DUMBASS")
            elif(line[0] == "done"):
                try:
                    temp =  disable_stack.pop() #stores what conditional done is referencing
                except:
                    if(count != 0): # if count = 0, we are not in a function.
                        return 1
                    else:
                        traceback(traceback_i,lines,"Done statement has no corresponding conditional dumbass")
                if(disable!=-1):
                    if(disable == temp): #checks if the done is part of the conditional that is disabled (will be false if part of a nested conditional)
                        disable = -1
                else:
                    if(better_split(lines[temp].strip().lstrip())[0] == "while"):
                        i = temp
                        continue
            elif(line[0] == "return" and disable == -1):
                try:
                    return get_val(traceback_i,lines,line[1],"DONT RECOGNIZE YOUR VALUE DUMBASS",parameters)
                except:
                    traceback(traceback_i,lines,"Need a value dumbass")
            elif(line[0] == "call"and disable == -1):
                try:
                    if(line[1] in built_in_functions):
                        if(len(line)-2 < built_in_functions[line[1]][0]):
                            traceback(traceback_i,lines,"Too few parameters dumbass")
                        else:
                            inp = []
                            for j in range(2,2+built_in_functions[line[1]][0]):
                                inp.append(get_val(traceback_i,lines,line[j],"Parameter "+str(j-1)+" is not a recognized variable, string or number dumbass",parameters))
                            variables["last"] = built_in_functions[line[1]][1](traceback_i,lines,inp)
                            if(check_is_num(variables["last"]) and int(float(variables["last"])) == float(variables["last"])):
                                variables["last"] = int(variables["last"])
                    elif(line[1] in functions):
                        if(len(line)-2 < len(functions[line[1]])):
                            traceback(traceback_i,lines,"too few parameters dumbass")
                        else:
                            inp = {}
                            for j in range(2,2+len(functions[line[1]])):
                                inp[functions[line[1]][j-2]] = get_val(traceback_i,lines,line[j],"Parameter "+str(j-1)+" is not a recognized variable, string or number dumbass",parameters)
                            traceback_i.append(functions_start[line[1]])
                            if(len(traceback_i) >= 467):
                                traceback(traceback_i,lines,"Recursion Limit error dumbass")
                            variables["last"] = logic(functions_start[line[1]],inp,traceback_i)
                            traceback_i.pop()
                            if(check_is_num(variables["last"]) and int(float(variables["last"])) == float(variables["last"])):
                                variables["last"] = int(variables["last"])
                    else:
                        traceback(traceback_i,lines,"UNRECOGNIZED FUNCTION DUMBASS")
                except:
                    traceback(traceback_i,lines,"Didnt find your function dumbass")
            else:
                if(disable == -1 and line != ['']):
                    traceback(traceback_i,lines,"You didnt put a command we recognize you dumbass(You cant have lines at the beginning of variables or functions)")
            i+=1
        if(disable != -1):
            traceback(traceback_i,lines,"Statement "+lines[disable].strip().lstrip()+" on line "+str(disable+1)+" has no corresponding done statement dumbass")
logic()

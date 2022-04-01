def arithmetic_arranger(problems, compute = False):

    x = problems
    num_probs = len(x)
    
    operand1 = []
    operand2 = []
    operator = []
    ans = []
    
    # 1st error
    if num_probs > 5:
        return print("Error: Too many problems.")
    
    for i in range(num_probs):
        prob = x[i].strip().split()
        
        operand1.append(prob[0])
        operand2.append(prob[2])
        operator.append(prob[1])
        
        # 2nd error
        if operator[i] != "+" and operator[i] != "-":
            return print("Error: Operator must be '+' or '-'.")
        
        #3rd error
        if operand1[i].isdigit() == False or operand2[i].isdigit() == False:
            return print("Error: Numbers must only contain digits.")
        
        # 4th error
        if len(operand1[i]) > 4 or len(operand2[i]) > 4:
            return print("Error: Numbers cannot be more than four digits.")
    
    for i in range(num_probs):
        # compute answers
        if operator[i] == "+":
            ans.append(int(operand1[i]) + int(operand2[i]))
        elif operator[i] == "-":
            ans.append(int(operand1[i]) - int(operand2[i]))
    
    spaces = "    "
    firstline = ""
    secondline = ""
    dashline = ""
    answers = ""
    
    for i in range(num_probs):
        if len(operand1[i]) > len(operand2[i]):
            whitespace1 = "  "
            whitespace2 = ""
            dashes = ""
            len_diff = len(operand1[i]) - len(operand2[i])
            for j in range(len_diff):
                whitespace2 = whitespace2 + " "
            firstline = firstline + whitespace1 + operand1[i] + spaces
            secondline = secondline + operator[i] + " " + whitespace2 + operand2[i] + spaces
            for k in range(len(operand1[i]) + 2):
                dashes = dashes + "-"
            dashline = dashline + dashes + spaces
            if len(str(ans[i])) < 5:
                answers = answers + whitespace1 + str(ans[i]) + spaces
            elif len(str(ans[i])) >= 5:
                answers = answers + " " + str(ans[i]) + spaces
        elif len(operand2[i]) > len(operand1[i]):
            whitespace1 = ""
            whitespace2 = " "
            dashes = ""
            len_diff = len(operand2[i]) - len(operand1[i])
            for j in range(len_diff + 2):
                whitespace1 = whitespace1 + " "
            firstline = firstline + whitespace1 + operand1[i] + spaces
            secondline = secondline + operator[i] + whitespace2 + operand2[i] + spaces
            for k in range(len(operand2[i]) + 2):
                dashes = dashes + "-"
            dashline = dashline + dashes + spaces
            if len(str(ans[i])) < 5:
                answers = answers + " " + whitespace2 + str(ans[i]) + spaces
            elif len(str(ans[i])) >= 5:
                answers = answers + " " + str(ans[i]) + spaces
        elif len(operand1[i]) == len(operand2[i]):
            whitespace1 = "  "
            whitespace2 = ""
            dashes = ""
            len_diff = len(operand1[i]) - len(operand2[i])
            for j in range(len_diff):
                whitespace2 = whitespace2 + " "
            firstline = firstline + whitespace1 + operand1[i] + spaces
            secondline = secondline + operator[i] + " " + whitespace2 + operand2[i] + spaces
            for k in range(len(operand1[i]) + 2):
                dashes = dashes + "-"
            dashline = dashline + dashes + spaces
            if len(str(ans[i])) < 5:
                answers = answers + whitespace1 + str(ans[i]) + spaces
            elif len(str(ans[i])) >= 5:
                answers = answers + " " + str(ans[i]) + spaces
    
    if compute == True:
        arranged_problems = firstline + "\n" + secondline + "\n" + dashline + "\n" + answers
        return print(arranged_problems)
    else:
        arranged_problems = firstline + "\n" + secondline + "\n" + dashline
        return print(arranged_problems)

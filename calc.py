def mycalc(oper, num1, num2):
    if oper == "+":
        ans = num1 + num2
    elif oper == "-":
        ans = num1 - num2
    elif oper == "*" or oper == "x":
        ans = num1 * num2
    elif oper == "/":
        ans = num1 / num2
    return (ans)

f = open('calc.txt')
total = 0

data = []
for line in f:
    data_line = line.splitlines()
    data.append(data_line)
    print (data_line)

    for line in data_line:
        #print (f"{line} \n")
        calc = line.split(" ")
        print(calc)
        oper = calc[1]
        num1 = int(calc[2])
        num2 = int(calc[3])
        print(oper)
        print(num1)
        print(num2)
        # per = calc[2]
        # print(oper)

        #mycalc(oper, num1, num2)
        #total += ans

        if oper == "+":
            ans = num1 + num2
        elif oper == "-":
            ans = num1 - num2
        elif oper == "*" or oper == "x":
            ans = num1 * num2
        elif oper == "/":
            ans = num1 / num2
        
        print (f"Answer is: {ans}")
        total += ans

print (f"Grand Total: {total}")

f.close()

#simple comment change


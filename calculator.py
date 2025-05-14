print("1_add")
print("2_subtract")
print("3_divide")
print("4_multiply")
print("5_module")
option=int(input("choose an operator: "))
if (option in [1,2,3,4,5]):
    num1=int(input("enter the first number: "))
    num2=int(input("enter second number: "))
    if option==1:
        result=num1+num2
    if option==2:
        result=num1-num2
    elif option==3:
        result=num1/num2
    elif option==4:
        result=num1*num2
    elif option==5:
        result=num1//num2
    else:
        print("invalid operator entered")
    print("the result is",format(result))                
def perform_calc (*args,**kwargs):
    num1,num2=args
    op=kwargs.get("operand")
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    elif op=="/":
        return num1/num2
    else:
        return"INVALID OPERAND"

print(perform_calc(10,20,operand="+"))
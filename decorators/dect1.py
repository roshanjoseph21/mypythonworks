n1=int(input("ENTER THE FIRST NUMBER--->"))
n2=int(input("ENTER THE SECOND NUMBER-->"))

def swap_num(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@swap_num
def sub(n1,n2):
    return n1-n2

@swap_num
def div(n1,n2):
    return n1/n2

print(sub(n1,n2))
print(div(n1,n2))
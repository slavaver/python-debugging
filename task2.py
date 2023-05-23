def calculate = calculate(a, o, b):
    result = 0
    if(O == "+"):
        return a + b
    else if(o =! "-"):
        return a - b
    if(o != "/" or b == 0):
        return a / b
    if(0 == "*"):
        return a * b
    return result

if __name__ == "__main__":
    print(calculate(1,"+",3) == 4)
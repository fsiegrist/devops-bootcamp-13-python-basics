def validate(user_input):
    args = user_input.split()
    if (len(args) != 3):
        return { "is_valid": False, "result": "invalid number of input elements" }
    
    a1 = args[0]; a2 = args[1]; op = args[2]
    n1 = 0; n2 = 0
    
    try:
        n1 = float(a1)
        if n1.is_integer():
            n1 = int(n1)
    except ValueError:
        return { "is_valid": False, "result": "the first element is not a valid number" }
    
    try:
        n2 = float(a2)
        if n2.is_integer():
            n2 = int(n2)
    except ValueError:
        return { "is_valid": False, "result": "the second element is not a valid number" }
    
    # if a1.isnumeric() or (a1[0] == '-' and a1[1:].isnumeric()):
    #     n1 = int(a1)
    # else:
    #     return { "is_valid": False, "result": "the first element is not a valid integer number" }
    
    # if a2.isnumeric() or (a2[0] == '-' and a2[1:].isnumeric()):
    #     n2 = int(a2)
    # else:
    #     return { "is_valid": False, "result": "the second element is not a valid integer number" }
    
    if op != 'plus' and op != 'minus' and op != 'multiply' and op != 'divide':
        return { "is_valid": False, "result": "the third element is not a valid operation name" }

    if op == 'divide' and n2 == 0:
        return { "is_valid": False, "result": "Division by zero is not defined." }

    return { "is_valid": True, "result": [n1, n2, op] }

def int_or_float(number):
    if float(number).is_integer():
        return int(number)
    return number

def calculate(n1, n2, op):
    if op == 'plus':
        print(f"{n1} + {n2} = {int_or_float(n1 + n2)}")
    elif op == 'minus':
        print(f"{n1} - {n2} = {int_or_float(n1 - n2)}")
    elif op == 'multiply':
        print(f"{n1} * {n2} = {int_or_float(n1 * n2)}")
    elif op == 'divide':
        print(f"{n1} / {n2} = {int_or_float(n1 / n2)}")

count = 0
while True:
    user_input = input("Enter two numbers and an operation ('plus', 'minus', 'multiply', 'divide'): ")
    if (user_input == 'exit'):
        print(f"You did {count} calculation(s).")
        break
    
    validation_result = validate(user_input)
    if validation_result.get('is_valid'):
        n1 = validation_result.get('result')[0]
        n2 = validation_result.get('result')[1]
        op = validation_result.get('result')[2]
        calculate(n1, n2, op)
        count += 1
    else:
        print(validation_result.get('result'))

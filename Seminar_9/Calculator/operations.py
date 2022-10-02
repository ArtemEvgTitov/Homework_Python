import check as ch

def sum(text):
    a, b = ch.check_number(text)
    total = a + b
    a = int(a) if a == float(int(a)) else a
    b = int(b) if b == float(int(b)) else b
    total = int(total) if total == float(int(total)) else total
    return f'{a} + {b} = {total}'

def diff(text):
    a, b = ch.check_number(text)
    total = a - b
    a = int(a) if a == float(int(a)) else a
    b = int(b) if b == float(int(b)) else b
    total = int(total) if total == float(int(total)) else total
    return f'{a} - {b} = {total}'

def div(text):
    a, b = ch.check_number(text)
    total = a / b
    a = int(a) if a == float(int(a)) else a
    b = int(b) if b == float(int(b)) else b
    total = int(total) if total == float(int(total)) else total
    return f'{a} / {b} = {total}'

def mult(text):
    a, b = ch.check_number(text)
    total = a * b
    a = int(a) if a == float(int(a)) else a
    b = int(b) if b == float(int(b)) else b
    total = int(total) if total == float(int(total)) else total
    return f'{a} * {b} = {total}'
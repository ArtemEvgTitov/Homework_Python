def priority(sym_1: str, sym_2: str, t_str: str) -> str:
    if sym_1 in t_str and sym_2 in t_str:
        if t_str.find(sym_1) > t_str.find(sym_2):
            return sym_2
        elif t_str.find(sym_1) < t_str.find(sym_2):
            return sym_1
    elif sym_1 in t_str:
        return sym_1
    elif sym_2 in t_str:
        return sym_2

def clear_sym_string(t_str: str) -> str:
    rez = t_str.replace('^', '**')
    rez = rez.replace(' ', '')
    rez = rez.replace('+-', '-')
    rez = rez.replace('-+', '-')
    rez = rez.replace(',', '.')

    return rez

def char_pr(sym: str, t_str: str):
    index = t_str.find(sym)
    right_num = ''
    t = 0
    if sym == '**':
        a = index + 2
    else:
        a = index +1
    sing = (t_str[a])
    if sing == '-':
        right_num = right_num + (t_str[i])
        a += 1
    elif sing == '+':
        a += 1
    for i in range(a, len(t_str)):
        bb = (t_str[i])
        if bb.isdigit() or bb == '.':
            right_num = right_num + bb
            if bb == '.':
                t += 1
        else:
            break
    if t > 0:
        right_num = float(right_num)
    else:
        right_num = int(right_num)
    return right_num

def char_lev(sym: str, t_str: str):
    index = t_str.find(sym)
    left_num = ''
    t = 0
    for i in range(index-1, -1, -1):
        bb = (t_str[i])
        if bb.isdigit() or bb == '.':
            left_num = bb + left_num
            if bb == '.':
                t += 1
        else:
            break
    if t > 0:
        left_num = float(left_num)
    else:
        left_num = int(left_num)
    return left_num

def calc(sym: str, left_num, right_num):
    if sym == '**':
        return left_num**right_num
    elif sym == '*':
        return left_num*right_num
    elif sym == '/':
        return left_num/right_num
    elif sym == '+':
        return left_num+right_num
    elif sym == '-':
        return left_num-right_num

def begin_calc(sym: str, t_str: str):
    index = t_str.find(sym)
    left_num = char_lev(sym, t_str)
    right_num = char_pr(sym, t_str)
    res = calc(sym, left_num, right_num)
    li = index - len(str(left_num))
    ri = li + len(str(left_num) + sym + str(right_num))
    return t_str[:li] + str(res) + t_str[ri:]

def run_oper(t_str: str):
    while '**' in t_str:
        sym = '**'
        t_str = begin_calc(sym, t_str)
    while '*' in t_str or '/' in t_str:
        sym = priority('*', '/', t_str)
        t_str = begin_calc(sym, t_str)
    while '+' in t_str or '-' in t_str:
        if t_str.find('-') == 0:
            break
        else:
            sym = priority('+', '-', t_str)
            t_str = begin_calc(sym, t_str)
    result = float(t_str)
    if result % 1 == 0:
        result = int(result)
    return result


input_string = '(2+((5.5-3)*(16-14)))/3'

try:
    pr_otv = eval(input_string)
except:
    print('Выражение не корректно!')
    exit()

print(f'Правильный ответ {pr_otv}')


new_str = clear_sym_string(input_string)

while new_str.count('(') != 0 or new_str.count(')') !=0:
    right_index = new_str.find(')')
    item = new_str.find('(')
    while new_str.find('(', item) != -1:
        if new_str.find('(', item + 1) > right_index or new_str.find('(', item + 1) == -1:
            left_index = new_str.find('(', item)
            break
        else:
            item = new_str.find('(', item + 1)
    expr = new_str[left_index + 1: right_index]
    res = run_oper(expr)
    new_str = new_str[:left_index] + str(res) + new_str[right_index + 1:]
    new_str = new_str.replace('+-', '-')

result = run_oper(new_str)
print(f'Мой расчет: {result}')
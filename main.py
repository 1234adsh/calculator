def add(num1, num2):
    temp_num = num1
    for fin_num in range(num2):
        temp_num += 1

    return temp_num


def subtract(num1, num2):
    temp_num = num1
    for fin_num in range(num2):
        temp_num -= 1

    return temp_num


def multiply(num_1, num_2):
    temp_num = num_1 * num_2
    return temp_num


def remainder_divide(num1,num2):
    result = {
        'quotient': None,
        'remainder': None
    }
    temp_num = num1 // num2
    result['quotient'] = temp_num
    temp_num = num1 % num2
    result['remainder'] = temp_num

    return result


def divide(num_1, num_2):
    return num_1/num_2


def exponent(num_1, num_2):
    temp = num_1
    fin = num_1
    for i in range(1, num_2):
        fin *= temp

    return fin


def factors(number):
    divisor = (number)
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1

    return result



print(factors(-12))
print(factors(12))
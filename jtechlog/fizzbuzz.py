def fizzbuzz(to_number):
    result = ""
    for i in range(1, to_number + 1):
        if result != "":
            result += " "
        if i % 3 == 0 and i % 5 == 0:
            result += 'fizzbuzz'
        elif i % 3 == 0:
            result += 'fizz'
        elif i % 5 == 0:
            result += 'buzz'
        else:
            result += str(i)
    return result

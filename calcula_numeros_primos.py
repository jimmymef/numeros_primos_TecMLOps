def is_prime(num):
    if num < 1:
        return False

    elif num == 2:
        return True
    
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Write a number: '))
    new_num = mersenne_number(num)
    print(f"mersenne generó el número {new_num}")
    result = is_prime(new_num)
    if result:
        print(f"El numero {new_num} es primo")
    
    else: print(f"El numero {new_num} no es primo")

def mersenne_number(p) :
    if not isinstance(p, int):
        raise TypeError("p must be integer")
    return (2 ** p) - 1

if __name__ == '__main__':
    app()



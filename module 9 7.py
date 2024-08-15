def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        if total > 1:
            for i in range(2, int(total // 2) + 1):
                if total % i == 0:
                    return 'Составное'
        return 'Простое'
    return wrapper


@is_prime
def summ_three(a, b, c):
    print(a + b + c)
    return a + b + c


result = summ_three(2, 3, 6)
print(result)

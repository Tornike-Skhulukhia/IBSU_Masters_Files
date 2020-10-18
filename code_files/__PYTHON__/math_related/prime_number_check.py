
def is_prime(number):

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True



# test
assert is_prime(13)
assert not is_prime(12)
assert is_prime(79)
assert not is_prime(840)


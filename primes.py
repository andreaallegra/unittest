
# Getting Started with PyCharm 7/8: Testing
# https://www.youtube.com/watch?v=-VzJvNLooj4

# from example by jeff Knupp


def is_prime(number):
    """
    Return true is number is prime
    """
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def print_next_prime(number):
    """
    print the closest prime number larger than numbers
    """
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)


def main():
    test = is_prime(11)
    print(test)
    print_next_prime(4)


if __name__ == '__main__':
    main()




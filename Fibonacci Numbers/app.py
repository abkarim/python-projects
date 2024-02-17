max_number = 1_00_000


def generate_fibonacci(max_number):
    a = 0
    b = 1

    while b < max_number:
        print(b)

        current_number = a + b
        a = b
        b = current_number


generate_fibonacci(max_number)

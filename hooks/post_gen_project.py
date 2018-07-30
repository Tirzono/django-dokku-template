import random


def generate_random_string(length=50, allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'):
    return ''.join(random.choice(allowed_chars) for i in range(length))


def main():
    pass


if __name__ == "__main__":
    main()

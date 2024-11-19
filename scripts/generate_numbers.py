import random

def generate_numbers_file(filename):
    with open(filename, 'w') as f:
        number1 = random.randint(1000, 100000)  # Large random integer
        number2 = random.randint(1000, 100000)  # Another large random integer
        f.write(f"{number1}\n{number2}\n")

generate_numbers_file("numbers.txt")
print("numbers.txt generated successfully!")

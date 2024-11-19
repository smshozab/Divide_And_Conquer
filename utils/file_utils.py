import random

def generate_points_file(filename, num_points=100):
    with open(filename, 'w') as f:
        for _ in range(num_points):
            x, y = random.randint(0, 1000), random.randint(0, 1000)
            f.write(f"{x} {y}\n")

def generate_numbers_file(filename, num_digits=100):
    with open(filename, 'w') as f:
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        f.write(f"{num1}\n{num2}\n")

def load_points(file):
    """Load points from an uploaded file."""
    points = []
    for line in file:
        x, y = map(float, line.strip().split())
        points.append((x, y))
    return points


def load_numbers(file):
    """Load a list of numbers from the uploaded file."""
    # Read the file-like object
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    return numbers


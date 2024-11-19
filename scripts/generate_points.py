import random

def generate_points_file(filename, num_points=10):
    with open(filename, 'w') as f:
        for _ in range(num_points):
            x = random.randint(0, 100)  # Random x-coordinate
            y = random.randint(0, 100)  # Random y-coordinate
            f.write(f"{x} {y}\n")

generate_points_file("points.txt")
print("points.txt generated successfully!")

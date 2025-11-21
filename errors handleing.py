filename = ("sample.txt")
try:
    print("Reading filee contents:")
    with open(filename, "r") as file:
        for idx, line in enumerate(file, 1):
            print(f"line {idx}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found")
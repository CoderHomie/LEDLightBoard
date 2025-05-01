def format_integers_from_txt(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))  # Read, split, and convert to integers
    
    numbers.sort()  # Sort the list
    formatted_numbers = ', '.join(map(str, numbers))  # Convert to string and join with commas
    result = f'{{{formatted_numbers}}}'  # Wrap in curly braces
    print(result)
    print(len(numbers))

if __name__ == "__main__":
    file_path = "numbers.txt"  # Specify text file path
    format_integers_from_txt(file_path)
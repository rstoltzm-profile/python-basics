def main():
    """
    Main function to execute the program.
    """
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    result = add_numbers(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is {result}")

def add_numbers(a, b):
    """
    Function to add two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The sum of the two numbers.
    """
    return a + b

if __name__ == "__main__":
    main()

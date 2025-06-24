try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
#finally block is used to execute code that should run regardless of whether an exception occurred or not
finally:   
    print("Execution completed.")
import os
import time
from datetime import datetime

def clear_screen():
    # Clear screen command based on operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print("=" * 40)
    print("           PRADEEP CALCULATOR           ")
    print("=" * 40)

def save_calculation(calculation):
    # Create a folder if it doesn't exist
    if not os.path.exists('calculations'):
        os.makedirs('calculations')
    
    # Generate filename with timestamp
    filename = f"calculations/calc_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Save calculation to file
    with open(filename, 'w') as f:
        f.write(calculation)
    return filename

def display_menu():
    print("\nAvailable Operations:")
    print("╔══════════════════════════════╗")
    print("║  1. Addition       (+)       ║")
    print("║  2. Subtraction    (-)       ║")
    print("║  3. Multiplication (×)       ║")
    print("║  4. Division       (÷)       ║")
    print("║  5. Save & Exit              ║")
    print("║  6. Exit without Saving      ║")
    print("╚══════════════════════════════╝")

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def calculator():
    calculations = []  # Store calculation history
    
    while True:
        clear_screen()
        display_header()
        display_menu()
        
        # Get user input for operation choice
        choice = input("\nEnter operation number (1-6): ")
        
        if choice == '5':
            if calculations:
                # Join all calculations with newlines
                history = '\n'.join(calculations)
                filename = save_calculation(history)
                print(f"\nCalculations saved to: {filename}")
                print("\nThank you for using the calculator!")
                time.sleep(2)
                clear_screen()
            else:
                print("\nNo calculations to save!")
                time.sleep(2)
            break
            
        elif choice == '6':
            print("\nExiting without saving...")
            time.sleep(2)
            clear_screen()
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid operation choice!")
            time.sleep(2)
            continue
        
        # Get user input for numbers
        print("\nEnter your numbers:")
        print("-------------------")
        num1 = get_number_input("First number: ")
        num2 = get_number_input("Second number: ")
        
        # Perform calculation based on user's choice
        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '×'
        elif choice == '4':
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
                time.sleep(2)
                continue
            result = num1 / num2
            operation = '÷'
        
        # After calculating result, store the calculation
        calculation_str = f"{num1} {operation} {num2} = {result:.2f}"
        calculations.append(calculation_str)
        
        # Display the result
        print("\nResult:")
        print("--------")
        print(calculation_str)
        
        # Ask if user wants to continue
        input("\nPress Enter to continue...")

def main():
    try:
        calculator()
    except KeyboardInterrupt:
        clear_screen()
        print("\nCalculator closed.")

if __name__ == "__main__":
    main()
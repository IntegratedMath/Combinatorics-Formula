import math
import Single_Subword
from multA import multA

def get_user_input():
    """
    Prompts the user for input values 'q', 't', 'd', and lists of 'a' and 'x' values.
    Performs validation on the inputs.
    Returns:
        q (int): The 'q' value (q > 1).
        t (int): The 't' value (t > 1).
        a_list (list): A list of multA objects containing 'a', 'x', and 'i' values.
    """
    # Prompt user for 'q' with validation (q > 1)
    while True:
        try:
            q = int(input("Enter the 'q' value (q > 1): "))
            if q > 1:
                break
            print("Error: 'q' must be greater than 1.")
        except ValueError:
            print("Error: Please enter a valid integer for 'q'.")

    # Prompt user for 't' with validation (t > 1)
    while True:
        try:
            t = int(input("Enter the 't' value (t > 1): "))
            if t > 1:
                break
            print("Error: 't' must be greater than 1.")
        except ValueError:
            print("Error: Please enter a valid integer for 't'.")

    # Prompt user for 'd' with validation (d > 0)
    while True:
        try:
            d = int(input("Enter the 'd' value (d > 0): "))
            if d > 0:
                break
            print("Error: 'd' must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer for 'd'.")

    a_list = []
    for j in range(d):
        # Prompt user for 'a' with validation (1 < a <= t)
        while True:
            try:
                a = int(input(f"Enter 'a_{j + 1}' value (1 < a_{j + 1} <= {t}): "))
                if 1 < a <= t:
                    break
                print(f"Error: 'a_{j + 1}' must be between 1 and {t}.")
            except ValueError:
                print(f"Error: Please enter a valid integer for 'a_{j + 1}'.")

        # Prompt user for 'x' with validation (x >= 1)
        while True:
            try:
                x = int(input(f"Enter 'x_{j + 1}' value (x_{j + 1} >= 1): "))
                if x >= 1:
                    break
                print(f"Error: 'x_{j + 1}' must be at least 1.")
            except ValueError:
                print(f"Error: Please enter a valid integer for 'x_{j + 1}'.")

        # Initialize multA object and append to list
        a_list.append(multA(a, x, x))

    return q, t, a_list

def calculate_iterative(a_list, q, t):
    """
    Performs the main calculation using an iterative approach to avoid recursion depth issues.
    Args:
        a_list (list): A list of multA objects.
        q (int): The 'q' value.
        t (int): The 't' value.
    Returns:
        total (int): The result of the calculation.
    """
    stack = [(a_list, 0, 0)]
    total = 0
    memo = {}

    while stack:
        current_list, depth, buffer = stack.pop()

        # Create a key for memoization based on the current state
        state_key = tuple((item.l, item.x, item.i) for item in current_list)
        if state_key in memo:
            total += memo[state_key]
            continue

        alternator = (-1) ** depth
        perm = 1
        total_size = 0
        total_copy = 0
        multiplier = 1

        # Calculate total_size, total_copy, perm, and multiplier
        for item in current_list:
            total_copy += item.i
            total_size += item.i * item.l
            perm *= math.factorial(item.i)
            multiplier *= Single_Subword.multiplier(item.i, item.x)

        if total_copy == 0:
            continue  # Avoid division by zero

        perm = math.factorial(total_copy) // perm
        temp_a = total_size / total_copy

        # Compute the answer for the current state
        answer = (alternator *
                  Single_Subword.exponent_term(q, t, temp_a, total_copy) *
                  Single_Subword.combForm(total_copy, t, temp_a) *
                  perm * multiplier)

        total += answer
        memo[state_key] = answer  # Store the result in the memoization dictionary

        # Iterate over possible next states
        for i in range(buffer, len(current_list)):
            if total_size + current_list[i].l <= t:
                # Create a copy of current_list and update the 'i' value
                new_list = current_list.copy()
                new_list[i] = multA(new_list[i].l, new_list[i].x, new_list[i].i + 1)
                stack.append((new_list, depth + 1, i))

    return total

def output_large_number(total):
    """
    Handles the output of large numbers by splitting them into manageable chunks.
    Args:
        total (int): The large number to output.
    """
    chunk_size = 4300
    num_chunks = []

    # Split the total into manageable chunks for output
    while total > 0:
        num_chunks.append(total % (10 ** chunk_size))
        total //= (10 ** chunk_size)

    # Print chunks in correct order with leading zeros where necessary
    for i in range(len(num_chunks) - 1, -1, -1):
        if i == len(num_chunks) - 1:
            print(num_chunks[i], end="")
        else:
            print(str(num_chunks[i]).zfill(chunk_size), end="")

    print()  # Final newline for clean output

def main():
    """
    Main function to execute the program.
    """
    # Get user input
    q, t, a_list = get_user_input()

    # Perform the calculation
    total = calculate_iterative(a_list, q, t)

    # Output the result
    output_large_number(total)

if __name__ == "__main__":
    main()

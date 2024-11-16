import math

### Input Section ###

# Prompt user for 'q' with validation (q > 1)
while True:
    q = int(input("What is your 'q' value (q > 1): "))
    if q > 1:
        break
    print("Error: 'q' must be greater than 1.")

# Prompt user for 't' with validation (t > 1)
while True:
    t = int(input("What is your 't' value (t > 1): "))
    if t > 1:
        break
    print("Error: 't' must be greater than 1.")

# Prompt user for 'a' with validation (1 < a <= t)
while True:
    a = int(input(f"What is your 'a' value (1 < a <= {t}): "))
    if 1 < a <= t:
        break
    print(f"Error: 'a' must be between 1 and {t}.")

# Prompt user for 'x' with validation (x >= 1)
while True:
    x = int(input("What is your 'x' value (x >= 1): "))
    if x >= 1:
        break
    print("Error: 'x' must be at least 1.")

### Helper Functions ###

# Calculates the alternating sign for each term
def alternator(i, x):
    return (-1) ** (i + 1 if x % 2 == 1 else i)

# Computes q raised to the power of (t - a * i)
def exponent_term(q, t, a, i):
    return q ** (t - a * i)

# Computes the combination with replacement: C(n + k - 1, k)
def combForm(i, t, a):
    k = t - a * i
    n = i + 1
    return math.comb(n + k - 1, k) if k >= 0 else 0

# Computes the regular combination: C(n, k)
def multiplier(i, x):
    k = i - x
    n = i - 1
    return math.comb(n, k) if k >= 0 else 0

### Main Calculation Loop ###
total = 0
for i in range(x, math.floor(t / a) + 1):
    term = alternator(i, x) * exponent_term(q, t, a, i) * combForm(i, t, a) * multiplier(i, x)
    total += term

### Large Number Output Handling ###
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


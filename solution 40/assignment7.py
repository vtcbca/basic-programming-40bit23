def print_triangle_recursive(n, i=1):
    if i > n:
        return
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers for each row
    for j in range(1, 2 * i):
        print(j, end=" ")
    print()  # Move to the next line
    print_triangle_recursive(n, i + 1)

# Example 
print_triangle_recursive(3)
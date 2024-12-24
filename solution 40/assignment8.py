def print_alphabet_pattern_list_comprehension(n):
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")

        # List comprehension for the increasing part of the row
        increasing_part = [chr(65 + j) for j in range(i + 1)]
        
        # List comprehension for the decreasing part of the row
        decreasing_part = [chr(65 + j) for j in range(i - 1, -1, -1)]

        # Join and print both parts of the row
        print(" ".join(increasing_part + decreasing_part))

# usage:
n = 3
print_alphabet_pattern_list_comprehension(n)

def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

# Example usage:
input_string = "hello"
print(reverse_string_recursive(input_string)) 
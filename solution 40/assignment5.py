def is_palindrome_stack(s):
    stack = []
    for char in s:
        stack.append(char)
    for char in s:
        if char != stack.pop():
            return False
    return True

# Example usage:
print(is_palindrome_stack("radar"))
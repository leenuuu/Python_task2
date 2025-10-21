def doOperation(val1, val2, operation):
    if operation == 'sub':
        return f"operation={operation} val1={val1}, val2={val2} val1 - val2 = {val1 - val2}"
    elif operation == 'mul':
        return f"operation={operation} val1={val1}, val2={val2} val1 * val2 = {val1 * val2}"
    elif operation == 'div':
        return f"operation={operation} val1={val1}, val2={val2} val1 / val2 = {val1 / val2}"
    elif operation == 'add':
        return f"operation={operation} val1={val1}, val2={val2} val1 + val2 = {val1 + val2}"
    else:
        return f"your operation did not match operation = {operation}"

print(doOperation(12, 3, 'add'))
print()  
print(doOperation(12, 3, 'sub'))
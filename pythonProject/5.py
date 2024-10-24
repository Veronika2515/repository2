result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a must be greater than or equal to b")
        if b > 100:
            raise IndexError("b must be less than or equal to 100")
        return a / b
    except (ValueError, IndexError, TypeError) as e:
        print(f"An error occurred: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}  # Видалив некоректний елемент зі списком

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print(f"Division by zero for key: {key}")

print(result)
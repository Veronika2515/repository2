def error_handler(func):
    def inner(expression):
        try:
            return func(expression)
        except ZeroDivisionError:
            return "Помилка: Діленя на нуль"
        except SyntaxError:
            return "Помилка: Некоректний синтаксис виразу"
        except Exception as e:
            return f"Непередбачена помилка: {str(e)}"
    return inner

@error_handler
def calculate(expression):
    return eval(expression)

print(calculate("2+2"))
print(calculate("5/0"))
print(calculate("2*3+4"))
print(calculate("27.6/34"))
print(calculate("2+2*2"))
print(calculate("9999*9999*9999*9999*9999"))
# ловушка при инициализации переменной как пустого списка в сигнатуре метода

def add_item(item, collection=[]):
    collection.append(item)
    return collection

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]

# как этого избежать

def add_item(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection

print(add_item(1))  # [1]
print(add_item(2))  # [2]


# * - tuple
# ** - dict
def greet(*names, **options):
    greeting = options.get("greeting", "Привет")
    age = options.get("age", 18)
    for name in names:
        print(f"{greeting}, {name}! Тебе {age} лет")

greet("Аня", "Игорь", greeting="Здравствуйте", age=20)
# Здравствуйте, Аня! Тебе 20 лет
# Здравствуйте, Игорь! Тебе 20 лет

# использование явного указания типа необязательно, 
# но очень показательно и является хорошей практикой
def square(x: int) -> int:
    return x * x


# функция может возвращать несколько значений, которые
# так же можно принимать сразу в несколько переменных
def divide(a, b):
    q = a // b
    r = a % b
    return q, r
 
quotient, remainder = divide(10, 3)
print(quotient, remainder)  # 3 1



# ====================================================
# конструкции и методы в python: примеры использования
# ====================================================

def demo_1():
    # создание элементов списка в строку 
    numbers = [x for x in range(10) if x % 2 == 0]
    print(numbers)

def demo_2():
    # создание элементов списка в строку через двойной цикл
    pairs = [(x, y) for x in range(3) for y in range(3)]
    print(pairs)

def demo_3():
    # создание элементов словаря и множества
    squares = {x: x**2 for x in range(5)}
    unique = {ch for ch in "hello world"}
    print(squares)
    print(unique)

def demo_4():
    # использование функции enumerate
    for i, value in enumerate(["a", "b", "c"], start=1):
        print(i, value)

def demo_5():
    # использование функции zip
    names = ["Иван", "Аня", "Олег"]
    grades = [5, 4, 3]
    for name, grade in zip(names, grades):
        print(name, grade)

def demo_6():
    # использование функций sorted, reversed
    for x in sorted([3, 1, 4, 2]):
        print(x, end=" ")
    print()
    for x in reversed("python"):
        print(x, end="_")
    print()

def demo_7():
    # использование срезов
    nums = [1, 2, 3, 4, 5, 6]
    print(nums[::-1])
    print(nums[::2])
    print(nums[1::2])
    print(nums[1:2])

# * - tuple
# ** - dict
def greet(*names, **options):
    # names = ("Аня", "Игорь")
    # options = {
    #     'greeting': "Здравствуйте", 
    #     'age': 20
    # }
    greeting = options.get("greeting", "Привет")
    age = options.get("age", 18)
    for name in names:
        print(f"{greeting}, {name}! Тебе {age} лет")

# greet("Аня", "Игорь", "Frank", age=20)

def demo_8():
    # распаковка с *
    a, b, *rest = [1, 2, 3, 4, 5]
    print(a, b, rest)
    first, *_, last = [10, 20, 30, 40]
    print(first, last)

def demo_9():
    # множественная инициализация переменных
    x, y = 5, 10
    x, y = y, x
    print(x, y)

def demo_10():
    # использование f в строках
    name, age = "Иван", 20
    print(f"Привет, {name.upper()}! Через 5 лет тебе будет {age+5}.")

def demo_11():
    # использование функции join
    words = ["Python", "is", "fun"]
    sentence = " ".join(words)
    print(sentence)
    print(sentence.split())

def demo_12():
    # использование функций ord, chr для получение кода и самого символа
    print(ord("🐀"))
    print(chr(128000))

def demo_13():
    # использование функций all, any
    nums = [2, 4, 6, 8]
    print(all(x % 2 == 0 for x in nums))
    print(any(x > 5 for x in nums))

    print(all([True, False]))
    print(any([True, False]))

def demo_14():
    # zip + *
    pairs = [(1, "a"), (2, "b"), (3, "c")]
    numbers, letters = zip(*pairs)
    print(numbers)
    print(letters)

def demo_17():
    # использование Counter для быстрого подсчета
    from collections import Counter

    words = ["apple", "kiwi", "banana", "banana", "banana", "apple", "banana", "apple"]
    counter = Counter(words)
    print(counter)
    print(counter.most_common(1)[0][0])

def demo_18():
    # zip + enumerate
    names = ["Иван", "Аня", "Олег"]
    scores = [90, 85, 70]
    for i, (name, score) in enumerate(zip(names, scores), start=1):
        print(f"{i}. {name}: {score}")

def demo_19():
    # map
    nums = ["1", "2", "3", "4"]
    nums = list(map(int, nums))
    print(nums)


# ========================================
# анонимные функции: примеры использования
# ========================================

# простые примеры создания и использования
def demo_lambda_square():
    square = lambda x: x**2
    print("5² =", square(5))

def demo_lambda_sum():
    add = lambda a, b: a + b
    print("2 + 3 =", add(2, 3))

def demo_lambda_even_odd():
    check = lambda x: "да" if x % 2 == 0 else "нет"
    print("3 →", check(3))
    print("10 →", check(10))

# использование анонимых функций с методами map, filter, reduce
def demo_lambda_map():
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x**2, nums))
    print("squares:", squares)

def demo_lambda_filter():
    nums = [10, 15, 20, 25]
    even = list(filter(lambda x: x % 2 == 0, nums))
    print("без остатка:", even)

def demo_lambda_reduce():
    from functools import reduce

    nums = [1, 2, 3, 4, 5]
    product = reduce(lambda a, b: a * b, nums)
    print("product:", product)

# использование анонимых функций для сортировок
def demo_lambda_sorted_multi():
    students = [("Иван", 20), ("Аня", 15), ("Олег", 17)]
    print(sorted(students, key=lambda x: x[0]))

def demo_lambda_sorted_dicts():
    people = [
        {"name": "Иван", "age": 20}, 
        {"name": "Аня", "age": 29}
    ]
    print(sorted(people, key=lambda p: p["age"]))

# динамический вызов функций 
def demo_lambda_in_dict():

    def func(a, b):
        return a + b

    ops = {
        "add": func,
        "mul": lambda a, b: a * b
    }

    print("add:", ops["add"](2, 3))
    print("mul:", ops["mul"](2, 3))
















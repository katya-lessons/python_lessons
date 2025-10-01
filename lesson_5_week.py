# алгоритмы

# линейный поиск
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1

students = ["Анна", "Борис", "Виктор", "Мария"]
index = linear_search(students, "Виктор")
print(index)

# бинарный поиск по отсортированному списку
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


grades = [65, 72, 78, 85, 90, 92, 95]
index = binary_search(grades, 78)
print(index)


# сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


products = [1200, 500, 800, 1500, 300]

sorted_products = bubble_sort(products) 
print(sorted_products)  # [300, 500, 800, 1200, 1500]

# фильтрация
def filter_by_condition(arr, condition):
    result = []
    for item in arr:
        if condition(item):
            result.append(item)
    return result

temperatures = [15, 22, 18, 25, 30, 12, 20]
hot_days = filter_by_condition(temperatures, lambda x: x > 20)
print(hot_days)  # [22, 25, 30]

rainy_days = [day for day in temperatures if day < 18]
print(rainy_days)  # [15, 12]

moderate_days = [day for day in temperatures if 18 <= day <= 25]
print(moderate_days)  # [22, 18, 25, 20]

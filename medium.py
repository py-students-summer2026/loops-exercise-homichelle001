def one():
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    numbers = [3, 7, 2, 9, 5, 1, 8, 4, 6]
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print(f"Largest element in {numbers} is {largest}")

def two():
    """
    Write a program that calculates the average of a list of numbers using a while loop.
    You are not allowed to use the built-in sum() function.
    """
    numbers = [10, 20, 30, 40, 50, 60]
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    average = total / len(numbers)
    print(f"Average of {numbers} is {average}")

def three():
    """
    Write a program that checks if a given string is a palindrome using a for loop.
    """
    test_string = "racecar"
    is_palindrome = True
    for i in range(len(test_string) // 2):
        if test_string[i] != test_string[len(test_string) - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        print(f'"{test_string}" is a palindrome')
    else:
        print(f'"{test_string}" is not a palindrome')

def four():
    """
    Write a program that prints the first n terms of the geometric sequence using a while loop.
    """
    n = 8
    first_term = 2
    common_ratio = 3
    i = 0
    term = first_term
    print(f"First {n} terms of geometric sequence (ratio={common_ratio}):")
    while i < n:
        print(term, end=" ")
        term *= common_ratio
        i += 1
    print()

def five():
    """
    Write a program that finds the second largest element in a given list using a for loop.
    """
    numbers = [12, 45, 78, 23, 56, 89, 34, 67]
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    print(f"Second largest in {numbers} is {second_largest}")

def six():
    """
    Write a program that calculates the factorial of a given number using a while loop.
    """
    number = 7
    factorial = 1
    i = number
    while i > 0:
        factorial *= i
        i -= 1
    print(f"{number}! = {factorial}")

def seven():
    """
    Write a program that checks if a given number is a perfect square using a for loop.
    """
    number = 64
    is_perfect_square = False
    for i in range(1, int(number ** 0.5) + 2):
        if i * i == number:
            is_perfect_square = True
            break
    if is_perfect_square:
        print(f"{number} is a perfect square")
    else:
        print(f"{number} is not a perfect square")

def eight():
    """
    Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
    """
    total = 0
    num = 2
    while num <= 100:
        is_prime = True
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            total += num
        num += 1
    print(f"Sum of prime numbers between 1 and 100 is {total}")

def nine():
    """
    Write a program that counts the number of words in a given sentence using a for loop.
    """
    sentence = "Hello, world! How are you doing today?"
    word_count = 1
    for char in sentence:
        if char in ' ,.!?;:':
            word_count += 1
    print(f'"{sentence}" has {word_count} words')

def ten():
    """
    Write a program that prints the common elements between two lists using a while loop.
    """
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [4, 5, 6, 7, 8, 9, 10]
    common = []
    i = 0
    while i < len(list1):
        j = 0
        while j < len(list2):
            if list1[i] == list2[j]:
                common.append(list1[i])
                break
            j += 1
        i += 1
    print(f"Common elements between {list1} and {list2}: {common}")
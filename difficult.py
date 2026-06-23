def one():
    """
    Write a program that finds the prime factors of a given number using a for loop.
    """
    number = 84
    temp = number
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        while temp % i == 0:
            factors.append(i)
            temp //= i
    if temp > 1:
        factors.append(temp)
    print(f"Prime factors of {number} are {factors}")

def two():
    """
    Write a program that calculates the nth term of the Fibonacci sequence using a while loop.
    """
    n = 15
    if n == 0:
        fib = 0
    elif n == 1:
        fib = 1
    else:
        a, b = 0, 1
        i = 2
        while i <= n:
            a, b = b, a + b
            i += 1
        fib = b
    print(f"The {n}th Fibonacci number is {fib}")

def three():
    """
    Write a program that checks if a given string is an anagram using a for loop.
    """
    str1 = "listen"
    str2 = "silent"
    if len(str1) != len(str2):
        print(f'"{str1}" and "{str2}" are not anagrams')
        return
    chars1 = {}
    for char in str1:
        if char in chars1:
            chars1[char] += 1
        else:
            chars1[char] = 1
    chars2 = {}
    for char in str2:
        if char in chars2:
            chars2[char] += 1
        else:
            chars2[char] = 1
    if chars1 == chars2:
        print(f'"{str1}" and "{str2}" are anagrams')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams')

def four():
    """
    Write a program that prints the first n terms of the arithmetic sequence using a while loop.
    """
    n = 10
    first_term = 3
    common_diff = 5
    i = 0
    term = first_term
    print(f"First {n} terms of arithmetic sequence (diff={common_diff}):")
    while i < n:
        print(term, end=" ")
        term += common_diff
        i += 1
    print()

def five():
    """
    Write a program that finds the median of a given list of numbers using a for loop.
    """
    numbers = [7, 3, 9, 1, 5, 11, 13, 2, 8]
    sorted_list = []
    for num in numbers:
        sorted_list.append(num)
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    print(f"Sorted: {sorted_list}")
    print(f"Median: {median}")

def six():
    """
    Write a program that checks if a given number is a perfect number using a while loop.
    """
    number = 28
    divisor_sum = 0
    i = 1
    while i < number:
        if number % i == 0:
            divisor_sum += i
        i += 1
    if divisor_sum == number:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")

def seven():
    """
    Write a program that prints the sum of all digits in a given number using a for loop.
    """
    number = 12345
    digit_sum = 0
    for char in str(number):
        digit_sum += int(char)
    print(f"Sum of digits in {number} is {digit_sum}")

def eight():
    """
    Write a program that finds the longest word in a given sentence using a while loop.
    """
    sentence = "The quick brown fox jumps over the lazy dog"
    words = []
    current_word = ""
    i = 0
    while i < len(sentence):
        if sentence[i] != ' ':
            current_word += sentence[i]
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
        i += 1
    if current_word:
        words.append(current_word)
    longest = ""
    i = 0
    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1
    print(f'Longest word in "{sentence}" is "{longest}"')

def nine():
    """
    Write a program that checks if a given string is a pangram using a for loop.
    """
    sentence = "The quick brown fox jumps over the lazy dog"
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_found = set()
    for char in sentence.lower():
        if char in alphabet:
            letters_found.add(char)
    if len(letters_found) == 26:
        print(f'"{sentence}" is a pangram')
    else:
        missing = sorted(alphabet - letters_found)
        print(f'"{sentence}" is not a pangram')
        print(f"Missing letters: {missing}")

def ten():
    """
    Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    num = 2
    primes = []
    while num <= 1000:
        is_prime = True
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            primes.append(str(num))
        num += 1
    print("Prime numbers between 1 and 1000:")
    i = 0
    while i < len(primes):
        print(primes[i], end=" ")
        i += 1
    print()

# Day 3 – Functions, Strings, Lists

# Q1: Prime check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Q2: Factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


# Q3: Largest of three
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Q4: Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Q5: Reverse string
def reverse_string(s):
    return s[::-1]


# Q6: Palindrome check
def is_palindrome(s):
    return s == s[::-1]


# Q7: Sum of list without sum()
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total


# Q8: Largest in list without max()
def largest_in_list(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest


# Q9: Count frequency
def count_frequency(nums, target):
    count = 0
    for n in nums:
        if n == target:
            count += 1
    return count


# Q10: Remove duplicates
def remove_duplicates(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result



# Recursive Algorithms

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


def fast_power(base, exponent):
    if exponent == 0:
        return 1

    half = fast_power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


def sum_array(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sum_array(arr[1:])


def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def print_countdown(n):
    if n < 0:
        return

    print(n)
    print_countdown(n - 1)


if __name__ == "__main__":
    print(factorial(5))
    print(fibonacci(6))
    print(fibonacci_memo(30))
    print(power(2, 5))
    print(fast_power(2, 10))
    print(sum_array([1, 2, 3, 4]))
    print(reverse_string("python"))

    data = [1, 3, 5, 7, 9, 11]
    print(binary_search_recursive(data, 7, 0, len(data) - 1))

    print(gcd(48, 18))
    print_countdown(5)

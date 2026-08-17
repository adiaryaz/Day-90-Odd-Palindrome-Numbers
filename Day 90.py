def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def find_odd_palindromes(start, end):
    odd_palindromes = []

    for num in range(start, end + 1):
        if num % 2 != 0 and is_palindrome(num):
            odd_palindromes.append(num)

    return odd_palindromes


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = find_odd_palindromes(start, end)

print(f"Odd palindrome numbers between {start} and {end}: {result}")
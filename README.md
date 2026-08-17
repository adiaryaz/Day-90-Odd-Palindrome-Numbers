# Day-90-Odd-Palindrome-Numbers

Day 90/100 - Python Program to Find All Odd Palindrome Numbers in a Range without using Recursion

# Find All Odd Palindrome Numbers in a Range

A program to dynamically scan a user-defined numerical range and extract a list of all integers that are simultaneously odd and read the same forwards and backwards.

## 📝 Description

This program processes a starting and ending integer provided by the user to find specific numbers that meet two mathematical conditions: they must be odd, and they must be palindromes.

The core logic is divided into two distinct functions. First, the `find_odd_palindromes(start, end)` function initializes an empty list `odd_palindromes = []` to store the valid numbers. It then utilizes a `for num in range(start, end + 1):` loop to iteratively sequence through every single number within the inclusive bounds.

During each iteration, the script checks if the number is odd using the modulo operator (`num % 2 != 0`). If it is odd, it then passes the number to the helper function `is_palindrome(n)`. This helper function temporarily converts the integer into a string (`str(n)`) and evaluates if it matches its reversed self using Python's extended slicing syntax `s == s[::-1]`. If both conditions evaluate to `True`, the number is appended to the list, which is ultimately returned and printed to the console.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** An integer representing the `start` of the range, provided via the terminal prompt.


* **Input 2:** An integer representing the `end` of the range, provided via the terminal prompt.



### Output:

* A formatted string stating: "Odd palindrome numbers between [start] and [end]: [result]".



### Rules:

1. The program must accept two integer inputs from the user for the `start` and `end` values.


2. The sequence generation must be iterative, utilizing a `for` loop across `range(start, end + 1)`.


3. The main function `find_odd_palindromes` must verify that `num % 2 != 0` before checking for palindrome status.


4. The `is_palindrome(n)` helper function must convert the number to a string and use slicing `[::-1]` to check for equality.


5. The valid numbers must be appended to a list and returned to the driver code.



---

## 💡 Examples

### Example 1 (Standard Range)

**Input:**

```text
10
50

```

**Output:**

```text
Odd palindrome numbers between 10 and 50: [11, 33]

```

**Explanation:** Between 10 and 50, the palindromes are 11, 22, 33, and 44. The modulo operator filters out the even numbers (22 and 44), leaving only the odd palindromes (11 and 33) to be appended to the final list.

### Example 2 (Single Digits)

**Input:**

```text
1
10

```

**Output:**

```text
Odd palindrome numbers between 1 and 10: [1, 3, 5, 7, 9]

```

**Explanation:** Every single-digit number is mathematically a palindrome because reversing it yields the same digit. The function successfully iterates through the range and isolates the odd numbers.

### Example 3 (Three-Digit Range)

**Input:**

```text
100
150

```

**Output:**

```text
Odd palindrome numbers between 100 and 150: [101, 111, 121, 131, 141]

```

**Explanation:** The program evaluates all numbers up to 150. Valid palindromes like 101 and 121 are also odd, so they evaluate to `True` for both conditions and are added to the list.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 90.py").

```bash
git clone https://github.com/adiaryaz/Day-90-Odd-Palindrome-Numbers.git
cd odd-palindrome-numbers

```

2. **Run the program**:

```bash
python "Day 90.py"

```

Enter your desired starting and ending numbers when prompted to instantly generate a list of all odd palindromes trapped within that range!

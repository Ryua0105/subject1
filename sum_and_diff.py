Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = int(input("첫 번째 정수를 입력하세요: "))
첫 번째 정수를 입력하세요: 10
>>> num2 = int(input("두 번째 정수를 입력하세요: "))
두 번째 정수를 입력하세요: 5
>>> sum_result = num1 + num2
... difference = num1 - num2
SyntaxError: multiple statements found while compiling a single statement
>>> sum_result = num1 + num2
>>> difference = num1 - num2
>>> print("두 정수의 합: ", sum_result)
두 정수의 합:  15
>>> print("두 정수의 합: ", difference)
두 정수의 합:  5

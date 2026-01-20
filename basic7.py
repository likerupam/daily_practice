def palindrome_check(s):
    rev = 0
    while s > 0:
        digit = s % 10
        rev = rev * 10 + digit
        s = s // 10
    return rev

num = int(input("Enter a number: "))
if num == palindrome_check(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
# try:
#     num = int(input("Enter a whole number: "))
#
#     print(num)
#
#     while num > 1:
#         if num % 2 == 0:
#             num = num // 2
#         else:
#             num = 3 * num + 1
#
#         print(num)
#
# except:
#     print("That was not a valid number.")

# recursive version of program

while True:
    try:
        num = int(input("Enter a positive whole number: "))
        if num <= 0:
            print("That was not a valid number. \n")
            continue
        else:
            break
    except:
        print("That was not a valid number. \n")

def collatz(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        return collatz(n)

collatz(num)

num = int(input("Enter a num"))
temp = num
rev=0
while num>0:
    rem = num %10
    rev = rev*10 +rem
    num = num//10
if rev == temp:
    print(temp,"is palindrome")
else :
    print(temp,"is not palindrome")

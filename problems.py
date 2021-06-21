# to find average of numbers in a given list
n = int(input('how many numbers you want:'))
a = []
for i in range(0,n):
    element = int(input('enter the numbers: '))
    a.append(element)
avg = sum(a)/n

print('avg of given numbers of list',round(avg,2))  #here round me it will give o/p in two decimal points

# to reversee a given num
num = int(input('enter the value:'))
rev = 0
while(num>0):
    dig = num%10       #The while loop is used and the last digit of the number is obtained by using the modulus operator.
    rev=rev*10 + dig  #The last digit is then stored at the one’s place, second last at the ten’s place and so on.
    num = num//10     #The last digit is then removed by truly dividing the number with 10.
print('reversed value is:',rev)

#sum of number
number = int(input('enter the value:'))
tot=0
while(number>0):
    x=number%10
    tot = tot+x
    number=number//10
print('addition of given number is ',tot)


# to get quotient and remainder from two values
b = int(input('enter the number:'))
c = int(input('enter the number:'))
quotient = b//c
remainder = b%c
print('quotirnt is ',quotient)
print('remainder is ',remainder)
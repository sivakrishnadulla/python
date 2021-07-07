#trying for faulty calculator by using below values
#23+3=23, 45/4= 2, 454-32=44, 5**2=52, 94*4=783, 22%2=34



n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = input("Enter operator: ")


if n1==23 and n2==3 and n3== '+':
    print('23')

elif n1==45 and n2==4 and n3=='/':
    print('2')

elif n1==454 and n2==32 and n3=='-':
    print('44')

elif n1==5 and n2==2 and n3=='**':
    print('52')

elif n1==94 and n2==4 and n3=='*':
    print('783')

elif n1==22 and n2==2 and n3=='%':
    print('34')

elif n3=='+':
    add = n1 + n2
    print(add)

elif n3=='-':
    sub = n1-n2
    print(sub)

elif n3=='/':
    div = n1/n2
    print(div)

elif n3=='%':
    mod = n1%n2
    print(mod)

elif n3=='*':
    multi = n1*n2
    print(multi)

elif n3=='**':
    power = n1**n2
    print(power)
else:
    print("Error: Please check input once")
         

#Print a string 1
print('Hello, world!')

#Print a String 2
your_name = input('Please Enter your Name: ')
print  ('I love you ' +  your_name)

#Print a number, also can add, subtract, divide, multiply
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
print (int(num1) + int(num2))

#tip cal
amount = float(input('Enter food amount $: '))
tip = float(input('Enter your tip %: ' )) /100
            
tip_amount = amount * tip


total = amount + tip_amount
print(f'amount: 🍲{amount}')

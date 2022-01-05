import random
number = input ("guess any number between 1 and 10")
x=random.randint(1,10)
while number !=x:
    if 1<float(number)<x:
        print(number + "? guess higher!" )
        number = input ("guess another number")

    elif 11>float(number)>x: 
        print(number + "? guess lower!" )   
        number = input ("guess another number")

    elif float (number)<=0 or float(number)>=10:
         print(number + "? guess a number between 1 and 10!" )   
         number = input ("guess another number")
  
    if float(number)==x:
         print(number +"?Congrats! You Won The Game!")
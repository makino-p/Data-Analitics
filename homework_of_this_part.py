import math
#Phrase lenth
#if len(phrase_1) > len(phrase_2):
#   print("Phrase 1 is more longer than phrase 2")
#elif len(phrase_1) < len(phrase_2):
#     print("Phrase 2 is more longer than phrase 1")
#elif len(phrase_1) == len(phrase_2):
#     print("They are both same")



#Long year 
#year = int(input("Enter year  "))

#if year % 4 == 0:
#  print("This year is long")
#else: 
#  print("this year is short")


#Zodiac
# birt_month = input("Enter month of your birthday:  ")
# birt_day = int(input("Enter day of your birthday:  "))



# if birt_month == "March" and birt_day in range(21, 31) or  birt_month == "April" and birt_day in range(1, 19):
#    print("Your zodiac is Oвeн")
 
# elif birt_month == "April"  and  birt_day  in range(20, 30) or  birt_month ==  "May" and birt_day  in range(1, 20): 
#    print("Your zodiac is Tелец") 
# elif birt_month == "May" and  birt_day  in range(21, 31) or birt_month ==  "June" and birt_day in range(1, 20): 
#    print("Your zodiac is Близнецы")
# elif birt_month == "June" and  birt_day  in range(21, 30) or  birt_month ==  "July" and  birt_day  in range(1, 22): 
#    print("Your zodiac is Рак")  
# elif birt_month == "July"  and  birt_day  in range(23, 31)  or birt_month ==  "August" and birt_day  in range(1, 22): 
#    print("Your zodiac is Лев")     
# elif birt_month == "August" and  birt_day  in range(23, 31) or birt_month ==  "September" and birt_day  in range(1, 22): 
#    print("Your zodiac is Дева")
# elif birt_month == "September" and  birt_day   in range(23, 31) or birt_month  == "October" and birt_day  in range(1, 22): 
#    print("Your zodiac is Весы")     
# elif birt_month == "October" and  birt_day  in range(23, 31) or birt_month ==  "November" and birt_day  in range(1, 21): 
#    print("Your zodiac is Skorpion")       
# elif birt_month == "November" and  birt_day  in range(22, 30) or birt_month ==  "December" and birt_day  in range(1, 21): 
#    print("Your zodiac is Strelec") 
# elif birt_month == "December" and  birt_day  in range(22, 31) or birt_month ==  "January" and birt_day  in range(1, 19): 
#    print("Your zodiac is Kozerok") 
# elif birt_month == "January" and  birt_day  in range(20, 31) or birt_month ==  "February" and birt_day  in range(1, 19): 
#    print("Your zodiac is Vodoley") 
# elif birt_month == "February" and  birt_day  in range(19, 29) or birt_month ==  "March" and birt_day  in range(1, 20): 
#    print("Your zodiac is Fish") 



# Box size 

# width = int(input("Enter width  "))
# lenth = int(input("Enter lenth  "))
# height = int(input("Enter height  "))



# if (width <= 15 and lenth <= 15 and height <= 15):
#    print("Kоробка №1") 
# elif (width > 200 or lenth > 200 or height > 200):
#    print("Упаковка для лыж")
# elif (width > 15 and width < 50 or lenth > 15 and lenth < 50 or height > 15 and height < 50):
#    print("Коробка №2")  
# else:
#    print("Коробка №3")

#Delenie stroki 



# lucky_numb = input("Enter number ")
# string_array = [s for s in lucky_numb] # It save our string type of input in list
# part_int = [int(item) for item in string_array] #It change elements from string type to int type 
# first_part = part_int[:3] # It gives us first 3 elements of list
# second_part = part_int[3:] # It gives us last 3 elements of list
# first_part_sum = sum(first_part) # It summirase our items of list
# second_part_sum = sum(second_part) 

# if first_part_sum == second_part_sum: # Just checking 
#    print("You are win!")
# else:
#    print("You lose!")   




#Geometry 
# type_of_figure = input("Enter figure name ")
# if type_of_figure == "Round":
#     radius = int(input("Enter radius "))
#     space_of_round = 3.14 * (radius * radius)
#     print(space_of_round)
# elif type_of_figure == "Triangle":
#      a = int(input("Enter a side  "))
#      b = int(input("Enter b side  "))    
#      c = int(input("Enter c side  "))
#      p = (a+b+c)/2
#      d = (p*(p-a)*(p-b)*(p-c))
#      space_of_triangle = math.sqrt(d)
#      print(space_of_triangle)
# elif type_of_figure == "Rectangle":
#      first_side_lenth = int(input("Enter a side  "))
#      second_side_lenth = int(input("Enter b side  "))   
#      space_of_rectangle = a*b
#      print(space_of_rectangle) 


# Words and letters game
# word  = input('Enter the word! ')

# if len(word) % 2 == 0:
#    x = len(word) / 2
#    y = x - 1
#    letter = word[int(y):int(-y)]
#    print(letter)
# elif len(word) % 2 != 0:
#    x = len(word) - 1
#    y = x / 2
#    letter = word[int(y):int(-y)]
#    print(letter)




#Game with numbers
# imput = 1
# numbs = []
# while imput != 0:
#    imput = int(input("Enter numb!  "))
#    numbs.append(imput) 
# print(sum(numbs))		



# Pares
#boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# boys_sorted = []
# girls_sorted = []
# boys_sorted = sorted(boys)
# girls_sorted = sorted(girls)


# if len(boys) != len(girls): 
#    print("Someone might be alone! ")

# elif len(boys) == len(girls):
#     couples_list = zip(boys, girls)
#     new_list = list(couples_list)
#     for couple in new_list:
#        print(couple[0], ' pare with ',  couple[1])



# # # # city = 'China'
# # # # print(city[2])
# # # # #city[2] = 'a'
# # # # print(city)
# # # # 
# # # # 
# # # name = 'Markus'
# # # # print(name[2])
# # # # print(num + 'Herstik')
# # # #
# # # print(name)
# # # name = "herstik"
# # # print(name)
# # # 
# # # list1 = [1,2,3,4]
# # # list2 = ['red', 'green', 'blue']
# # # list3 = ['hello', 100, 3.14, [1,2,3] ]
# # # 
# # # list1[2] = 5
# # # print(list1)
# # #     
# # # 
# # # num = range(3,10)
# # # print( type(num) )
# # # print(num)
# # # 
# # # if list1[2] in range(1,10):
# # #     print("Something")
# # #     
# # # NULL
# # 
# # age = int(input("Give me your age: "))
# # name = input("Give me your name: ")
# # if name == "Tom":
# #     print("Hi Tom")
# # elif (name == "Marcus" or name == "Bob") and age > 17 :
# #     print("Hello", name)
# #     if age > 99:
# #         print("You old bastard")
# #     else:
# #         print("Keep growing")
# #         
# #         
# # elif name == "Bob":
# #     print("hello Bobby boy")
# # 
# # # else:
# # #     print("Go away!")
# # ## Do stuff
# #     
# # print("This is the end")
# # 
# # 
# #
# marks = int(input("Give me a score: "))
# if (marks > 100):
#     print("Out of range 0-100")
# elif (marks > 84):
#     print("HD")
# elif (marks > 74):
#     print("D")
# elif (marks> 64):
#     print("C")
# elif (marks > 49):
#     print("P")
# else:
#     print("F ")
# 
#

# previous_drinks NOT greater than 3
# age >= 18
# if age < 18 = no entry
# if female get free entry
# otherwise pay $15

drinks = int(input("How many drinks have you had: "))
age = int(input("How old are you: "))
sex = input("Do you identify as female: ")

if age >= 18:
    print("you are old enough")
    if not drinks > 3:
        print("You are OK")
        
        if sex.lower() == "yes" or sex.lower() == "y":
            print("You get in for free")
        else:
            print("$15 please")
    else:
        print("Sorry, better cool off")
else:
    print("You are too young")



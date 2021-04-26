# # დავალება 1
# # # ფიბონაჩის რეკურსია
# def Fibonacci_recursion(x):
#    if x <= 1:
#        return x
#    else:
#        return(Fibonacci_recursion(x-1) + Fibonacci_recursion(x-2))
#
# # ინფორმაციის შეტანა
# while True:
#     try:
#         x = int(input("შეიყვანეთ 0 ზე მეტი რიცხვი: "))
#         if x <= 0:
#             print("გთხოვთ რიცხვი შეიყვანოთ პირობის შესაბამისად!")
#             continue
#         break
#     except ValueError:
#         print("დაფიქსირდა შეცდომა!")
#
# # ფიბონაჩის მასივი
# massive = [Fibonacci_recursion(i) for i in range(x)]
# print(massive)

# დავალება 2
# from math import fabs
#
#
# def action(x):
#     if x <= 0:
#         return int(str(int(fabs(x)))[::-1])
#     else:
#         return int(str(x)[::-1])
#
#
# while True:
#     try:
#         number = int(input("შეიყვანეთ რიცხვი: "))
#         break
#     except ValueError:
#         print("დაფიქსირდა შეცდომა, სცადეთ თავიდან")
#
#
# print(action(number))

# დავალება 3
# from random import randint
#
# # რიცხვათა რაოდენობა მასივში
# while True:
#     try:
#         number = int(input("შეიყვანე რიცხვთა რაოდენობა: "))
#         break
#     except:
#         print("დაფიქსირდა შეცდომა სცადეთ თავიდან.")
# massive = []
#
# # რანდომული მიმდევრობის ჩამატება მასივში
# for i in range(number):
#     if randint(1, 20) in massive:
#         pass
#     else:
#         massive.append(randint(1, 10))
#
#
# print(f"რიცხვები: {massive}")
# # სხვაობა (მათემატიკურად "d")
# changer = massive[1] - massive[0]
# print(f"სხვაობა: {changer}")
#
# # შემოწმების ფუნქცია
# def check(x = list):
#     for i in x:
#         if x.index(i) == 0:
#             pass
#         elif  ((x[x.index(i)] - x[x.index(i)-1]) == changer) and (x.index(i) == (number-1)):
#             print("მოცემული რიცხვათა რაოდენობა არის არითმეტიკული პროგრესია.")
#             break
#         elif (x[x.index(i)] - x[x.index(i)-1]) != changer:
#             print("პროგრესია დაირღვა")
#             break
#         elif (x[x.index(i)] - x[x.index(i)-1]) == changer:
#             pass
#
#
# check(massive)
#
# დავალება 4
# from random import randint
#
# massive = [randint(1, 100) for i in range(10)]
# print(massive)
# for i in massive:
#     if "0" in str(i):
#         massive.remove(i)
#         massive.append(i)
# print(f"შეცვლის შემდეგ მიიღება მასივი: {massive}")

# დავალება 5
# from random import randint
#
#
# massive = [randint(1, 100) for i in range(30)]
# print(massive)
#
# def most_frequent(x):
#     count = 0
#     for i in x:
#         Current_frequency = x.count(i)
#         if (Current_frequency > count):
#             count = Current_frequency
#             element = i
#     return element
#
# print(f"ყველაზე ხშირად გამოყენებული რიცხვია {most_frequent(massive)}")
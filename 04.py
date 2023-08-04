# اعداد اول
# a = int(input())
# b = int(input())
# n = a
# while n < b:
#     i = 2
#     p = True
#     while i < n:
#         if n % i == 0:
#             p = False
#         i += 1
#     if p:
#         print(n)
#     n += 1


# def hello(name):
#     print ('hello im :',name)
# hello('ghazal')

# def v(a ,b):
#     return a,b

# a = int(input())
# b = int(input())
# print (a**b)


# n = int(input())
# i = 2
# p = True
# while i < n:
#     if n % i == 0:
#         p = False
#     i += 1
# print(p)


#تشخیص عدد اول با تابع
# def prime(n):
#     if n==1:
#         return False
#     p = True
#     i = 2
#     while i < n:
#         if n % i == 0:
#             p = False
#         i += 1
#     return p

# n = int(input())
# result = prime(n)
# if result:
#     print("The number is prime.")
# else:
#     print("The number is NOT prime.")

 
#چاپ مربع
# n = int(input())
# i=0
# while i<n:
#     j=0
#     while j<n:
#         if i==0 or i ==n-1:
#             print ('*', end="")
#         else:
#             if j==0 or j==n-1:
#                 print ('*', end="")
#             else:
#                 print (' ', end="")
#         j+=1
#     print ()
#     i+=1

#چاپ مربع با for loop
# n = int(input())

# for i in range(n):
#     if i == 0 or i == n-1:
#         for j in range(n):
#             print("*", end="")
#     else:
#         for j in range(n):
#             if j == 0 or j == n-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#     print()


# spliting a sentence without split() | until the comma ','

# m= 'hi, hey, sup, gm gn, mnbvc, ;)'

# def split(s,char):
#     start, end=0,0
#     while end<len(m):
#         if m[end]==char or end==len(s)-1:
#             print (s[start:end])
#             start=end+1
#         end+=1
# split(m,",")



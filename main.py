# # def rev(num):
# #     if (num>0):
# #         last=num%10
# #         if(num//10>0):
# #             current=rev((int)(num//10))
# #             return last*pow(10,len(str(current)))+current
# #         return num  

# # n=int(input("Enter number:"))
# # print(rev(n))








# def reverse(s):
#     if len(s) == 1:
#         return s[0]
#     firstchar = s[0]
#     return reverse(s[1:])+firstchar

# s=input("Enter characters:")

# print(reverse(s))








n=int(input("Enter number:"))

def checkpower(n):
    if (n<=0):
        return False
    if (n==1):
        return True
    if (n%4==0):
        return checkpower(n/4)
    return False

if (checkpower(n)):
    print("It is power of 4.")

else:
    print("It is not power of 4.")
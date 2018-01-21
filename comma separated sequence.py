#Write a program which will find all such numbers which are divisible by 7 but
#not a multiple of 5, between 2000 and 3200 (both included).
#the numbers obtained should be printed in a comma-separated sequence on a single line


for i in range(2000, 3200, 1):
    num_full = i
    if num_full % 7 == 0 and num_full % 5 != 0:
        print(num_full, end=",")
    




    


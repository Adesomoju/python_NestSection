#With a given integral number , write a program to generate a dictionary that contains (i,
#i*i)  such that is an integral number between 1 and  (both included), and then the program
#should print the dictionary

output = {}

enter = int(input('enter the intrgral number: '))

for i in range(enter, 0, -1):
    j = i*i
    term = i
    output[term] = j
print(output)

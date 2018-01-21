#Write a program that accepts a comma separated sequence of words as input and prints the
#words in a comma-separated sequence after sorting them alphabetically

user_words = input('enter your words with a comma separated sequence: ')
comma_seq = user_words.split(',')
sorted_seq = sorted(comma_seq)

print(','.join(sorted_seq))

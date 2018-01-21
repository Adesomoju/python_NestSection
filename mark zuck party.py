#My neighbor, Mark Zuckerberg is having a party for his sent fort for creating FaceMash.
#However he only want Harvard students in this party of his. Entering the party comes with
#a few constraints, which are listed below:
#You must be an Harvad student
#You must be in the age range of 18 - 25.
#You must come with opposite gender
#Your partner must be hot

min_age = 17
max_age = 26
print('\twelcome you all to this Party!!')
age = int(input('\n\nhow old are you? '))

    

if age < max_age and age > min_age:
    print('\n\nYou\'re welcome to the party ')
    school = input('What school are you from? ')
    school = school.lower()
    

    opposite_sex = input('are you with an opposite sex? ')
    opposite_sex = opposite_sex.lower()
    hot_partn = input('is your partner hot? ')
    hot_partn = hot_partn.lower()

    if school == 'harvad' and opposite_sex == 'yes' and hot_partn == 'yes':
        print('you\'re welcome to this party!!')
    else:
        print('you\'re not allowed in this party!!')
        
else:
    print('YOU CAN\'T ATTEND THIS PARTY.\n YOU ARE TOO YOUNG')

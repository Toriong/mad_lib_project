
fill_in_sentence = print('1)____ is a wise person. He likes to 2)_____. But his dad thinks that _____ is a 3)_____.'
                         '4)But his mom still 4)______ him. Either way, at least he likes to 2)_______.')

blank_name = input('\n1)Choose name:'
                   '\na. Bob'
                   '\nb. Bill'
                   '\nc. Sergio'
                   '\nd. Stan'
                   '\nANSWER:        ')
blank_name_dictionary = {
    'a': 'Bob',
    'b': 'Bill',
    'c': 'Sergio',
    'd': 'Stan',}

if blank_name == 'a':
    blank_name = 'Bob'
elif blank_name == 'b':
    blank_name = 'Bill'
elif blank_name == 'c':
    blank_name = 'Sergio'
elif blank_name == 'd':
    blank_name = 'Stan'
else:
    exit("ERROR! Please enter a valid entry. (RESET the program.)")




blank_spot_2 = input('\n2) choose one: '
                     '\na. read'
                     '\nb. play video games'
                     '\nc. Watch television'
                     '\nd. start a global thermal nuclear war'
                     '\nANSWER: ')

if blank_spot_2 == 'a':
    blank_spot_2 = 'read'
elif blank_spot_2 == 'b':
    blank_spot_2 = 'play video games'
elif blank_spot_2 == 'c':
    blank_spot_2 = 'watch television'
elif blank_spot_2 == 'd':
    blank_spot_2 = 'start a global thermal nuclear war'
else:
    exit("ERROR! Please enter a valid entry. (RESET the program.)")

blank_spot_3 = input('\n3) choose one: '
                     '\na. moron'
                     '\nb. a good man'
                     '\nc. lunatic'
                     '\nd. pyschopath'
                     '\nANSWER:      ')

if blank_spot_3 == 'a':
    blank_spot_3 = 'moron'
elif blank_spot_3 == 'b':
    blank_spot_3 = 'a good man'
elif blank_spot_3 == 'c':
    blank_spot_3 = 'lunatic'
elif blank_spot_3 == 'd':
    blank_spot_3 = 'pyschopath'
else:
    exit("ERROR! Please enter a valid entry. (RESET the program.)")

blank_spot_4 = input('\n4) choose one: '
                     '\na. loves'
                     '\nb. hates'
                     '\nc. ignores'
                     '\nd. nags'
                     '\nANSWER:    ')
if blank_spot_4 == 'a':
    blank_spot_4 = 'loves'
elif blank_spot_4 == 'b':
    blank_spot_4 = 'hates'
elif blank_spot_4 =='c':
    blank_spot_4 = 'ignores'
elif blank_spot_4 == 'd':
    blank_spot_4 = 'nags'
else:
    exit("ERROR! Please enter a valid entry. (RESET the program.)")


final_mad_lib = ('\n' + blank_name + ' is a wise person. He likes to ' + blank_spot_2 + '.'
                '\nBut his dad thinks that ' + blank_name + ' is a ' + blank_spot_3 + '.'
                 '\nBut his mom still ' + blank_spot_4 + ' him.' ' Either way, at least he likes to ' + blank_spot_2 + '.')

print(final_mad_lib)



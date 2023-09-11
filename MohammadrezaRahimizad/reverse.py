
#how to reverse string with for:

AlphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#1
print(AlphabetString[::-1])

#2
for char in reversed(AlphabetString):
    print(char)

#how to reverse list:
capitals = ['oslo', 'skopje', 'riga', 'madrid']
capitals.reverse()
print('reversed list:', capitals)

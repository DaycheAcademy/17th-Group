print("Exercise:")
A = "Hey, what's up?" \
    " So, I was thinking," \
    " we should totally hit up that new burger joint down the street." \
    " I heard they have some bomb burgers and fries." \
    " Plus, I'm starving and could use a good meal." \
    " What do you say? Are you down to grab some grub with me?" \
    " We could even make it a little adventure and try some of their crazy milkshake flavors." \
    " It'll be fun! Let me know if you're in and we'll make it happen."


print('Number Of Characters: ', len(A))         # Character
print('Number Of Words: ', len(A.split()))      # Words


# Clearing text
A = A.lower() #apple has no defference with Apple
words = A.split()
words = [word.strip('.,!;()[]?') for word in words]
words = [word.replace("'s", '') for word in words]
words = [word.replace("'m", '') for word in words]
words = [word.replace("'ll", '') for word in words]
words = [word.replace("'re", '') for word in words]

# Finding unique words
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

print("Total number of unique words: ", len(unique))
unique.sort()
print("list of sorted unique words:\n", unique)

print('=' * 40)
words = A.split()
toBe = ["am", "'m", "is", "'s", "are", "'re",
        "was", "were", "be", "being", "been"]
numbersOfToBe = []

for word in words:
    if word in toBe:
        numbersOfToBe.append(word)
print(numbersOfToBe)
print(len(numbersOfToBe))



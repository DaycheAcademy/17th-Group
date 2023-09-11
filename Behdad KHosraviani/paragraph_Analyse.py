# Step 1: select the text we want to analyze

mainText = '''
The European languages are members of the same family. 
Their separate existence is a myth. For science, music, 
sport, etc, Europe uses the same vocabulary.
The languages only differ in their grammar,
their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: 
one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar
, pronunciation and more common words. If several languages coalesce,
the grammar of the resulting language is more simple and regular than that of the individual languages.
he new common language will be more simple and regular than the existing European languages.
It will be as simple as Occidental; in fact, it will be Occidental.
To an English person,
it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.
The European languages are members of the same family. Their separate existence is a myth.
For science, music, sport, etc, Europe uses the same vocabulary.
The languages only differ in their grammar, their pronunciation and their most common words.
Everyone realizes why a new common language would be desirable:
one could refuse to pay expensive translators.'''

# to count total number of words we need to make in into list
# firs lets replace \n with a space to split it easier.

list_of_words = mainText.replace('\n', ' ').split(' ')

# in our list there is some '' value we should remove
for i in range(list_of_words.count('')):
    list_of_words.remove('')

for i in range(list_of_words.count('\'')):
    list_of_words.remove('\'')

# now  we have a list of words
print('Total number of words: ' ,len(list_of_words))

# to count the unique words let's convert the list to a set

set_of_words = set(list_of_words)
print('Total number of unique words: ', len(set_of_words))

# for counting the 'to be' words we should make a list of it

to_be_list = ['am', 'is', 'are', 'be', 'being', 'was', 'were', 'been']

# to be precise here, let's remove the dots

for i in range(len(list_of_words)):
    list_of_words[i] = list_of_words[i].replace('.', '')

# now we count the number of To be words and make a list of it

count = 0
to_be_words_all = list()
for i in range(len(list_of_words)):
    if list_of_words[i] in to_be_list:
        count += 1
        to_be_words_all.append(list_of_words[i])

print('Total number of \'To Be \' words: ', count)

# making a set of To Be words
to_be_words_all_set = set(to_be_words_all)

print('Total number of \'To Be \' unique words: ',len(to_be_words_all_set))
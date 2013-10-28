def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    print ('expecting', expecting)
    if word_list:
        word = word_list.pop(0)

        print (word[0], expecting)
        print (word[0] == expecting)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

word_list = [('verb', 'eat'), ('error', 'nose'), ('verb', 'run')]
# print peek(word_list)
# print match(word_list, 'verb')
print skip(word_list, 'verb')


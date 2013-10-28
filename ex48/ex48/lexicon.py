def scan(s):
    words = s.split()
    tuple_list = []
    for word in words:
        if word in ['north', 'south', 'east', 'west', 'down',
                     'up', 'left', 'right', 'back']:
            pair = ('direction', word)
        elif word in ['go', 'stop', 'kill', 'eat']:
            pair = ('verb', word)
        elif word in ['the', 'in', 'of', 'from', 'at', 'it']:
            pair = ('stop', word)
        elif word in ['door', 'bear', 'princess', 'cabinet']:
            pair = ('noun', word)
        else:
            try:
                pair = ('number', int(word))
            except ValueError:
                pair = ('error', word)
        tuple_list.append(pair)
    return tuple_list

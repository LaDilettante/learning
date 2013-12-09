from random import randint
from datetime import datetime

startTime = datetime.now()

alphabet = "abcdefghijklmnopqrstwuvxyz "
target = "methinks it is like a weasel"

def generate():
    res = list()
    for i in range(27):
        letter = alphabet[randint(0, 26)]
        res.append(letter)
    return "".join(res)
    
def score(string, target):
    score = 0
    for i in range(len(string)):
        if string[i] == target[i]:
            score += 1
    return score
    
def invoke(target):
    i = 0
    best_score = 0
    while best_score < len(target):
        current_string = generate()
        current_score = score(current_string, target)
        if current_score >= best_score:
            best_score = current_score
            best_string = current_string
        if i % 1000 == 0:
            print (best_string + " " + str(best_score) + 
            " " + str(i / 1000))
        i += 1
    print i

if __name__ == "__main__":
    invoke(target)

print(datetime.now() - startTime)

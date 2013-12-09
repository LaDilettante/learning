from random import randint
from datetime import datetime

startTime = datetime.now()

alphabet = "abcdefghijklmnopqrstwuvxyz "
target = "methinks it is like a weasel"

def generate(correct_sofar):
    res = correct_sofar
    for i in range(28):
        if correct_sofar[i] == "-":
            res[i] = alphabet[randint(0, 26)]
    return res
    
def score(string, target):
    score = 0
    correct_sofar = []
    for i in range(len(string)):
        if string[i] == target[i]:
            score += 1
            correct_sofar.append(string[i])
        else:
            correct_sofar.append("-")
    return (score, correct_sofar)
    
def hill_climb(target):
    i = 0
    best_score = 0
    correct_sofar = ["-" for i in range(28)]
    
    while best_score < len(target):
        current_string = generate(correct_sofar)
        current_score, correct_sofar = score(current_string, target)
        if current_score >= best_score:
            best_score = current_score
            best_string = "".join(correct_sofar)
        if i % 1 == 0:
            print (best_string + " " + str(best_score) + 
            " " + str(i / 1000))
        i += 1
    print i

if __name__ == "__main__":
    hill_climb(target)

print(datetime.now() - startTime)

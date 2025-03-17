import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the 26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish)

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    for i in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        X[i] = 0
    with open (filename,encoding='utf-8') as f:
        text = f.read().upper()
        for char in text:
            if char in X:
                X[char] += 1
    
    return X

def F(lang_p, p, X):
    sum = 0
    index = 0
    # find the summation of each letter count multiplied by the log of its probability
    for i in X:
        sum += X[i] * math.log(p[index])
        index += 1
    # return the addition to the log of lang probability
    return math.log(lang_p) + sum

def main():
    # set the variables according to the user input
    filename = sys.argv[1]
    e = float(sys.argv[2])
    s = float(sys.argv[3])
    # print out the answer to Q1
    X = shred(filename)
    print("Q1")
    for i in X:
        print(i + ' ' + str(X[i]))

    # get the parameeter vectors
    pE,pS = get_parameter_vectors()

    # print out the answer to Q2
    print("Q2")
    print(round(X['A'] * math.log(pE[0]), 4))
    print(round(X['A'] * math.log(pS[0]), 4))

    # print out the answer to Q3
    print("Q3")
    E = round(F(e, pE, X),4)
    S = round(F(s, pS, X),4)
    print(E)
    print(S)

    #print out the answer to Q4
    print("Q4")
    if S - E >= 100:
        print(0)
    elif E - S <= -100:
        print(1)
    else:
        print(round(1 / (1 + math.exp(S-E)), 4))

main()



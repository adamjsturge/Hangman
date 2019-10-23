import random
def replace_at_index(x,y,z):
    iy = int(y)
    yy = int(iy) + 1
    semi = x[:y] + z + x[yy:]
    return semi
def update_counts(dic, x):
    xlen = len(x)
    for i in range(xlen):
        new = x[i]
        if new in dic:
            dic[x[i]] = dic[x[i]] + 1
        else:
            dic[x[i]] = 1
def get_guess(word, dic):
    while True:
        x = raw_input("Guess: ")
        if x == "":
            print "Wrong"
        if len(x) != 1:
            print "Your guess must have exactly one character!"
        elif not(x.islower()):
            print "Your guess must be a lowercase letter!"
        elif x in dic:
            print "Letter already used"
        elif not(x in word):
            print "That letter is not in the secret word!"
            dic[x] = 1
            return x
        elif x in word:
            print "That letter is in the secret word!"
            return x
def dashes(word):
    leng = len(word)
    full = ""
    for i in range (leng):
        full = full + "-"
    return full
def update_dashes(word, dash, guess, dic):
    temp = 0
    full = ""
    ind = int
    if guess in word:
        ind = word.find(guess)
        if dic[guess] > 1 and temp == 0:
            for i in range(len(word)):
                full = full + word[i]
            for i in range (dic[guess]):
                ind = full.find(guess)
                dash = replace_at_index(dash,ind,guess)
                #full = replace_at_index(full,ind," ") (x,y,z)
                full = full[:ind] + "-" + full[ind+1:]
            temp = 1
            return dash
        elif dic[guess] == 1:
            dash = replace_at_index(dash,ind,guess)
            return dash

words = ["banana", "woahh" , "everyday", "robert", "logic", "apple", "coconut" ,"bacteria", "xylem", "phlegm", "why", "hi", "katrina", "radio", "git", "switch", "zoo"]

guesses_left = 10    
secret_word = random.choice(words)
dash = dashes(secret_word)
dic = {}
update_counts(dic, secret_word)
usedletter = {}

while True:
    print dash
    print str(guesses_left) + " incorrect guesses left."
    gg = get_guess(secret_word, usedletter)
    if gg in secret_word:
        dash = update_dashes(secret_word, dash, gg, dic)
        if dash == secret_word:
            print "The word was (" + dash + ")"
            print "You won!"
            break
    else:
        guesses_left = guesses_left - 1
    if guesses_left == 0:
        print "You lost"
        break

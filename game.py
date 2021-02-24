words = list("apple")
hide = []

for word in words:
    hide.append('_')

tries = 0
max_tries = 5

game_run = False
while not game_run:
    print('You have {} ' .format(max_tries - tries) + 'tries left')
    hideString = " ".join(hide)
    print ('the current word is : {}'.format(hideString))

    print ('          __________')
    print ('          |        |')
    print ('          |        ' + ('O' if tries > 0 else ''))
    print ('          |        ' + ('/\\' if tries > 1 else ''))
    print ('          |        ' + ('|' if tries > 2 else ''))
    print ('          |        ' + ('/\\' if tries > 3 else ''))
    print ('    ____________    ')

    guess = raw_input("please guess a letter to save the man : ")
    print ('\n\n\n\n')
    if guess in words:
        print('You guessed correct {} '.format(guess) + 'Thank you for saving the man')
        for i in range(len(words)):
            word = words[i]
            if word == guess:
                hide[i] = words[i]
                words[i] = '_'
    else:
        print ("You killed the man, by the guess".format(guess))
        tries +=1

    if(all('_' == char for char in words)) :
        print ("He is saved")
        game_run = True


    if (tries >= max_tries):
        print ("YOU lost")
        game_run = True



import random

word_bank=["rizz","ohio","cat","university","management"]

word=random.choice(word_bank)
guessedWord=['_']*len(word)
attemps=10

while attemps>0:
    print('\nCurrent word: ',''.join(guessedWord))
    guess= input('Enter a letter: ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessedWord[i]=guess
        print('Correct guess!')
    else:
        attemps-=1
        print(f'Wrong guess! Attempts {attemps} left')
        if '_' not in guessedWord:
            print('Congratulations! You guessed the word:', word)
            break            
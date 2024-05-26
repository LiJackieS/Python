import random

wordList = ['analogue', 'boolean', 'cache', 'domain', 'encryption', 'firewall', 'gateway', 'html', 'internet', 'java', 'kepler', 'lagrange', 'malware', 'network', 'online', 'phishing', 'quotient', 'radius', 'server', 'tuple', 'url', 'virus', 'wifi', 'xenon', 'wolfram', 'zip' ]

word = random.choice(wordList)

attemptsLeft = 7
guesses = ''
correctGuesses= ['-'] * len(word)
attempts = 0
i = 0

boolean = True

print(f"You will have {attemptsLeft} attempts to guess the word by guessing each indiviual character.")
print('-\n' * len(word))
while attemptsLeft > 0:
    guesses = (input("Guess the character: "))
    for char in word:
        if guesses in char:
            correctGuesses[i] = guesses
            boolean = False
        if len(correctGuesses) > i:
            print(correctGuesses[i])
        elif guesses not in char:
            print("-")
        if correctGuesses == word:
            print(f"You Won with only {attempts} attempts. :)")
            break
        i += 1
    
    if boolean == True:
        attemptsLeft -= 1
    attempts += 1
    i = 0
    print(f"You have {attemptsLeft} lives left.")
    boolean = True
    

if word != correctGuesses:
    print("You lost")
print(word)
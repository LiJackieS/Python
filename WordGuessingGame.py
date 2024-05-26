import random

wordList = ['analogue', 'boolean', 'cache', 'domain', 'encryption', 'firewall', 'gateway', 'html', 'internet', 'java', 'kepler', 'lagrange', 'malware', 'network', 'online', 'phishing', 'quotient', 'radius', 'server', 'tuple', 'url', 'virus', 'wifi', 'xenon', 'wolfram', 'zip' ]

word = random.choice(wordList)

attemptsLeft = 7
guesses = ''
correctGuesses = []
attempts = 0
i = 0
print(f"You will have {attemptsLeft} attempts to guess the word by guessing each indiviual character.")

while attemptsLeft > 0:
    guesses = (input("Guess the character: "))
    for char in word:
        if guesses in char:
            correctGuesses.append(guesses)
        if len(correctGuesses) > i:
            print(correctGuesses[i])
        elif guesses not in char:
            print("-")
        i += 1
    attemptsLeft -= 1
    attempts += 1
    i = 0
    
if len(correctGuesses) == len(word):
    print(f"You Won with only {attempts} attempts. :)")
else:
    print("You lost")
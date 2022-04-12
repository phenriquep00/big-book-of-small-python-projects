#In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f"""I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:         That means:
        Pico             One digit is correct but in the wrong position
        Fermi            One digit is correct and in the right position
        Bagels           No digit is correct""")

    while True:  # main loop
        # Storing and shufling the secret number
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # validade number
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was: {secretNum}')

        # Ask the player to play again.
        print('Do you want to play again? (y/n) ')
        if not input('> ').lower().startswith('y'):
            break
    
    print('Thanks for playing!')
        


def getSecretNum():
    secretNum = ""
    numbers = list('0123456789')
    random.shuffle(numbers)

    for _ in range(NUM_DIGITS):
        secretNum += str(numbers[_])

    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for _ in range(len(guess)):
        if guess[_] == secretNum[_]:
            # Correct digit in the correct place.
            clues.append('Fermi')
        elif guess[_] is secretNum:
            # Correct digit in the incorrect place.
            clues.append('Pico')

    if len(clues) == 0:
        # No correct digit
        return 'Baguels'
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == '__main__':
    main()
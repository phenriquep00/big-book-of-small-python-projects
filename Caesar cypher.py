"""Caesar Cypher following the book Big book of Small Python Projects, by Al Swiegart"""

try:
    import pyperclip
except ImportError:
    pass


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


print("""The Caesar cipher encrypts letters by shiftring them over by a
key number. For exemple, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on""")
mode = ''
key = 0
# get the mode for the cypher
while ...:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input("-> ").lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please, enter a valid mode')

while ...:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key: [0 to {maxKey}]')
    response = input("-> ").upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Get the user message
print(f'Enter the message to {mode}')
message = input("-> ").upper()

# Caesar cypher only works with upper case

# final message
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # Handle wrap-around
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0 :
            num += len(SYMBOLS)

        # add the encrypted/decrypted number's symbol to translated
        translated += SYMBOLS[num]
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full  {mode}ed text copied to clipboard')
except:
    pass

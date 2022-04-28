secret_word = 'tiger'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# Print helper
if out_of_guesses:
    print('******Sorry but you lost!*******')
else:
    print(f"""{guess.upper()} is correct!""")

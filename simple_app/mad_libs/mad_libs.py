import pyttsx3


def game():
    colour = input('Enter a colour: ')
    plural_noun = input('Enter a plural noun : ')
    celebrity = input('Enter a celebrity: ')

    mad_libs = f"""Roses are {colour} 
{plural_noun} are blue 
I love {celebrity}"""

    return mad_libs


print(game())
pyttsx3.speak(game())
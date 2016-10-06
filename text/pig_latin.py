# To create the Pig Latin form of an English word the initial consonant sound is transposed
# to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay)

def pig_latin(word):
    new_word = word[1:] + word[0] + 'ay'
    return new_word


if __name__ == '__main__':
    p = input('enter text:')
    print(pig_latin(p))
import random

def load_words(word_size):
    return open('l_{}.txt'.format(word_size)).read().splitlines()

def is_taken(word, set_list):
    for i, _ in enumerate(word):
        if word[i] in set_list[i]:
            return True
    return False

def taken_letters(words):
    return [set(letters) for letters in (zip(*words))]

def one_step(thesaurus, words):
    return [word for word in thesaurus if not is_taken(word, taken_letters(words))]

def uncrash(thesaurus, words):
    candidate_words = one_step(thesaurus, words)
    if not candidate_words:
        return words
    else:
        new_word = [random.choice(candidate_words)]
        return uncrash(thesaurus, words + new_word)

def solver(starter=None):
    start = starter or input("Please enter a word: ").upper()
    word_size = len(start)
    thesaurus = load_words(word_size)
    print("\n".join(uncrash(thesaurus, [start])))

def play():
    def take_a_turn(thesaurus, words=[]):
        if not words:
            next_word = random.choice(thesaurus) 
        else:
            candidate_words = one_step(thesaurus, words)
            if not candidate_words:
                exit("No more choices! I lose.")
            else:
                next_word = random.choice(candidate_words)
        print(next_word)
        return next_word

    first_move = random.choice(('me', 'you'))
    if first_move == 'me':
        word_size = input('What size words? ')
        thesaurus = load_words(word_size)
        words = [take_a_turn(thesaurus)]
        turn = 'you'
    else:
        words = [input("You start: ").upper()]
        word_size = str(len(words[0]))
        thesaurus = load_words(word_size)
        turn = 'me'

    while True:
        if turn == 'me':
            words.append(take_a_turn(thesaurus, words))
            turn = 'you'
        else:
            next_word = input("Enter your next word: ").upper()
            if is_taken(next_word, taken_letters(words)):
                exit("That word is invalid! You lose.")
            elif next_word not in thesaurus:
                exit("That's not a real word! You lose.")
            else:
                words.append(next_word)
                turn = 'me'

if __name__ == "__main__":
    play()

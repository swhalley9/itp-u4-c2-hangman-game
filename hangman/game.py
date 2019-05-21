from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['skip','jump','hop']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException(Exceiption)
    else:
        return random.choice(list_of_words)

def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    else:
        return len(word) * '*'


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0 or len(answer_word) != len(masked_word):
        raise InvalidWordException()
        
    if len(character) != 1:
        raise InvalidGuessedLetterException()
        
    character = character.lower()
    answer_word = answer_word.lower()
    if character in answer_word:
        place_index = answer_word.index(character)
        masked_word = masked_word[:place_index] + character + masked_word[place_index + 1:]
    else:
        masked_word = masked_word
    return masked_word


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game

import nltk
from nltk.chat.util import Chat, reflections
from set_pairs import ENG_SET_PAIRS

chat = Chat(ENG_SET_PAIRS, reflections)

if __name__ == '__main__':
    chat.converse()
"""
    generate passphrases using the diceware method

    author: Guillaume Martin
    date: 2018-07-24
"""

import sys
import random

def read_wordlist():
    """ import list of words into a dictionary

    Returns
    -------
    wrdlist: dictionary
        A dictionary containing all the words contains in the word list file
    """
    wrdlist = {}
    with open('eff_large_wordlist.txt', 'r') as f:
        for line in f:
            (key, val) = line.split()
            wrdlist[key] = val
    return wrdlist

def get_word_key():
    """ generates a five digits key 

    Returns
    -------
    wordkey: string
        A five digits key
    """
    wordkey = ''
    for i in range(5):
        wordkey += str(random.randrange(1, 7))
    return wordkey

def generate_passphrase(nwords):
    """ generate a passphrase by randomly selecting words in  a list.

    Parameters
    ----------
    nwords: integer
        The number of words in the passphrase

    Returns
    passphrase: string
        The generated passphrase
    """
    wrdlst = read_wordlist()
    words = []
    for i in range(nwords):
        key = get_word_key()
        words.append(wrdlst[key])
    passphrase = ' '.join(words)
    return passphrase

def main():
    if len(sys.argv) > 1:
        nwords = int(sys.argv[1])
    else:
        print('choose nwords')
        return None

    passphrase = generate_passphrase(nwords)

    print(passphrase)

if __name__ == '__main__':
    main()

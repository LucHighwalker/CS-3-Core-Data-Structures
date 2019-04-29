from hashtable import HashTable


def redact_words(sentence, banned, replacement=None):
    table = HashTable()
    for ban in banned:
        table.set(ban, None)

    new_sentence = []
    for word in sentence:
        if table.contains(word) is False:
            new_sentence.append(word)
        elif replacement is not None:
            new_sentence.append(replacement)

    return new_sentence


def main():
    sentence = 'what the actual fuck'.split(' ')
    banned = ['fuck']

    assert redact_words(sentence, banned) == 'what the actual'.split(
        ' ')  # without replacement
    # with replacement
    assert redact_words(
        sentence, banned, '***') == 'what the actual ***'.split(' ')

    # no banned words
    banned = []

    assert redact_words(sentence, banned) == 'what the actual fuck'.split(
        ' ')  # without replacement
    # with replacement
    assert redact_words(
        sentence, banned, '***') == 'what the actual fuck'.split(' ')

    # none existing banned word
    banned = ['poop']

    assert redact_words(sentence, banned) == 'what the actual fuck'.split(
        ' ')  # without replacement
    # with replacement
    assert redact_words(
        sentence, banned, '***') == 'what the actual fuck'.split(' ')

    # all banned words
    banned = 'what the actual fuck'.split(' ')

    assert redact_words(sentence, banned) == []  # without replacement
    # with replacement
    assert redact_words(
        sentence, banned, '***') == '*** *** *** ***'.split(' ')


if __name__ == '__main__':
    main()

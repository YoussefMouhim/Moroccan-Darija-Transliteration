def latinToOSL(word, mapping):
    word = word.lower()
    OSL_word = ''
    i = 0
    while i < len(word):
        if word[i].isdigit():
            if i < len(word) - 1 and (word[i+1].isdigit() or word[i+1] == ' '):
                OSL_word += word[i]
                i += 1
            else:
                OSL_word += mapping[word[i]]
                i += 1
        if word[i:i+2] == 'ch':
                OSL_word += mapping['ch']
                i += 2
        elif word[i:i+2] == 'gh':
                OSL_word += mapping['gh']
                i += 2
        elif word[i] in mapping:
                OSL_word += mapping[word[i]]
                i += 1
        else:
                OSL_word += word[i]
                i += 1

    return OSL_word

mapping = {
  'a': 'A',
  'b': 'b',
  't': 't',
 #'T': 'T',
  'j': 'j',
  '7': 'H',
  '5': 'X',
  'd': 'd',
  'r': 'r',
  'z': 'z',
  's': 's',
  'ch': '$',
  #'sh': 'X',
  #'S': 'S',
  #'D': 'D',
  #'T': 'T',
  #'D': 'D',
  '3': 'E',
  'gh': 'G',
  'f': 'f',
  'q': 'q',
  'l': 'l',
  'm': 'm',
  'n': 'n',
  'h': 'h',
  'w': 'w',
  'y': 'y',
  '2': '^',
  'a': 'a',
  'o': 'o',
  'i': 'i',
}

latin_word = 'bghito ndiro ftor m3a al3a2ila'
#bGiyto ndiyro fTowr mEa AlEaA^ila
OSL_word = latinToOSL(latin_word, mapping)
print(OSL_word)

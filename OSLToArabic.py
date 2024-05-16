def OSLToArabic(word, mapping):
    arabic_word = ''
    i = 0
    while i < len(word):
        if i + 1 < len(word) and word[i] == '^':
            if word[i+1] == 'y':
                arabic_word += mapping['^y']
                i += 2
            elif word[i+1] == 'w':
                arabic_word += mapping['^w']
                i += 2
            elif word[i+1] == 'A':
                arabic_word += mapping['^A']
                i += 2
            else:
                arabic_word += mapping['^']
                i += 1
        elif word[i] in mapping:
            arabic_word += mapping[word[i]]
            i += 1
        else:
            arabic_word += word[i]
            i += 1
    
    # For Tachkil
    arabic_word = arabic_word.replace('a', 'َ')
    arabic_word = arabic_word.replace('o', 'ُ')
    arabic_word = arabic_word.replace('i', 'ِ')
    
    return arabic_word

mapping = {
  'A': 'ا',
  'b': 'ب',
  't': 'ت',
  'T': 'ث',
  'j': 'ج',
  'H': 'ح',
  'X': 'خ',
  'd': 'د',
  'd': 'د',
  'r': 'ر',
  'z': 'ز',
  's': 'س',
  '$': 'ش',
  'S': 'ص',
  'D': 'ض',
  'T': 'ط',
  'D': 'ض',
  'E': 'ع',
  'G': 'غ',
  'f': 'ف',
  'q': 'ق',
  'q': 'ك',
  'l': 'ل',
  'm': 'م',
  'n': 'ن',
  'h': 'ه',
  'w': 'و',
  'y': 'ي',
  '"':'ة',
  '^y':'ئ',
  '^w':'ؤ',
  '^A':'أ',
  'A^':'إ',
  '^':'ء',
  'a': 'َ',
  'o': 'ُ',
  'i': 'ِ',
}

latin_word = 'bGiyto ndiyro fTowr mEa AlEaA^yila"'
arabic_word = OSLToArabic(latin_word, mapping)
print(arabic_word)

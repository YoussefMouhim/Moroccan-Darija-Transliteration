def ArabicToOSL(word, mapping):
    latin_word = ''
    for letter in word:
        if letter in mapping:
            latin_word += mapping[letter]
        else:
            latin_word += letter
    
    # For Tachkil
    latin_word = latin_word.replace('َ', 'a')
    latin_word = latin_word.replace('ُ', 'o')
    latin_word = latin_word.replace('ِ', 'i')
    
    return latin_word

mapping = {
  'ا': 'A',
  'ب': 'b',
  'ت': 't',
  'ث': 't',
  'ج': 'j',
  'ح': 'H',
  'خ': 'X',
  'د': 'd',
  'ذ': 'd',
  'ر': 'r',
  'ز': 'z',
  'س': 's',
  'ش': '$',
  'ص': 'S',
  'ض': 'D',
  'ط': 'T',
  'ظ': 'D',
  'ع': 'E',
  'غ': 'G',
  'ف': 'f',
  'ق': 'q',
  'ك': 'q',
  'ل': 'l',
  'م': 'm',
  'ن': 'n',
  'ه': 'h',
  'و': 'w',
  'ي': 'y',
  'ة':'"',
  'ئ':'^y',
  'ؤ':'^w',
  'أ':'^A',
  'إ':'A^',
  'ء':'^',
  'َ': 'a',
  'ُ': 'o',
  'ِ': 'i',
}


arabic_word = 'بغِيتُ ندِيرُ فطُور معَ العَائِلَة'
latin_word = ArabicToOSL(arabic_word, mapping)
print(latin_word)

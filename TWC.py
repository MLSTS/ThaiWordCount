from collections import Counter
Index = 0
Dictionary_Words = []
Text_woSpace = []
Words_From_Text = []
Sentence_From_Text = []
Char_From_Sentence = []
String_From_Char = ''
Word_From_Char = []

#Dictionary in
Dictionary = open('TWC_Dict.txt', encoding='utf8', errors='ignore')
Dictionary_Words = list(set([d.rstrip() for d in Dictionary.readlines()]))

#Text in
Text = Dictionary = open('Text.txt', encoding='utf8', errors='ignore')
Text_woSpace = Text.read().split()

#Phrase in
for Phrase in Text_woSpace:
    if Phrase in Dictionary_Words:
        print("Word", Phrase,"is in the Dictionary")
        Words_From_Text.append(Phrase)

    else:
        print("Word", Phrase,"is not in the Dictionary")
        Sentence_From_Text.append(Phrase)

#Sentence in
for Sentence in Sentence_From_Text:
    for i in range(len(Sentence)):
        Char_From_Sentence.append(Sentence[i])

    for x in range(len(Char_From_Sentence)):
        String_From_Char += Char_From_Sentence[x]
        if String_From_Char in Dictionary_Words:
            Word_From_Char.append(String_From_Char)
        y = String_From_Char
        for z in range(len(Word_From_Char)):
            Word_From_Char.sort(reverse=True)
            y = y.replace(Word_From_Char[z], '')
            if y in Dictionary_Words:
                Word_From_Char.append(y)
                y = y.replace(y, '')
        y = ''
    String_From_Char = ''
    Char_From_Sentence.clear()

    Words_From_Text.extend(Word_From_Char)
    Word_From_Char.clear()

    print(Char_From_Sentence)
    


print(Words_From_Text)
print(Sentence_From_Text)
print(Counter(Words_From_Text))
print(Counter(Sentence_From_Text))
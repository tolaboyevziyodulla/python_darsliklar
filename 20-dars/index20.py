from transliter import to_cyrillic ,to_latin
ques = True

while ques:
    text = input("Matn kiriting: ")
    if text.isascii():
        print(to_cyrillic(text))
    else:
        print(to_latin(text))
    
    ques = int(input("Yana matn kiritasizmi?(HA(1), YO'Q(0)): "))
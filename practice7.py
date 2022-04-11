text = input ('Введите предложение:')
text_small = text[:len(text)//2].lower()
text_big = text[len(text)//2:].upper()
print (text_small+text_big)

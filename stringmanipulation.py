def cipher(text):
    spaces = [i for i, c in enumerate(text) if c == ' ']
    return text.replace(' ', '').upper(), spaces

def decipher(text, spaces):
    for i in spaces:
        text = text[:i] + ' ' + text[i:]
    text = text.lower()
    return text[0].upper() + text[1:]

msg = "The world population is increasing rapidly"
c, s = cipher(msg)
print(c, s)
print(decipher(c, s))

#https://github.com/AReverri/SSW540/blob/main/stringmanipulation.py
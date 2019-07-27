def changeToUpperCase(text):
    new_text = ""
    for i in text:
        i = ord(i) - 32
        new_text = new_text + chr(i)    
    return new_text
print (changeToUpperCase("HackerRank.com presents "))    
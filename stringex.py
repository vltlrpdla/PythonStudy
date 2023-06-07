words = 'Connect Foundation'

if 'F' in words:
    words.lower()
    #words[7] = '&'
    replaceworkds = words.replace(' ', '&')
else:
    print(words)
print(words + '\nreplacewords : ' + replaceworkds) 
alpha = "abcdefghijklmnopqrstuvwxyz"
shift = 3
plainText = "hello"
cipherText = ""
id = 0

for id in range(len(plainText)):
    cipherText += alpha[ ( alpha.index(plainText[id]) + shift ) % 26 ]

print(cipherText)
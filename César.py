alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for x in range(len(alphabet)):
        alphabet.append(alphabet[x])

message = input("Entrez votre message : ").upper()
clef = int(input("Entrez votre clef : "))

def chiffrage_lettre(lettre, alphabet, clef):
        for i in range(len(alphabet)):
                if lettre == ' ':
                        return ' '
                elif alphabet[i]==lettre:
                        return str(alphabet[i+clef])
        return '?'

message_chiffré = str()

for lettre in message :
        message_chiffré += chiffrage_lettre(lettre,alphabet,clef)

print(message_chiffré)

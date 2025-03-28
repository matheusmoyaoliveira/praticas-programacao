frase = input('Digite uma frase ou palavra: ')
vogais = 'aeiou'

frase = frase.lower()

total = 0
for vogal in vogais:
    total += frase.count(vogal)

print(f'Sua frase/palavra tem {total} vogais.')


                
    
#Fim do Programa
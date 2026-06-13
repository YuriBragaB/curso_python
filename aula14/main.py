import os

def forca():
    palavra = 'melancia'
    
    print('-' * 30 )
    print('Bem vindo ao jogo da forca!')
    print('-' * 30 )
    print('\n')
    for i in range(5):
        tentativa = 6 - i
        print(f'Você possui {tentativa} tentativas')
        tracos = ''
        for i in palavra:
            tracos += '_'
        
        print('\n' + tracos + '\n')  
        chute = input('Digite uma letra:\n')

        lista_tracos = list(tracos)
        if chute in palavra:
            print(f'A palavra secreta possui a letra : {chute}')
            indice = 0
            for i in palavra:
                if chute == i:
                    print(palavra[indice])
                    print(indice)
                    lista_tracos[indice] = chute
                indice += 1
        tracos = "".join(lista_tracos)
        print(tracos)
        continue

forca()
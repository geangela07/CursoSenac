import random


from classPokemon import *
from classTreinador import *


def batalharPokemons(treinador1,treinador2):
    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()


    p1Forca = 2 *(p1._ataque + p1._defesa)
    p2Forca = 2 *(p2._ataque + p2._defesa) 

    print(f"{p1._nome} atacou com {p1Forca} e com movimento {p1._movimento}")
    print(f"{p2._nome} atacou com {p2Forca} e com movimento {p2._movimento}")


    if(p1Forca > p2Forca):
         print(f"O vencedor foi {p1._nome} com a força {p1Forca} do treinador {treinador1._nome}")

    elif(p1Forca < p2Forca):
        print(f"o vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")


pokemonDisponiveis = [
pokemonFogo("Eva","Charmander","Fogo",100,60,90),
pokemonEletrico("Ton","Pikachu","Eletrico",100,30,78),
pokemonAquatico("Bola","Squirtle","Aquatico",200,92,78),
pokemonFogo("Kaio","Charmelon","Fogo",200,60,52),
pokemonAquatico("Tata","Wartortle","Aquatico",300,65,32),
pokemonEletrico("Gabi","Raichu","Eletrico",250,85,69),
pokemonVenenoso("Ana","Nidorino","Venenoso",600,69,30),
pokemonVenenoso("Dana","Nidorina","Venenoso",542,68,52)
]

nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(4):
    print(f"{i+1}. {pokemonDisponiveis[i]._nome}")

pokemonInicial = pokemonDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
print(f"O pokemon escolhido foi o {pokemonInicial._nome}")

jogador = Jogador(nomeJogador,[pokemonInicial])
inimigo = Inimigo("Bob",pokemonDisponiveis)
inimigo2 = Inimigo("Arthur",pokemonDisponiveis)
inimigo3 = Inimigo("Mateus",pokemonDisponiveis)
Inimigos =[inimigo,inimigo2,inimigo3]
while True:
    print("""
    Escolha o que você quer fazer:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3.Batalhar contra um oponente
    0. sair do Jogo
    """)

    menu = input("Digite a opção escolhida: ")

    if menu == "0":
        print("Você saiu do jogo.")
        break
    elif menu == "1":
        jogador.listaPokemons()

    elif menu == "2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(pokemonDisponiveis)):
            print(f"{i+1}. {pokemonDisponiveis[i]._nome}")

        capturado = pokemonDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu == "3":
        batalharPokemons(jogador,random.choice(Inimigos))

    else:
        print("Você digitou algo inválido,tente novamente.")




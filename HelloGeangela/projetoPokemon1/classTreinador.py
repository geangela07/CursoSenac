import random

class Treinador:          
    def __init__(self,nome,pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

#Definição das subclasses: requisito 4

class Jogador(Treinador):   
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)


    def escolherPokemon(self):
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")
            return self._pokemons[int(pokemonEscolhido)-1]

# Definição do metodo capturar: requisito 6
    def capturarPokemon(self,pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")


# Defiição do metodo lista de pokemons: requisito 7
    def listaPokemons(self):
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
            print(f"{i+1}. {self._pokemons[i]._nome}")

        
        
class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

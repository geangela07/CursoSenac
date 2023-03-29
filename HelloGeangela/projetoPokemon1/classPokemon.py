
#Definição classe pokemon: requisito 1
class Pokemon:                      
    def __init__(self,nome,especie,tipo,ataque,defesa,hp):
        self._nome = nome
        self._tipo = tipo
        self._hp = hp
        self._especie = especie
        self._ataque = ataque
        self._defesa = defesa

 #Definição das subclasses: requisito 2
class pokemonAquatico(Pokemon):           
    def __init__(self,nome,especie,ataque,defesa,tipo,hp):
        super().__init__(nome,especie,ataque,defesa,tipo,hp)
        self._tipo = "aquatico"
        self._movimento = "Jato d'agua"
    

class pokemonEletrico(Pokemon):
    def __init__(self,nome,especie,ataque,defesa,tipo,hp):
        super().__init__(nome,especie,ataque,defesa,tipo,hp)
        self._tipo = "eletrico"
        self._movimento = "Choque do trovão"

class pokemonFogo(Pokemon):
    def __init__(self,nome,especie,ataque,defesa,tipo,hp):
        super().__init__(nome,especie,ataque,defesa,tipo,hp)
        self._tipo = "fogo"
        self._movimento = "Lança chamas"

class pokemonVenenoso(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "veneno"
        self._movimento = "Spray"
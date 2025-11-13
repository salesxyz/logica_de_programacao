# atributos - carcteristicas do objeto
# metodos - açõess que o objeto pode fazer

# nome e vida - atacar
# self - quando quero me referir a algum atributo de classe 
# construtor - quando quero criar um novo objeto, chamo o construtor para acesar os atributos

class Personagem:
    # construtor
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    # definindo GET
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

class Guerreiro:
    def __init__(self, nome, vida, escudo=False):
      super().__init__(nome, vida)
      self.__escudo = escudo
    @property
    def escudo(self):
        return self.__escudo
    
    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo
    
    def atacar(self, personagem):
        return super().atacar(personagem)
   
    #sobreescrevendo o metodo da class pai
    def atacar(self, personagem):
        personagem.vida -= 40
        print(f'{self.nome} atacou {personagem.nome} e causou 40 de dano!')
        print(f'Vida restante de {personagem.nome}: {personagem.vida}')
    
    def protecao(self):
        self.__vida




class Mago:
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def curar(self, personagem):
        personagem.vida += 15
        print(f'{self.__nome} usou o poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')



class Arqueiro:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

Frodo = Personagem('Frodo', 100)
gandof = Mago('Gandof', 100)
Aragon = Guerreiro('Aragorn', 100)

Aragon.atacar(Frodo)
gandof.curar(Frodo)
Aragon.atacar(gandof)
gandof.curar(gandof)

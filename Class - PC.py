# Class 
# Syntaxe
# Marca, Memoria ram, PLaca de Video



class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

    #computador1 = Computador('GIGABYTE', '16GB', 'RTX2060')
    #computador2 = Computador('ASUS','12GB','GTX1050TI')
    #computador3 = Computador('MSI','32GB','RTX3070TI')

    #print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
    #print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
    #print(computador3.marca, computador3.memoria_ram,computador3.placa_de_video)

    def ligar(self):
        print('Estou a ligar')

    def desligar(self):
        print('Estamos a desligar')

    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Gigabyte - ','32gb - ', 'RTX-2060')
computador1.ligar()
computador1.ExibirInformacoesDesteComputador()
computador1.desligar()

print('\n Mudança de PC \n')

computador2 = Computador('ASUS - ', '32GB - ', 'RTX3070TI')
computador2.ligar()
computador2.ExibirInformacoesDesteComputador()
computador2.desligar()




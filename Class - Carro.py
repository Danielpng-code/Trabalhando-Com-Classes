class Carro:
    def __init__(self, marca, modelo, cor, motor, ano, combustivel):
        self.marca_veiculo = input(str('Digite a marca do carro: '))
        self.modelo_veiculo = input(str('Digite o modelo do carro: '))
        self.cor_veiculo = input(str('Digite a cor do veículo: '))
        self.potencia_motor = input(str('Digite a potencia do veículo: '))
        self.fabricação_veiculo = input(str('Digite o ano de fabricação do veículo: '))
        self.combustivel_veiculo = input(str('Digite o combustivel do carro: '))
        
    pass

    def marca(self):
        print(self.marca_veiculo)

    def modelo(self):
        print(self.modelo_veiculo)

    def cor(self):
        print(self.cor_veiculo)

    def potencia(self):
        print(self.potencia_motor) 

    def fabricação(self):
        print(self.fabricação_veiculo)

    def combustivel(self):
        print(self.combustivel_veiculo)

carro1 = Carro(' ',' ', ' ', ' ', ' ', ' ')
carro1.marca()
carro1.modelo()
carro1.cor()
carro1.potencia()
carro1.fabricação()
carro1.combustivel()

print('\n Mudança de veículos \n')

carro2 = Carro(' ', ' ', ' ', ' ', ' ', ' ')
carro2.marca()
carro2.modelo()
carro2.cor()
carro2.potencia()
carro2.fabricação()
carro2.combustivel()
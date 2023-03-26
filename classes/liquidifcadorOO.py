class Liquidificador:
    def _init_(self, velocidade=1,pulsancao=1):
        self.velocidade = velocidade
        self.pulsancao=pulsancao

    def pulsar(self):
        print("estou pulsando",self.pulsancao)

    def girar(self):
        print("ESTOU GIRANDO A  ", self.velocidade)

    def setVelocidade(self, velocidade):
        if (velocidade <= 3):
            self.velocidade = velocidade
            self.girar()
        else:
            print("erro")


class Processador(Liquidificador):
    def _init_(self, velocidade=1):
        super.__init__(velocidade)

    def triturar(self, velocidade):
        if (velocidade <= 3):
            self.velocidade = velocidade
            print("estou triturar a  ", self.velocidade)
        else:
            print("erro")


velocidade = int(input("digite a velocidade desejada"))
meuProcessador = Processador()
meuProcessador.setVelocidade(velocidade)

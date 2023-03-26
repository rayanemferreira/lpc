def pulsar():
    print("estou pulsando")


def girar(velocidade):
    print("estou girando a velocidade ", velocidade)


velocidade = 1

velocidade = int(input("digite a velocidade desejada"))

if (velocidade <= 3):
    girar(velocidade)

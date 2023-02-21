class Blocks:
    def __init__(self, num_arena):
        self.num_arena = num_arena

    def blocks(self):
        doc = open(f"arenas/arena_{self.num_arena}", "r")
        lista = doc.readlines()
        lista_cor = []

        for i in range(26):
            for j in range(38):
                if lista[i][j] == 'X' or lista[i][j] == 'x':
                    lista_cor.append((i + 1, j + 1))
        return lista_cor

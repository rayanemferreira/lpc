class Blocks:
    def __init__(self, map_name):
        self.map_name = map_name

    def blocks(self):
        doc = open(f"map/{self.map_name}.txt", "r")
        lista = doc.readlines()
        doc.close()
        map_tiles = []

        for i in range(36):
            for j in range(64):
                if lista[i][j] == "1":
                    map_tiles.append((i, j))
        return map_tiles

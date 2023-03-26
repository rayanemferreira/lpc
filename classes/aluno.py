class aluno:
    def _init_(self,id, name,age):
        self.name= name
        self.age = age
        self.id = id

    def __str__(self):
        return f"{self.name}{self.age}{self.id}"
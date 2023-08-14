class Empregado:
    id = 0

    def trabalhar(self):
        if self.id == 1:
            print('trabalhando')
        else:
            print('nao trabalhando')

Empregado1 = Empregado()
Empregado2 = Empregado()
Empregado1.id = 310
Empregado2.id = 200
print(Empregado1.id)
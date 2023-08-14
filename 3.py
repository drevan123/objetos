class Jogos:
    def __init__(self,nome, ano, tipo):
        self.nome=nome
        self.ano=ano
        self.tipo=tipo
        
    def informacoes(self):
        return f"Jogos: {self.nome}\nAno: {self.ano}\nTipo: {self.tipo}"
    
    def inicio_jogo(self):
        return F"inicio o jogo{self.nome}.."
    def desligol(self):
        return F"morre e saiu do {self.nome}"

class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo=titulo
        self.ano=ano
        self.genero=genero
    
    def informacoes(self):
        return f"Filme: {self.titulo}\nAno: {self.ano}\nGênero: {self.genero}"

    def inicio(self):
        return F"iniciol o filme {self.titulo}"
    def fim(self):
        return F"foi no banheiro e perdeu o filme {self.titulo}"
    
class carros:
    def __init__(self,marca,modelo,ano,motor):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.motor=motor
    def informacoes(self):
        return f"carros: {self.marca}\nMarca:{self.ano}\nMotor:{self.motor}"
    
    def inicio(self):
        return f"Ligando o carro  {self.marca} {self.modelo}as 6H"

    def desligar(self):
        return f"Desligando o carro {self.marca} {self.modelo}as 14H"



jogo1 = Jogos("valorant", 2020, "FPS")
filme1 = Filme("O Pacto", 2023,"ação")
carro1 = carros("NISSAN","SENTRA","2023","2.0L 16 válvulas CVVTCS gasolina 4 cilindros")

print(jogo1.informacoes())
print(jogo1.inicio_jogo())
print(jogo1.desligol())

print("---------------------------------------------------------------------")

print(filme1.informacoes())
print(filme1.inicio())
print(filme1.fim())

print("---------------------------------------------------------------------")

print(carro1.informacoes())
print(carro1.inicio())
print(carro1.desligar())

print("---------------------------------------------------------------------FIM")
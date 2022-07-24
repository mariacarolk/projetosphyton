from datetime import datetime

class Empregado:
    numero_empregados = 0

    def __init__(self,
                 nome_completo : str,
                 email : str,
                 matricula_func : str,
                 salario : int):

        self.nome_completo = nome_completo
        self.email = email
        self.matricula_func = matricula_func
        self.salario = salario

        Empregado.numero_empregados += 1

    def iniciar_jornada(self):
        print(f'O empregado {self.nome_completo} iniciou sua jornada de trabalho as {datetime.now()}')

    def finalizar_jornada(self):
        print(f'O empregado {self.nome_completo} finalizou sua jornada de trabalho as {datetime.now()}')

    def receber_aumento(self):
        raise NotImplementedError

    def numero_empregados_atual(self):
        print("O número de empregados atual é de: ", Empregado.numero_empregados)

class Desenvolvedor(Empregado):
    pct_aumento_desenv = 1.10
    limite_cafe = 5

    def __init__(self,
                 nome_completo : str,
                 email: str,
                 matricula_func : str,
                 salario : int,
                 linguagens_prog : list,
                 litros_cafe : float = 0,
                 burnout : bool = False):

        #Chamada construtor classe superior
        super().__init__(nome_completo, email, matricula_func, salario)

        self.linguagens_prog = linguagens_prog
        self.litros_cafe = litros_cafe
        self.burnout = burnout

        print(f'Contratado desenvolvedor {self.matricula_func} {self.nome_completo}')

    def add_linguagem(self, nova_linguagem):
        self.linguagens_prog.append(nova_linguagem)
        print(f'Agora o desenvolvedor {self.nome_completo} também possui experiência na linguagem {nova_linguagem}')

    def beber_cafe(self, qtd_cafe):
        self.litros_cafe += qtd_cafe
        print(f'O desenvolvedor {self.nome_completo} já bebeu {self.litros_cafe} litros de café.')

        if self.litros_cafe > Desenvolvedor.limite_cafe:
            print('Cuidado! Desenvolvedor em Burnout!!!')
            self.burnout = True

    def receber_aumento(self):
        self.salario = self.salario * Desenvolvedor.pct_aumento_desenv
        print(f'O desenvolvedor {self.nome_completo} recebeu aumento e o seu salário passou a ser de {self.salario}')

class GerenteProjeto(Empregado):
    pct_aumento_gerente = 1.20

    def __init__(self,
                 nome_completo: str,
                 email: str,
                 matricula_func: str,
                 salario: int,
                 time: list,
                 projetos_envolvidos: list):

        # Chamada construtor classe superior
        super().__init__(nome_completo, email, matricula_func, salario)

        self.time = time
        self.projetos_envolvidos = projetos_envolvidos

        print(f'Contratado gerente {self.matricula_func} {self.nome_completo}')

    def add_desenv(self, dev):
        self.time.append(dev)
        print(f'O desenvolvedor {dev.nome_completo} foi adicionado ao time do gestor {self.nome_completo}')

    def remover_desenv(self, dev):
        self.time.remove(dev)
        print(f'O desenvolvedor {dev.nome_completo} foi removido do time do gestor {self.nome_completo}')

    def participar_projeto(self, projeto):
        self.projetos_envolvidos.append(projeto)
        print(f'O gestor {self.nome_completo} passou a integrar o projeto {projeto}.')

    def sair_projeto(self, projeto):
        self.projetos_envolvidos.remove(projeto)
        print(f'O gestor {self.nome_completo} saiu do projeto {projeto}.')

    def receber_aumento(self):
        self.salario = self.salario * GerenteProjeto.pct_aumento_gerente
        print(f'O gerente {self.nome_completo} recebeu aumento e o seu salário passou a ser de {self.salario}')




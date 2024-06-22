import re

class Lexer:
    def __init__(self, trechoCodigo):
        self.estadoAtual = 0
        self.trechoCodigo = trechoCodigo
        self.caracterAtual = trechoCodigo[0]
        self.contador = 0
        self.lexema = ''
        self.listaTokens = []
        self.tabelaSimbolos = []
        self.variavelControle = True
        self.expressaoDigito = r"\d"


    def getToken(self):
        while(self.contador < len(self.trechoCodigo) and self.variavelControle):
            self.caracterAtual = self.trechoCodigo[self.contador]
            switch_case = {
                0: self.estado_0,
                1: self.estado_1,
                2: self.estado_2,
                93: self.estado_93,
                94: self.estado_94,
                95: self.estado_95,
                96: self.estado_96,
                97: self.estado_97,
                98: self.estado_98,
                99: self.estado_99,
                100: self.estado_100,
                101: self.estado_101,
            }
            switch_case.get(self.estadoAtual, self.padrao)()
            self.contador+=1
            print('tabela simbolos,', self.tabelaSimbolos)
            print('lista tokens: ', self.listaTokens)

    def padrao(self):
        print('estado {self.estadoAtual} nao encontrado')
        
    def estado_0(self):
        print('entra estado 0')
        expressaoLetrasEstado0 = r"a|g|h|j|k|l|m|q|u|w|x|y|z|ç|_|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|V|W|X|Y|Z|Ç"
        
        #letras que nao são de variaveis
        if re.match(expressaoLetrasEstado0, self.caracterAtual):
            self.estadoAtual = 93
            self.lexema += self.caracterAtual

        #digitos
        elif re.match(self.expressaoDigito, self.caracterAtual):
            self.estadoAtual = 95
            self.lexema += self.caracterAtual
        # b de `boleano`

        elif self.caracterAtual == 'b':
            pass
        # c de `continua`
        elif self.caracterAtual == 'c':
            pass
        # d de `de`
        elif self.caracterAtual == 'd':
            pass
        # e de `enquanto` ou 'e'
        elif self.caracterAtual == 'e':
            pass
        # f de `funcao` ou `falso`
        elif self.caracterAtual == 'f':
            self.estadoAtual = 1
            self
        # i de `inteiro` ou `importe`
        elif self.caracterAtual == 'i':
            pass
        # n de `nulo` ou 'nao'
        elif self.caracterAtual == 'n':
            pass
        # s de `se`, `senao` ou `senaose`
        elif self.caracterAtual == 's':
            pass
        # t de `texto`
        elif self.caracterAtual == 't':
            pass
        # p de `para` ou `passa`
        elif self.caracterAtual == 'p':
            pass
        # o de 'ou'
        elif self.caracterAtual == 'o':
            pass
        # r de `retorna` ou `real`
        elif self.caracterAtual == 'r':
            pass
        # v de `verdade`
        elif self.caracterAtual == 'v':
            pass
        # Operador aritmético '+' ou  de atribuição '+='
        elif self.caracterAtual == '+':
            pass
        # Operador aritmético '-' ou atribuição '-='
        elif self.caracterAtual == '-':
            pass
        # Operador aritmético *
        elif self.caracterAtual == '*':
            pass
        # Operador aritmético /
        elif self.caracterAtual == '/':
            pass
        # Operador de atribuição '=' ou comparação '=='
        elif self.caracterAtual == '=':
            pass
        # Operador de comparação '!='
        elif self.caracterAtual == '!':
            pass
        # Operador de comparação '>' ou '>='
        elif self.caracterAtual == '>':
            pass
        # Operador de comparação '<' ou '<='
        elif self.caracterAtual == '<':
            pass
        # abre parenteses
        elif self.caracterAtual == '(':
            pass
        # fecha parenteses
        elif self.caracterAtual == ')':
            pass
        # abre colchetes
        elif self.caracterAtual == '[':
            pass
        # fecha colchetes
        elif self.caracterAtual == ']':
            pass
        # abre chaves
        elif self.caracterAtual == '{':
            pass
        # fecha chaves
        elif self.caracterAtual == '}':
            pass
        # dois pontos para fim de funções
        elif self.caracterAtual == ':':
            pass
        # virgula para divisor de atributos
        elif self.caracterAtual == ',':
            pass
        # hashtag para comentarios
        elif self.caracterAtual == '#':
            pass
        # aspas simples para abrir e fechar textos
        elif self.caracterAtual == " ' ":
            pass
        # espaço para finalizar os lexemas
        elif self.caracterAtual == ' ':
            pass
        # tabulação para organizar as hierarquias
        elif self.caracterAtual == '\t':
            pass
        # quebra de linha para organizar as linhas
        elif self.caracterAtual == '\n':
            pass
        
    def estado_1(self):
        print('1')
    
    def estado_2(self):
        print('2')

    def estado_93(self):
        print('entra estado 93')
        expressaoLetrasAndDigitosEstado93 = r"[a-zA-Z0-9_]"
        if re.match(expressaoLetrasAndDigitosEstado93, self.caracterAtual):
            self.estadoAtual = 93
            self.lexema += self.caracterAtual
        #vai para estado final, reconhecendo um IDENTIFICADOR como lexema
        else:
            self.estadoAtual = 94
            self.estado_94()

    #estado final de IDENTIFICADOR
    def estado_94(self):
        print('entra estado 94')
        if self.lexema not in self.tabelaSimbolos:
            self.listaTokens.append(('id', len(self.tabelaSimbolos)))
            self.tabelaSimbolos.append(self.lexema)
        else:
            indice = self.tabelaSimbolos.index(self.lexema)
            self.listaTokens.append(('id', indice))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    # Primeiro estado dos NUMEROS
    def estado_95(self):
        print('entra estado 95')
        if re.match(self.expressaoDigito, self.caracterAtual):
            # estado continua o 95
            self.lexema += self.caracterAtual
        elif self.caracterAtual == '.':
            self.estadoAtual = 96
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 100
            self.estado_100()

    #Estado do 'ponto' dos numeros reais
    def estado_96(self):
        print('entra no 96')
        if re.match(self.expressaoDigito, self.caracterAtual):
            self.estadoAtual = 97
            self.lexema += self.caracterAtual
        else:
            #Vai para o ERRO 101, que nao pode ter outra coisa, alem de numeros depois do ponto
            self.estadoAtual = 101
            self.estado_101()

    #Estado de repetição de digitos dos numeros reais
    def estado_97(self):
        print('entra no 97')
        if re.match(self.expressaoDigito, self.caracterAtual):
            # Mantem no estado 97 
            self.lexema += self.caracterAtual
        elif self.caracterAtual == '.':
            self.estadoAtual = 99
            self.estado_99()
        else:
            #Vai para o estado final do NUMERO REAL 98
            self.estadoAtual = 98
            self.estado_98()

    # Estado Final para NUMERO REAL
    def estado_98(self):
        print('entra no estado 98')
        self.listaTokens.append(('real', self.lexema))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #Estado final de ERRO quando digita ponto depois do numero real
    def estado_99(self):
        print('entra no estado 99')
        #MENSAGEM DE ERRO POR VIR PONTO DEPOIS DO NUMERO REAL, ex: 22.25.
        print('ERRO, no numero real {lexema}. Depois do numero real nao podem vir pontos')
        self.variavelControle = False

    def estado_100(self):
        print('entra no estado 100')
        self.listaTokens.append(('inteiro', self.lexema))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    def estado_101(self):
        print('entra no estado 101')
        #MENSAGEM DE ERRO POR VIR ALGO DEPOIS DO PONTO QUE NÃO SEJA UM DIGITO, ex: 23.a
        print('ERRO, no numero real {lexema}. Depois do ".", tem de vir um digito ')
        self.variavelControle = False
            

codigo = input('Digite o codigo: ')
l = Lexer(codigo)
l.getToken()
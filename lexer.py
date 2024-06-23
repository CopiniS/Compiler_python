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
        self.expressaoLetrasAndDigitosAndUnderline = r"[a-zA-Z0-9_]"


    def getToken(self):
        while(self.contador < len(self.trechoCodigo) and self.variavelControle):
            self.caracterAtual = self.trechoCodigo[self.contador]
            switch_case = {
                0: self.estado_0,
                1: self.estado_1,
                2: self.estado_2,
                3: self.estado_3,
                4: self.estado_4,
                5: self.estado_5,
                6: self.estado_6,
                7: self.estado_7,
                8: self.estado_8,
                9: self.estado_9,
                10: self.estado_10,
                11: self.estado_11,
                12: self.estado_12,
                13: self.estado_13,
                14: self.estado_14,
                15: self.estado_15,
                16: self.estado_16,
                17: self.estado_17,
                18: self.estado_18,
                19: self.estado_19,
                20: self.estado_20,
                21: self.estado_21,
                22: self.estado_22,
                23: self.estado_23,
                24: self.estado_24,
                25: self.estado_25,
                26: self.estado_26,
                27: self.estado_27,
                28: self.estado_28,
                29: self.estado_29,
                30: self.estado_30,
                31: self.estado_31,
                32: self.estado_32,
                33: self.estado_33,
                34: self.estado_34,
                35: self.estado_35,
                36: self.estado_36,
                37: self.estado_37,
                38: self.estado_38,
                39: self.estado_39,
                40: self.estado_40,
                41: self.estado_41,
                42: self.estado_42,
                43: self.estado_43,
                44: self.estado_44,
                45: self.estado_45,
                46: self.estado_46,
                47: self.estado_47,
                48: self.estado_48,
                49: self.estado_49,
                50: self.estado_50,
                51: self.estado_51,
                52: self.estado_52,
                53: self.estado_53,
                54: self.estado_54,
                55: self.estado_55,
                56: self.estado_56,
                57: self.estado_57,
                58: self.estado_58,
                59: self.estado_59,
                60: self.estado_60,
                61: self.estado_61,
                62: self.estado_62,
                63: self.estado_63,
                64: self.estado_64,
                65: self.estado_65,
                66: self.estado_66,
                67: self.estado_67,
                68: self.estado_68,
                69: self.estado_69,
                70: self.estado_70,
                71: self.estado_71,
                72: self.estado_72,
                73: self.estado_73,
                74: self.estado_74,
                75: self.estado_75,
                76: self.estado_76,
                77: self.estado_77,
                78: self.estado_78,
                79: self.estado_79,
                80: self.estado_80,
                81: self.estado_81,
                82: self.estado_82,
                83: self.estado_83,
                84: self.estado_84,
                85: self.estado_85,
                86: self.estado_86,
                87: self.estado_87,
                88: self.estado_88,
                89: self.estado_89,
                90: self.estado_90,
                91: self.estado_91,
                92: self.estado_92,
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
        
    #Estado inicial do autômato
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
            self.lexema += self.caracterAtual
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
        
    #FUNCAO | FALSO - (q0 --> q1 --> q2 | q3 | q93 | q94)
    def estado_1(self):
        if self.caracterAtual == 'u':
            self.estadoAtual = 2
            self.lexema += self.caracterAtual
        elif self.caracterAtual == 'a':
            self.estadoAtual = 3
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 93
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 94
            self.estado_94()
      
    #!!!!!!!!NAO FEITO
    def estado_2(self):
        print('entra estado 2')
        
    #!!!!!!!!NAO FEITO
    def estado_3(self):
        print('entra estado 3')

    #!!!!!!!!NAO FEITO
    def estado_4(self):
        print('entra estado 4')

    #!!!!!!!!NAO FEITO
    def estado_5(self):
        print('entra estado 5')

    #!!!!!!!!NAO FEITO
    def estado_6(self):
        print('entra estado 6')

    #!!!!!!!!NAO FEITO
    def estado_7(self):
        print('entra estado 7')

    #!!!!!!!!NAO FEITO
    def estado_8(self):
        print('entra estado 8')

    #!!!!!!!!NAO FEITO
    def estado_9(self):
        print('entra estado 9')

    #!!!!!!!!NAO FEITO
    def estado_10(self):
        print('entra estado 10')

    #!!!!!!!!NAO FEITO
    def estado_11(self):
        print('entra estado 11')

    #!!!!!!!!NAO FEITO
    def estado_12(self):
        print('entra estado 12')

    #!!!!!!!!NAO FEITO
    def estado_13(self):
        print('entra estado 13')

    #!!!!!!!!NAO FEITO
    def estado_14(self):
        print('entra estado 14')

    #!!!!!!!!NAO FEITO
    def estado_15(self):
        print('entra estado 15')

    #!!!!!!!!NAO FEITO
    def estado_16(self):
        print('entra estado 16')

    #!!!!!!!!NAO FEITO
    def estado_17(self):
        print('entra estado 17')

    #!!!!!!!!NAO FEITO
    def estado_18(self):
        print('entra estado 18')

    #!!!!!!!!NAO FEITO
    def estado_19(self):
        print('entra estado 19')

    #!!!!!!!!NAO FEITO
    def estado_20(self):
        print('entra estado 20')

    #!!!!!!!!NAO FEITO
    def estado_21(self):
        print('entra estado 21')

    #!!!!!!!!NAO FEITO
    def estado_22(self):
        print('entra estado 22')

    #!!!!!!!!NAO FEITO
    def estado_23(self):
        print('entra estado 23')

    #!!!!!!!!NAO FEITO
    def estado_24(self):
        print('entra estado 24')

    #!!!!!!!!NAO FEITO
    def estado_25(self):
        print('entra estado 25')

    #!!!!!!!!NAO FEITO
    def estado_26(self):
        print('entra estado 26')

    #!!!!!!!!NAO FEITO
    def estado_27(self):
        print('entra estado 27')

    #!!!!!!!!NAO FEITO
    def estado_28(self):
        print('entra estado 28')

    #!!!!!!!!NAO FEITO
    def estado_29(self):
        print('entra estado 29')

    #!!!!!!!!NAO FEITO
    def estado_30(self):
        print('entra estado 30')

    #!!!!!!!!NAO FEITO
    def estado_31(self):
        print('entra estado 31')

    #!!!!!!!!NAO FEITO
    def estado_32(self):
        print('entra estado 32')

    #!!!!!!!!NAO FEITO
    def estado_33(self):
        print('entra estado 33')

    #!!!!!!!!NAO FEITO
    def estado_34(self):
        print('entra estado 34')

    #!!!!!!!!NAO FEITO
    def estado_35(self):
        print('entra estado 35')

    #!!!!!!!!NAO FEITO
    def estado_36(self):
        print('entra estado 36')

    #!!!!!!!!NAO FEITO
    def estado_37(self):
        print('entra estado 37')

    #!!!!!!!!NAO FEITO
    def estado_38(self):
        print('entra estado 38')

    #!!!!!!!!NAO FEITO
    def estado_39(self):
        print('entra estado 39')

    #!!!!!!!!NAO FEITO
    def estado_40(self):
        print('entra estado 40')

    #!!!!!!!!NAO FEITO
    def estado_41(self):
        print('entra estado 41')

    #!!!!!!!!NAO FEITO
    def estado_42(self):
        print('entra estado 42')

    #!!!!!!!!NAO FEITO
    def estado_43(self):
        print('entra estado 43')

    #!!!!!!!!NAO FEITO
    def estado_44(self):
        print('entra estado 44')

    #!!!!!!!!NAO FEITO
    def estado_45(self):
        print('entra estado 45')

    #!!!!!!!!NAO FEITO
    def estado_46(self):
        print('entra estado 46')

    #!!!!!!!!NAO FEITO
    def estado_47(self):
        print('entra estado 47')

    #!!!!!!!!NAO FEITO
    def estado_48(self):
        print('entra estado 48')

    #!!!!!!!!NAO FEITO
    def estado_49(self):
        print('entra estado 49')

    #!!!!!!!!NAO FEITO
    def estado_50(self):
        print('entra estado 50')

    #!!!!!!!!NAO FEITO
    def estado_51(self):
        print('entra estado 51')

    #!!!!!!!!NAO FEITO
    def estado_52(self):
        print('entra estado 52')

    #!!!!!!!!NAO FEITO
    def estado_53(self):
        print('entra estado 53')

    #!!!!!!!!NAO FEITO
    def estado_54(self):
        print('entra estado 54')

    #!!!!!!!!NAO FEITO
    def estado_55(self):
        print('entra estado 55')

    #!!!!!!!!NAO FEITO
    def estado_56(self):
        print('entra estado 56')

    #!!!!!!!!NAO FEITO
    def estado_57(self):
        print('entra estado 57')

    #!!!!!!!!NAO FEITO
    def estado_58(self):
        print('entra estado 58')

    #!!!!!!!!NAO FEITO
    def estado_59(self):
        print('entra estado 59')

    #!!!!!!!!NAO FEITO
    def estado_60(self):
        print('entra estado 60')

    #!!!!!!!!NAO FEITO
    def estado_61(self):
        print('entra estado 61')

    #!!!!!!!!NAO FEITO
    def estado_62(self):
        print('entra estado 62')

    #!!!!!!!!NAO FEITO
    def estado_63(self):
        print('entra estado 63')

    #!!!!!!!!NAO FEITO
    def estado_64(self):
        print('entra estado 64')

    #!!!!!!!!NAO FEITO
    def estado_65(self):
        print('entra estado 65')

    #!!!!!!!!NAO FEITO
    def estado_66(self):
        print('entra estado 66')

    #!!!!!!!!NAO FEITO
    def estado_67(self):
        print('entra estado 67')

    #!!!!!!!!NAO FEITO
    def estado_68(self):
        print('entra estado 68')

    #!!!!!!!!NAO FEITO
    def estado_69(self):
        print('entra estado 69')

    #!!!!!!!!NAO FEITO
    def estado_71(self):
        print('entra estado 71')

    #!!!!!!!!NAO FEITO
    def estado_72(self):
        print('entra estado 72')

    #!!!!!!!!NAO FEITO
    def estado_73(self):
        print('entra estado 73')

    #!!!!!!!!NAO FEITO
    def estado_74(self):
        print('entra estado 74')

    #!!!!!!!!NAO FEITO
    def estado_70(self):
        print('entra estado 70')

    #!!!!!!!!NAO FEITO
    def estado_75(self):
        print('entra estado 75')

    #!!!!!!!!NAO FEITO
    def estado_76(self):
        print('entra estado 76')

    #!!!!!!!!NAO FEITO
    def estado_77(self):
        print('entra estado 77')

    #!!!!!!!!NAO FEITO
    def estado_78(self):
        print('entra estado 78')

    #!!!!!!!!NAO FEITO
    def estado_79(self):
        print('entra estado 79')

    #!!!!!!!!NAO FEITO
    def estado_80(self):
        print('entra estado 80')

    #!!!!!!!!NAO FEITO
    def estado_81(self):
        print('entra estado 81')

    #!!!!!!!!NAO FEITO
    def estado_82(self):
        print('entra estado 82')

    #!!!!!!!!NAO FEITO
    def estado_83(self):
        print('entra estado 84')

    #!!!!!!!!NAO FEITO
    def estado_84(self):
        print('entra estado 84')

    #!!!!!!!!NAO FEITO
    def estado_85(self):
        print('entra estado 85')

    #!!!!!!!!NAO FEITO
    def estado_86(self):
        print('entra estado 86')

    #!!!!!!!!NAO FEITO
    def estado_87(self):
        print('entra estado 87')

    #!!!!!!!!NAO FEITO
    def estado_88(self):
        print('entra estado 88')

    #!!!!!!!!NAO FEITO
    def estado_89(self):
        print('entra estado 89')

    #!!!!!!!!NAO FEITO
    def estado_90(self):
        print('entra estado 90')

    #!!!!!!!!NAO FEITO
    def estado_91(self):
        print('entra estado 91')

    #!!!!!!!!NAO FEITO
    def estado_92(self):
        print('entra estado 92')

    #IDENTIFICADORES - (q0 --> q93 --> q93 | q94) - (Vem pra cá, quando é digitado uma letra diferente das que iniciam nas keywords, estando no estado inical)
    def estado_93(self):
        print('entra estado 93')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 93
            self.lexema += self.caracterAtual
        #vai para estado final, reconhecendo um IDENTIFICADOR como lexema
        else:
            self.estadoAtual = 94
            self.estado_94()

    #IDENTIFICADORES - (q93 --> q94 --> q0) - Estado FINAL (Vem pra cá, quando é digitado outra coisa, que não letras, digitos ou underline)
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

    #DIGITOS - (q0 --> q95 --> q100 | q96) - (Vem pra cá, quando é digitado um digito, estando no estado inicial)
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

    #DIGITOS - (q95 --> q96 --> q97 | q101) - (Vem pra cá, quando é digitado um ponto depois do digito)
    def estado_96(self):
        print('entra no 96')
        if re.match(self.expressaoDigito, self.caracterAtual):
            self.estadoAtual = 97
            self.lexema += self.caracterAtual
        else:
            #Vai para o ERRO 101, que nao pode ter outra coisa, alem de numeros depois do ponto
            self.lexema += self.caracterAtual
            self.estadoAtual = 101
            self.estado_101()

    #DIGITOS - (q96 --> q97 --> q97 | q98 | q99) - (Vem pra cá quando digita um digito depois do ponto do numero real)
    def estado_97(self):
        print('entra no 97')
        if re.match(self.expressaoDigito, self.caracterAtual):
            # Mantem no estado 97 
            self.lexema += self.caracterAtual

        
        elif self.caracterAtual == '.':
            #Vai para estado de erro 99
            self.lexema += self.caracterAtual
            self.estadoAtual = 99
            self.estado_99()
        else:
            #Vai para o estado final do NUMERO REAL 98
            self.estadoAtual = 98
            self.estado_98()

    #DIGITOS - (q97 --> q98 --> q0) - Estado FINAL dos números REAIS (Vem pra cá quando digita outra coisa depois do numero real completo)
    def estado_98(self):
        print('entra no estado 98')
        self.listaTokens.append(('real', self.lexema))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #DIGITOS - (q97 --> q99 --> q0) - Estado de ERRO (Vem pra cá quando digita um ponto('.'), quando estiver no estado dos decimais, Ex: 22.22.)
    def estado_99(self):
        print('entra no estado 99')
        print('ERRO, no numero real '+ self.lexema + ' --> Depois do numero real nao podem vir pontos')
        self.variavelControle = False

    #DIGITOS - (q95 --> q100 --> q0) - Estado FINAL dos números INTEIROS (Vem pra cá qunado digita outra coisa depois do número inteiro)
    def estado_100(self):
        print('entra no estado 100')
        self.listaTokens.append(('inteiro', self.lexema))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #DIGITOS - (q96 --> q101 --> q0) - Estado de ERRO (Vem pra cá, quando é digitado outra coisa depois do ponto de numero flutuante, Ex: 22.a)
    def estado_101(self):
        print('entra no estado 101')
        #MENSAGEM DE ERRO POR VIR ALGO DEPOIS DO PONTO QUE NÃO SEJA UM DIGITO, ex: 23.a
        print('ERRO, no numero real '+ self.lexema +' --> Depois do ".", tem de vir um digito ')
        self.variavelControle = False
            

codigo = input('Digite o codigo: ')
l = Lexer(codigo)
l.getToken()
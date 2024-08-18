import re
from collections import deque;
import sys;

class Lexer:
    def __init__(self, trechoCodigo):
        self.estadoAtual = 0
        self.nivelIndetacao = 0
        self.pilhaTab = deque()
        self.pilhaTab.append(0)
        self.trechoCodigo = trechoCodigo
        self.caracterAtual = trechoCodigo[0]
        self.contador = 0
        self.contadorNovasLinhas = 0
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
                102: self.estado_102,
                103: self.estado_103,
                104: self.estado_104,
                105: self.estado_105,
                106: self.estado_106,
                107: self.estado_107,
                108: self.estado_108,
                109: self.estado_109,
                110: self.estado_110,
                111: self.estado_111,
                112: self.estado_112,
                113: self.estado_113,
                114: self.estado_114,
                115: self.estado_115,
                116: self.estado_116,
                117: self.estado_117,
                118: self.estado_118,
                119: self.estado_119,
                120: self.estado_120,
                121: self.estado_121,
                122: self.estado_122,
                123: self.estado_123,
                124: self.estado_124,
                125: self.estado_125,
                126: self.estado_126,
                127: self.estado_127,
                128: self.estado_128,
                129: self.estado_129,
                130: self.estado_130,
                131: self.estado_131,
                132: self.estado_132,
                133: self.estado_133,
                134: self.estado_134,
                135: self.estado_135,
                136: self.estado_136,
                137: self.estado_137,
                138: self.estado_138,
                139: self.estado_139,
            }
            switch_case.get(self.estadoAtual, self.padrao)()
            self.contador+=1
        while(len(self.pilhaTab) > 1):
            self.listaTokens.append(('dedent', None))
            self.pilhaTab.pop()
        self.listaTokens.append(('$', None))
           

    #caso de nao haver o estado chamado, só para a fase de testes
    def padrao(self):
        print('estado {self.estadoAtual} nao encontrado')
        
    #INICIAL q0
    def estado_0(self):
        print('entra estado 0')
        expressaoLetrasEstado0 = r"a|g|h|i|j|k|l|m|q|u|w|x|y|z|ç|_|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|V|W|X|Y|Z|Ç"
        
        #letras que nao são de variaveis
        if re.match(expressaoLetrasEstado0, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual

        #digitos
        elif re.match(self.expressaoDigito, self.caracterAtual):
            self.estadoAtual = 100
            self.lexema += self.caracterAtual
        # b de `boleano`

        elif self.caracterAtual == 'b':
            self.estadoAtual = 54
            self.lexema += self.caracterAtual
        # c de `continua`
        elif self.caracterAtual == 'c':
            self.estadoAtual = 26
            self.lexema += self.caracterAtual
        # d de `de`
        elif self.caracterAtual == 'd':
            self.estadoAtual = 51
            self.lexema += self.caracterAtual
        # e de `enquanto` ou 'e'
        elif self.caracterAtual == 'e':
            self.estadoAtual = 62
            self.lexema += self.caracterAtual
        # f de `funcao` ou `falso`
        elif self.caracterAtual == 'f':
            self.estadoAtual = 1
            self.lexema += self.caracterAtual
        # n de `nulo` ou 'nao'
        elif self.caracterAtual == 'n':
            self.estadoAtual = 13
            self.lexema += self.caracterAtual
        # s de `se`, `senao` ou `senaose`
        elif self.caracterAtual == 's':
            self.estadoAtual = 41
            self.lexema += self.caracterAtual
        # t de `texto`
        elif self.caracterAtual == 't':
            self.estadoAtual = 72
            self.lexema = self.caracterAtual
        # p de `para` ou `passa`
        elif self.caracterAtual == 'p':
            self.estadoAtual = 89
            self.lexema += self.caracterAtual
        # o de 'ou'
        elif self.caracterAtual == 'o':
            self.estadoAtual = 78
            self.lexema += self.caracterAtual
        # r de `retorna` ou `real`
        elif self.caracterAtual == 'r':
            self.estadoAtual = 81
            self.lexema += self.caracterAtual
        # v de `verdade`
        elif self.caracterAtual == 'v':
            self.estadoAtual = 18
            self.lexema += self.caracterAtual
        # Operador aritmético '+' ou  de atribuição '+='
        elif self.caracterAtual == '+':
            self.estadoAtual = 107
            self.lexema += self.caracterAtual
        # Operador aritmético '-' ou atribuição '-='
        elif self.caracterAtual == '-':
            self.estadoAtual = 110
            self.lexema += self.caracterAtual
        # Operador aritmético *
        elif self.caracterAtual == '*':
            self.estadoAtual = 113
            self.estado_113()
        # Operador aritmético /
        elif self.caracterAtual == '/':
            self.estadoAtual = 114
            self.estado_114()
        # Operador de atribuição '=' ou comparação '=='
        elif self.caracterAtual == '=':
            self.estadoAtual = 115
            self.lexema = self.caracterAtual
        # Operador de comparação '!='
        elif self.caracterAtual == '!':
            self.estadoAtual = 118
            self.lexema = self.caracterAtual
        # Operador de comparação '>' ou '>='
        elif self.caracterAtual == '>':
            self.estadoAtual = 121
            self.lexema = self.caracterAtual
        # Operador de comparação '<' ou '<='
        elif self.caracterAtual == '<':
            self.estadoAtual = 124
            self.lexema = self.caracterAtual
        # abre parenteses
        elif self.caracterAtual == '(':
            self.estadoAtual = 127
            self.estado_127()
        # fecha parenteses
        elif self.caracterAtual == ')':
            self.estadoAtual = 128
            self.estado_128()
        # abre colchetes
        elif self.caracterAtual == '[':
            self.estadoAtual = 129
            self.estado_129()
        # fecha colchetes
        elif self.caracterAtual == ']':
            self.estadoAtual = 130
            self.estado_130()
        # abre chaves
        elif self.caracterAtual == '{':
            self.estadoAtual = 131
            self.estado_131()
        # fecha chaves
        elif self.caracterAtual == '}':
            self.estadoAtual = 132
            self.estado_132()
        # dois pontos para fim de funções
        elif self.caracterAtual == ':':
            self.estadoAtual = 133
            self.estado_133()
        # virgula para divisor de atributos
        elif self.caracterAtual == ',':
            self.estadoAtual = 134
            self.estado_134()
        # hashtag para comentarios
        elif self.caracterAtual == '#':
            self.estadoAtual = 135
            self.estado_135()
        # aspas simples para abrir e fechar textos
        elif self.caracterAtual == '\'':
            self.estadoAtual = 136
            self.estado_136()
        # espaço para finalizar os lexemas
        elif self.caracterAtual == ' ':
            pass
            # self.estadoAtual = 137
            # self.estado_137()
        # tabulação para organizar as hierarquias
        elif self.caracterAtual == '\t':
            pass
            # self.estadoAtual = 138
            # self.estado_138()
        # quebra de linha para organizar as linhas
        elif self.caracterAtual == '\n':
            self.estadoAtual = 139

    #FUNCAO | FALSO - (q0 --> q1 --> q2 | q8 | q98 | q99)
    def estado_1(self):
        print('entra estado 1')
        if self.caracterAtual == 'u':
            self.estadoAtual = 2
            self.lexema += self.caracterAtual
        elif self.caracterAtual == 'a':
            self.estadoAtual = 8
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()
      
    #FUNCAO - (q1 --> q2 --> q3 | q98 | q99)
    def estado_2(self):
        print('entra estado 2')
        if self.caracterAtual == 'n':
            self.estadoAtual = 3
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()
        
    #FUNCAO - (q2 --> q3 --> q4 | q98 | q99)
    def estado_3(self):
        print('entra estado 3')
        if self.caracterAtual == 'c':
            self.estadoAtual = 4
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #FUNCAO - (q3 --> q4 --> q5 | q98 | q99)
    def estado_4(self):
        print('entra estado 4')
        if self.caracterAtual == 'a':
            self.estadoAtual = 5
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #FUNCAO - (q4 --> q5 --> q6 | q98 | q99)
    def estado_5(self):
        print('entra estado 5')
        if self.caracterAtual == 'o':
            self.estadoAtual = 6
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #FUNCAO - (q5 --> q6 --> q7 | q98)
    def estado_6(self):
        print('entra estado 6')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 7
            self.estado_7()

    #FUNCAO FINAL- (q6 --> q7 --> q0) 
    def estado_7(self):
        print('entra estado 7')
        self.listaTokens.append(('funcao', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #FALSO - (q1 --> q8 --> q9 | q98 | q99)
    def estado_8(self):
        print('entra estado 8')
        if self.caracterAtual == 'l':
            self.estadoAtual = 9
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #FALSO - (q8 --> q9 --> q10 | q98 | q99)
    def estado_9(self):
        print('entra estado 9')
        if self.caracterAtual == 's':
            self.estadoAtual = 10
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #FALSO - (q9 --> q10 --> q11 | q98 | q99)
    def estado_10(self):
        print('entra estado 10')
        if self.caracterAtual == 'o':
            self.estadoAtual = 11
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #FALSO - (q10 --> q11 --> q12 | q98)
    def estado_11(self):
        print('entra estado 11')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 12
            self.estado_12()

    #FALSO FINAL- (q10 --> q11 --> q12 | q98) 
    def estado_12(self):
        print('entra estado 12')
        self.listaTokens.append(('falso', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #NULO - (q0 --> q13 --> q14 | q98 | q99)
    def estado_13(self):
        print('entra estado 13')
        if self.caracterAtual == 'u':
            self.estadoAtual = 14
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #NULO - (q13 --> q14 --> q15 | q98 | q99)
    def estado_14(self):
        print('entra estado 14')
        if self.caracterAtual == 'l':
            self.estadoAtual = 15
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #NULO - (q14 --> q15 --> q16 | q98 | q99)
    def estado_15(self):
        print('entra estado 15')
        if self.caracterAtual == 'o':
            self.estadoAtual = 16
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #NULO - (q15 --> q16 --> q17 | q98)
    def estado_16(self):
        print('entra estado 16')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 17
            self.estado_17()

    #NULO FINAL- (q16 --> q17 --> q0)
    def estado_17(self):
        print('entra estado 17')
        self.listaTokens.append(('nulo', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador -=1

    #VERDADE - (q0 --> q18 --> q19 | q98 | q99)
    def estado_18(self):
        print('entra estado 18')
        if self.caracterAtual == 'e':
            self.estadoAtual = 19
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #VERDADE - (q18 --> q19 --> q20 | q98 | q99)
    def estado_19(self):
        print('entra estado 19')
        if self.caracterAtual == 'r':
            self.estadoAtual = 20
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #VERDADE - (q19 --> q20 --> q21 | q98 | q99)
    def estado_20(self):
        print('entra estado 20')
        if self.caracterAtual == 'd':
            self.estadoAtual = 21
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #VERDADE - (q20 --> q21 --> q22 | q98 | q99)
    def estado_21(self):
        print('entra estado 21')
        if self.caracterAtual == 'a':
            self.estadoAtual = 22
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #VERDADE - (q21 --> q22 --> q23 | q98 | q99)
    def estado_22(self):
        print('entra estado 22')
        if self.caracterAtual == 'd':
            self.estadoAtual = 23
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #VERDADE - (q22 --> q23 --> q24 | q98 | q99)
    def estado_23(self):
        print('entra estado 23')
        if self.caracterAtual == 'e':
            self.estadoAtual = 24
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #VERDADE - (q23 --> q24 --> q25 | q98)
    def estado_24(self):
        print('entra estado 24')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 25
            self.estado_25()

    #VERDADE FINAL - (q24 --> q25 --> q0)
    def estado_25(self):
        print('entra estado 25')
        self.listaTokens.append(('verdade', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -=1

    #CLASSE | CONTINUA - (q0 --> q26 --> q27 | q33 | q98 | q99)
    def estado_26(self):
        print('entra estado 26')
        if self.caracterAtual == 'l':
            self.estadoAtual = 27
            self.lexema += self.caracterAtual
        elif self.caracterAtual == 'o':
            self.estadoAtual = 33
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CLASSE - (q26 --> q27 --> q28 | q98 | q99)
    def estado_27(self):
        print('entra estado 27')
        if self.caracterAtual == 'a':
            self.estadoAtual = 28
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CLASSE - (q27 --> q28 --> q29 | q98 | q99)
    def estado_28(self):
        print('entra estado 28')
        if self.caracterAtual == 's':
            self.estadoAtual = 29
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CLASSE - (q28 --> q29 --> q30 | q98 | q99)
    def estado_29(self):
        print('entra estado 29')
        if self.caracterAtual == 's':
            self.estadoAtual = 30
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CLASSE - (q29 --> q30 --> q31 | q98 | q99)
    def estado_30(self):
        print('entra estado 30')
        if self.caracterAtual == 'e':
            self.estadoAtual = 31
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CLASSE - (q30 --> q31 --> q32 | q98)
    def estado_31(self):
        print('entra estado 31')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 32
            self.estado_32()

    #CLASSE FINAL - (q31 --> q32 --> q0)
    def estado_32(self):
        print('entra estado 32')
        self.listaTokens.append(('classe', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #CONTINUA - (q26 --> q33 --> q34 | q98 | q99)
    def estado_33(self):
        print('entra estado 33')
        if self.caracterAtual == 'n':
            self.estadoAtual = 34
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CONTINUA - (q33 --> q34 --> q35 | q98 | q99)
    def estado_34(self):
        print('entra estado 34')
        if self.caracterAtual == 't':
            self.estadoAtual = 35
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CONTINUA - (q34 --> q35 --> q36 | q98 | q99)
    def estado_35(self):
        print('entra estado 35')
        if self.caracterAtual == 'i':
            self.estadoAtual = 36
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CONTINUA - (q35 --> q36 --> q37 | q98 | q99)
    def estado_36(self):
        print('entra estado 36')
        if self.caracterAtual == 'n':
            self.estadoAtual = 37
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CONTINUA - (q36 --> q37 --> q38 | q98 | q99)
    def estado_37(self):
        print('entra estado 37')
        if self.caracterAtual == 'u':
            self.estadoAtual = 38
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CONTINUA - (q37 --> q38 --> q39 | q98 | q99)
    def estado_38(self):
        print('entra estado 38')
        if self.caracterAtual == 'a':
            self.estadoAtual = 39
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #CONTINUA - (q38 --> q39 --> q40 | q98)
    def estado_39(self):
        print('entra estado 39')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 40
            self.estado_40()

    #CONTINUA FINAL - (q39 --> q40 --> q0)
    def estado_40(self):
        print('entra estado 40')
        self.listaTokens.append(('continua', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #SE | SENAO | SENAOSE - (q0 --> q41 --> q42 | q98 | q99)
    def estado_41(self):
        print('entra estado 41')
        if self.caracterAtual == 'e':
            self.estadoAtual = 42
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #SE | SENAO | SENAOSE - (q41 --> q42 --> q43 | q44 | q98)
    def estado_42(self):
        print('entra estado 42')
        if self.caracterAtual == 'n':
            self.estadoAtual = 44
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 43
            self.estado_43()

    #SE FINAL - (q42 --> q43 --> q0)
    def estado_43(self):
        print('entra estado 43')
        self.listaTokens.append(('se', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #SENAO | SENAOSE - (q42 --> q44 --> q45 | q98 | q99)
    def estado_44(self):
        print('entra estado 44')
        if self.caracterAtual == 'a':
            self.estadoAtual = 45
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #SENAO | SENAOSE - (q44 --> q45 --> q46 | q98 | q99)
    def estado_45(self):
        print('entra estado 45')
        if self.caracterAtual == 'o':
            self.estadoAtual = 46
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #SENAO | SENAOSE - (q45 --> q46 --> q47 | q48 | q98)
    def estado_46(self):
        print('entra estado 46')
        if self.caracterAtual == 's':
            self.estadoAtual = 48
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 47
            self.estado_47()

    #SENAO FINAL - (q46 --> q47 --> q0)
    def estado_47(self):
        print('entra estado 47')
        self.listaTokens.append(('senao', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #SENAOSE - (q46 --> q48 --> q49 | q98 | q99)
    def estado_48(self):
        print('entra estado 48')
        if self.caracterAtual == 'e':
            self.estadoAtual = 49
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #SENAOSE - (q48 --> q49 --> q50 | q98)
    def estado_49(self):
        print('entra estado 49')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 50
            self.estado_50()

    #SENAOSE FINAL - (q49 --> q50 --> q0)
    def estado_50(self):
        print('entra estado 50')
        self.listaTokens.append(('senaose', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #DE - (q0 --> q51 --> q52 | q98 | q99)
    def estado_51(self):
        print('entra estado 51')
        if self.caracterAtual == 'e':
            self.estadoAtual = 52
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #DE - (q51 --> q52 --> q53 | q98)
    def estado_52(self):
        print('entra estado 52')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 53
            self.estado_53()

    #DE FINAL - (q52 --> q53 --> q0)
    def estado_53(self):
        print('entra estado 53')
        self.listaTokens.append(('de', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #BOLEANO - (q0 --> q54 --> q55 | q98 | q99)
    def estado_54(self):
        print('entra estado 54')
        if self.caracterAtual == 'o':
            self.estadoAtual = 55
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #BOLEANO - (q54 --> q55 --> q56 | q98 | q99)
    def estado_55(self):
        print('entra estado 55')
        if self.caracterAtual == 'l':
            self.estadoAtual = 56
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #BOLEANO - (q55 --> q56 --> q57 | q98 | q99)
    def estado_56(self):
        print('entra estado 56')
        if self.caracterAtual == 'e':
            self.estadoAtual = 57
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #BOLEANO - (q56 --> q57 --> q58 | q98 | q99)
    def estado_57(self):
        print('entra estado 57')
        if self.caracterAtual == 'a':
            self.estadoAtual = 58
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #BOLEANO - (q57 --> q58 --> q59 | q98 | q99)
    def estado_58(self):
        print('entra estado 58')
        if self.caracterAtual == 'n':
            self.estadoAtual = 59
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #BOLEANO - (q58 --> q59 --> q60 | q98 | q99)
    def estado_59(self):
        print('entra estado 59')
        if self.caracterAtual == 'o':
            self.estadoAtual = 60
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #BOLEANO - (q59 --> q60 --> q61 | q98)
    def estado_60(self):
        print('entra estado 60')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 61
            self.estado_61()

    #BOLEANO FINAL - (q60 --> q61 --> q0)
    def estado_61(self):
        print('entra estado 61')
        self.listaTokens.append(('boleano', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #ENQUANTO | E - (q0 --> q62 --> q63 | q64 | q98)
    def estado_62(self):
        print('entra estado 62')
        if self.caracterAtual == 'n':
            self.estadoAtual = 64
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 63
            self.estado_63()

    #E FINAL - (Q62 --> q63 --> q0)
    def estado_63(self):
        print('entra estado 63')
        self.listaTokens.append(('e', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #ENQUANTO - (q62 --> q64 --> q65 | q98 | q99)
    def estado_64(self):
        print('entra estado 64')
        if self.caracterAtual == 'q':
            self.estadoAtual = 65
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #ENQUANTO - (q64 --> q65 --> q66 | q98 | q99)
    def estado_65(self):
        print('entra estado 65')
        if self.caracterAtual == 'u':
            self.estadoAtual = 66
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #ENQUANTO - (q65 --> q66 --> q67 | q98 | q99)
    def estado_66(self):
        print('entra estado 66')
        if self.caracterAtual == 'a':
            self.estadoAtual = 67
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #ENQUANTO - (q66 --> q67 --> q68 | q98 | q99)
    def estado_67(self):
        print('entra estado 67')
        if self.caracterAtual == 'n':
            self.estadoAtual = 68
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #ENQUANTO - (q67 --> q68 --> q69 | q98 | q99)
    def estado_68(self):
        print('entra estado 68')
        if self.caracterAtual == 't':
            self.estadoAtual = 69
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #ENQUANTO - (q68 --> q69 --> q70 | q98 | q99)
    def estado_69(self):
        print('entra estado 69')
        if self.caracterAtual == 'o':
            self.estadoAtual = 70
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #ENQUANTO - (q69 --> q70 --> q71 | q98)
    def estado_70(self):
        print('entra estado 70')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 71
            self.estado_71()
    
    #ENQUANTO FINAL- (q70 --> q71 --> q0)
    def estado_71(self):
        print('entra estado 71')
        self.listaTokens.append(('enquanto', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #TEXTO - (q0 --> q72 --> q73 | q98 | q99)
    def estado_72(self):
        print('entra estado 72')
        if self.caracterAtual == 'e':
            self.estadoAtual = 73
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #TEXTO - (q72 --> q73 --> q74 | q98 | q99)
    def estado_73(self):
        print('entra estado 73')
        if self.caracterAtual == 'x':
            self.estadoAtual = 74
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #TEXTO - (q73 --> q74 --> q75 | q98 | q99)
    def estado_74(self):
        print('entra estado 74')
        if self.caracterAtual == 't':
            self.estadoAtual = 75
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #TEXTO - (q74 --> q75 --> q76 | q98 | q99)
    def estado_75(self):
        print('entra estado 75')
        if self.caracterAtual == 'o':
            self.estadoAtual = 76
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #TEXTO - (q75 --> q76 --> q77 | q98)
    def estado_76(self):
        print('entra estado 76')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 77
            self.estado_77()

    #TEXTO FINAL - (q76 --> q77 --> q0)
    def estado_77(self):
        print('entra estado 77')
        self.listaTokens.append(('texto', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #OU - (q0 --> q78 --> q79 | q98 | q99)
    def estado_78(self):
        print('entra estado 78')
        if self.caracterAtual == 'u':
            self.estadoAtual = 79
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #OU - (q78 --> q79 --> q80 | q98)
    def estado_79(self):
        print('entra estado 79')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 80
            self.estado_80()

    #OU FINAL- (q79 --> q80 --> q0)
    def estado_80(self):
        print('entra estado 80')
        self.listaTokens.append(('ou', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #RETORNA - (q0 --> q81 --> q82 | q98 | q99) 
    def estado_81(self):
        print('entra estado 81')
        if self.caracterAtual == 'e':
            self.estadoAtual = 82
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #RETORNA - (q81 --> q82 --> q83 | q98 | q99) 
    def estado_82(self):
        print('entra estado 82')
        if self.caracterAtual == 't':
            self.estadoAtual = 83
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #RETORNA - (q82 --> q83 --> q84 | q98 | q99) 
    def estado_83(self):
        print('entra estado 84')
        if self.caracterAtual == 'o':
            self.estadoAtual = 84
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #RETORNA - (q83 --> q84 --> q85 | q98 | q99)
    def estado_84(self):
        print('entra estado 84')
        if self.caracterAtual == 'r':
            self.estadoAtual = 85
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #RETORNA - (q84 --> q85 --> q86 | q98 | q99)
    def estado_85(self):
        print('entra estado 85')
        if self.caracterAtual == 'n':
            self.estadoAtual = 86
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #RETORNA - (q85 --> q86 --> q87 | q98 | q99)
    def estado_86(self):
        print('entra estado 86')
        if self.caracterAtual == 'a':
            self.estadoAtual = 87
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #RETORNA - (q86 --> q87 --> q88 | q98)
    def estado_87(self):
        print('entra estado 87')
        print(re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual))
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 88
            self.estado_88()

    #RETORNA FINAL - (q87 --> q88 --> q0)
    def estado_88(self):
        print('entra estado 88')
        self.listaTokens.append(('retorna', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #PARA | PASSA - (q0 --> q89 --> q90 | q98 | q99)
    def estado_89(self):
        print('entra estado 89')
        if self.caracterAtual == 'a':
            self.estadoAtual = 90
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #PARA | PASSA - (q89 --> q90 --> q91 | q94 | q98 | q99)
    def estado_90(self):
        print('entra estado 90')
        if self.caracterAtual == 'r':
            self.estadoAtual = 91
            self.lexema += self.caracterAtual
        elif self.caracterAtual == 's':
            self.estadoAtual = 94
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #PARA - (q90 --> q91 --> q92 | q98 | q99)
    def estado_91(self):
        print('entra estado 91')
        if self.caracterAtual == 'a':
            self.estadoAtual = 92
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #PARA - (q91 --> q92 --> q93 | q98)
    def estado_92(self):
        print('entra estado 92')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 93
            self.estado_93()

    #PARA FINAL - (q92 --> q93 --> q0)
    def estado_93(self):
        print('entra estado 93')
        self.listaTokens.append(('para', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #PASSA- (q90 --> q94 --> q95 | q98 | q99)
    def estado_94(self):
        print('entra estado 94')
        if self.caracterAtual == 's':
            self.estadoAtual = 95
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #PASSA- (q94 --> q95 --> q96 | q98 | q99)
    def estado_95(self):
        print('entra estado 95')
        if self.caracterAtual == 'a':
            self.estadoAtual = 96
            self.lexema += self.caracterAtual
        elif re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 99
            self.estado_99()

    #PASSA - (q95 --> q96 --> q97 | q98)
    def estado_96(self):
        print('entra estado 96')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            self.estadoAtual = 98
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 97
            self.estado_97()

    #PASSA FINAL - (q96 --> q97 -->q0)
    def estado_97(self):
        print('entra estado 97')
        self.listaTokens.append(('passa', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #IDENTIFICADORES - (q0 --> q98 --> q98 | q99)
    def estado_98(self):
        print('entra estado 98')
        if re.match(self.expressaoLetrasAndDigitosAndUnderline, self.caracterAtual):
            #Mantém no estado atual
            self.lexema += self.caracterAtual
        #vai para estado final, reconhecendo um IDENTIFICADOR como lexema
        else:
            self.estadoAtual = 99
            self.estado_99()

    #IDENTIFICADORES FINAL - (q98 --> q99 --> q0)
    def estado_99(self):
        print('entra estado 99')
        if self.lexema not in self.tabelaSimbolos:
            self.listaTokens.append(('id', len(self.tabelaSimbolos)))
            self.tabelaSimbolos.append(self.lexema)
        else:
            indice = self.tabelaSimbolos.index(self.lexema)
            self.listaTokens.append(('id', indice))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #NUMERO INTEIRO | NUMERO REAL - (q0 --> q100 --> q100 | q96)
    def estado_100(self):
        print('entra estado 100')
        if re.match(self.expressaoDigito, self.caracterAtual):
            # estado continua no 100
            self.lexema += self.caracterAtual
        elif self.caracterAtual == '.':
            self.estadoAtual = 102
            self.lexema += self.caracterAtual
        else:
            self.estadoAtual = 101
            self.estado_101()

    #NUMERO INTEIRO FINAL- (q100 --> q101 --> q0)
    def estado_101(self):
        print('entra no estado 101')
        self.listaTokens.append(('num_inteiro', self.lexema))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #NUMERO REAL - (q101 --> q102 --> q103 | q104) 
    def estado_102(self):
        print('entra no 102')
        if re.match(self.expressaoDigito, self.caracterAtual):
            self.estadoAtual = 104
            self.lexema += self.caracterAtual
        else:
            #Vai para o ERRO 103, que nao pode ter outra coisa, alem de numeros depois do ponto
            self.lexema += self.caracterAtual
            self.estadoAtual = 103
            self.estado_103()

    #NUMERO REAL ERRO - (q102 --> q103) (quando é digitado outra coisa depois do ponto de numero flutuante, Ex: 22.a)
    def estado_103(self):
        print('entra no estado 103')
        print('ERRO, no numero real '+ self.lexema +' --> Depois do ".", tem de vir um digito ')
        self.variavelControle = False

    #NUMERO REAL - (q102 --> q104 --> q104 | q105 | q106)
    def estado_104(self):
        print('entra no 104')
        if re.match(self.expressaoDigito, self.caracterAtual):
            # Mantem no estado 104
            self.lexema += self.caracterAtual

        elif self.caracterAtual == '.':
            #Vai para estado de erro 105
            self.lexema += self.caracterAtual
            self.estadoAtual = 105
            self.estado_105()

        else:
            #Vai para o estado final do NUMERO REAL 106
            self.estadoAtual = 106
            self.estado_106()

    #NUMERO REAL ERRO - (q104 --> q105) - (quando é digitado um ponto('.'), após um numero real, Ex: 22.22.)
    def estado_105(self):
        print('entra no estado 105')
        print('ERRO, no numero real '+ self.lexema + ' --> Depois do numero real nao podem vir pontos')
        self.variavelControle = False
    
    #NUMERO REAL FINAL - (q104 --> q106 --> q0)
    def estado_106(self):
        print('entra no estado 106')
        self.listaTokens.append(('num_real', self.lexema))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador-=1

    #+ | +=    (q0 --> q107 --> q108 | q109)
    def estado_107(self):
        print('entra no estado 107')
        if(self.caracterAtual == '='):
            self.estadoAtual = 109
            self.lexema += self.caracterAtual
            self.estado_109()
        else:
            self.estadoAtual = 108
            self.estado_108()

    #+ FINAL - (q107 --> q108 --> q0)
    def estado_108(self):
        print('entra no estado 108')
        self.listaTokens.append(('+', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #+= FINAL - (q0 --> 107 --> 108 | 109)
    def estado_109(self):
        print('entra no estado 109')
        self.listaTokens.append(('+=', None))
        
        self.lexema = ''
        self.estadoAtual = 0

    #- | -=    (q0 --> q110 --> q111 | q112)
    def estado_110(self):
        print('entra no estado 110')
        if(self.caracterAtual == '='):
            self.estadoAtual = 112
            self.lexema += self.caracterAtual
            self.estado_112()
        else:
            self.estadoAtual = 111
            self.estado_111()

    #- FINAL - (q110 --> q111 --> q0)
    def estado_111(self):
        print('entra no estado 111')
        self.listaTokens.append(('-', None))

        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #-= FINAL - (q110 --> q112 --> q0)
    def estado_112(self):
        print('entra no estado 112')
        self.listaTokens.append(('-=', None))
        
        self.lexema = ''
        self.estadoAtual = 0

    #* FINAL - (q0 --> q113 --> q0)
    def estado_113(self):
        print('entra no estado 113')
        self.listaTokens.append(('*', None))
        
        self.estadoAtual = 0
        
    #/ FINAL - (q0 --> q114 --> q0)
    def estado_114(self):
        print('entra no estado 114')
        self.listaTokens.append(('/', None))
        
        self.estadoAtual = 0

    #= | ==   (q0 --> q115 --> q116 | q117)
    def estado_115(self):
        print('entra no estado 115')
        if(self.caracterAtual == '='):
            self.estadoAtual = 117
            self.lexema += self.caracterAtual
            self.estado_117()
        else:
            self.estadoAtual = 116
            self.estado_116()

    #= FINAL - (q115 --> q116 --> q0)
    def estado_116(self):
        print('entra no estado 116')
        self.listaTokens.append(('=', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1
        
    #== FINAL - (q115 --> q117 --> q0)
    def estado_117(self):
        print('entra no estado 117')
        self.listaTokens.append(('==', None))
        
        self.lexema = ''
        self.estadoAtual = 0 

    #! | !=  -  (q0 --> q118 --> q119 | q120)
    def estado_118(self):
        print('entra no estado 118')
        if(self.caracterAtual == '='):
            self.estadoAtual = 120
            self.lexema += self.caracterAtual
            self.estado_120()
        else:
            self.estadoAtual = 119
            self.estado_119()

        #= FINAL - (q115 --> q116 --> q0)
    
    #! FINAL - (q118 --> q119 --> q0)
    def estado_119(self):
        print('entra no estado 119')
        self.listaTokens.append(('!', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1
        
    #!= FINAL - (q118 --> q120 --> q0)
    def estado_120(self):
        print('entra no estado 120')
        self.listaTokens.append(('!=', None))
        
        self.lexema = ''
        self.estadoAtual = 0 

    #> | >=  -  (q0 --> q121 --> q122 | q123)
    def estado_121(self):
        print('entra no estado 121')
        if(self.caracterAtual == '='):
            self.estadoAtual = 123
            self.lexema += self.caracterAtual
            self.estado_123()
        else:
            self.estadoAtual = 122
            self.estado_122()

    #> FINAL - (q121 --> q122 --> q0)
    def estado_122(self):
        print('entra no estado 122')
        self.listaTokens.append(('>', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #>= FINAL - (q121 --> q123 --> q0)
    def estado_123(self):
        print('entra no estado 123')
        self.listaTokens.append(('>=', None))
        
        self.lexema = ''
        self.estadoAtual = 0

    #< | <=  -  (q0 --> q124 --> q125 | q126)
    def estado_124(self):
        print('entra no estado 124')
        if(self.caracterAtual == '='):
            self.estadoAtual = 126
            self.lexema += self.caracterAtual
            self.estado_126()
        else:
            self.estadoAtual = 125
            self.estado_125()

    #< FINAL - (q124 --> q125 --> q0)
    def estado_125(self):
        print('entra no estado 125')
        self.listaTokens.append(('<', None))
        
        self.lexema = ''
        self.estadoAtual = 0
        self.contador -= 1

    #<= FINAL - (q124 --> q126 --> q0)
    def estado_126(self):
        print('entra no estado 126')
        self.listaTokens.append(('<=', None))
        
        self.lexema = ''
        self.estadoAtual = 0

    #( FINAL  -  (q0 --> q127 --> q0)
    def estado_127(self):
        print('entra no estado 127')
        self.listaTokens.append(('(', None))

        self.estadoAtual = 0

    #) FINAL  -  (q0 --> q128 --> q0)
    def estado_128(self):
        print('entra no estado 128')
        self.listaTokens.append((')', None))

        self.estadoAtual = 0

    #[ FINAL  -  (q0 --> q129 --> q0)
    def estado_129(self):
        print('entra no estado 129')
        self.listaTokens.append(('[', None))

        self.estadoAtual = 0

    #] FINAL  -  (q0 --> q130 --> q0)
    def estado_130(self):
        print('entra no estado 130')
        self.listaTokens.append((']', None))

        self.estadoAtual = 0

    #{ FINAL  -  (q0 --> q131 --> q0)
    def estado_131(self):
        print('entra no estado 131')
        self.listaTokens.append(('{', None))

        self.estadoAtual = 0

    #} FINAL  -  (q0 --> q132 --> q0)
    def estado_132(self):
        print('entra no estado 132')
        self.listaTokens.append(('}', None))

        self.estadoAtual = 0

    #: FINAL  -  (q0 --> q133 --> q0)
    def estado_133(self):
        print('entra no estado 133')
        self.listaTokens.append((':', None))

        self.estadoAtual = 0

    #, FINAL  -  (q0 --> q134 --> q0)
    def estado_134(self):
        print('entra no estado 134')
        self.listaTokens.append((',', None))

        self.estadoAtual = 0

    ## FINAL  -  (q0 --> q135 --> q0)
    def estado_135(self):
        print('entra no estado 135')
        self.listaTokens.append(('#', None))

        self.estadoAtual = 0

    #' FINAL  -  (q0 --> q136 --> q0)
    def estado_136(self):
        print('entra no estado 136')
        self.listaTokens.append(('aspas', None))

        self.estadoAtual = 0

    #IDENTAÇÃO  -  (q0 --> q137 --> q0)
    def estado_137(self):
        print('entra no estado 137')
        if(self.caracterAtual == ' '):
            self.nivelIndetacao += 1
            self.estadoAtual = 137
        elif(self.caracterAtual == '\t'):
            self.nivelIndetacao += 4
            self.estadoAtual = 137
        elif(self.caracterAtual == '\n'):
            self.nivelIndetacao = 0
            self.estadoAtual = 139
        else:
            self.estadoAtual = 138
            self.estado_138()
            
    #IDENTAÇÃO  -  (q0 --> q138 --> q0)
    def estado_138(self):
        print('entra no estado 138')
        if(self.pilhaTab[-1] < self.nivelIndetacao):
            self.pilhaTab.append(self.nivelIndetacao)
            for i in range(self.contadorNovasLinhas):
                self.listaTokens.append(('novalinha', None))
            self.listaTokens.append(('indent', None))
        elif(self.pilhaTab[-1] > self.nivelIndetacao):
            while(self.pilhaTab[-1] > self.nivelIndetacao):
                self.listaTokens.append(('dedent', None))
                self.pilhaTab.pop()
            for i in range(self.contadorNovasLinhas):
                self.listaTokens.append(('novalinha', None))
        else:
            for i in range(self.contadorNovasLinhas):
                self.listaTokens.append(('novalinha', None))
        self.nivelIndetacao = 0
        self.lexema = ''
        self.contadorNovasLinhas = 0
        self.estadoAtual = 0
        self.estado_0()

    #\n FINAL  -  (q0 --> q139 --> q0)
    def estado_139(self):
        print('entra no estado 139')
        self.contadorNovasLinhas += 1
        if(self.caracterAtual == '\n'):
            self.estadoAtual = 139
        elif(self.caracterAtual == ' ' or self.caracterAtual == '\t'):
            self.estadoAtual = 137
            self.estado_137()
        else:
            self.estadoAtual = 138
            self.estado_138()


# print('Digite o código. Para compilar digite Ctrl+Z')
# codigo = sys.stdin.read()
# x = Lexer(codigo) 
# x.getToken()
# print(x.listaTokens)
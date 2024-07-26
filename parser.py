from lexer import Lexer;
from collections import deque;
import sys;

class Parser:
    def __init__(self):
        self.tab = 0,
        self.listaTokens = [],
        self.tabelaSimb = [],
        self.pilha = deque()
        self.pilha.append('PROGRAMA')

    def getListaTokenAndTabSimb(self, trechoCodigo):
        lexer = Lexer(trechoCodigo)
        lexer.getToken()
        self.tabelaSimb = lexer.tabelaSimbolos
        self.listaTokens = lexer.listaTokens
        self.tokenAtual = self.listaTokens

    def achaTokenAtual(self):
        self.tokenAtual = self.listaTokens[0]

    def calculaTab(self):
        quantidadeTab = 0
        for car in self.listaTokens:
            if(car == 'TAB'):
                quantidadeTab += 1
            else:
                break

    def empilhaTab(self):
        i = 0
        for i in range(self.tab):
            self.pilha.append('TAB') 

    def deriva(self, derivacoes):
        self.pilha.pop()
        for derivacao in derivacoes:
            self.pilha.append(derivacao)

    def popTerminais(self):
        while self.tokenAtual == self.pilha[-1]:
            self.listaTokens.pop()
            self.pilha.pop()
            self.achaTokenAtual()

    def fazAnalise(self):
        while(len(self.pilha) != 0):
        # i = 0
        # for i in range(5):
            if len(self.listaTokens) == 0:
                print('ERRO')
                break

            self.popTerminais()
            switch_case = {
                'PROGRAMA' : self.programa,
                
                'BLOCO' : self.bloco,
                
                'BLOCOOBRIGATORIO' : self.blocoObrigatorio,
                
                'INSTRUCOES' : self.instrucoes,

                'INSTRUCAO' : self.instrucao,

                'CONDICIONAL' : self.condicional,

                'SENAO' : self.senao,

                'LEITURA' : self.leitura,

                'TERMOLEITURA' : self.termoLeitura,

                'NOVOTERMOLEITURA' : self.novoTermoLeitura,

                'DIMENSAO' : self.dimensao,

                'ESCRITA' : self.escrita,

                'TERMOESCRITA' : self.termoEscrita,
                
                'NOVOTERMOESCRITA' : self.novoTermoEscrita,
                
                'FUNCAO' : self.funcao,
                
                'PARAMETRO' : self.parametro,
                
                'PARAMETRO2' : self.parametro2,
                
                'ATRIBUICAO' : self.atribuicao,
                
                'COMPLEMENTO' : self.complemento,
                
                'EXPRESSAO' : self.expressao,
                
                'EXPR_OU' : self.expr_ou,
                
                'EXPR_OU2' : self.expr_ou2,
                
                'EXPR_E' : self.expr_e,
                
                'EXPR_E2' : self.expr_e2,
                
                'EXPR_RELACIONAL' : self.expr_relacional,
                
                'EXPR_RELACIONAL2' : self.expr_relacional2,
                
                'OP_COMPARATIVO' : self.op_comparativo,
                
                'EXPR_ADITIVA' : self.expr_aditiva,
                
                'EXPR_ADITIVA2' : self.expr_aditiva2,
                
                'EXPR_MULTIPLICATIVA' : self.expr_multiplicativa,
                
                'EXPR_MULTIPLICATIVA2' : self.expr_multiplicativa2,
                
                'OP_MULTIPLICATIVO' : self.op_multiplicativo,
                
                'FATOR' : self.fator,
                
                'TERMO' : self.termo,
                
                'SINAL' : self.sinal,
                
                'CONSTANTE' : self.constante,
                
            }
            switch_case.get(self.pilha[-1], self.padrao)()

        if len(self.listaTokens) == 0:
            #SUCESSO
            print('SUCESSO')

    def padrao(self):
        print('LEXEMA {self.pilha[-1]} nao encontrado')

    def programa(self):
        print('entra em programa')
        if( self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'se' or 
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escreve' or 
        self.tokenAtual == 'id' or 
        self.tokenAtual == 'enquanto' or 
        self.tokenAtual == 'retorna' or 
        self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            self.deriva(['INSTRUCOES'])
        elif(self.tokenAtual == '$'):
            #SUCESSO
            print('Sucesso')

        else:
            #ERRO
            print('ERRO PROGRAMA: simbolo não permitido')
        
    def bloco(self):
        if self.tokenAtual == 'enter':
            self.listaTokens.pop()
            quantidadeTab = self.calculaTab
            ##VERIFICA EM QUAL NIVEL ESTÁ O BLOCO
            if quantidadeTab == self.tab:
                ## BLOCO --> enter {empilha na pilha 'tab' 'global.tab' vezes} INSTRUÇÕES
                self.empilhaTab
                self.deriva(['INSTRUCOES'])
            elif quantidadeTab < self.tab:
                ## BLOCO --> ε {global.tab -= 1}
                self.pilha.pop()
                self.tab -= 1
            else:
                #ERRO
                print('ERRO BLOCO quantTab > self.tab')
        else: 
            #ERRO
            print('ERRO BLOCO carcter diferente de ENTER')

    def blocoObrigatorio(self):
        if self.tokenAtual == 'enter':
            self.listaTokens.pop()
            self.empilhaTab
            self.deriva(['INSTRUCOES'])
        else: 
            #ERRO
            print('ERRO BLOCOOBRIGATORIO carcter diferente de ENTER')

    def instrucoes(self):
        print('entra em instruções')
        if( self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'se' or 
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escreve' or 
        self.tokenAtual == 'id' or 
        self.tokenAtual == 'enquanto' or 
        self.tokenAtual == 'retorna' or 
        self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            self.deriva(['BLOCO', 'INSTRUCAO'])

        else:
            #ERRO
            print('ERRO INSTRUCOES: símbolo não permitido')

    def instrucao(self):
        print('entra em instrução')
        if self.tokenAtual == 'se':
            print('entra no se')
            # INSTRUÇÃO --> CONDICIONAL
            self.deriva(['CONDICIONAL'])
        elif self.tokenAtual == 'ler':
            # INSTRUÇÃO --> LEITURA
            self.deriva(['LEITURA'])
        elif self.tokenAtual == 'escrever':
            # INSTRUÇÃO --> ESCRITA
            self.deriva(['ESCRITA'])
        elif self.tokenAtual == 'funcao':
            # INSTRUÇÃO --> FUNCAO
            self.deriva('FUNCAO')
        elif self.tokenAtual == 'id':
            # INSTRUÇÃO --> ATRIBUICAO
            self.deriva('ATRIBUICAO')
        elif self.tokenAtual == 'enquanto':
            # INSTRUÇÃO --> ENQUANTO
            self.deriva('ENQUANTO')
        elif self.tokenAtual == 'retorna':
            # INSTRUÇÃO --> RETORNO
            self.deriva('RETORNO')
        elif self.tokenAtual == '+':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.tokenAtual == '-':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.tokenAtual == 'num_inteiro':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.tokenAtual == 'num_real':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.tokenAtual == 'texto':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.tokenAtual == '!':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.tokenAtual == '(':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        else:
            #ERRO
            print('ERRO INSTRUCAO: simbolo nao reconhecido')

    def condicional(self):
        if(self.tokenAtual == 'se'):
            #CONDICIONAL --> se ( EXPRESSÃO ) : {global.tab += 1} BLOCOOBRIGATORIO SENAO
            self.deriva(['SENAO', 'BLOCOOBRIGATORIO', ':', ')', 'EXPRESSAO', '(', 'se'])
        else:
            #ERRO
            print('ERRO CONDICIONAL: símbolo não permitido')

    def senao(self):
        if(self.tokenAtual == 'senao'):
            #SENAO --> senao : BLOCOOBRIGATORIO
            self.deriva(['senao',':', 'BLOCOOBRIGATORIO'])
        elif(self.tokenAtual == 'enter'):
            #SENAO --> ε {global.tab -= 1}
            self.pilha.pop()
            self.tab -= 1
        else:
            #ERRO
            print('ERRO SENAO: símbolo não permitido')

    def leitura(self):
        if(self.tokenAtual == 'ler'):
            #LEITURA --> ler ( TERMOLEITURA NOVOTERMOLEITURA )
            self.deriva([')','NOVOTERMOLEITURA', 'TERMOLEITURA', '(', 'ler'])
        else:
            #ERRO
            print('ERRO LEITURA: simbolo nao reconhecido')

    def termoLeitura(self):
        if(self.tokenAtual == 'id'):
            #TERMOLEITURA --> id DIMENSAO
            self.deriva(['DIMENSAO', 'id'])
        else:
            #ERRO
            print('ERRO TERMOLEITURA: simbolo nao reconhecido')
    
    def novoTermoLeitura(self):
        if(self.tokenAtual == ','):
            #NOVOTERMOLEITURA --> , TERMOLEITURA NOVOTERMOLEITURA
            self.deriva(['NOVOTERMOLEITURA', 'TERMOLEITURA', ','])
        elif(self.tokenAtual == ')'):
            #NOVOTERMOLEITURA --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO NOVOTERMOLEITURA: simbolo nao reconhecido')

    def dimensao(self):
        if(self.tokenAtual == '['):
            #DIMENSAO --> [ EXPR_ADITIVA ] DIMENSAO
            self.deriva(['DIMENSAO', ']', 'EXPR_ADITIVA', '['])
        elif(self.tokenAtual == ')' or self.tokenAtual == ','):
            #DIMENSAO --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO DIMENSAO: simbolo nao reconhecido')

    def escrita(self):
        if(self.tokenAtual == 'escrever'):
            #LEITURA --> ler ( TERMOLEITURA NOVOTERMOLEITURA )
            self.deriva(')','NOVOTERMOESCRITA', 'TERMOESCRITA', '(', 'escrever')
        else:
            #ERRO
            print('ERRO ESCRITA: simbolo nao reconhecido')

    def termoEscrita(self):
        if(self.tokenAtual == 'id'):
            #TERMOESCRITA --> id DIMENSAO
            self.deriva(['DIMENSAO', 'id']) 
        elif(self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real'):
            #TERMOESCRITA --> CONSTANTE
            self.deriva(['CONSTANTE'])
        elif(self.tokenAtual == 'texto'):
            self.deriva(['texto'])
        else:
            #ERRO
            print('ERRO TERMOESCRITA: simbolo não reconhecido')

    def novoTermoEscrita(self):
        #NOVOTERMOESCRITA --> , TERMOESCRITA NOVOTERMOESCRITA
        if(self.tokenAtual == ','):
            self.deriva(['NOVOTERMOESCRITA', 'TERMOESCRITA' ','])
        elif(self.tokenAtual == ')'):
            #NOVOTERMOESCRITA --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO NOVOTERMOESCRITA: simbolo nao reconhecido')

    def funcao(self):
        if(self.tokenAtual == 'funcao'):
            #FUNÇÃO --> funcao id ( PARAMETRO ) : {global.tab += 1} BLOCOOBRIGATORIO 
            self.deriva(['BLOCOOBRIGATORIO', ':', ')', 'PARAMETRO', '(', 'id', 'funcao'])
            self.tab += 1
        else:
            #ERRO
            print('ERRO FUNCAO: simbolo nao reconhecido')

    def parametro(self):
        if(self.tokenAtual == 'id'):
            #PARAMETRO --> id PARAMETRO2
            self.deriva(['PARAMETRO2', 'id'])
        elif(self.tokenAtual == ')'):
            #PARAMETRO --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO PARAMETRO: simbolo nao reconhecido')

    def parametro2(self):
        if(self.tokenAtual == ','):
            #PARAMETRO2 --> , id PARAMETRO2
            self.deriva(['PARAMETRO2', 'id', ','])
        elif(self.tokenAtual == ')'):
            #PARAMETRO2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO PARAMETRO2: simbolo nao reconhecido')

    def atribuicao(self):
        if(self.tokenAtual == 'id'):
            #ATRIBUIÇÃO --> id = COMPLEMENTO 
            self.deriva(['COMPLEMENTO', '=', 'id'])
        else:
            print('ERRO ATRIBUICAO: simbolo nao reconhecido')

    def complemento(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #COMPLEMENTO --> EXPRESSÃO
            self.deriva(['EXPRESSAO'])
        elif(self.tokenAtual == 'funcao'):
            #COMPLEMENTO --> FUNCAO
            self.deriva(['FUNCAO'])
        else:
            #ERRO
            print('ERRO COMPLEMENTO: simbolo nao identificado')

    def enquanto(self):
        if(self.tokenAtual == 'enquanto'):
            #ENQUANTO  --> enquanto ( EXPRESSÃO ): {global.tab += 1} BLOCOOBRIGATORIO
            self.deriva(['BLOCOOBRIGATORIO', ':', ')', 'EXPRESSAO', '(', 'enquanto'])
            self.tab += 1
        else:
            #ERRO
            print('ERRO ENQUANTO: simbolo nao reconhecido')

    def retorno(self):
        if(self.tokenAtual == 'retorna'):
            #RETORNO --> retorna EXPRESSÃO
            self.deriva(['EXPRESSAO', 'retorna'])
        else:
            #ERRO
            print('ERRO RETORNO: simbolo nao reconhecido')

    def expressao(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #EXPRESSÃO --> EXPR_OU
            self.deriva(['EXPR_OU'])
        else:
            #ERRO
            print('ERRO EXPRESSAO: simbolo nao reconhecido')

    def expr_ou(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #EXPR_OU --> EXPR_E EXPR_OU2
            self.deriva(['EXPR_OU2', 'EXPR_E'])
        else:
            #ERRO
            print('ERRO EXPR_OU: simbolo nao reconhecido')

    def expr_ou2(self):
        if(self.tokenAtual == 'ou'):
            #EXPR_OU2 --> ou EXPR_E EXPR_OU2
            self.deriva(['EXPR_OU2', 'EXPR_E', 'ou'])
        elif(self.tokenAtual == 'enter'):
            #EXPR_OU2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_OU2: simbolo nao reconhecido')

    def expr_e(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #EXPR_E --> EXPR_RELACIONAL EXPR_E2
            self.deriva(['EXPR_E2', 'EXPR_RELACIONAL'])
        else:
            #ERRO
            print('ERRO EXPR_E: simbolo nao reconhecido')

    def expr_e2(self):
        if(self.tokenAtual == 'e'):
            #EXPR_E2 --> e EXPR_RELACIONAL EXPR_E2
            self.deriva(['EXPR_E2', 'EXPR_RELACIONAL', 'e'])
        elif(self.tokenAtual == 'enter'):
            #EXPR_E2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_E2: simbolo nao reconhecido')

    def expr_relacional(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #EXPR_RELACIONAL --> EXPR_ADITIVA EXPR_RELACIONAL2
            self.deriva(['EXPR_RELACIONAL2', 'EXPR_ADITIVA'])
        else:
            #ERRO
            print('ERRO EXPR_RELACIONAL: simbolo nao reconhecido')

    def expr_relacional2(self):
        if(self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!='): 
            #EXPR_RELACIONAL2 --> OP_COMPARATIVO EXPR_ADITIVA
            self.deriva(['EXPR_ADITIVA', 'OP_COMPARATIVO'])
        elif(self.tokenAtual == 'enter' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou'):
            #EXPR_REALACIONAL2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO RELACIONAL_E2: simbolo nao reconhecido')

    def op_comparativo(self):
        if(self.tokenAtual == '<'):
            #OP_COMPARATIVO --> <
            self.deriva(['<'])
        elif(self.tokenAtual == '<='):
            #OP_COMPARATIVO --> <=
            self.deriva(['<='])
        elif(self.tokenAtual == '>'):
            #OP_COMPARATIVO --> >
            self.deriva(['>'])
        elif(self.tokenAtual == '>='):
            #OP_COMPARATIVO --> >=
            self.deriva(['>=']) 
        elif(self.tokenAtual == '=='):
            #OP_COMPARATIVO --> ==
            self.deriva(['==']) 
        elif(self.tokenAtual == '!='):
            #OP_COMPARATIVO --> !=
            self.deriva(['!='])
        else:
            #ERRO
            print('ERRO OP_COMPARATIVO: simbolo nao reconhecido') 
             
    def expr_aditiva(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #EXPR_ADITIVA --> EXPR_MULTIPLICATIVA EXPR_ADITIVA2
            self.deriva(['EXPR_ADITIVA2', 'EXPR_MULTIPLICATIVA'])
        else:
            #ERRO
            print('ERRO EXPR_ADITIVA: simbolo nao reconhecido')

    def expr_aditiva2(self):
        if(self.tokenAtual == '+' or self.tokenAtual == '-'):
            #EXPR_ADITIVA2 --> OP_ADITIVO EXPR_MULTIPLICATIVA EXPR_ADITIVA2
            self.deriva(['EXPR_ADITIVA2', 'EXPR_MULTIPLICATIVA', 'OP_ADITIVO'])
        elif(self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!=' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou' or
        self.tokenAtual == 'enter'): 
            #EXPR_ADITIVA2 -->  ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_ADITIVA2: simbolo nao reconhecido')

    def op_aditivo(self):
        if(self.tokenAtual == '+'):
            #OP_ADITIVO --> +
            self.deriva(['+'])
        elif(self.tokenAtual == '-'):
            #OP_ADITIVO --> -
            self.deriva(['-'])
        else:
            #ERRO
            print('ERRO OP_ADITIVO: simbolo nao reconhecido')

    def expr_multiplicativa(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #EXPR_MULTIPLICATIVA --> FATOR EXPR_MULTIPLICATIVA2
            self.deriva(['EXPR_MULTIPLICATIVA2', 'FATOR'])
        else:
            #ERRO
            print('ERRO EXPR_MULTIPLIVATIVA: simbolo nao reconhecido')

    def expr_multiplicativa2(self):
        if(self.tokenAtual == '*' or self.tokenAtual == '/'):
            #EXPR_MULTIPLICATIVA2 --> OP_MULTIPLICATIVO FATOR EXPR_MULTIPLICATIVA2
            self.deriva(['EXPR_MULTIPLICATIVA2', 'FATOR', 'OP_MULTIPLICATIVO'])
        elif(self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!=' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou' or
        self.tokenAtual == 'enter' or
        self.tokenAtual == '+' or
        self.tokenAtual == '-'): 
            #EXPR_MULTIPLICATIVA2 -->  ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_MULTIPLICATIVA2: simbolo nao reconhecido')

    def op_multiplicativo(self):
        if(self.tokenAtual == '*'):
            #OP_MULTIPLICATIVO --> *
            self.deriva(['*'])
        elif(self.tokenAtual == '/'):
            #OP_MULTIPLICATIVO --> /
            self.deriva(['/'])
        else:
            #ERRO
            print('ERRO OP_MULTIPLICATIVO: simbolo nao reconhecido')

    def fator(self):
        if(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real'):
            #FATOR --> SINAL TERMO
            self.deriva(['TERMO', 'SINAL'])
        elif(self.tokenAtual == 'texto'):
            #FATOR --> texto
            self.deriva('texto')
        elif(self.tokenAtual == '!'):
            #FATOR --> ! FATOR
            self.deriva(['FATOR', '!'])
        elif(self.tokenAtual == '('):
            #FATOR --> ( EXPRESSÃO )
            self.deriva([')', 'EXPRESSAO', '('])
        else:
            #ERRO
            print('ERRO FATOR: simbolo nao reconhecido')

    def termo(self):
        if(self.tokenAtual == 'id'):
            #TERMO --> id DIMENSAO
            self.deriva(['DIMENSAO', 'id'])
        elif(self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real'):
            #TERMO --> CONSTANTE
            self.deriva(['CONSTANTE'])
        else:
            #ERRO
            print('ERRO TERMO: simbolo nao reconhecido')

    def sinal(self):
        if(self.tokenAtual == '+'):
            #SINAL --> +
            self.deriva(['+'])
        elif(self.tokenAtual == '-'):
            #SINAL --> -
            self.deriva(['-'])
        elif(self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or
        self.tokenAtual == 'num_real'):
            #SINAL --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO SINAL: simbolo nao reconhecido')

    def constante(self):
        if(self.tokenAtual == 'num_inteiro'):
            #CONSTANTE --> num_inteiro
            self.deriva(['num_inteiro'])
        elif(self.tokenAtual == 'num_real'):
            #CONSTANTE --> num_real
            self.deriva(['num_real'])
        else:
            #ERRO
            print('ERRO CONSTANTE: simbolo nao reconhecido')


print('Digite o código. Para compilar digite Ctrl+Z')
codigo = sys.stdin.read()
x = Parser() 
x.getListaTokenAndTabSimb(codigo)

x.fazAnalise()
print('Lista Tokens: ', x.listaTokens)
print('tab simb: ' , x.tabelaSimb)
print('pilha: ', x.pilha)
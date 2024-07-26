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

                'ESCRITA' : self.escrita
            }
            switch_case.get(self.pilha[-1], self.padrao)()

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
            self.deriva(')','NOVOTERMOLEITURA', 'TERMOLEITURA', '(', 'ler')
        else:
            #ERRO
            print('ERRO LEITURA: simbolo nao reconhecido')

    def termoLeitura(self):
        if(self.tokenAtual == 'id'):
            #TERMOLEITURA --> id DIMENSAO
            self.deriva('DIMENSAO', 'id')
        else:
            #ERRO
            print('ERRO TERMOLEITURA: simbolo nao reconhecido')
    
    def novoTermoLeitura(self):
        if(self.tokenAtual == ','):
            #NOVOTERMOLEITURA --> , TERMOLEITURA NOVOTERMOLEITURA
            self.deriva('NOVOTERMOLEITURA', 'TERMOLEITURA', ',')
        elif(self.tokenAtual == ')'):
            #NOVOTERMOLEITURA --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO NOVOTERMOLEITURA: simbolo nao reconhecido')

    def dimensao(self):
        if(self.tokenAtual == '['):
            #DIMENSAO --> [ EXPR_ADITIVA ] DIMENSAO
            self.deriva('DIMENSAO', ']', 'EXPR_ADITIVA', '[')
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



print('Digite o código. Para compilar digite Ctrl+Z')
codigo = sys.stdin.read()
x = Parser() 
x.getListaTokenAndTabSimb(codigo)

x.fazAnalise()
print('Lista Tokens: ', x.listaTokens)
print('tab simb: ' , x.tabelaSimb)
print('pilha: ', x.pilha)
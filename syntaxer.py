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

    def achaTokenAtual(self):
        return self.listaTokens[0]

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
            print('self.pilha no fderiva: ', self.pilha[-1])

    def fazAnalise(self):
        while(len(self.pilha) != 0):
        # i = 0
        # for i in range(5):
            switch_case = {
                'PROGRAMA' : self.programa,
                
                'BLOCO' : self.bloco,
                
                'BLOCOOBRIGATORIO' : self.blocoObrigatorio,
                
                'INSTRUCOES' : self.instrucoes,

                'INSTRUCAO' : self.instrucao,
            }
            print('self.pilha: ', self.pilha[-1])
            switch_case.get(self.pilha[-1], self.padrao)()

    def padrao(self):
        print('LEXEMA {self.pilha[-1]} nao encontrado')

    def programa(self):
        print('entra em programa')
        if( self.achaTokenAtual() == 'FUNCAO' or 
        self.achaTokenAtual() == 'SE' or 
        self.achaTokenAtual() == 'LER' or 
        self.achaTokenAtual() == 'ESCREVE' or 
        self.achaTokenAtual() == 'ID' or 
        self.achaTokenAtual() == 'ENQUANTO' or 
        self.achaTokenAtual() == 'RETORNA' or 
        self.achaTokenAtual() == '+' or 
        self.achaTokenAtual() == '-' or 
        self.achaTokenAtual() == 'INTEIRO' or 
        self.achaTokenAtual() == 'REAL' or 
        self.achaTokenAtual() == 'TEXTO' or 
        self.achaTokenAtual() == '!' or 
        self.achaTokenAtual() == '('):
            self.deriva(['INSTRUCOES'])
        elif(self.achaTokenAtual() == '$'):
            #SUCESSO
            print('Sucesso')

        else:
            #ERRO
            print('ERRO PROGRAMA: simbolo não permitido')
        
    def bloco(self):
        if self.achaTokenAtual() == 'ENTER':
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
        if self.achaTokenAtual() == 'ENTER':
            self.listaTokens.pop()
            self.empilhaTab
            self.deriva(['INSTRUCOES'])
        else: 
            #ERRO
            print('ERRO BLOCOOBRIGATORIO carcter diferente de ENTER')

    def instrucoes(self):
        print('entra em instruções')
        if( self.achaTokenAtual() == 'FUNCAO' or 
        self.achaTokenAtual() == 'SE' or 
        self.achaTokenAtual() == 'LER' or 
        self.achaTokenAtual() == 'ESCREVE' or 
        self.achaTokenAtual() == 'ID' or 
        self.achaTokenAtual() == 'ENQUANTO' or 
        self.achaTokenAtual() == 'RETORNA' or 
        self.achaTokenAtual() == '+' or 
        self.achaTokenAtual() == '-' or 
        self.achaTokenAtual() == 'INTEIRO' or 
        self.achaTokenAtual() == 'REAL' or 
        self.achaTokenAtual() == 'TEXTO' or 
        self.achaTokenAtual() == '!' or 
        self.achaTokenAtual() == '('):
            self.deriva(['BLOCO', 'INSTRUCAO'])

        else:
            #ERRO
            print('ERRO INSTRUCOES: símbolo não permitido')

    def instrucao(self):
        print('entra em instrução')
        if self.achaTokenAtual() == 'SE':
            print('entra no se')
            # INSTRUÇÃO --> CONDICIONAL
            self.deriva(['CONDICIONAL'])
        elif self.achaTokenAtual() == 'LER':
            # INSTRUÇÃO --> LEITURA
            self.deriva(['LEITURA'])
        elif self.achaTokenAtual() == 'ESCREVER':
            # INSTRUÇÃO --> ESCRITA
            self.deriva(['ESCRITA'])
        elif self.achaTokenAtual() == 'FUNCAO':
            # INSTRUÇÃO --> FUNCAO
            self.deriva('FUNCAO')
        elif self.achaTokenAtual() == 'ID':
            # INSTRUÇÃO --> ATRIBUICAO
            self.deriva('ATRIBUICAO')
        elif self.achaTokenAtual() == 'ENQUANTO':
            # INSTRUÇÃO --> ENQUANTO
            self.deriva('ENQUANTO')
        elif self.achaTokenAtual() == 'RETORNA':
            # INSTRUÇÃO --> RETORNO
            self.deriva('RETORNO')
        elif self.achaTokenAtual() == '+':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.achaTokenAtual() == '-':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.achaTokenAtual() == 'INTEIRO':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.achaTokenAtual() == 'REAL':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.achaTokenAtual() == 'TEXTO':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.achaTokenAtual() == '!':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        elif self.achaTokenAtual() == '(':
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva('EXPRESSAO')
        else:
            #ERRO
            print('ERRO INSTRUCAO: simbolo nao reconhecido')


print('Digite o código. Para compilar digite Ctrl+Z')
codigo = sys.stdin.read()
x = Parser() 
x.getListaTokenAndTabSimb(codigo)

x.fazAnalise()
print('Lista Tokens: ', x.listaTokens)
print('tab simb: ' , x.tabelaSimb)
print('pilha: ', x.pilha)
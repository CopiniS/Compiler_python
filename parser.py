from lexer import Lexer;
from collections import deque;
import sys;

class Parser:
    def __init__(self):
        self.tab = 0
        self.listaTokens = []
        self.tabelaSimb = []
        self.pilha = deque()
        self.pilha.append('PROGRAMA')

    def getListaTokenAndTabSimb(self, trechoCodigo):
        lexer = Lexer(trechoCodigo)
        lexer.getToken()
        self.tabelaSimb = lexer.tabelaSimbolos
        self.listaTokens = lexer.listaTokens
        self.achaTokenAtual()

    def achaTokenAtual(self):
        self.tokenAtual = self.listaTokens[0][0]
        self.valorTokenAtual = self.listaTokens[0][1]

    def calculaTab(self):
        quantidadeTab = 0
        for token in self.listaTokens:
            if(token == 'tab'):
                quantidadeTab += 1
            else:
                break
        return quantidadeTab

    def removeNovasLinhas(self):
        while self.tokenAtual == 'enter':
            self.listaTokens.pop(0)
        self.achaTokenAtual()

    def empilhaTab(self):
        i = 0
        for i in range(self.tab):
            self.pilha.append('tab') 

    def deriva(self, derivacoes):
        self.pilha.pop()
        for derivacao in derivacoes:
            self.pilha.append(derivacao)

    def removeTerminais(self):
        while(self.tokenAtual == self.pilha[-1]):
            self.listaTokens.pop(0)
            self.pilha.pop()
            self.achaTokenAtual()

    def fazAnalise(self):
        while(len(self.pilha) != 0):
        # i = 0
        # for i in range(10):
            if len(self.listaTokens) == 0:
                print('ERRO')
                break

            self.removeTerminais()
            switch_case = {
                'PROGRAMA' : self.programa,
                
                'BLOCO' : self.bloco,

                'NOVALINHA' : self.novaLinha,

                'NOVALINHA2' : self.novaLinha2,

                'DEDENT' : self.dedent, 
                
                'INSTRUCOESINICIO' : self.instrucoesInicio,
                
                'INSTRUCOES' : self.instrucoes,

                'INSTRUCOES2' : self.instrucoes2,

                'INSTRUCAO' : self.instrucao,

                'CONDICIONAL' : self.condicional,

                'SENAOSE' : self.senaose,

                'SENAO' : self.senao,

                'LEITURA' : self.leitura,

                'TERMOLEITURA' : self.termoLeitura,

                'NOVOTERMOLEITURA' : self.novoTermoLeitura,

                'DIMENSAO' : self.dimensao,

                'ESCRITA' : self.escrita,

                'TERMOESCRITA' : self.termoEscrita,
                
                'NOVOTERMOESCRITA' : self.novoTermoEscrita,
                
                'FUNCAO' : self.funcao,

                'ENQUANTO' : self.enquanto,
                
                'CLASSE' : self.classe,
                
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

                'DIMENSAO2' : self.dimensao2,
                
                'SINAL' : self.sinal,
                
                'CONSTANTE' : self.constante,
                
            }
            switch_case.get(self.pilha[-1], self.padrao)()

        if len(self.listaTokens) == 1 and self.listaTokens[0][0] == 'enter':
            #SUCESSO
            print('SUCESSO')

    def padrao(self):
        print('LEXEMA: ',self.pilha, ' - nao encontrado')

    def programa(self):
        print('entra em programa')
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna' or 
        self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            self.deriva(['INSTRUCOESINICIO'])
        elif(self.tokenAtual == '$'):
            #SUCESSO
            print('Sucesso')

        else:
            #ERRO
            print('ERRO PROGRAMA: simbolo não permitido')
            self.pilha.clear()
        
    def instrucoesInicio(self):  
        print('Entra em INSTRUCOESINICIO') 
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna' or 
        self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #INSTRUCOESINICIO --> INSTRUCAO INTRUCOES2 
            self.deriva(['INSTRUCOES2', 'INSTRUCAO'])
        elif(self.tokenAtual == '$'):
            #INSTRUCOESINICIO --> ε
            self.pilha.pop()

    def bloco(self):
        print('entra em bloco')
        if self.tokenAtual == 'novalinha':
            #BLOCO --> NOVALINHA indent INSTRUCOES DEDENT 
            self.deriva(['DEDENT', 'INSTRUCOES', 'indent', 'NOVALINHA'])
        else: 
            #ERRO
            print('ERRO BLOCO carcter diferente de NOVALINHA')
            self.pilha.clear()

    def novaLinha(self):
        if self.tokenAtual == 'novalinha':
            #NOVALINHA --> novaLinha NOVALINHA2
            self.deriva(['NOVALINHA2', 'novalinha'])
        else: 
            #ERRO
            print('ERRO NOVALINHA carcter diferente de novalinha')
            self.pilha.clear()

    def novaLinha2(self):
        if self.tokenAtual == 'novalinha':
            #NOVALINHA2 --> novaLinha NOVALINHA2
            self.deriva(['NOVALINHA2', 'novalinha'])
        elif(self.tokenAtual == 'indent'):
            self.pilha.pop()
            #NOVALINHA2 --> ε
        else: 
            #ERRO
            print('ERRO NOVALINHA2 carcter diferente de novalinha')
            self.pilha.clear()

    def dedent(self):
        if(self.tokenAtual == 'novalinha'):
            #DEDENT --> novaLinha dedent
            self.deriva(['dedent', 'novalinha'])
        elif(self.tokenAtual == 'dedent'):
            #DEDENT --> dedent
            self.deriva(['dedent'])
        else: 
            #ERRO
            print('ERRO DEDENT: SIMBOLO NAO RECONHECIDO')
            self.pilha.clear()

    def instrucoes(self):
        print('entra em instruções')
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna' or 
        self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #INSTRUÇÕES --> INSTRUÇÃO INSTRUCOES2
            self.deriva(['INSTRUCOES2', 'INSTRUCAO'])

        else:
            #ERRO
            print('ERRO INSTRUCOES: símbolo não permitido')
            self.pilha.clear()

    def instrucoes2(self):
        print('entra em instruções2')
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna' or 
        self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            #INSTRUCOES2 --> NOVALINHA INSTRUCAO INSTRUCOES2 | ε
            self.deriva(['INSTRUCOES2', 'INSTRUCAO', 'NOVALINHA'])
        elif(self.tokenAtual == '$' or
        self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent'):  
            #INSTRUCOES2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO INSTRUCOES2: simbolo nao reconhecido')
            self.pilha.clear()

    def instrucao(self):
        print('entra em instrução')
        if self.tokenAtual == 'se':
            print('entra no se')
            # INSTRUÇÃO --> CONDICIONAL
            self.deriva(['CONDICIONAL'])
        elif self.tokenAtual == 'funcao':
            # INSTRUÇÃO --> FUNCAO
            self.deriva(['FUNCAO'])
        elif self.tokenAtual == 'enquanto':
            # INSTRUÇÃO --> ENQUANTO
            self.deriva(['ENQUANTO'])
        elif self.tokenAtual == 'classe':
            self.deriva(['CLASSE'])
        elif self.tokenAtual == 'ler':
            # INSTRUÇÃO --> LEITURA
            self.deriva(['LEITURA'])
        elif self.tokenAtual == 'escrever':
            # INSTRUÇÃO --> ESCRITA
            self.deriva(['ESCRITA'])
        elif self.tokenAtual == 'id':
            # INSTRUÇÃO --> ATRIBUICAO
            self.deriva(['ATRIBUICAO'])
        elif self.tokenAtual == 'retorna':
            # INSTRUÇÃO --> RETORNO
            self.deriva(['RETORNO'])
        elif(self.tokenAtual == '+' or 
        self.tokenAtual == '-' or 
        self.tokenAtual == 'id' or
        self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real' or 
        self.tokenAtual == 'texto' or 
        self.tokenAtual == '!' or 
        self.tokenAtual == '('):
            # INSTRUÇÃO --> EXPRESSAO
            self.deriva(['EXPRESSAO'])
        else:
            #ERRO
            print('ERRO INSTRUCAO: simbolo nao reconhecido')
            self.pilha.clear()

    def condicional(self):
        if(self.tokenAtual == 'se'):
            #CONDICIONAL --> se ( EXPRESSÃO ) : BLOCO SENAOSE SENAO
            self.deriva(['SENAO','SENAOSE', 'BLOCO', ':', ')', 'EXPRESSAO', '(', 'se'])
        else:
            #ERRO
            print('ERRO CONDICIONAL: símbolo não permitido')
            self.pilha.clear()

    def senaose(self):
        if(self.tokenAtual == 'senaose'):
            #SENAOSE --> senaose ( EXPRESSAO ) : BLOCO
            self.deriva(['BLOCO', ':', ')', 'EXPRESSAO', '(', 'senaose'])
        elif(self.tokenAtual == 'senao' or
        self.tokenAtual == '$' or
        self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent'):
            #SENAOSE --> ε
            self.pilha.pop()
    
    def senao(self):
        if(self.tokenAtual == 'senao'):
            #SENAO --> senao : BLOCO
            self.deriva(['BLOCO', ':', 'senao'])
        elif(self.tokenAtual == '$' or
        self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent'):
            #SENAO --> ε 
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO SENAO: símbolo não permitido')
            self.pilha.clear()

    def leitura(self):
        if(self.tokenAtual == 'ler'):
            #LEITURA --> ler ( TERMOLEITURA NOVOTERMOLEITURA )
            self.deriva([')','NOVOTERMOLEITURA', 'TERMOLEITURA', '(', 'ler'])
        else:
            #ERRO
            print('ERRO LEITURA: simbolo nao reconhecido')
            self.pilha.clear()

    def termoLeitura(self):
        if(self.tokenAtual == 'id'):
            #TERMOLEITURA --> id DIMENSAO
            self.deriva(['DIMENSAO', 'id'])
        else:
            #ERRO
            print('ERRO TERMOLEITURA: simbolo nao reconhecido')
            self.pilha.clear()
    
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
            self.pilha.clear()

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
            self.pilha.clear()

    def escrita(self):
        if(self.tokenAtual == 'escrever'):
            #LEITURA --> ler ( TERMOLEITURA NOVOTERMOLEITURA )
            self.deriva(')','NOVOTERMOESCRITA', 'TERMOESCRITA', '(', 'escrever')
        else:
            #ERRO
            print('ERRO ESCRITA: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

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
            self.pilha.clear()

    def funcao(self):
        if(self.tokenAtual == 'funcao'):
            #FUNÇÃO --> funcao id ( PARAMETRO ) : BLOCO 
            self.deriva(['BLOCO', ':', ')', 'PARAMETRO', '(', 'id', 'funcao'])
        else:
            #ERRO
            print('ERRO FUNCAO: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

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
            self.pilha.clear()

    def atribuicao(self):
        if(self.tokenAtual == 'id'):
            #ATRIBUIÇÃO --> id = COMPLEMENTO 
            self.deriva(['COMPLEMENTO', '=', 'id'])
        else:
            print('ERRO ATRIBUICAO: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

    def enquanto(self):
        if(self.tokenAtual == 'enquanto'):
            #ENQUANTO  --> enquanto ( EXPRESSÃO ): BLOCO
            self.deriva(['BLOCO', ':', ')', 'EXPRESSAO', '(', 'enquanto'])
        else:
            #ERRO
            print('ERRO ENQUANTO: simbolo nao reconhecido')
            self.pilha.clear()

    def classe(self):
        if(self.tokenAtual == 'classe'):
            self.deriva('BLOCO', ':', 'id', 'classe')
        else:
            #ERRO
            print('ERRO CLASSE: simbolo nao reconhecido')
            self.pilha.clear()

    def retorno(self):
        if(self.tokenAtual == 'retorna'):
            #RETORNO --> retorna EXPRESSÃO
            self.deriva(['EXPRESSAO', 'retorna'])
        else:
            #ERRO
            print('ERRO RETORNO: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

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
            self.pilha.clear()

    def expr_ou2(self):
        if(self.tokenAtual == 'ou'):
            #EXPR_OU2 --> ou EXPR_E EXPR_OU2
            self.deriva(['EXPR_OU2', 'EXPR_E', 'ou'])
        elif(self.tokenAtual == 'enter' or
             self.tokenAtual == ')'):
            #EXPR_OU2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_OU2: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

    def expr_e2(self):
        if(self.tokenAtual == 'e'):
            #EXPR_E2 --> e EXPR_RELACIONAL EXPR_E2
            self.deriva(['EXPR_E2', 'EXPR_RELACIONAL', 'e'])
        elif(self.tokenAtual == 'enter' or
             self.tokenAtual == ')'):
            #EXPR_E2 --> ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_E2: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

    def expr_relacional2(self):
        if(self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!=' or
        self.tokenAtual == ')'): 
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
            self.pilha.clear()

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
            self.pilha.clear()
             
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
            self.pilha.clear()

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
        self.tokenAtual == ')' or
        self.tokenAtual == 'enter'): 
            #EXPR_ADITIVA2 -->  ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_ADITIVA2: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

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
            self.pilha.clear()

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
        self.tokenAtual == ')' or
        self.tokenAtual == '+' or
        self.tokenAtual == '-'): 
            #EXPR_MULTIPLICATIVA2 -->  ε
            self.pilha.pop()
        else:
            #ERRO
            print('ERRO EXPR_MULTIPLICATIVA2: simbolo nao reconhecido')
            print('token atual: ', self.tokenAtual)
            self.pilha.clear()

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
            self.pilha.clear()

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
            self.pilha.clear()

    def termo(self):
        if(self.tokenAtual == 'id'):
            #TERMO --> id DIMENSAO
            self.deriva(['DIMENSAO2', 'id'])
        elif(self.tokenAtual == 'num_inteiro' or 
        self.tokenAtual == 'num_real'):
            #TERMO --> CONSTANTE
            self.deriva(['CONSTANTE'])
        else:
            #ERRO
            print('ERRO TERMO: simbolo nao reconhecido')
            self.pilha.clear()

    def dimensao2(self):
        if(self.tokenAtual == '['):
            #DIMENSAO2 --> [ EXPR_ADITIVA ] DIMENSAO2
            self.deriva(['DIMENSAO2', ']', 'EXPR_ADITIVA', '['])
        elif(self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!=' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou' or
        self.tokenAtual == 'enter' or
        self.tokenAtual == ')' or
        self.tokenAtual == '+' or
        self.tokenAtual == '-' or
        self.tokenAtual == '*' or
        self.tokenAtual == '/'): 
            #DIMENSAO2 --> ε
            self.pilha.pop()
        else:
        #ERRO
            print('ERRO DIMENSAO2: simbolo nao reconhecido')
            self.pilha.clear()

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
            self.pilha.clear()

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
            self.pilha.clear()

print('Digite o código. Para compilar digite Ctrl+Z')
codigo = sys.stdin.read()
x = Parser() 
x.getListaTokenAndTabSimb(codigo)

x.fazAnalise()
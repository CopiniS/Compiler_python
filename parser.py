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
        print('Lista de tokens inicial: ', self.listaTokens)
        self.achaTokenAtual()

    def achaTokenAtual(self):
        self.tokenAtual = self.listaTokens[0][0]
        self.valorTokenAtual = self.listaTokens[0][1]

    def deriva(self, derivacoes):
        string = self.pilha[-1] + ' --> '
        self.pilha.pop()
        for derivacao in derivacoes:
            self.pilha.append(derivacao)
            string = string + derivacao + ' '
        print(string)

    def removeTerminais(self):
        print('checando se '+ self.tokenAtual + ' é igual a ' + self.pilha[-1])
        while(self.tokenAtual == self.pilha[-1]):
            print(self.tokenAtual + ' é igual a ' + self.pilha[-1])
            self.listaTokens.pop(0)
            self.pilha.pop()
            self.achaTokenAtual()

    def fazAnalise(self):
        while(len(self.pilha) != 0):
            if len(self.listaTokens) == 0:
                sys.exit('Erro')
            self.removeTerminais()
            switch_case = {
                'PROGRAMA' : self.programa,
                
                'BLOCO' : self.bloco,

                'NOVALINHA' : self.novaLinha,

                'NOVALINHA2' : self.novaLinha2,

                'NOVALINHA3' : self.novaLinha3,

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

        if len(self.listaTokens) == 1 and self.tokenAtual == '$':
            #SUCESSO
            sys.exit('Sucesso')
        else:
            #ERRO
            sys.exit("Simbolo " + self.tokenAtual + " no lugar incorreto")

    def padrao(self):
        print('pilha temporario: ', self.pilha)
        sys.exit('símbolo esperado: '+ self.pilha[-1])

    def programa(self):
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna'):
            self.deriva(['INSTRUCOESINICIO'])
        elif(self.tokenAtual == '$'):
            #SUCESSO
            sys.exit('Sucesso')

        else:
            #ERRO
            sys.exit('ERRO PROGRAMA: simbolo não permitido')
        
    def instrucoesInicio(self):  
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna'):
            #INSTRUCOESINICIO --> INSTRUCAO INTRUCOES2 
            self.deriva(['INSTRUCOES2', 'INSTRUCAO'])
        elif(self.tokenAtual == '$'):
            #INSTRUCOESINICIO --> ε
            print('INSTRUCOESINICIO --> ε')
            self.pilha.pop()

    def bloco(self):
        if self.tokenAtual == 'novalinha':
            #BLOCO --> NOVALINHA indent INSTRUCOES dedent
            self.deriva(['dedent', 'INSTRUCOES', 'indent', 'NOVALINHA'])
        else: 
            #ERRO
            sys.exit('ERRO BLOCO carcter diferente de NOVALINHA')

    def novaLinha(self):
        if self.tokenAtual == 'novalinha':
            #NOVALINHA --> novaLinha NOVALINHA2
            self.deriva(['NOVALINHA2', 'novalinha'])
        else: 
            #ERRO
            sys.exit('ERRO NOVALINHA caracter diferente de novalinha')

    def novaLinha2(self):
        print('dentro de novalinha2 token atua: ', self.tokenAtual)
        if self.tokenAtual == 'novalinha':
            #NOVALINHA2 --> novaLinha NOVALINHA2
            self.deriva(['NOVALINHA2', 'novalinha'])
        elif(self.tokenAtual == 'indent' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna'):
            self.pilha.pop()
            #NOVALINHA2 --> ε
            print('NOVALINHA2 --> ε')
        else: 
            #ERRO
            sys.exit('ERRO NOVALINHA2 carcter diferente de novalinha')

    def novaLinha3(self):
        if self.tokenAtual == 'novalinha':
            #NOVALINHA3 --> NOVALINHA DEDENT
            self.deriva(['DEDENT', 'NOVALINHA'])
        else: 
            #ERRO
            sys.exit('ERRO NOVALINHA3 carcter diferente de novalinha')

    def dedent(self):
        if self.tokenAtual == 'dedent':
            #DEDENT --> dedent
            self.deriva(['dedent'])
        elif (self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna'):
            #DEDENT --> ε
            print('DEDENT --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO DEDENT carcter nao reconhecido')

    def instrucoes(self):
        if(self.tokenAtual == 'se' or  
        self.tokenAtual == 'funcao' or 
        self.tokenAtual == 'enquanto' or
        self.tokenAtual == 'classe' or
        self.tokenAtual == 'ler' or 
        self.tokenAtual == 'escrever' or 
        self.tokenAtual == 'id' or  
        self.tokenAtual == 'retorna'):
            #INSTRUÇÕES --> INSTRUÇÃO INSTRUCOES2
            self.deriva(['INSTRUCOES2', 'INSTRUCAO'])

        else:
            #ERRO
            sys.exit('ERRO INSTRUCOES: símbolo não permitido')

    def instrucoes2(self):
        print('token atual temporario: ', self.tokenAtual)
        if(self.tokenAtual == 'novalinha'):
            #INSTRUCOES2 --> NOVALINHA3 INSTRUCAO INSTRUCOES2
            self.deriva(['INSTRUCOES2', 'INSTRUCAO', 'NOVALINHA3'])
        elif(self.tokenAtual == '$' or
        self.tokenAtual == 'dedent'):  
            #INSTRUCOES2 --> ε
            print('INSTRUCOES2 --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO INSTRUCOES2: simbolo nao reconhecido')

    def instrucao(self):
        if self.tokenAtual == 'se':
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
        else:
            #ERRO
            sys.exit('ERRO INSTRUCAO: simbolo nao reconhecido')

    def condicional(self):
        if(self.tokenAtual == 'se'):
            #CONDICIONAL --> se ( EXPRESSÃO ) : BLOCO SENAOSE SENAO
            self.deriva(['SENAO','SENAOSE', 'BLOCO', ':', ')', 'EXPRESSAO', '(', 'se'])
        else:
            #ERRO
            sys.exit('ERRO CONDICIONAL: símbolo não permitido')

    def senaose(self):
        if(self.tokenAtual == 'senaose'):
            #SENAOSE --> senaose ( EXPRESSAO ) : BLOCO
            self.deriva(['BLOCO', ':', ')', 'EXPRESSAO', '(', 'senaose'])
        elif(self.tokenAtual == 'senao' or
        self.tokenAtual == '$' or
        self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent'):
            #SENAOSE --> ε
            print('SENAOSE --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO SENAOSE: símbolo não permitido')
    
    def senao(self):
        if(self.tokenAtual == 'senao'):
            #SENAO --> senao : BLOCO
            self.deriva(['BLOCO', ':', 'senao'])
        elif(self.tokenAtual == '$' or
        self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent'):
            #SENAO --> ε 
            print('SENAO --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO SENAO: simbolo nao reconhecido')

    def leitura(self):
        if(self.tokenAtual == 'ler'):
            #LEITURA --> ler ( TERMOLEITURA NOVOTERMOLEITURA )
            self.deriva([')','NOVOTERMOLEITURA', 'TERMOLEITURA', '(', 'ler'])
        else:
            #ERRO
            sys.exit('ERRO LEITURA: simbolo nao reconhecido')

    def termoLeitura(self):
        if(self.tokenAtual == 'id'):
            #TERMOLEITURA --> id DIMENSAO
            self.deriva(['DIMENSAO', 'id'])
        else:
            #ERRO
            sys.exit('ERRO TERMOLEITURA: simbolo nao reconhecido')
 
    def novoTermoLeitura(self):
        if(self.tokenAtual == ','):
            #NOVOTERMOLEITURA --> , TERMOLEITURA NOVOTERMOLEITURA
            self.deriva(['NOVOTERMOLEITURA', 'TERMOLEITURA', ','])
        elif(self.tokenAtual == ')'):
            #NOVOTERMOLEITURA --> ε
            print('NOVOTERMOLEITURA --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO NOVOTERMOLEITURA: simbolo nao reconhecido')

    def dimensao(self):
        if(self.tokenAtual == '['):
            #DIMENSAO --> [ EXPR_ADITIVA ] DIMENSAO
            self.deriva(['DIMENSAO', ']', 'EXPR_ADITIVA', '['])
        elif(self.tokenAtual == ')' or self.tokenAtual == ','):
            #DIMENSAO --> ε
            print('DIMENSAO --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO DIMENSAO: simbolo nao reconhecido')

    def escrita(self):
        if(self.tokenAtual == 'escrever'):
            #LEITURA --> ler ( TERMOLEITURA NOVOTERMOLEITURA )
            self.deriva(')','NOVOTERMOESCRITA', 'TERMOESCRITA', '(', 'escrever')
        else:
            #ERRO
            sys.exit('ERRO ESCRITA: simbolo nao reconhecido')

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
            sys.exit('ERRO TERMOESCRITA: simbolo nao reconhecido')

    def novoTermoEscrita(self):
        #NOVOTERMOESCRITA --> , TERMOESCRITA NOVOTERMOESCRITA
        if(self.tokenAtual == ','):
            self.deriva(['NOVOTERMOESCRITA', 'TERMOESCRITA' ','])
        elif(self.tokenAtual == ')'):
            #NOVOTERMOESCRITA --> ε
            print('NOVOTERMOESCRITA --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO NOVOTERMOESCRITA: simbolo nao reconhecido')

    def funcao(self):
        if(self.tokenAtual == 'funcao'):
            #FUNÇÃO --> funcao id ( PARAMETRO ) : BLOCO 
            self.deriva(['BLOCO', ':', ')', 'PARAMETRO', '(', 'id', 'funcao'])
        else:
            #ERRO
            sys.exit('ERRO FUNCAO: simbolo nao reconhecido')

    def parametro(self):
        if(self.tokenAtual == 'id'):
            #PARAMETRO --> id PARAMETRO2
            self.deriva(['PARAMETRO2', 'id'])
        elif(self.tokenAtual == ')'):
            #PARAMETRO --> ε
            print('PARAMETRO --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO PARAMETRO: simbolo nao reconhecido')

    def parametro2(self):
        if(self.tokenAtual == ','):
            #PARAMETRO2 --> , id PARAMETRO2
            self.deriva(['PARAMETRO2', 'id', ','])
        elif(self.tokenAtual == ')'):
            #PARAMETRO2 --> ε
            print('PARAMETRO2 --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO PARAMETRO2: simbolo nao reconhecido')

    def atribuicao(self):
        if(self.tokenAtual == 'id'):
            #ATRIBUIÇÃO --> id = COMPLEMENTO 
            self.deriva(['COMPLEMENTO', '=', 'id'])
        else:
            sys.exit('ERRO ATRIBUICAO: simbolo nao reconhecido')

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
            sys.exit('ERRO COMPLEMENTO: simbolo nao reconhecido')

    def enquanto(self):
        if(self.tokenAtual == 'enquanto'):
            #ENQUANTO  --> enquanto ( EXPRESSÃO ): BLOCO
            self.deriva(['BLOCO', ':', ')', 'EXPRESSAO', '(', 'enquanto'])
        else:
            #ERRO
            sys.exit('ERRO ENQUANTO: simbolo nao reconhecido')

    def classe(self):
        if(self.tokenAtual == 'classe'):
            self.deriva('BLOCO', ':', 'id', 'classe')
        else:
            #ERRO
            sys.exit('ERRO CLASSE: simbolo nao reconhecido')

    def retorno(self):
        if(self.tokenAtual == 'retorna'):
            #RETORNO --> retorna EXPRESSÃO
            self.deriva(['EXPRESSAO', 'retorna'])
        else:
            #ERRO
            sys.exit('ERRO RETORNO: simbolo nao reconhecido')

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
            sys.exit('ERRO EXPRESSAO: simbolo nao reconhecido')

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
            sys.exit('ERRO EXPR_OU: simbolo nao reconhecido')

    def expr_ou2(self):
        if(self.tokenAtual == 'ou'):
            #EXPR_OU2 --> ou EXPR_E EXPR_OU2
            self.deriva(['EXPR_OU2', 'EXPR_E', 'ou'])
        elif(self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == ')'):
            #EXPR_OU2 --> ε
            print('EXPR_OU2 --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO EXPR_OU2: simbolo nao reconhecido')

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
            sys.exit('ERRO EXPR_E: simbolo nao reconhecido')

    def expr_e2(self):
        if(self.tokenAtual == 'e'):
            #EXPR_E2 --> e EXPR_RELACIONAL EXPR_E2
            self.deriva(['EXPR_E2', 'EXPR_RELACIONAL', 'e'])
        elif(self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == ')' or
        self.tokenAtual == 'ou'):
            #EXPR_E2 --> ε
            print('EXPR_E2 --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO EXPR_E2: simbolo nao reconhecido')

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
            sys.exit('ERRO EXPR_RELACIONAL: simbolo nao reconhecido')

    def expr_relacional2(self):
        if(self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!='): 
            #EXPR_RELACIONAL2 --> OP_COMPARATIVO EXPR_ADITIVA
            self.deriva(['EXPR_ADITIVA', 'OP_COMPARATIVO'])
        elif(self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == ')' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou'):
            #EXPR_REALACIONAL2 --> ε
            print('EXPR_REALACIONAL2 --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO EXPR_RELACIONAL2: simbolo nao reconhecido')

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
            sys.exit('ERRO OP_COMPARATIVO: simbolo nao reconhecido')
         
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
            sys.exit('ERRO EXPR_ADITIVA: simbolo nao reconhecido')

    def expr_aditiva2(self):
        if(self.tokenAtual == '+' or self.tokenAtual == '-'):
            #EXPR_ADITIVA2 --> OP_ADITIVO EXPR_MULTIPLICATIVA EXPR_ADITIVA2
            self.deriva(['EXPR_ADITIVA2', 'EXPR_MULTIPLICATIVA', 'OP_ADITIVO'])
        elif(self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == ')' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou' or
        self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!='): 
            #EXPR_ADITIVA2 -->  ε
            print('EXPR_ADITIVA2 -->  ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO EXPR_ADITIVA: simbolo nao reconhecido')

    def op_aditivo(self):
        if(self.tokenAtual == '+'):
            #OP_ADITIVO --> +
            self.deriva(['+'])
        elif(self.tokenAtual == '-'):
            #OP_ADITIVO --> -
            self.deriva(['-'])
        else:
            #ERRO
            sys.exit('ERRO OP_ADITIVO: simbolo nao reconhecido')

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
            sys.exit('ERRO EXPR_MULTIPLICATIVA: simbolo nao reconhecido')

    def expr_multiplicativa2(self):
        if(self.tokenAtual == '*' or self.tokenAtual == '/'):
            #EXPR_MULTIPLICATIVA2 --> OP_MULTIPLICATIVO FATOR EXPR_MULTIPLICATIVA2
            self.deriva(['EXPR_MULTIPLICATIVA2', 'FATOR', 'OP_MULTIPLICATIVO'])
        elif(self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == ')' or
        self.tokenAtual == 'e' or
        self.tokenAtual == 'ou' or
        self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!=' or
        self.tokenAtual == '+' or
        self.tokenAtual == '-'): 
            #EXPR_MULTIPLICATIVA2 -->  
            print('EXPR_MULTIPLICATIVA2 -->  ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO EXPR_MULTIPLICATIVA2: simbolo nao reconhecido')

    def op_multiplicativo(self):
        if(self.tokenAtual == '*'):
            #OP_MULTIPLICATIVO --> *
            self.deriva(['*'])
        elif(self.tokenAtual == '/'):
            #OP_MULTIPLICATIVO --> /
            self.deriva(['/'])
        else:
            #ERRO
            sys.exit('ERRO OP_MULTIPLICATIVO: simbolo nao reconhecido')

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
            sys.exit('ERRO FATOR: simbolo nao reconhecido')

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
            sys.exit('ERRO TERMO: simbolo nao reconhecido')

    def dimensao2(self):
        if(self.tokenAtual == '['):
            #DIMENSAO2 --> [ EXPR_ADITIVA ] DIMENSAO2
            self.deriva(['DIMENSAO2', ']', 'EXPR_ADITIVA', '['])
        elif(self.tokenAtual == 'novalinha' or
        self.tokenAtual == 'dedent' or
        self.tokenAtual == ')' or
        self.tokenAtual == '<' or 
        self.tokenAtual == '<=' or 
        self.tokenAtual == '>' or
        self.tokenAtual == '>=' or 
        self.tokenAtual == '==' or 
        self.tokenAtual == '!=' or
        self.tokenAtual == '+' or
        self.tokenAtual == '-' or
        self.tokenAtual == '*' or
        self.tokenAtual == '/'): 
            #DIMENSAO2 --> ε
            print('DIMENSAO2 --> ε')
            self.pilha.pop()
        else:
        #ERRO
            sys.exit('ERRO DIMENSAO2: simbolo nao reconhecido')

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
            print('SINAL --> ε')
            self.pilha.pop()
        else:
            #ERRO
            sys.exit('ERRO SINAL: simbolo nao reconhecido')

    def constante(self):
        if(self.tokenAtual == 'num_inteiro'):
            #CONSTANTE --> num_inteiro
            self.deriva(['num_inteiro'])
        elif(self.tokenAtual == 'num_real'):
            #CONSTANTE --> num_real
            self.deriva(['num_real'])
        else:
            #ERRO
            sys.exit('ERRO CONSTANTE: simbolo nao reconhecido')


print('Digite o código. Para compilar digite Ctrl+Z')
codigo = sys.stdin.read()
x = Parser() 
x.getListaTokenAndTabSimb(codigo)

x.fazAnalise()
from random import random
import matplotlib.pyplot as plt
import datetime

class Produto():
    def __init__(self, nome, espaco, peso, valor):
        self.nome = nome
        self.espaco = espaco
        self.peso = peso
        self.valor = valor
        
class Individuo():
    def __init__(self, espacos, pesos, valores, limite_espacos, limite_pesos, geracao=0):
        self.espacos = espacos
        self.pesos = pesos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.limite_pesos = limite_pesos
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.peso_usado = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
                
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        soma_pesos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                soma_pesos += self.pesos[i]
                soma_espacos += self.espacos[i]
                if (soma_pesos <= self.limite_pesos) and (soma_espacos <= self.limite_espacos):                    
                    nota += self.valores[i]
                else: 
                    nota = 1

        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
        self.peso_usado = soma_pesos
        
    def crossover(self, outro_individuo):
        corte = round(random()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.espacos, self.pesos, self.valores, self.limite_espacos, self.limite_pesos, self.geracao + 1),
                  Individuo(self.espacos, self.pesos, self.valores, self.limite_espacos, self.limite_pesos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        return self
        
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
                
    def inicializa_populacao(self, espacos, pesos, valores, limite_espacos, limite_pesos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, pesos, valores, limite_espacos, limite_pesos))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.nota_avaliacao
        return soma
    
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self):
        timeDiff = datetime.datetime.now() - startTime
        melhor = self.populacao[0]
        print("G:%s -> Valor: %s Espaço: %s  Peso: %s \n       Cromossomo: %s   Tempo: %s" % (self.populacao[0].geracao,
                                                               melhor.nota_avaliacao,
                                                               melhor.espaco_usado,
                                                               melhor.peso_usado,
                                                               melhor.cromossomo, 
                                                               str(timeDiff)))
    
    def resolver(self, taxa_mutacao, numero_geracoes, espacos, pesos, valores, limite_espacos, limite_pesos):
        self.inicializa_populacao(espacos, pesos, valores, limite_espacos, limite_pesos)
        
        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
        
        self.visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
            
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
            
            self.ordena_populacao()
            
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.nota_avaliacao)
            self.melhor_individuo(melhor)
        
        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Peso: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.espaco_usado,
               self.melhor_solucao.peso_usado,
               self.melhor_solucao.cromossomo))
        
        return self.melhor_solucao.cromossomo
        
        
if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 30, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 5, 2911.12))
    lista_produtos.append(Produto("Iphone 8", 0.0000899, 5, 3499.00))
    lista_produtos.append(Produto("TV 58' ", 0.398, 20, 1856.99))
    lista_produtos.append(Produto("TV 55' ", 0.286, 16, 1738.99))
    lista_produtos.append(Produto("TV 50' ", 0.274, 14, 1529.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 12.1, 1399.00))
    lista_produtos.append(Produto("Home Theater Blu-ray 3D", 0.200, 9.5, 2590.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 3, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.0796, 2.5, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 9.4, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 9.4, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 9, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 31, 1049.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 33, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.00498, 3, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.00527, 3, 3999.00))
    lista_produtos.append(Produto("Split 7000BTUs", 0.512, 25, 899.00))
    lista_produtos.append(Produto("Split 9000BTUs", 0.532, 28.7, 1244.00))
    lista_produtos.append(Produto("Split 12000BTUs", 0.580, 30, 1499.00))
    lista_produtos.append(Produto("Split 30000BTUs", 0.590, 35, 2499.00))
    lista_produtos.append(Produto("Lavadoura de roupas", 0.490, 35, 4499.00))
    espacos = []
    pesos = []
    valores = []
    nomes = []
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        pesos.append(produto.peso)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 3
    limitep = 300
    tamanho_populacao = 100
    taxa_mutacao = 0.01
    numero_geracoes = 100
    startTime = datetime.datetime.now()
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, espacos, pesos, valores, limite, limitep)
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print("Nome: %s Valor: %s Peso: %s " % (lista_produtos[i].nome,
                                             lista_produtos[i].valor, 
                                             lista_produtos[i].peso))
    #for valor in ag.lista_solucoes:
    #    print(valor)
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.show()
    
    

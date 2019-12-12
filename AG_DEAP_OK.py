import random
import numpy
from deap import base
from deap import creator
from deap import algorithms
from deap import tools
import matplotlib.pyplot as plt

class Produto():
    def __init__(self, nome, espaco, peso, valor):
        self.nome = nome
        self.espaco = espaco
        self.peso = peso
        self.valor = valor
        
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
valores = []
pesos = []
nomes = []
for produto in lista_produtos:
    espacos.append(produto.espaco)
    pesos.append(produto.peso)
    valores.append(produto.valor)
    nomes.append(produto.nome)
limite_volume = 3
limite_peso = 3

toolbox = base.Toolbox()
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual,toolbox.attr_bool, n=len(espacos))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def avaliacao(individual):
    nota = 0
    soma_espacos = 0
    soma_pesos = 0
    for i in range(len(individual)):
      if individual[i] == 1:
           nota += valores[i]
           soma_espacos += espacos[i]
           soma_pesos += pesos[i]
    if (soma_espacos > limite_volume) and (soma_pesos > limite_peso):
        nota = 1
    return nota / 100000,  #aqui coloquei a vírgula pois a minha funcao fitness também tem aquele espaco em branco após a virgula

toolbox.register("evaluate", avaliacao)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = 0.01)
toolbox.register("select", tools.selRoulette)


def plot_log(info):
    gen = info.select("gen")
    min = info.select("min")
    mean = info.select("med")
    max = info.select("max")

    fig, ax1 = plt.subplots()
    line1 = ax1.plot(gen, max, "b-", label="Max Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    ax2 = ax1.twinx()
    line2 = ax2.plot(gen, mean, "g-", label="Average Fitness")
    for tl in ax2.get_yticklabels():
        tl.set_color("g")

    ax3 = ax1.twinx()
    line3 = ax3.plot(gen, min, "y-", label="Min Fitness")
    ax3.set_ylabel("Size")
    for tl in ax3.get_yticklabels():
        tl.set_color("y")

    lns = line1 + line2 + line3
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    plt.show()

if __name__ == "__main__":
    random.seed(1)
    populacao = toolbox.population(n = 22)
    probabilidade_crossover = 1.0
    probabilidade_mutacao = 0.01
    numero_geracoes = 100
    
    estatisticas = tools.Statistics(key=lambda individuo: individuo.fitness.values)
    estatisticas.register("max", numpy.max)
    estatisticas.register("min", numpy.min)
    estatisticas.register("med", numpy.mean)
    estatisticas.register("std", numpy.std)
    
    
    
    populacao, info = algorithms.eaSimple(populacao, toolbox,
                                          probabilidade_crossover,
                                          probabilidade_mutacao,
                                          numero_geracoes, estatisticas)
    melhores = tools.selBest(populacao, 1)
    for individuo in melhores:
        print(individuo)
        print(individuo.fitness)
        #print(individuo[1])
        somav = 0
        somap = 0
        for i in range(len(lista_produtos)):
            if individuo[i] == 1:
                somap += pesos[i]
                somav += valores[i]
                print("Nome: %s Valor: %s Peso: %s" % (lista_produtos[i].nome,
                                                       lista_produtos[i].peso,
                                                       lista_produtos[i].valor))
        print("Melhor solução: Valor %s Peso %s" % (somav, somap))
        
    
    
    valores_grafico = info.select("max")
    plt.plot(valores_grafico)
    plt.title("Acompanhamento dos valores")
    plt.show()
    
     #Plota o Gráfico
    plot_log(info)













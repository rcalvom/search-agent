import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtpl
import random as rn
import copy
#from drawer import *

from numpy.lib.function_base import piecewise
#from drawer.models import laminate_dimensions

class GeneticAlgorithm:

    def __init__(self):
        self

    laminate_dimensions = [(8, 3), (5, 1), (2, 2), (1, 1), (9, 4), (6, 2), (4, 3), (7, 5), (3, 2), (4, 2)]

    areas = []
    chromosomes = []
    newGenes = []
    fullTable = []

    cutProb = 0.98
    mutProb = 0.1

    for piece in laminate_dimensions:
       areas.append(piece[0]*piece[1]) 

    for i in range(10):
        chromosomes.append(rn.choices([0, 1], k = 10))

    def zLineCalculus(self, chromosome, areas):
         
        z = np.multiply(chromosome, areas)
        z = sum(z)

        return z


    def tableCalculation(self, chromosomes, areas):
        
        zTotal = 0
        accumProb = 0
        fullTable = copy.deepcopy(chromosomes)

        for p in range(10):   
            if(len(fullTable[p]) != 10):
                fullTable[p] = fullTable[p][:10]
            z = np.multiply(fullTable[p], areas)
            z = sum(z)
            zTotal += z
            piecesQ = sum(fullTable[p]) 
            fullTable[p].append(piecesQ)
            fullTable[p].append(z)

        for chromosome in fullTable:
            localProb = chromosome[11]/zTotal
            chromosome.append(localProb)
            accumProb += localProb
            chromosome.append(accumProb)

        #print(fullTable)    

        return fullTable

    def parentSelection(self, fullTable, chromosomes, cutProb):

        no1 = rn.random()
        no2 = rn.random()
        actualCutProb = rn.random()
        cutting = True

        no1Chromosome = []
        no2Chromosome = []

        for x in range(10):
          if(no1 <= fullTable[x][13]):
            no1Chromosome = chromosomes[x]
            break

        for x in range(10):
          if(no2 <= fullTable[x][13]):
            no2Chromosome = chromosomes[x]
            break

        if(actualCutProb >= cutProb):
            cutting = False

        return no1Chromosome, no2Chromosome, cutting

    def cutProcedure(self, parentNo1, parentNo2):
        
        cutPoint = rn.random()
        intervalProb = (100/9)/100
        interval = 0

        newSon1 = []
        newSon2 = []

        for x in range(9):
            if(cutPoint < intervalProb*(x+1)):    
                interval = x +1
                break

        newSon1 = parentNo1[0:interval] + parentNo2[interval:10]
        newSon2 = parentNo2[0:interval] + parentNo1[interval:10]

        return newSon1, newSon2
    
    def mutProcedure(self, newBorn1, newBorn2, mutProb):

        alterations1 = []
        alterations2 = []
        indexes1 = []
        indexes2 = []

        for i in range(10):

            a = rn.random()
            b = rn.random()

            if(a < mutProb):
                alterations1.append(True)
            else:   alterations1.append(False)
            
            if(b < mutProb):
                alterations2.append(True)
            else:   alterations2.append(False)

        for w in range(10):
          if(alterations1[w]): indexes1.append(w)
          if(alterations2[w]): indexes2.append(w)


        if(len(indexes1) > 0):
            #print(len(newBorn1))
            for index in indexes1:
                newBorn1[index] = abs(newBorn1[index] - 1)

        if(len(indexes2) > 0):
            for index2 in indexes2:
                newBorn2[index2] = abs(newBorn2[index2] - 1)

        return newBorn1, newBorn2

    def getsAdded(self, son1, son2, newGenes, areas):

        length = len(newGenes)
        
        if(self.zLineCalculus(son1, areas) <= 100):
            newGenes.append(son1)
            length = len(newGenes)
        if(length != 10):
            if(self.zLineCalculus(son2, areas) <= 100):
                newGenes.append(son2)

        return newGenes


    def doGenetic(self, chromosomes, areas, cutProb, mutProb, newGenes):

        newGeneration = []

        while(len(newGeneration) < 10):
            
            presentGenes = self.tableCalculation(chromosomes, areas)
            parents = self.parentSelection(presentGenes, chromosomes, cutProb)

            if(parents[2]): 
                parents = self.cutProcedure(parents[0], parents[1])

            mutatedGenes = self.mutProcedure(parents[0], parents[1], mutProb)

            newGeneration = self.getsAdded(mutatedGenes[0], mutatedGenes[1], newGeneration, areas)

        newTable = self.tableCalculation(newGeneration,areas)

        return newGeneration, newTable

    def updateGen(self, future):
        self.chromosomes = copy.deepcopy(future)
    

class GeneticPieceAlgorithm:

    def __init__(self):
        self

    laminate_dimensions = [(8, 3), (5, 1), (2, 2), (1, 1), (9, 4), (6, 2), (4, 3), (7, 5), (3, 2), (4, 2)]

    laminateDisplay = np.zeros((10,10))
    areas = []
    inheritance = []
    newinheritance = []
    completeTable = []

    cutProb = 0.98
    mutProb = 0.1

    for piece in laminate_dimensions:
       areas.append(piece[0]*piece[1]) 

    for i in range(10):
        inheritance.append(rn.choices([0, 1], k = 3))




attempt = GeneticAlgorithm()
newBorns = []

for y in range(100):

    newBorns = attempt.doGenetic(attempt.chromosomes, attempt.areas, attempt.cutProb, attempt.mutProb, attempt.newGenes)
    if(y==0):
        for item in newBorns[1]:
            print(item)
    attempt.updateGen(newBorns[0])
    
    #newBorns = []

print("----------------------------------------------------------------")

for newBorns in newBorns[1]:
    print(newBorns)


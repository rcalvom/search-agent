import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtpl
import random as rn
import copy

from numpy.lib.function_base import disp, piecewise

currentPreTable = []
currentEndTable = []

class GeneticAlgorithm:

    def __init__(self):
        self

    laminate_dimensions = [(8, 3), (5, 1), (2, 2), (1, 1), (9, 4), (6, 2), (4, 3), (7, 5), (3, 2), (4, 2)]

    areas = []
    chromosomes = []
    newGenes = []
    fullTable = []
    doneTable = []

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
        zProm = 0
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

        zProm = zTotal/10

        for chromosome in fullTable:
            localProb = chromosome[11]/zTotal
            chromosome.append(localProb)
            accumProb += localProb
            chromosome.append(accumProb)

        #print(fullTable)    

        return fullTable, zProm

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

    def getsAdded(self, son1, son2, newGenes, areas, zProm):

        length = len(newGenes)
        zSon1 = self.zLineCalculus(son1, areas)
        zSon2 = self.zLineCalculus(son2, areas)
        
        if((zSon1 <= 100) and (zSon1 >= zProm)):
            newGenes.append(son1)
            length = len(newGenes)
        if(length != 10):
            if((zSon2 <= 100) and (zSon2 >= zProm)):
                newGenes.append(son2)

        return newGenes


    def doGenetic(self, chromosomes, areas, cutProb, mutProb, newGenes):

        newGeneration = []

        while(len(newGeneration) < 10):
            
            presentGenes = self.tableCalculation(chromosomes, areas)
            parents = self.parentSelection(presentGenes[0], chromosomes, cutProb)

            if(parents[2]): 
                parents = self.cutProcedure(parents[0], parents[1])

            mutatedGenes = self.mutProcedure(parents[0], parents[1], mutProb)

            newGeneration = self.getsAdded(mutatedGenes[0], mutatedGenes[1], newGeneration, areas, presentGenes[1])

        newTable = self.tableCalculation(newGeneration,areas)

        return newGeneration, newTable

    def updateGen(self, future):
        self.chromosomes = copy.deepcopy(future)

    def updateLastTable(self, futureTable):
        self.doneTable = copy.deepcopy(futureTable)
    

class GeneticPieceAlgorithm:

    def __init__(self):
        self

    laminate_dimensions = [(8, 3), (5, 1), (2, 2), (1, 1), (9, 4), (6, 2), (4, 3), (7, 5), (3, 2), (4, 2)]

    laminateDisplay = np.zeros((10,10))
    areas = []
    inheritance = []
    newinheritance = []
    completeTable = GeneticAlgorithm.doneTable
    beginTable = GeneticAlgorithm.chromosomes
    zeds = []
    fitnessMeasure = 0


    optimized =  False

    for piece in laminate_dimensions:
       areas.append(piece[0]*piece[1]) 

    def pieceAssignment(self, table, genomesTable):

        if(len(self.zeds) == 0):
            for piece in table:
                self.zeds.append(piece[11])

        bestZed = max(self.zeds)    

        bestZedIndex = self.zeds.index(bestZed)

        self.zeds.pop(bestZedIndex)

        takenGenome = genomesTable[bestZedIndex]

        for i in range(10):

            actualPiece = self.laminate_dimensions[i]
            xMargin = 10 - actualPiece[0]
            yMargin = 10 - actualPiece[1]

            xCor =  rn.randrange(xMargin + 1)
            yCor =  rn.randrange(yMargin + 1)

            used = takenGenome[i]

            orientation = rn.randint(0, 1)

            if orientation == 1:
                wholeGen = [xCor, yCor, orientation, used]
            else: wholeGen = [yCor, xCor, orientation, used]

            

            self.inheritance.append(wholeGen)

        return bestZedIndex, bestZed

    

    def piecePlacement(self, genomePieces, display):

        for x in range(10):

            actualDimension = self.laminate_dimensions[x]
            prefixOrientation = ""
            treatingChromosome = genomePieces[x]

            if(actualDimension[0] >= actualDimension[1]):
                prefixOrientation = "wide"
            else: prefixOrientation = "long"

            if(treatingChromosome[3] == 1):
                for i in range(actualDimension[0]):
                    for j in range(actualDimension[1]):
                        if((treatingChromosome[2] == 1) and (prefixOrientation == "wide")):
                            display[treatingChromosome[0]+ i][treatingChromosome[1] + j] +=  x + 1
                        elif((treatingChromosome[2] == 1) and (prefixOrientation == "long")): 
                            display[treatingChromosome[0]+ j][treatingChromosome[1] + i] +=  x + 1
                        elif((treatingChromosome[2] == 0) and (prefixOrientation == "wide")):
                            display[treatingChromosome[0]+ j][treatingChromosome[1] + i] +=  x + 1
                        elif((treatingChromosome[2] == 0) and (prefixOrientation == "long")): 
                            display[treatingChromosome[0]+ i][treatingChromosome[1] + j] +=  x + 1
            
    def areaCalculus(self, display):

        uncoveredArea = np.count_nonzero(display)

        usedArea = 100 - uncoveredArea

        return usedArea

    def runPosition(self, beginTable, completeTable, factGenomes, display):

        zComparisson = self.pieceAssignment(completeTable, beginTable)[1]

        self.piecePlacement(factGenomes, display)

        usedArea = self.areaCalculus(display)

        if(usedArea == zComparisson):
            optimized = True

        return usedArea, zComparisson    



    
attempt = GeneticAlgorithm()
newBorns = []
finalGen = []

for y in range(3):

    newBorns = attempt.doGenetic(attempt.chromosomes, attempt.areas, attempt.cutProb, attempt.mutProb, attempt.newGenes)
    if(y==0):
        print("Primera generación:")
        for item in newBorns[1][0]:
            print(item)
    finalGen = attempt.updateGen(newBorns[0])
print("--------------------------------------------------------------------")
attempt.updateLastTable(newBorns[1][0])
print("Ultima generación:")
for item in newBorns[1][0]:
    print(item)

print("--------------------------------------------------------------------")

assingation = GeneticPieceAlgorithm()

for g in range(150):

    fitnessCheck = assingation.runPosition(attempt.chromosomes, attempt.doneTable, assingation.inheritance, assingation.laminateDisplay)

    if(fitnessCheck[0] > (fitnessCheck[1])*0.57): 
        print("Intento #" + str(g))
        break
    assingation.laminateDisplay = np.zeros((10,10))
    assingation.inheritance = []

print("**********************************************************")

plt.imshow(assingation.laminateDisplay)
plt.colorbar()
plt.show()    

finalGen = []
newBorns = []
attempt.newGenes = []
attempt.doneTable = []


# -*- coding: utf-8 -*-

import os
import numpy as np
import operator #used to use the method itemGetter

criteriaList = list() #list of the criterias
pvList = list() #list of PV of the criterias
goalList = list() #list of the goals(in this case is ot required a list because we defined just one goal but it could be used in future development)

def checkMatrix(matrix):#calculate the reciprocal number in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 0:
               matrix[i][j] = 1/matrix[j][i]
    return matrix
 
def consistencyCheck(element):
    element['CI'] = (element['lambdamax'] - len(listOfAlternatives))/(len(listOfAlternatives)-1)
    element['CR'] = (element['CI']/(float(RCIvalues[len(listOfAlternatives)-1])) )                

for filename in os.listdir("CriteriaAlternatives"): #takes all the files in the folder of criterias
    criteriaElement = dict() #single criteria
    criteriaElement['name'] = filename.replace('.txt','')
    criteriaElement[filename] = np.loadtxt(fname= (os.getcwd()+'\\CriteriaAlternatives\\' + filename))
    criteriaElement[filename] = checkMatrix(criteriaElement[filename]) #contains the matrix of the criteria linked with the name of the criteria
    criteriaSum = np.sum(criteriaElement[filename], axis =0) #sum of the line of the matrix
    criteriaNormalized = criteriaElement[filename] /criteriaSum #normalization of the matrix
    criteriaPV = np.mean(criteriaNormalized, axis = 1) #calculation of the PV
    criteriaElement['PV'] = criteriaPV #saving the PV
    criteriaElement['lambdamax'] = criteriaSum.dot(criteriaPV) #save the lambdamax
    criteriaList.append(criteriaElement) #adding the element in the list of criteria
    
for filename in os.listdir("CriteriaVersusGoal"): #takes all the files in the folder of goals
    goalElement = dict() #single goal
    goalElement['name'] = filename.replace('.txt','')
    goalElement[filename] = np.loadtxt(fname= (os.getcwd()+'\\CriteriaVersusGoal\\' + filename))
    goalElement[filename] = checkMatrix(goalElement[filename]) #contains the matrix of the goal linked with the name of the goal
    goalSum = np.sum(goalElement[filename], axis =0) #sum of the line of the matrix
    goalNormalized = goalElement[filename] /goalSum #normalization of the matrix
    goalPV = np.mean(goalNormalized, axis = 1)  #calculation of the PV
    goalElement['PV'] = goalPV #saving the PV
    goalElement['lambdamax'] = goalSum.dot(goalPV) #save the lambdamax
    goalList.append(goalElement) #adding the element in the list of goal
    
# ==== create the matrix of PV
for el in criteriaList: 
   pvList.append(el['PV'])#add PV to a list
       
pvMatrix =np.array(pvList) #list of PV is converted into a NUMPY array
pvMatrixTransposed = pvMatrix.transpose()   #the array is transposed
# =============================================================================
fp = pvMatrixTransposed.dot(goalList[0]['PV']) 

fhand = open('Alternatives.txt') #open the file that contains the name of alternatives
for line in fhand: #slide the file line by line
    listOfAlternatives =(line.split(',')) #split a line in subparts

result = dict() #chart of the results
for k in range(fp.shape[0]):
    result[listOfAlternatives[k]] = fp[k]
    
bestAlternative = max(result.items(), key=operator.itemgetter(1))[0] #best alternative with highest PV

print('The best alternative is the alternative '+ bestAlternative)

fhand = open('RCIvalues.txt')
for line in fhand:
    RCIvalues = (line.split(','))
    
for el in criteriaList: #Consistency Check for the Criterias
    consistencyCheck(el)
    if not el['CR'] >= 0.10:
        print(el['name']+" Consistency OK")
    else:
        print(el['name']+" Revise the comparison matrix")
    
for el in goalList: #Consistency Check for the Goal
    consistencyCheck(el)
    if not el['CR'] >= 0.10:
        print(el['name']+" Consistency OK")
    else:
        print(el['name']+" Revise the comparison matrix")




    
    
    
    
    
    
    
    
    
    
    
    
    
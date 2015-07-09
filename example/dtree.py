# coding:gbk

from math import log
import operator
 
'''��⵱ǰ���ݼ����������Ӽ�������ũ�أ�ShannonEntropy��'''
def clacShannonEnt(dataSet):
    numEntries = len(dataSet)    #���������
    labelCounts = {}             #Ϊÿ��label�����������������������м���
    '''Ϊ���п��ܷ��ഴ���ֵ�'''
    for featVec in dataSet:
        currentLabel = featVec[-1]   #��ȡ��ǰ�����ı�ǩ
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        '''��2Ϊ�� �����'''
        shannonEnt -= prob*log(prob, 2)
    return shannonEnt   #�� H

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,0,'yes'],
               [0,1,'no'],
               [0,0,'no']
               ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels
 
 
'''������'''
myDat,labels = createDataSet()
print myDat
print clacShannonEnt(myDat)

def splitDataSet(dataSet, axis, value):
    retDataSet = []         #�����µ�list����
    for featVec in dataSet:
        if featVec[axis] == value:
            '''���������������ݳ�ȡ��������ȥ�������������ݼ�������'''
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


'''����'''
myDat,labels = createDataSet()
print splitDataSet(myDat, 0, 1)  #0������Ӧ��1ֵ����
print splitDataSet(myDat, 0, 0)  #0������Ӧ��0ֵ����




'''ѡ����õ����ݼ����ַ�ʽ'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) -1         #����������
    baseEntropy = clacShannonEnt(dataSet)    #�����ʼ���ݼ�����
    bestInfoGain = 0.0; bestFeature = -1;    #����best��Ϣ���棬best����
    for i in range(numFeatures):
        #����Ψһ�ķ����ǩ�б�
        featList = [example[i] for example in dataSet]  #i��Ӧ����������������ȡֵ���б�
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
        #����ÿ�ֻ��ַ�ʽ����Ϣ��
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*clacShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            '''������õ���Ϣ����'''
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


'''����'''
myDat,labels = createDataSet()
print chooseBestFeatureToSplit(myDat)


'''��������ķ���������Ҷ�ӽڵ�ķ���'''
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
  
  
  
'''�������ĺ�������'''
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  #��ȡ�������������б�
    if classList.count(classList[0]) == len(classList): #������classList[0]����Ŀ��classList���б���һ���󣬼����ݼ��е������ȫ��ͬ -> ֹͣ�������֣���������
        return classList[0]
    if len(dataSet[0]) == 1:    #���ݼ�����Ϊ1��Ҳ�������������־��ѽ��У��б���ֻʣ��"���"����ʱʹ�ö�������ķ���������Ҷ�ӽڵ�ķ���
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)   #��ǰ���ݼ�ѡȡ���������
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}  #�洢������Ϣ
    
    '''�õ��б������ ��������ֵ '''
    del(labels[bestFeat])    #�Ƴ����滮�����õ�����
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    
    
    '''������ǰѡ������������ ��������ֵ ����ÿ�����ݼ������ϵݹ���ú���createTree(),
                    �õ��ķ���ֵ�������뵽�ֵ����myTree�У���˺�����ִֹ��ʱ���ֵ��н���Ƕ�׺ܶ����Ҷ�ӽڵ���Ϣ���ֵ�����'''
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat,value), subLabels)
    return myTree

'''����'''
myDat,labels = createDataSet()
myTree = createTree(myDat, labels)
print myTree 

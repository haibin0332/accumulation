# coding:gbk

from math import log
import operator
 
'''求解当前数据集（或数据子集）的香农熵（ShannonEntropy）'''
def clacShannonEnt(dataSet):
    numEntries = len(dataSet)    #获得样本数
    labelCounts = {}             #为每个label（特征）包含的样本数进行计数
    '''为所有可能分类创建字典'''
    for featVec in dataSet:
        currentLabel = featVec[-1]   #获取当前样本的标签
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        '''以2为底 求对数'''
        shannonEnt -= prob*log(prob, 2)
    return shannonEnt   #即 H

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,0,'yes'],
               [0,1,'no'],
               [0,0,'no']
               ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels
 
 
'''输出结果'''
myDat,labels = createDataSet()
print myDat
print clacShannonEnt(myDat)

def splitDataSet(dataSet, axis, value):
    retDataSet = []         #创建新的list对象
    for featVec in dataSet:
        if featVec[axis] == value:
            '''将符合特征的数据抽取出来，并去掉用来划分数据集的特征'''
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


'''测试'''
myDat,labels = createDataSet()
print splitDataSet(myDat, 0, 1)  #0特征对应的1值划分
print splitDataSet(myDat, 0, 0)  #0特征对应的0值划分




'''选择最好的数据集划分方式'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) -1         #特征的数量
    baseEntropy = clacShannonEnt(dataSet)    #计算初始数据集的熵
    bestInfoGain = 0.0; bestFeature = -1;    #定义best信息增益，best特征
    for i in range(numFeatures):
        #创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]  #i对应的特征的所有样本取值的列表
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
        #计算每种划分方式的信息熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*clacShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            '''计算最好的信息增益'''
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


'''测试'''
myDat,labels = createDataSet()
print chooseBestFeatureToSplit(myDat)


'''多数表决的方法决定该叶子节点的分类'''
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
  
  
  
'''创建树的函数代码'''
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  #获取所有样本的类列表
    if classList.count(classList[0]) == len(classList): #如果类别classList[0]的数目和classList的列表长度一样大，即数据集中的类别完全相同 -> 停止继续划分，返回类型
        return classList[0]
    if len(dataSet[0]) == 1:    #数据集长度为1，也即所有特征划分均已进行，列表中只剩下"类别"，此时使用多数表决的方法决定该叶子节点的分类
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)   #当前数据集选取的最好特征
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}  #存储树的信息
    
    '''得到列表包含的 所有属性值 '''
    del(labels[bestFeat])    #移除上面划分所用的特征
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    
    
    '''遍历当前选择特征包含的 所有属性值 ，在每个数据集划分上递归调用函数createTree(),
                    得到的返回值将被插入到字典变量myTree中，因此函数终止执行时，字典中将会嵌套很多代表叶子节点信息的字典数据'''
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat,value), subLabels)
    return myTree

'''测试'''
myDat,labels = createDataSet()
myTree = createTree(myDat, labels)
print myTree 

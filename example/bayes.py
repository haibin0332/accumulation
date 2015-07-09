# -*- coding:utf-8 -*-

from numpy import *

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 表示侮辱性言语, 0 表示非侮辱性言语
    return postingList,classVec

'''创建词汇表'''
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets  #去掉重复的词
    return list(vocabSet)

'''设置词向量'''
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)    #创建一个其中所含元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec
  

'''查看loadDataSet() createVocabList(dataSet)的执行效果'''
 
#print myVocabList

'''查看setOfWords2Vec()的运行效果'''
#print setOfWords2Vec(myVocabList, listOPosts[0])
#print setOfWords2Vec(myVocabList, listOPosts[3])


'''朴素贝叶斯分类器训练函数'''
'''trainMatrix:文档矩阵'''
'''trainCategory:文档类别标签构成的向量'''
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)   # 总文档数：6
    numWords = len(trainMatrix[0])    # 文档1的长度：32
    pAbusive = sum(trainCategory)/float(numTrainDocs)   # 训练文档中,属于侮辱类型的概率：3/6.0, 3个文档为类型1,即侮辱类的文档
    p0Num = zeros(numWords); p1Num = zeros(numWords)    # 初始化概率
    p0Denom = 0.0; p1Denom = 0.0                        
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            #向量相加
            p1Num += trainMatrix[i]          #类别1的分子，是个词向量，最后值为：在侮辱类文档，词表中各个词出现的次数
            p1Denom += sum(trainMatrix[i])   #类别1的分母，是个常数，表示每个侮辱类文档中出现的词数的总和
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    #对每个元素作除法
    p1Vect = p1Num/p1Denom   #属于侮辱类文档时，每个词出现的概率，即p(w0|c1),p(w1|c1),p(w2|c1)···
    p0Vect = p0Num/p0Denom   #属于非侮辱类文档时，每个词出现的概率，即p（w0|c0）,p(w1|c1),p(w2|c1)···
    return p0Vect,p1Vect,pAbusive

listOPosts, listClasses = loadDataSet()
myVocabList = createVocabList(listOPosts)  
  
trainMat = []
for postinDoc in listOPosts:
    trainMat.append(setOfWords2Vec(myVocabList, postinDoc))  #将文档转换为词向量

p0V, p1V, pAb = trainNB0(trainMat,listClasses)   #训练算法
#print pAb
#print p0V
#print p1V


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0


'''测试函数'''
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)

'''调用测试函数'''
testingNB()

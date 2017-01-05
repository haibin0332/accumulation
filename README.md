#important notes

1) tools

DM/ML training 

http://scikit-learn.org/stable/

python scipy numpy quick look

http://docs.scipy.org/doc/numpy/genindex.html

http://sebug.net/paper/books/scipydoc/numpy_intro.html

2) code

python re

http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

http://www.cnblogs.com/gsblog/p/3342843.html

python thread

http://www.cnblogs.com/huxi/archive/2010/06/26/1765808.html


python logistic regression

http://blog.csdn.net/zouxy09/article/details/20319673

SVM tutorial

http://blog.csdn.net/v_july_v/article/details/7624837

http://blog.csdn.net/abcjennifer/article/details/7849812

HMM

http://www.52nlp.cn/category/hidden-markov-model/page/4

ML code analysis

http://www.zyh1690.org/the-machine-learning-based-on-machine-learning-2/

3) NLP

LDA

http://www.52nlp.cn/lda-math-lda-%E6%96%87%E6%9C%AC%E5%BB%BA%E6%A8%A1

http://blog.csdn.net/v_july_v/article/details/41209515

http://cos.name/2013/01/lda-math-beta-dirichlet/

http://blog.csdn.net/yangliuy/article/details/8302599

Stanford Chinese character parsing

http://blog.csdn.net/cuixianpeng/article/details/16864785

Dependency relations

http://wiki.opencog.org/w/Dependency_relations

http://www.xperseverance.net/blogs/2012/03/510/



我用GET浏览文章，不管浏览多少次，那篇文章还在那，没有变化.
我用PUT修改一篇文章，然后在做同样的操作，每次操作后的结果并没有不同.
POST重复加载问题：当我们多次发出同样的POST请求后，其结果是创建出了若干的资源.


get用来告诉服务器需要获取哪些内容（uri+query），
向静态页面（uri）请求则直接返回文件内容给浏览器，向一个动态页面请求时可以提供查询参数（query）以获得相应内容。
post用来向服务器提交内容，主要是为了提交，而不是为了请求内容，就是说post的初衷并不要求服务器返回内容，
只是提交内容让服务器处理（主要是存储或者处理之后再存储）。
get和post出现混淆是因为对提交的数据处理方法的滥用造成的，数据是无辜的。


一个URL地址，它用于描述一个网络上的资源，而HTTP中的GET，POST，PUT，DELETE就对应着对这个资源的查 ，改 ，增 ，删 4个操作。


Java静态对象和非静态对象有什么区别
                          静态对象                                                       非静态对象     
拥有属性：               是类共同拥有的                                             是类各对象独立拥有的
内存分配：              内存空间上是固定的                                      空间在各个附属类里面分配 
分配顺序：              先分配静态对象的空间                    继而再对非静态对象分配空间,也就是初始化顺序是先静态再非静态.


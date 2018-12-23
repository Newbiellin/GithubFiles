# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:08:24 2018

@author: a7720
"""

class Node():
    def __init__(self, item):
        self.item = item   #结点数值
        self.isin = False  #用于判断是否已经提取
        self.left = None
        self.right = None
        

#构建哈夫曼树,计算出最小值
class HuffmanTree():
    def __init__(self, l):
        self.li = []
        for x in range(0, len(l)):
            self.li.append(Node(l[x]))
        k = Node(float('inf'))
        while len(self.li) < 2 * len(l) - 1:
            m1 = m2 = k  #用于获取两个最小结点
            for x in range(0, len(self.li)):
                if m1.item > self.li[x].item and (self.li[x].isin is False):
                    m2 = m1
                    m1 = self.li[x]
                elif m2.item > self.li[x].item and (self.li[x].isin is False):
                    m2 = self.li[x]
            
            newNode = Node(m1.item + m2.item)  #建立新结点左右小孩为获取的最小结点
            newNode.right = m1
            newNode.left = m2
            self.li.append(newNode)
            m1.isin = m2.isin = True
            print ('m1=%d m2=%d m1+m2=%d' % (m1.item, m2.item, newNode.item))
            
if __name__ =='__main__':
    Node1=[20,11,14,6,32,41,23,19]
    t=HuffmanTree(Node1)
    print ('success')
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 22:34:09 2018

@author: a7720
"""

#寻找全部路径
def searchGraph(graph, start, end):
    results =[]
    generatePath(graph, [start], end, results)
    results.sort(key =lambda x:len(x))
    return results

def generatePath(graph, path, end, results):
    state = path[-1]
    if state == end:
        results.append(path)
    else:
        for temp in graph[state]:
            if temp not in path:
                generatePath(graph, path + [temp], end, results)
                
#对于无权值图可用
def findShortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if not shortest or len(newpath) < len(shortest):
                shortest = newpath
                print(shortest)
                
    return shortest

#计算出最小距离
#分别在只允许经过某个点k的情况下，更新点和点之间的最短路径
def FloydWarshall(graph):
    for k in graph.keys():      # 不断试图往两点i,j之间添加新的点k，更新最短距离
        for i in graph.keys():
            for j in graph[i].keys():
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    return graph

                
if __name__ =='__main__':
#    Graph={'A':['B','C','D'],
#           'B':['E'],
#           'C':['D','F'],
#           'D':['B','E','G'],
#           'E':[],
#           'F':['D','G'],
#           'G':['E']}
#    r = searchGraph(Graph, 'A', 'E')
#    r = findShortestPath(Graph, 'A', 'E')
#    print("******************")
#    print(' path A to E')
#    print("******************")
#    for i in r:
#        print(i)
        
    INF = 999
    G = {1:{1:0,    2:2,    3:6,    4:4},
          2:{1:INF,  2:0,    3:3,    4:INF},
          3:{1:7,    2:INF,  3:0,    4:1},
          4:{1:5,    2:INF,  3:12,   4:0}
          }

    processedGraph = FloydWarshall(G)
    for temp in processedGraph.keys():
        print(processedGraph[temp].values())
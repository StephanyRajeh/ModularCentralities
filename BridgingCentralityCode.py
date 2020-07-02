"""
Based on the article: Hwang, W., Cho, Y. R., Zhang, A., & Ramanathan, M. (2006, March). Bridging centrality: identifying bridging nodes in scale-free networks. 
In Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining (pp. 20-23).
"""


# ---------------------------------------------- Helper functions -----------------------------------------------------
from networkx.algorithms.centrality import *

def getNeighborsOfEachNode(g):
    dict_neighbors=dict()
    for i in g:
        dict_neighbors[i]=[]
        for j in g[i]:
            dict_neighbors[i].append(j)
    return dict_neighbors


def degree_conf(g):
    #list_nodes = g.nodes ()  # list of nodes
    dict_degree = dict()  # nodes and their degree centrality

    for i in g:
        dict_degree[i] = len(g[i])

    return dict_degree


# ---------------------------------------------- Main functions -----------------------------------------------------
def bridging_centrality(g):
	n = getNeighborsOfEachNode(g) # call external function

	dict_deno = {}
	deno = list()	
	
	dict_deg = {}
	dict_deg = degree_conf(g)
	
	dict_bet = {}
	dict_bet = betweenness_centrality(g)
	
	for i in n: # for each node
		for j in n[i]: # for each of its neighbors
			x = 1/dict_deg[j]
			deno.append(x)
		dict_deno[i] = deno
		deno = list()  # empty list for new node


	sum_temp = 0
	dict_deno_sum = {}
	for i in dict_deno:
		dict_deno_sum[i]=0
		for j in dict_deno[i]:
			sum_temp = j + sum_temp
		dict_deno_sum[i]= sum_temp
		sum_temp=0
        
        
	bridgecoeff = {}
	for i in n: # for each node
		bridgecoeff[i]= (1/dict_deg[i])/dict_deno_sum[i]

    
	dict_bridgecentrality = {}
	for i in n:
		dict_bridgecentrality[i]=bridgecoeff[i]*dict_bet[i]
        
	return dict_bridgecentrality
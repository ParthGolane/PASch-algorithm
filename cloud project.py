#!/usr/bin/env python
# coding: utf-8

# In[1]:


from hashlib import md5
from bisect import bisect
import numpy as np

class Ring(object):
    #initialize the variables
    #ring is of size 5
    
    def __init__(self, server_list, num_replicas=5):
        nodes = self.generate_nodes(server_list, num_replicas)
        hnodes = [self.hash(node) for node in nodes]
        hnodes.sort()

        self.num_replicas = num_replicas
        self.nodes = nodes
        self.hnodes = hnodes
        self.nodes_map = {self.hash(node): node.split("-")[1] for node in nodes}

    @staticmethod
    def hash(val):
        m = md5(val.encode())
        return int(m.hexdigest(), 16) 

    @staticmethod
    #function that generate nodes and return it back to init
    def generate_nodes(server_list, num_replicas):
        nodes = []
        for i in range(num_replicas):
            for server in server_list:
                nodes.append("{0}-{1}".format(i, server))
        return nodes
    #
    def get_node(self, val):
        pos = bisect(self.hnodes, self.hash(val))
        if pos == len(self.hnodes):
            return self.nodes_map[self.hnodes[0]]
        else:
            return self.nodes_map[self.hnodes[pos]]


server_list = ["127.0.0.1", "127.0.0.2", "127.0.0.3","127.0.0.4","127.0.0.5"]
threshold={"127.0.0.1":3, "127.0.0.2":4, "127.0.0.3":5, "127.0.0.4":2, "127.0.0.5":6}
inputs=input("enter package name")
worker=[]
if inputs !="0":
    j=0
    ring = Ring(server_list)
    for i in range(0,2):
        a=inputs+str(j)
        b=(ring.get_node(a))
        j+=20
        d=(threshold.get(b))
        if d not in worker:
            worker.append(b)
        else:
            worker.append((ring.get_node(a+str(30))))
    print(threshold)
    print(worker)
    if threshold.get(worker[0])> threshold.get(worker[-1]):
        A=worker[0]
        threshold[A]=(threshold.get(A))-1
    else:
        A=worker[-1]
        threshold[A]=(threshold.get(A))-1
    print(A)
    print(threshold)
    if threshold.get(A)!=0:
        threshold[A]=(threshold.get(A))-1
else:
    key_list = list(threshold.keys())
    val_list = list(threshold.values())
    position = val_list.index(min(val_list))
    print(key_list[position])    


# In[ ]:





# In[ ]:





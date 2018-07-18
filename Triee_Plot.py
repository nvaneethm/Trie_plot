import pydot
import pickle


with open('wordlist.pkl', 'rb') as inputfile:
     words = pickle.load(inputfile)


class TrieNode(object):
    def __init__(self, char:str):
        self.char = char
        self.children = []
        self.wordFinished = False
        self.counter = 1
        self.num = 0


def addword(root, word:str):
    node = root
    #print(word)
    cc = root.num
    pr = node
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                found_in_child = True
                child.counter += 1
                cc += 1
                node.num = cc
                node = child
                break
        
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
            cc += 1
            node.num = cc
            gnode = pydot.Node(pr.char+"."+str(pr.counter)+"."+str(pr.num))
            G.add_node(gnode)
            #print(pr.num)
            pr = node
    cc += 1
    node.num = cc
    gnode = pydot.Node(pr.char+"."+str(pr.counter)+"."+str(pr.num))
    G.add_node(gnode)
    #print(pr.num)
    node.wordFinished = True


def plotgr(root):
    if root.children:
        for i in root.children:
            if i.char:
                edge = pydot.Edge(root.char+"."+str(root.counter)+"."+str(root.num),i.char+"."+str(i.counter)+"."+str(i.num))
                G.add_edge(edge)
                plotgr(i)



root = TrieNode("+")
wordList = words[:100]
G= pydot.Dot(graph_type = "digraph")
completed = 0.0
for i in wordList:
    addword(root, i)
    completed += 1.0
    perc = completed / len(wordList)
    if (perc*100)%5 == 0:
        print(str(perc*100.0)+"%")


plotgr(root)

G.write_jpg("malayalam.jpg")
'''
from IPython.display import Image,display
ln = Image(G.create_jpg())
display(ln)
'''




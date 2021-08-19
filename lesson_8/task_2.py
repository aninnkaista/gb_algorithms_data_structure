from collections import Counter
stroka = "beep boop beer!"
# to count each element and arrange them in a dict sorted by values asc
count_els = sorted(dict(Counter(stroka)).items(), key=lambda x: x[1])

# to create a tree class of elements
class Node:
    """"Node class to add nodes for symbols and their frequences"""
    def __init__(self, symbol, freq=None, right=None, left=None, code = ''):        
        self.symbol = symbol
        self.freq = freq
        self.right = right
        self.left = left
        self.code = code
        
        
class Tree:
    """To create Huffman tree"""    
    def __init__(self, init_string):
        """To create initial dict of all nodes from string els and freqs"""
        string_counter = Counter(init_string)
        self.heap_list = [Node(i, string_counter[i]) for i in string_counter]
        self.huf_tree = self.huffman_tree()
        self.hashed_symbols = dict()
        self.add_hashed_symbols(self.huf_tree)
    
    def huffman_tree(self):
        """To create huffman tree as a list out of heap dict"""
        huf_tree = self.heap_list.copy()
        while len(huf_tree) > 1:
            
            # take 2 smallest nodes out from the huf tree, add code values as str
            left_node = huf_tree.pop(huf_tree.index(
                min(huf_tree, key=lambda x: x.freq)))
            left_node.code = '0'
            right_node = huf_tree.pop(huf_tree.index(
                min(huf_tree, key=lambda x: x.freq)))
            right_node.code = '1'
                       
            # create new node from them
            new_node = Node(left_node.symbol+right_node.symbol, 
                            freq=left_node.freq+right_node.freq,
                            left=left_node, right=right_node)                  
            # append new node
            huf_tree.append(new_node)
        # to unpack element from the common list, it is not necessary anymore
        huf_tree = huf_tree[0]
        return huf_tree         
   

    def add_hashed_symbols(self, huf_tree=None, exist_code = ''):
        """To return hashed string for given symbols"""
        # huffman code for the node
        if huf_tree == None:
            huf_tree = self.huffman_tree()
        node_code = exist_code + str(huf_tree.code)
        
        # to go through all nodes with recursion till it reaches leaves 
        if huf_tree.left:
            self.add_hashed_symbols(huf_tree.left, node_code)
        if huf_tree.right:
            self.add_hashed_symbols(huf_tree.right, node_code)
        # else if it is leave huf_tree than return the value
        if not huf_tree.left and not huf_tree.right:
            self.hashed_symbols[huf_tree.symbol] = node_code



huf_tree = Tree(stroka)
# resulting output
huf_output = huf_tree.hashed_symbols

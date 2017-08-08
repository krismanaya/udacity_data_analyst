
############################# QUESTION 1 #############################

"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.

"""

### step 1 - check if 't' is an anagram ### 

def check_if_anagram(string_1, string_2): 

	""" anagram - a word, phrase, or name formed by 
	   rearranging the letters of another, 
	   such as cinema, formed from iceman. """

	return sorted(string_1) == sorted(string_2)

### step 2 - check if 't' is a substring of 's' ### 

assert True == check_if_anagram('da', 'ad')

def question1(s,t): 

	"""
	to check if 't' is in 's' we need 
	to check if each letter is in 's'.

	"""

	### create lenght of 's' & 't' for index.
	lenght_of_s = len(s)
	length_of_t = len(t)

	### need to make sure the index is the size of 's'. 
	### +1 will give me the proper python index.
	index = range(lenght_of_s - length_of_t + 1)

	### iterate through the index 
	for number in index: 
		### print s[number: number + length_of_t] sanity check for re ordering. 
		### check if the groups of lenght 't' are a substring anagram of 's'.
		if check_if_anagram(s[number: number + length_of_t],t) == True: 
			return True 
	return False  

### Test Cases 
def test():
	assert True == question1('udacity', 'ad')
	assert True == question1('udacity', 'city')
	assert False == question1('udacity', 'and')
	assert False == question1('udacity', "#$224")
	print "Sure, okay."

### run test
test()

############################# QUESTION 2 #############################

"""
Question 2
Given a string 'a', find the longest palindromic substring contained in 'a'. 
Your function definition should look like question2(a), and return a string.

"""

### step 1 - check if 'string' is a palidrome###

def palindromic(string): 

	### want to make all the strings lower, create a storage facility 
	if string == None: 
		return None 

	if string == '': 
		return ''

	else: 

        ### want to make all the strings lower, create a storage facility 
		string = string.lower()
		store_palindromes = []
		index = range(len(string))

		### iterate through the index and the character
		### complexity time for this is O(n^2). 
		### challenging problem for me. 

		for number in index:
		
			character = range(0,number)
			for char in character: 
				
				### this is a Naive solution 
				### by keeping track of the longest i've seen so far. 
				### then appending it to my store_palindroms
			
				search_palindrome = string[char: number + 1]
				if search_palindrome == search_palindrome[::-1]:
					store_palindromes.append(search_palindrome)
		return store_palindromes


### step 2 - find longest palidromic substring of 'a' ### 

def question2(a): 
	"""
	to find the longest palidromic substring 
	we need to split 'a' and then check each word. 
	Was only able to achieve Naive approach of O(n^3).
	There is obviously a better solution but I can't 
	wrap my head around it. It actually took me a long 
	time to actually understand what the question was
	asking. 

	"""
	
	### here comes the next n solution 
	### I loop through and look for the greedy approach. 
	### then print out the max solution. 
	
	palindrome = palindromic(a)
	max_palindrome = " "

	if palindromic(a) == None: 
		return None

	for char in palindrome: 
		if len(char) > len(max_palindrome): 
			max_palindrome = char
	return max_palindrome
	
### Test Case 
def test():

	assert "madam" ==  question2("madammmdd")
	assert "adcbbcda" == question2("ABCBACADCBBCDA")
	assert "aaaaaa" == question2('aaaaaa')
	assert None == question2(None)
	assert type('') == type(question2(''))
	print "Sure, okay."


### run test
test()


############################# QUESTION 3 #############################

"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the 
smallest possible total weight of edges. Your function should take in 
and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}


"""
### skip for now.  

class graph(object):
    """
    This Class is a helper for question 3 and it 
    containts a graph that may getedges and vertices. 
    the edge instance is complexity O(n^2), which may be slower
    for larger graphs but in this case it gets the job done. 
    
    """ 
    def __init__(self):
        self.graph = dict()

    def getvertices(self): 
        return set(self.graph.keys())


    def getedges(self):
        edges = set()
        for vertex in self.graph.keys():
            for edge_weight in self.graph[vertex]:
                edges.add((edge_weight[1], vertex, edge_weight[0]))
        return sorted(edges)


def question3(G): 

	### gives me the nothing i want. 
    if not G:
        return None

    ### make a tree that is connected only to itsel. 
    graph_tree = {vertex: vertex for vertex in G.graph}

    ### collect all the weights and edges of tree. 
    edges = G.getedges()

    ### make the mst. 
    minimum_span_tree = dict() 

    ### here we check all the conditions of vertexs. 
    for weights, vertex_1, vertex_2 in edges: 
        if graph_tree[vertex_1] != graph_tree[vertex_2]: 
            graph_tree[vertex_2] = graph_tree[vertex_1]
            minimum_span_tree[vertex_1] = [(vertex_2, weights)]

    return minimum_span_tree

### Test Case
def test():

    G = graph() 
    G.graph = {'A': [('B', 2)],
               'B': [('A', 2), ('C', 5)], 
               'C': [('B', 5)]}

    answer_1 = {'A': [('B', 2)], 'B': [('C', 5)]}
      
    assert question3(G) == answer_1

    G = graph()
    G.graph = {'A': [('B', 1), ('C', 2)],
               'B': [('D', 3)],
               'C': [('D', 4)],
               'D': []}

    answer_2 = {'A': [('C', 2)],
                'B': [('D', 3)]}

    assert question3(G) == answer_2
    assert question3(None) is None 
    assert question3({}) is None

    print "Sure, okay."

### run test
test()

############################# QUESTION 4 #############################

"""
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor 
of both nodes. For example, the root is a common ancestor of all nodes on the tree, 
but if both nodes are descendents of the root's left child, then that left child might 
be the lowest common ancestor. You can assume that both nodes are in the tree, 
and the tree itself adheres to all BST properties. The function definition should 
look like question4(T, r, n1, n2), where T is the tree represented as a matrix, 
where the index of the list is equal to the integer stored in that node and a 1 
represents a child node, r is a non-negative integer representing the root, 
and n1 and n2 are non-negative integers representing the two nodes in no particular order. 
For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.

    
	0 = Ancestor 
   / \
  1   2 = Parent / Child
  	   \ 
  	    3 = Child 

adjancey matrix = 5 x 5

[0 [0,1,0,0,0]                  
 1 [0,0,0,0,0]
 2 [0,0,0,0,0]
 3 [1,0,0,0,1]
 4 [0,0,0,0,0]]

"""
def question4(T, r, n1, n2): 
	list_node = []

	### Checks the empty case 
	if not T or r is None or n1 is None or n2 is None:
		return None

	while n1 != r:
		### searches for it's first node position
		### if found, it appends the position.  
		n1 = find_parent(T, n1)
		list_node.append(n1)

		## check for bugs. This was nightmare. 
		# print "list node {}".format(list_node)
		# print "n1 {}".format(n1)

	### this just shows a disconnection. 
	if len(list_node) == 0: 
		return -1 

	while n2 != r:

		### searches for it's child poistion 
		### if it's found it checks if poistion 
		### is in the list and returns the child

		n2 = find_parent(T, n2)

		### check for bugs. 
		# print "n2 {}".format(n2)
		# print "list node again {}".format(list_node)

		if n2 in list_node:
			return n2

	return -1



def find_parent(T, node):

	### row of n x n adjancey matrix 
	adjancey_row = len(T)

	### checks every element in the matrix row 
	### if a one is not present it prints -1 and
	### not its a_{i,j} position in that row

	for element in range(adjancey_row):

		### check for bugs
		# print "position {}".format(element)
		# print "node {}".format(node)
		# print "element {}".format(T[element][node])
		# print "element equal one? {}".format(T[element][node] == 1)

		### if it's found the a_{i,j} position

		if T[element][node] == 1: 
			return element

    ### if it hasn't
	return -1

### Test Case.
def test(): 
	assert question4([[0,1,0,0,0],
			   [0,0,0,0,0],
			   [0,0,0,0,0],
			   [1,0,0,0,1],
			   [0,0,0,0,0]],3,1,4) == 3 

	assert question4([[0, 0, 0],
		       [1, 0, 1],
	
		       [0, 0, 0]], 1, 0, 2) == 1 
	assert question4([], None, None, None) is None
	assert question4(None, None, None, None) is None
	print "Sure, okay."

### run test 
test()

############################# QUESTION 5 ############################
"""
Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the 
end is the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node 
in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

"""

class Node(object):

  ### constructor to initilize the node object. 
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m): 
	
	"""
	complexity time is O(n) because 
	if we pass through the entire 
	linked list of n elements the slower 
	pointer is at the middle node already. 
	"""

	### setup points to both start
	### at the head of the linked list

	linked_fast = ll 
	linked_slow = ll 

	### loop through the linked list 
	### when linked_fast reaches the end 
	### then linked_slwo will be at the middle node.
	for index in range(m): 
		if linked_fast == None: 
			### deal with the empty case 
			return None 

		### if no empty case lets move to the next node.
		linked_fast = linked_fast.next 
    
	while linked_fast != None: 
		linked_fast = linked_fast.next
		linked_slow = linked_slow.next 

	return linked_slow.data



def test(): 
	### make nodes. 
	one = Node(1)
	two = Node(2)
	three = Node(5)
	four = Node(10)

	one.next = two 
	two.next = three
	three.next = four

	assert question5(one, 2) == 5
	assert question5(one, 3) == 2
	assert question5(None, 1) is None 
	assert question5(None, 10) is None
	print "YES!"

test()






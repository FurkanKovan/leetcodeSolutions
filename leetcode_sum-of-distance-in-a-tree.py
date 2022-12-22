# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/sum-of-distances-in-tree/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    # (1) Create the tree with edges[]
    graph = defaultdict(list)
    for a,b in edges: # bidirectional -> append both ways
        graph[a].append(b)
        graph[b].append(a)
    
    # (2) Create the necessary lists for the search algorithms
    answer = [0] * n # holds the distance
    count = [1] * n # holds the number of nodes under an ith node
    self.root = 0 # holds the root's answer

    # (3) Find the number of nodes under an any(i) node and save them to the count[]
    # No visited set is used to avoid cycles since no need to turn back after reaching the bottom
    def dfsCount(curr,parent,depth):
        output = 1 # start with the root as it has a child
        for child in graph[curr]: # traverse the tree
            if child != parent: # no turning back needed
                output += dfsCount(child, curr, depth+1) # count every other node under the child, recursively
                self.root += (depth+1) # track answer for the root node, it'll be needed
        count[curr] = output # update the count numbers
        return output # Return output for recursive calls for the childs
    
    # (4) Calling the dfsCount to initialize node counts
    dfsCount(0,-1,0)

    # (5) Find the distances of a node in the tree
    def dfsAnswer(curr,parent,distOfParent):
        answer[curr] = distOfParent # distOfParent starts as self.root, an initial value needed thus calculated beforehand
        for child in graph[curr]: # traverse the tree
            if child != parent: # no turning back needed aswell
                """
                If the distance of Parent is known, the child node's distance can be found with an equation:
                ParentDist - count[Child_otherSide] + (N - count[Child_shiftedSide]) 
                Here, 
                - ParentDist refers to the Parent distance to all of the nodes;
                - count[Child_otherSide] refers to the child which is 'shifted' to become the parent-like so that we calulate its distance.
                - (N - count[Child_shiftedSide]) refers to all other childs that are left at the other side of the parent
                """
                dfsAnswer(child, curr, distOfParent+(n-count[child])-count[child])
    
    # (6) Calling dfsAnswer to set the answers
    dfsAnswer(0,-1,self.root)
    
    return answer
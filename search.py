from collections import deque
import string
from node import Node
from dictionary import Dictionary

class Search:
    """
        Implements search algorithms for word transformations.
    """
    def __init__(self, start_word="", end_word=""):
        """
        Initializes the Search object with start and end words.

        Args:
            start_word (str): The word to start the transformation from.
            end_word (str): The target word to transform into.
        """    
        self.start_word = start_word
        self.end_word = end_word
        self.nodes_expanded = 0 #To track the number of nodes expanded

    def bfs(self):
        """
        Performs Breadth-First Search (BFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement BFS logic
        queue = deque([Node(self.start_word)]) #Initialie the queue with the start word
        visited = set([self.start_word]) #To avoid re-expanding words
        self.nodes_expanded = 0 #Reset nodes expanded for BFS

        while queue:
            current_node = queue.popleft() #Pop from the front of the queue
            self.nodes_expanded += 1 #Increment nodes expanded

            #If we have reached the end word, return the current node
            if current_node.word == self.end_word:
                return current_node
            
            #Generate valid neighbors by changing one letter at a time
            for neighbor in self.get_neighbors(current_node.word):
                if neighbor not in visited:
                    visited.add(neighbor) #Mark this word as visited
                    queue.append(Node(neighbor, current_node)) #Add neighbor to the queue
        return None #If no path is found

    def dfs(self):
        """
        Performs Depth-First Search (DFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement DFS logic
        stack = [Node(self.start_word)] #Initialize the stack with the start word
        visited = set([self.start_word]) #to avoid re-expanding words
        self.nodes_expanded = 0 #Reset nodes expanded for DFS

        while stack:
            current_node = stack.pop() #Pop from the top of the stack
            self.nodes_expanded += 1 #Increment nodes expanded

            #If we have reached the end word, return the current node
            if current_node.word == self.end_word:
                return current_node
            
            #Generate valid neighbors by changing one letter at a time
            for neighbor in self.get_neighbors(current_node.word):
                if neighbor not in visited:
                    visited.add(neighbor) #Mark this word as visited
                    stack.append(Node,(neighbor, current_node)) #Add neighbor to the stack
        return None #If no path is found
    
    def get_neighbors(self, word):
        """
        Given a word, generates all valid neighbors by changing one letter at a time.

        Args:
            word (str): The word for which neighbors are generated.

        Returns:
            list: List of valid neighbors (words that exist in the dictionary)
        """
        neighbors = []
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                #Only replace the character if it's different
                if word[i] != letter:
                    neighbor = word[:i] + letter + word[i+1:]
                    if Dictionary.is_valid_word(neighbor): #Check if it's a valid word
                        neighbors.append(neighbor)
        return neighbors
    
    def print_transformations(self, word_list):
        """
        Helper method to print the sequence of words
        Args:
            world_list(list) Sequence of words 
        """
        print(" --> ".join(word_list))

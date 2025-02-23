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

    def bfs(self):
        """
        Performs Breadth-First Search (BFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement BFS logic
        return None

    def dfs(self):
        """
        Performs Depth-First Search (DFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement DFS logic
        return None

    def print_transformations(self, word_list):
        """
        Helper method to print the sequence of words
        Args:
            world_list(list) Sequence of words 
        """
        print(" --> ".join(word_list))

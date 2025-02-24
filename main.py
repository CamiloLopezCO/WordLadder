from dictionary import Dictionary
from search import Search
def print_path(goal_node):
    """
    Helper function to print the transformation path from start to end.

    Args:
        goal_node (Node): The final node reached in the search.
    """
    path = []
    while goal_node:
        path.append(goal_node.value)
        goal_node = goal_node.get_parent()
    print("-> ".join(reversed(path)))

def main():
    print("**************Dictionary usage example**************")
    file_name = "words.txt"
    dictionary = Dictionary(file_name)
    
    print("**************Example to test search implementation **************")
    start_word = "lurk"
    end_word = "hide"
    search_instance = Search(start_word, end_word, dictionary)

    #BFS Execution
    print("\nRunning BFS...")
    bfs_goal = search_instance.bfs()
    if bfs_goal:
        print("BFS Path Found:")
        print_path(bfs_goal)
        print(f"Nodes Expanded (BFS): {search_instance.nodes_expanded}")
    else:
        print("No path found using BFS.")

    #DFS Execution 
    print("\nRunning DFS...")
    search_instance.nodes_expanded = 0 #Reset count before running DFS
    dfs_goal = search_instance.dfs()
    if dfs_goal:
        print("DFS Path Found:")
        print_path(dfs_goal)
        print(f"Nodes Expanded (DFS): {search_instance.nodes_expanded}")
    else:
        print("No path found using DFS.")

if __name__ == "__main__":
    main()

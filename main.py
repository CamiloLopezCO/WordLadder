from dictionary import Dictionary
from search import Search

def main():
    print("**************Dictionary usage example**************")
    file_name = "words.txt"
    dict_obj = Dictionary(file_name)
    
    if dict_obj.search_word("test"):
        print("The tested word is in our dictionary")

    print("**************Example to test search implementation **************")
    start_word = "lurk"
    end_word = "hide"
    new_search = Search(start_word, end_word)

    goal_node = new_search.bfs()
    
    if goal_node is not None:
        while goal_node.get_parent() is not None:
            print(f"{goal_node.value} <-", end="")
            goal_node = goal_node.get_parent()
        print(goal_node.value)
    else:
        print("You are yet to implement the code, try after implementation")

if __name__ == "__main__":
    main()

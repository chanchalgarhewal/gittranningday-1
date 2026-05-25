# Alpha-Beta Pruning in Minimax Algorithm 
 
# Function to perform Alpha-Beta Pruning 
def alpha_beta_pruning(depth, node_index, is_maximizing, values, alpha, beta): 
    # Terminal condition: If leaf node or depth limit is reached 
    if node_index >= len(values): 
        return 0  # Return 0 if index is out of bounds
    if depth == 0:
        return values[node_index] 
 
    if is_maximizing:  # Maximizer's turn 
        best_value = float('-inf') 
        for i in range(2):  # Simulating two children 
            val = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta) 
            best_value = max(best_value, val) 
            alpha = max(alpha, best_value) 
 
            # Prune the remaining nodes 
            if beta <= alpha: 
                break 
        return best_value 
 
    else:  # Minimizer's turn 
        best_value = float('inf') 
        for i in range(2):  # Simulating two children 
            val = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta) 
            best_value = min(best_value, val) 
            beta = min(beta, best_value) 
 
            # Prune the remaining nodes 
            if beta <= alpha: 
                break 
        return best_value 
# Example game tree 
if __name__ == "__main__": 
   values = list(map(int,input("enter number: ").split())) # Leaf nodes
   print(values) 
   depth = 4 # Depth of the game tree 
   alpha = float('-inf')  # Initial alpha 
   beta = float('inf')    # Initial beta 
   optimal_value = alpha_beta_pruning(depth, 0, True, values, alpha, beta) 
   print(f"The optimal value is: {optimal_value}")  


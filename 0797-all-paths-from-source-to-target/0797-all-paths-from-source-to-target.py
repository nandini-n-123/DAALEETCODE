class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        if n == 0:
            return []
        
        def dfs(node, current_path):
            if node == n - 1:
                result.append(current_path[:])
                return
            
            for neighbor in graph[node]:
                current_path.append(neighbor)
                dfs(neighbor, current_path)
                current_path.pop()
        
        result = []
        dfs(0, [0])
        return result        
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)

        for u,v,t in times: #building adjacency graph list
            graph[u].append((v,t))
        
        min_times={}
        min_heap=[(0,k)] # distance from source to node,node

        while min_heap:
            dis_k_to_i,i=heapq.heappop(min_heap)
            if i in min_times:
                continue
            
            min_times[i]=dis_k_to_i # {node:dist}
            for nei_node,nei_dis in graph[i]:
                if nei_node not in min_times:
                    heapq.heappush(min_heap,(dis_k_to_i+nei_dis,nei_node))
        
        if len(min_times)==n:
            return max(min_times.values())
        else:
            return -1
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        M = [0] * len(cost)
        M[0] = cost[0]
        M[1] = cost[1]

        for i in range(2, len(cost)):
            M[i] = min(M[i-1] + cost[i], M[i - 2]  + cost[i])

        return(M[len(cost) - 1])
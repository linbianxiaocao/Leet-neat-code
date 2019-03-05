ass Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        # dijikstra, mine own implementation
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        unVisitedVertexes = set(i for i in range(1,N+1))
        distance = [float('inf')] * (N+1)

        distance[K] = 0
        for _ in range(N):
            curVertex = min(unVisitedVertexes, key=lambda vertex:distance[vertex])
            for v, w in graph[curVertex].items():
                if v in unVisitedVertexes:
                    distance[v] = min(distance[v], distance[curVertex] + w)
            unVisitedVertexes.remove(curVertex)

        distance = distance[1:]
        return -1 if float('inf') in distance else max(distance)


        # also reference: https://blog.csdn.net/fuxuemingzhu/article/details/82862769
        # K -= 1
        # nodes = collections.defaultdict(list)
        # for u, v, w in times:
        #     nodes[u - 1].append((v - 1, w))
        # dist = [float('inf')] * N
        # dist[K] = 0
        # done = set()
        # for _ in range(N):
        #     smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
        #     for v, w in nodes[smallest]:
        #         if v not in done and dist[smallest] + w < dist[v]:
        #             dist[v] = dist[smallest] + w
        #     done.add(smallest)
        # return -1 if float('inf') in dist else max(dist)




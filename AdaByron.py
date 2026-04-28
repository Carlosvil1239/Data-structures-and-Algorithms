from collections import deque
from bisect import bisect_right
import heapq



def solve_espantaperros():
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0 or dy == 0 or abs(dx) == abs(dy):
            print("Yes")
        else:
            print("No")




def solve_plastic_rings():
    while True:
        n = int(input())
        if n == 0:
            break
        edges = 0
        while True:
            a, b = map(int, input().split())
            if a == 0 and b == 0:
                break
            edges += 1
        print(edges - n + 1)



def solve_avoiding_trips():
    while True:
        c, m, n = map(int, input().split())
        if c == 0 and m == 0 and n == 0:
            break
        heights = list(map(int, input().split()))
        steps = []
        for i in range(1, len(heights)):
            steps.append(heights[i] - heights[i - 1])
        ok = True
        for i in range(1, len(steps)):
            if abs(steps[i] - steps[i - 1]) > c:
                ok = False
        if max(steps) - min(steps) > m:
            ok = False
        if ok:
            print("Ok")
        else:
            print("Trip")



def solve_office_party():
    try:
        while True:
            n, p, capacity = map(int, input().split())
            graph = [[] for _ in range(n)]
            for _ in range(p):
                a, b = map(int, input().split())
                a -= 1
                b -= 1
                graph[a].append(b)
                graph[b].append(a)
            color = [-1] * n
            options = []
            for start in range(n):
                if color[start] != -1:
                    continue
                q = deque([start])
                color[start] = 0
                count = [1, 0]
                while q:
                    node = q.popleft()
                    for nxt in graph[node]:
                        if color[nxt] == -1:
                            color[nxt] = 1 - color[node]
                            count[color[nxt]] += 1
                            q.append(nxt)

                options.append((count[0], count[1]))
            dp = [False] * (capacity + 1)
            dp[0] = True
            for a, b in options:
                new_dp = dp[:]

                for current in range(capacity + 1):
                    if not dp[current]:
                        continue

                    if current + a <= capacity:
                        new_dp[current + a] = True

                    if current + b <= capacity:
                        new_dp[current + b] = True

                dp = new_dp

            ans = 0

            for i in range(capacity + 1):
                if dp[i]:
                    ans = i
            print(ans)
    except EOFError:
        pass


def solve_ticket_office():
    try:
        while True:
            f, seats, clients = map(int, input().split())
            occupied = list(map(int, input().split()))
            heap = []
            for x in occupied:
                free = seats - x

                if free > 0:
                    heapq.heappush(heap, -free)
            revenue = 0
            while clients > 0 and heap:
                free = -heapq.heappop(heap)
                revenue += free
                free -= 1
                clients -= 1
                if free > 0:
                    heapq.heappush(heap, -free)
            print(revenue)
    except EOFError:
        pass


def solve_bike_collisions():
    while True:
        n = int(input())
        if n == 0:
            break
        data = list(map(int, input().split()))
        cyclists = []
        for i in range(0, len(data), 2):
            position = data[i]
            speed = data[i + 1]
            cyclists.append((position, speed))
        cyclists.sort()
        best = None
        for i in range(n - 1):
            p1, v1 = cyclists[i]
            p2, v2 = cyclists[i + 1]
            if p1 == p2:
                best = 0
                break
            if v1 > v2:
                time_num = p2 - p1
                time_den = v1 - v2
                t = time_num // time_den
                if best is None or t < best:
                    best = t
        if best is None:
            print("No collision")
        else:
            print(best)


def solve_highway_restaurants():
    try:
        while True:
            n, k = map(int, input().split())
            positions = list(map(int, input().split()))
            benefits = list(map(int, input().split()))
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                pos = positions[i - 1]
                benefit = benefits[i - 1]
                j = bisect_right(positions, pos - k)
                take = benefit + dp[j]
                skip = dp[i - 1]
                dp[i] = max(skip, take)
            print(dp[n])
    except EOFError:
        pass

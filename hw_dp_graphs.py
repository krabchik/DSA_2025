import heapq


def count_sequences_without_11_recuresive(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return count_sequences_without_11_recuresive(n - 1) + count_sequences_without_11_recuresive(n - 2)


def count_sequences_without_11_dynamic(n: int):
    dp = [1, 2]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


def count_sequences_without_111_recursive(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    return count_sequences_without_111_recursive(n - 1) + count_sequences_without_111_recursive(n - 2) + count_sequences_without_111_recursive(n - 3)


def count_sequences_without_111_dynamic(n: int):
    dp = [1, 2, 4]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[n]


def build_pascal_tree(n):
    dp = []
    for i in range(1, n + 1):
        tmp = []
        for j in range(1, i + 1):
            tmp.append(1)
        dp.append(tmp)

    for row in range(1, n):
        for col in range(1, row):
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]

    return dp


def find_LIS(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1

    return max(dp)


def max_profit(prices: list[int]):
    profit = 0
    min_price = prices[0]
    for currentPriceIndex in range(1, len(prices)):
        profit = max(profit, prices[currentPriceIndex] - min_price)
        min_price = min(prices[currentPriceIndex], min_price)

    return profit


def coin_change_recursive(coins, amount, cache=dict()):
    if amount == 0: return 0
    if amount < 0: return -1
    if amount in cache:
        return cache[amount]

    min_coins = float('inf')
    for coin in coins:
        res = coin_change_recursive(coins, amount - coin, cache)
        if 0 <= res < min_coins:
            min_coins = res + 1

    if min_coins == float('inf'):
        cache[amount] = -1
    else:
        cache[amount] = min_coins

    return cache[amount]


def coin_change_dynamic(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    return l + 1, r - 1


def longest_palindrome(s):
    current_max_left = 0
    current_max_right = 0
    diff = 0

    for i in range(len(s)):
        l, r = expand_around_center(s, i, i)
        if r - l > diff:
            diff = r - l
            current_max_left = l
            current_max_right = r
        l, r = expand_around_center(s, i, i + 1)
        if r - l > diff:
            diff = r - l
            current_max_left = l
            current_max_right = r

    return s[current_max_left: current_max_right + 1]


def longest_palindrome_dp(s):
    dp = [[False] * len(s) for _ in range(len(s))]

    for j in range(len(s)):
        for i in range(0, j + 1):
            if i == j:
                dp[i][j] = True
            elif s[i] == s[j]:
                if j - i == 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

    for distance in range(len(s)):
        for distance_i in range(distance + 1):
            distance_j = distance - distance_i
            i = distance_i
            j = len(s) - distance_j - 1
            if dp[i][j]:
                return s[i: j + 1]

    return ''


def dfs(graph, v, visited, color):
    visited[v] = color
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited, color)


def find_connected_components(graph):
    visited = {i: 0 for i in range(1, len(graph) + 1)}

    color = 0
    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(graph, node, visited, color)

    return visited


def has_cycle(graph):
    visited = []
    for vertex in graph:
        if vertex not in visited:
            if dfs_cycle(graph, vertex, None, visited):
                return True

    return False


def dfs_cycle(graph, vertex, parent, visited):
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or dfs_cycle(graph, neighbor, vertex, visited):
                return True

    return False


def is_tree(graph, start):
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        vertex = queue.pop()
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            elif parent[vertex] != neighbor:
                return False

    return len(visited) == len(graph)


def dfs_bipartite(node, c, graph, colors):
    colors[node] = c

    for neighbor in graph[node]:
        if colors[neighbor] == 0:
            if not dfs_bipartite(neighbor, -c):
                return False
        elif colors[neighbor] == colors[node]:
            return False

    return True

def is_bipartite(graph):
    n = len(graph)
    colors = [0] * n

    for i in range(n):
        if colors[i] == 0:
            if not dfs_bipartite(i, 1, graph, colors):
                return False

    return True

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [( 0, start)]

    while priority_queue:
        current_distance , current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue , (distance, neighbor))

    return distances


def main():
    assert count_sequences_without_11_recuresive(7) == 34
    assert count_sequences_without_11_dynamic(7) == 34

    assert count_sequences_without_111_recursive(7) == 81
    assert count_sequences_without_111_dynamic(7) == 81

    assert build_pascal_tree(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    assert find_LIS([3, 2, 8, 9, 5, 10]) == 3
    assert find_LIS([1, 2, 7, 9, 0, 10]) == 4
    assert find_LIS([8, 8, 8, 8]) == 1

    assert max_profit([8, 9, 3, 7, 4, 16, 12]) == 13
    assert max_profit([8, 9, 16, 3, 7, 4, 12]) == 9

    assert coin_change_recursive([1, 2], 3) == 2
    assert coin_change_recursive([1, 2], 4) == 2
    assert coin_change_recursive([1, 2], 5) == 3

    assert coin_change_dynamic([1, 2], 3) == 2
    assert coin_change_dynamic([1, 2], 4) == 2
    assert coin_change_dynamic([1, 2], 5) == 3

    assert longest_palindrome('babad') == 'bab'
    assert longest_palindrome('ababad') == 'ababa'
    assert longest_palindrome('ababaddab') == 'baddab'

    assert longest_palindrome_dp('babad') == 'bab'
    assert longest_palindrome_dp('ababad') == 'ababa'
    assert longest_palindrome_dp('ababaddab') == 'baddab'

    graph_with_components = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [6, 7],
        5: [6, 7],
        6: [4, 5, 7],
        7: [4, 5, 6],
        8: [11],
        9: [10, 11],
        10: [9],
        11: [8, 9]
    }

    assert find_connected_components(graph_with_components) =={1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3, 10: 3, 11: 3}

    graph_with_cycle = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 6],
        4: [3, 5],
        5: [4, 6],
        6: [5, 3],
    }

    assert has_cycle(graph_with_cycle) == True

    graph_without_cycle = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4, 6],
        6: [5],
    }

    assert has_cycle(graph_without_cycle) == False

    graph_dijkstra = {
        'A': {'B': 1, 'C': 5},
        'B': {'A': 1, 'C': 2, 'D': 3},
        'C': {'A': 5, 'B': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }

    assert dijkstra(graph_dijkstra, 'A') == {'A': 0, 'B': 1, 'C': 3, 'D': 4}

if __name__ == '__main__':
    main()

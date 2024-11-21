def determine_ranks(N, matches):
    def dfs(tiger):
        nonlocal count_determined

        visited[tiger] = True

        for opponent in defeated_by[tiger]:
            if not visited[opponent]:
                dfs(opponent)

    defeated_by = {i: [] for i in range(1, N + 1)}

    for A, B in matches:
        defeated_by[B].append(A)

    count_determined = 0

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(i)
        count_determined += all(visited)  # 判断是否所有老虎都被访问过

    return count_determined

def main():
    N, M = map(int, input().split())
    matches = [tuple(map(int, input().split())) for _ in range(M)]

    result = determine_ranks(N, matches)

    print(result)

if __name__ == "__main__":
    main()
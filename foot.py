def winnergy(n, matches):
    wins = [0] * n
    for match in matches:
        wins[match[0] - 1] += 1
    max_wins = max(wins)
    winners = [i + 1 for i in range(n) if wins[i] == max_wins]
    print(winners)
    return winners

print(winnergy(4, [[1, 2], [2, 3], [3, 4], [4, 1]]))



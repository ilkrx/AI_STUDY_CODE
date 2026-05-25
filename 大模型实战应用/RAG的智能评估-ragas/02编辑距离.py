strA = "故宫在北京"
strB = "故宫位于北京"


# def edit_distance(strA: str, strB: str) -> int:
#     m, n = len(strA) + 1, len(strB) + 1
#     dp = [[0] * n for _ in range(m)]
#     # print(dp)
#
#     # 初始化dp数组
#     for i in range(m):
#         dp[i][0] = i
#     for j in range(n):
#         dp[0][j] = j
#     # print(dp)
#     for i in range(1, m):
#         for j in range(1, n):
#             if strA[i - 1] == strB[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
#     return dp[-1][-1]
#
#
# distance = edit_distance(strA, strB)
# print(distance)
# print(distance / max(len(strA), len(strB)))

# 使用库函数：
from rapidfuzz import distance

print(distance.Levenshtein.normalized_distance(strA, strB))
# greedy - 2번

n, m, = map(int, input().split())

result = 0
# 한 줄씩 입력받고 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은수 찾기
  min_value = min(data)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(min_value, result)

print(result)
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(N)]
    scores.sort()

    cnt = 1

    # 일단 서류 성적순으로 나열이 됐으니, 다른 성적에서 순위가 높은지만 확인
    top = scores[0][1]

    for i in range(1, N):
        if top > scores[i][1]:
            cnt += 1
            top = scores[i][1]
            
    print(cnt)


#  map은 리스트의 요소를 지정된 함수로 처리해주는 함수


T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0

    for num in numbers :
        if num % 2 != 0:
            total += num

    print(f'#{test_case} {total}')

# f-string 사용법

T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    average = 0
    average = round(sum(numbers) / 10)
# https://xlworks.net/excel-function-round-roundup-rounddown/

    print(f'#{test_case} {average}')

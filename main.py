# 연산의 달인(연달)
import random
print ('연산 게임시작')

#repeat start
#10Q print (1-10)
for i in range(1,11):
    res = 0 # 문제의 답
    # 두자리 수가 랜덤으로 하나
    n1 = random.randrange(1, 100)
    # 두자리 수가 랜덤으로 둘
    n2 = random.randrange(1, 10)
    # +, -, *, / 중에 하나
    op_list = ['+', '-', '*', '/']
    op = random.choice(op_list)
    # 위 두수와 연산자로 연산 문제 생성
    # op = '+' # 치트키 (개발 완료 시 주석처리)
    # 만약에 -, / 에서 n1 이 n2 보다 작으면 앞뒤로 바꿈
    if op == '-' or op == '/':
        
        # 두수 바꿈 만들어 보세요
        #큰값 저장기능
        front = max (n1,n2)
        #작은값 저장기능
        back = min (n1,n2)
        #두 수 변경
        n1 = front
        n2 = back
    if op == '+':
        res = n1 + n2
    elif op =='-':
        res = n1 - n2
    elif op =='*':
        res = n1 * n2
    elif op =='/':
        res = n1 / n2

    # 사용자에게 문제 보여주고 사용자가 입력할 수 있게 하고 
    user = int(input(f'{i}Q {n1} {op} {n2} = ' ))
    # 문제의 정답을 맞추면
    if user == res:
        print('정답 계속 문제 발생')
    else:
        print('땡~ 소쿠리')
    # 맞다고 하고 계속 문제 생성
    # 틀리면 틀렸다고 하고 프로그램 종료
    #10Q print and repeat
    #end
    print ('game end')
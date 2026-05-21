# 파일이름 : 60232179 강성재 2차과제
# 작 성 자 : 60232179 강성재

# 투자자의 이름, 목표 수익률을 입력
user_name = input("투자자의 이름을 입력하세요: ")
goal_profit = float(input("목표 수익률을 입력하세요: "))
# 총 투자금액 변수 설정
total_investment = 0
# 종목과 매수 단가 빈 리스트 생성
stock_list = []
price_list = []
# 종목과 매수단가 입력
for i in range(3) :
    print()
    print(f"--- {i+1}번째 종목 등록 ---")
    s_name = input("종목명: ")
    s_price = int(input("매수 단가: "))
    if s_price <= 0:
        print("오류!: 가격은 0보다 커야 합니다 이 종목은 목록에서 제외됩니다.")
        continue
    stock_list.append(s_name)
    price_list.append(s_price)

# 종목개수, 평균수익률
stock_count = len(stock_list)
average_price = sum(price_list) / stock_count

# 현재 시세와 현재 시세 대비 수익률 (현재 시세는 실제로 반영할려면 API를 사용해야해서 임의로 40000원이라고 설정)
current_price = 40000
current_profit = ((current_price - average_price ) / average_price)

#총 투자금액
total_investment += s_price
if total_investment > 0 :
    print()
    print("성공적으로 포트폴리오가 구성되었습니다!")

#투자 분석결과 
print(f'--- {user_name}님의 투자 분석 결과 ---')

if current_profit >= goal_profit :
    if current_profit >= 50.0 :
        status = '수익률 50% 달성 오늘 저녁은 먹고싶은거 드세요!'
    else :
        status = '목표 달성 완료'
elif current_profit > 0 and current_profit < goal_profit :
    status = '아직 수익 중이나 목표 수익까지는 미달입니다'
else :
    status = '손실중입니다. 대책을 강구하세요'

# 포매팅 출력 결과
print(f'분석된 종목 수 : {stock_count}개 ') 
print(f'보유 종목 리스트 : {stock_list}')
print(f'평균 매수 단가 : {average_price}원')
print(f'현재 수익률 : {current_profit}%')
print(f'투자 상태 : {status}')
print('=' * 40)

# 파일이름 : 60232179 강성재 3차과제
# 작 성 자 : 60232179 강성재

#사용자 이름 , 목표수익률, 손절선, 종목, 가격, 총투자금액 설정
user_name = ""
goal_profit = 0.0
stop_loss_limit = 0.0 
stock_list = []
price_list = []
total_investment = 0

# 함수 정의 및 분리

def input_portfolio() :
    #전역 변수들 값 변경하기 위해 global 사용
    global user_name, goal_profit, stop_loss_limit, stock_list, price_list, total_investment

    print('--포트폴리오 및 리스크 설정--')
    user_name = input('투자자의 이름을 입력하세요: ')
    goal_profit = float(input('목표 수익률(%)을 입력하세요'))
    #최대 손실율(stop loss)입력받기
    stop_loss_limit = float(input('감당할 수 있는 최대 손실률(%)을 입력하세요'))
    
    # 입력 데이터 초기화
    stock_list = []
    price_list = []
    total_investment = 0
    
    # 반복입력 받기
    for i in range(3) :
        print(f'--- {i+1}번째 종목 등록 ---')
        s_name = input('종목명: ')
        s_price = int(input('매수 단가: '))

        if s_price <= 0 :
            print('오류! 가격은 0보다 커야합니다. 이 종목은 목록에서 제외됩니다.')
            continue
        stock_list.append(s_name)
        price_list.append(s_price)
        total_investment += s_price # 총 투자금액 누적

    if len(stock_list) > 0 :
        print('성공적으로 포트폴리오와 스마트 손절선이 설정되었습니다!')

#매개변수를 전달받는 함수
def analyze_investment(p_list, goal, loss_limit) :
    # 매수 단가 리스트, 목표수익률, 손절선을 받아서 투자현황및 위험을 연산하는 함수
    stock_count = len(p_list)

    if stock_count == 0:
        return 0, 0.0, 0.0, '등록된 종목이 없습니다.', False
    
    average_price = sum(p_list) / stock_count
    current_price = 40000 #임의로 시세 설정 40000원

    # 현재 시세 대비 수익률 계산

    current_profit = ((current_price - average_price) / average_price) * 100
    current_profit = round(current_profit, 2)

    # 스마트 손절선 및 투자 상태 등급 판정 (lost_limit이 10.0, 수익률이 -10.0% 이하일 때 위험한 상태로 판단)

    is_danger = False

    if current_profit <= -(loss_limit) :
        status = '위험! 설정하신 최대 손절선을 이탈했습니다! 즉시 매도를 검토하세요.'
        is_danger = True
    elif current_profit >= goal :
        if current_profit >= 50.0 :
            status = '수익률 50% 달성! 축하드립니다!'
        else :
            status = '목표 달성! 익절을 고려해보세요.'
    elif 0 < current_profit < goal :
        status = '아직 수익중이나 목표 수익까지는 미달입니다.'
    else :
        status = '손실 중입니다. 추가 하락 시 손절선을 주의하세요.'

    #결과를 return 을 통해서 반환
    return stock_count, average_price, current_profit, status, is_danger

# 무한루프 시스템
while True :
    input_portfolio() 

    if len(stock_list) == 0 :
        print('등록된 종목이 없어 포트폴리오를 다시 설정합니다.')
        continue 

    #전역 변수를 매개변수로 전달, 결과를 return 받아서 지역변수에 저장
    
    s_count, avg_price, cur_profit, status_msg, danger_flag = analyze_investment(price_list, goal_profit, stop_loss_limit)

    #투자 분석 결과 

    print('-'*40)
    print(f'--- {user_name}님의 투자 분석 결과 ---')
    print(f'분석된 종목 수 : {s_count}개')
    print(f'보유 종목 리스트 : {stock_list}')
    print(f'현재 수익률 : {cur_profit}% (설정한 손절선: -{stop_loss_limit}%')
    print(f'투자 상태 : {status_msg}')
    print('-'*40)

    #손절선 이탈 시 break로 무한루프 종료

    if danger_flag :
        print('===최대 손실 한도를 초과하여 스탑로스가 발동되었습니다===')
        print('자산 보호를 위해 프로그램을 강제로 안전하게 종료합니다.')
        print('=====================================================')
        break
    else :
        # 손절선에 걸리지 않았으면 계속 시뮬레이션을 돌릴지 사용자에게 확인
        retry = input('다시 포트폴리오를 구성하시겠습니까? (y/n): ')
        if retry.lower() != 'y' :
            print('프로그램을 정상 종료합니다 성투하세요!')
            break





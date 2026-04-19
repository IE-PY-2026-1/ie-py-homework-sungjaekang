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





# 파일이름 : 60232179 강성재 4차과제
# 작 성 자 : 60232179 강성재

#사용자 정보 및 종목 데이터를 입력받아 이중 리스트로 저장하는 함수 생성
def input_portfolio() :

    print('='*15 + '포트폴리오 및 리스크 설정' + '='*15)

    user_name = input('투자자의 이름을 입력하세요: ').strip()
    if not user_name :

        user_name = '무명 투자자'
    
    #목표 수익률 입력 (예외처리 활용)
    while True :

        try:
            goal_profit = float(input('목표 수익률(%)을 입력하세요: '))
            break
        except ValueError :
            print('오류! 숫자로만 입력해 주세요.')
    
    while True :
        try:
            stop_loss_limit = float(input('감당할 수 있는 최대 손절률(%)을 입력하세요: '))
            break
        except ValueError :
            print('오류! 숫자로만 입력해 주세요.')
    #이중리스트로 종목명, 매수단가 구성
    portfolio_data = []

    for i in range(3) :
        print(f'---{i+1}번째 종목 등록 ---')
        s_name = input('종목명: ').strip()
        if not s_name :
            print('종목명이 비어있어 스킵합니다.')
            continue

        while True :
            try:
                s_price = int(input('매수 단가(원): '))
                break
            except ValueError :
                print('오류! 숫자로만 입력해 주세요.')
        if s_price <= 0:
            print('오류! 가격보다 0보다 커야 합니다. 이 종목은 목록에서 제외됩니다.')
            continue
            
        #새로운 종목데이터를 이중리스트에 추가
        portfolio_data.append([s_name, s_price])

    if len(portfolio_data) > 0:
        print('성공적으로 포트폴리오와 스마트 손절선이 설정되었습니다!')
    
    return user_name, goal_profit, stop_loss_limit, portfolio_data

#이중 리스트를 전달받아서 투자 현황을 연산하고 위험을 분석하는 함수 생성
def analyze_investment(portfolio_data, goal, loss_limit):
    stock_count = len(portfolio_data)

    if stock_count == 0:
        return 0, 0.0, 0.0, '등록된 종목이 없습니다.', False

    total_price = 0
    for stock in portfolio_data:
        total_price += stock[1]
    
    average_price = total_price / stock_count
    current_price = 40000 #임의로 시세 설정

    #현재 시세 대비 수익률 계산
    current_profit = ((current_price - average_price) / average_price) * 100
    current_profit = round(current_profit, 2)

    #스마트 손절선 및 투자 상태 판정
    is_danger = False

    if current_profit <= -(loss_limit) :
        status = '위험! 설정하신 최대 손절선을 이탈했습니다! 즉시 매도를 검토하세요.'
        is_danger = True

    elif current_profit >= goal :
        if current_profit >= 50.0 :
            status = '대박! 수익율 50% 달성! 오늘 저녁은 맛있는 거 드세요!'
        else :
            status = '목표 달성! 익절을 고려해 보세요.'
    elif 0 < current_profit < goal :
        status = '아직 수익 중이나 목표 수익까지는 미달입니다.'
    else :
        status = '손실 중입니다. 추가 하락 시 손절선에 주의하세요.'
    
    return stock_count, average_price, current_profit, status, is_danger


#open() 함수를 사용하여 투자 데이터를 텍스트 파일로 저장하는 함수 생성
def save_to_file(filename, name, portfolio, cur_profit, status):


    try:

        with open(filename, 'w', encoding='utf-8') as f :
            f.write(f'=== {name}님의 투자 포트폴리오 보고서 ===')
            f.write(f'현재 수익률 : {cur_profit}')
            f.write(f'투자 상태 : {status}')
            f.write('-' * 40)
            f.write('[보유 종목 상세 리스트]')

            #파일 작성에 이중 리스트 순회 활용

            for stock in portfolio :

                f.write(f'종목명 : {stock[0]} 매수단가 : {stock[1]:,}원')
        print(f'투자 분석 결과가 {filename} 파일로 성공적으로 저장되었습니다.')
    except Exception as e :
        print(f'파일 저장 중 오류가 발생했습니다: {e}')

#메인 프로그램 실행부
if __name__ == '__main__':


    while True :

        #포트폴리오 입력 받기
        user_name, goal_profit, stop_loss_limit, portfolio_list = input_portfolio()

        if len(portfolio_list) == 0 :
            print('등록된 종목이 없어 포트폴리오를 다시 설정합니다.')
            continue

        #투자 현황 분석
        s_count, avg_price, cur_profit, status_msg, danger_flag = analyze_investment(portfolio_list, goal_profit, stop_loss_limit)

        #투자 분석 결과 출력
        print('='*45)
        print(f'{user_name}님의 투자 포트폴리오 분석 결과')
        print('='*45)
        print(f'분석된 보유 종목 수 : {s_count}개')

        #이중 순회를 활용해서 반복출력

        print(f'보유 종목 상세 내역: ')
        for i, stock in enumerate(portfolio_list):
            print(f' {i+1}. 종목: {stock[0]:<10} 매수단가: {stock[1]:,}원')
        print(f'평균 매수 단가 : {int(avg_price):,}원')
        print(f'현재 설정 수익률: {cur_profit}% (목표: {goal_profit}%, 손절선: {stop_loss_limit}%)')
        print(f'현재 리스크 상태: {status_msg}')
        print('='*45)

        #프로그램 종료 혹은 분석 완료시에 자동저장

        save_to_file('portfolio_report.txt', user_name, portfolio_list, cur_profit, status_msg)

        #종료 조건

        if danger_flag :
            print('=== 최대 손실 한도를 초과하여 스탑로스가 발동되었습니다. ===')
            print(' 자산 보호를 위해 프로그램을 안전하게 강제 종료합니다.')
            print('='*55)
            break
        else:
            retry = input('다시 포트폴리오를 구성하시겠습니까? (y/n): ')
            if retry.lower() != 'y' :
                print('프로그램을 정상 종료합니다.')
                break


            





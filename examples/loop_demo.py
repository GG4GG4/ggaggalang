from interpreter import GgaggalangInterpreter

# 카운트다운 예제 코드
countdown_code = """
# 카운트다운 예제 (10부터 1까지)
# 셀 0에 10을 저장
gga gga gga gga gga gga gga gga gga gga # 10 설정

# 루프 시작: 셀 0이 0이 될 때까지 반복
galanglang
    # 현재 값 출력 (ASCII 코드로 변환됨)
    gguggaggugga
    
    # 줄바꿈 출력을 위해 셀 1로 이동하여 10(줄바꿈) 저장 후 출력
    gugu
    gga gga gga gga gga gga gga gga gga gga # 10 (줄바꿈)
    gguggaggugga
    
    # 셀 0으로 돌아가서 값을 1 감소
    gugugga
    kka
langlaggug
"""

# 사용자 입력 에코 예제 코드
echo_code = """
# 사용자가 입력한 문자를 그대로 출력
# 입력 -> 저장 -> 출력의 루프를 반복 (ASCII 0이 입력될 때까지)

# 안내 메시지 (첫 번째 셀에서 시작)
# Hello, 를 출력
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga # 72 (H)
gguggaggugga

gugu
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga gga gga gga gga gga gga gga gga # 80
gga gga gga gga gga gga gga gga gga gga # 90
gga gga gga gga gga gga gga gga gga gga # 100
gga # 101 (e)
gguggaggugga

gugu
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga gga gga gga gga gga gga gga gga # 80
gga gga gga gga gga gga gga gga gga gga # 90
gga gga gga gga gga gga gga gga gga gga # 100
gga gga gga gga gga gga gga gga # 108 (l)
gguggaggugga

gugu
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga gga gga gga gga gga gga gga gga # 80
gga gga gga gga gga gga gga gga gga gga # 90
gga gga gga gga gga gga gga gga gga gga # 100
gga gga gga gga gga gga gga gga # 108 (l)
gguggaggugga

gugu
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga gga gga gga gga gga gga gga gga # 80
gga gga gga gga gga gga gga gga gga gga # 90
gga gga gga gga gga gga gga gga gga gga # 100
gga gga gga gga gga gga gga gga gga gga # 110
gga # 111 (o)
gguggaggugga

gugu
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga # 32 (공백)
gguggaggugga

# 새 셀로 이동하여 입력 받기
gugu

# 메인 루프: 입력값이 0이 될 때까지 반복
galanglang
    # 현재 셀(입력값이 저장된)에서 입력 받기
    ggalgga
    
    # 값이 0인지 확인용으로 복사 (다음 셀에)
    gga # 우선 1을 더해서
    
    gugu # 다음 셀로
    
    # 입력 받은 값 복사 (셀 n+1 = 셀 n)
    galanglang
        gugugga # 이전 셀로
        kka     # 감소
        gugu    # 다음 셀로
        gga     # 증가
    langlaggug
    
    # 값 확인 후, 0이면 루프 종료
    kka # 값을 1 감소 (원래 0이었으면 255가 됨)
    
    galanglang # 값이 0이면(원래 1이었으면) 루프 종료
        gugugga # 원래 셀로 돌아가기
        gguggaggugga # 입력된 문자 출력
        gugu # 비교용 셀로 돌아가기
        
        # 255로 설정해서 확실히 루프 종료
        gga gga gga gga gga gga gga gga gga gga # 10
        gga gga gga gga gga gga gga gga gga gga # 20
        gga gga gga gga gga gga gga gga gga gga # 30
        gga gga gga gga gga gga gga gga gga gga # 40
        gga gga gga gga gga gga gga gga gga gga # 50
        gga gga gga gga gga gga gga gga gga gga # 60
        gga gga gga gga gga gga gga gga gga gga # 70
        gga gga gga gga gga gga gga gga gga gga # 80
        gga gga gga gga gga gga gga gga gga gga # 90
        gga gga gga gga gga gga gga gga gga gga # 100
        gga gga gga gga gga gga gga gga gga gga # 110
        gga gga gga gga gga gga gga gga gga gga # 120
        gga gga gga gga gga gga gga gga gga gga # 130
        gga gga gga gga gga gga gga gga gga gga # 140
        gga gga gga gga gga gga gga gga gga gga # 150
        gga gga gga gga gga gga gga gga gga gga # 160
        gga gga gga gga gga gga gga gga gga gga # 170
        gga gga gga gga gga gga gga gga gga gga # 180
        gga gga gga gga gga gga gga gga gga gga # 190
        gga gga gga gga gga gga gga gga gga gga # 200
        gga gga gga gga gga gga gga gga gga gga # 210
        gga gga gga gga gga gga gga gga gga gga # 220
        gga gga gga gga gga gga gga gga gga gga # 230
        gga gga gga gga gga gga gga gga gga gga # 240
        gga gga gga gga gga gga gga gga gga gga # 250
        gga gga gga gga gga # 255
    langlaggug
    
    # 현재 셀을 초기화하고 이전 셀로 이동
    kka kka kka kka kka kka kka kka kka kka # 값을 0으로 초기화
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka kka kka kka kka
    kka kka kka kka kka kka
    
    gugugga # 이전 셀로 돌아가기
langlaggug
"""

def main():
    print("\n=== 카운트다운 예제 실행 ===")
    print("(10부터 1까지 카운트)")
    interpreter = GgaggalangInterpreter(debug=True)
    interpreter.execute(countdown_code)
    print("\n")
    
    print("\n=== 입력 에코 예제 실행 ===")
    print("(입력한 문자를 그대로 출력, Ctrl+D로 종료)")
    interpreter = GgaggalangInterpreter(debug=True)
    interpreter.execute(echo_code)
    print("\n")

if __name__ == "__main__":
    main()
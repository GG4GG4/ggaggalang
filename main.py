from interpreter import GgaggalangInterpreter

def main():
    # 디버그 모드로 실행
    print("=== Debug Mode ===")
    interpreter_debug = GgaggalangInterpreter(debug=True)
    test_code = """
    # H (72)
    gga gga gga gga gga gga gga gga gga gga # 10
    gga gga gga gga gga gga gga gga gga gga # 20
    gga gga gga gga gga gga gga gga gga gga # 30
    gga gga gga gga gga gga gga gga gga gga # 40
    gga gga gga gga gga gga gga gga gga gga # 50
    gga gga gga gga gga gga gga gga gga gga # 60
    gga gga gga gga gga gga gga gga gga gga # 70
    gga gga # 72
    gguggaggugga
    """
    interpreter_debug.execute(test_code)
    print("\n")
    
    # 일반 모드로 실행
    print("=== Normal Mode ===")
    interpreter = GgaggalangInterpreter(debug=False)
    hello_world = """
    # H (72)
    gga gga gga gga gga gga gga gga gga gga # 10
    gga gga gga gga gga gga gga gga gga gga # 20
    gga gga gga gga gga gga gga gga gga gga # 30
    gga gga gga gga gga gga gga gga gga gga # 40
    gga gga gga gga gga gga gga gga gga gga # 50
    gga gga gga gga gga gga gga gga gga gga # 60
    gga gga gga gga gga gga gga gga gga gga # 70
    gga gga # 72
    gguggaggugga

    gugu # 다음 셀로 이동

    # e (101)
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
    gga # 101
    gguggaggugga

    gugu # 다음 셀로 이동

    # l (108)
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
    gga gga gga gga gga gga gga gga # 108
    gguggaggugga

    gugu # 다음 셀로 이동

    # l (108)
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
    gga gga gga gga gga gga gga gga # 108
    gguggaggugga

    gugu # 다음 셀로 이동

    # o (111)
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
    gga # 111
    gguggaggugga

    gugu # 다음 셀로 이동

    # 공백 (32)
    gga gga gga gga gga gga gga gga gga gga # 10
    gga gga gga gga gga gga gga gga gga gga # 20
    gga gga gga gga gga gga gga gga gga gga # 30
    gga gga # 32
    gguggaggugga

    gugu # 다음 셀로 이동

    # W (87)
    gga gga gga gga gga gga gga gga gga gga # 10
    gga gga gga gga gga gga gga gga gga gga # 20
    gga gga gga gga gga gga gga gga gga gga # 30
    gga gga gga gga gga gga gga gga gga gga # 40
    gga gga gga gga gga gga gga gga gga gga # 50
    gga gga gga gga gga gga gga gga gga gga # 60
    gga gga gga gga gga gga gga gga gga gga # 70
    gga gga gga gga gga gga gga gga gga gga # 80
    gga gga gga gga gga gga gga # 87
    gguggaggugga

    gugu # 다음 셀로 이동

    # o (111)
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
    gga # 111
    gguggaggugga

    gugu # 다음 셀로 이동

    # r (114)
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
    gga gga gga gga # 114
    gguggaggugga

    gugu # 다음 셀로 이동

    # l (108)
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
    gga gga gga gga gga gga gga gga # 108
    gguggaggugga

    gugu # 다음 셀로 이동

    # d (100)
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
    gguggaggugga

    gugu # 다음 셀로 이동

    # ! (33)
    gga gga gga gga gga gga gga gga gga gga # 10
    gga gga gga gga gga gga gga gga gga gga # 20
    gga gga gga gga gga gga gga gga gga gga # 30
    gga gga gga # 33
    gguggaggugga
    """
    interpreter.execute(hello_world)

if __name__ == "__main__":
    main()
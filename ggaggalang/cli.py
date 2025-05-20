"""
Ggaggalang 명령줄 인터페이스 모듈
"""
import argparse
import sys
from typing import List, Optional, Dict, Any
from .interpreter import GgaggalangInterpreter
from .utils import string_to_ggaggalang, load_code_from_file

def get_hello_world_code() -> str:
    """Hello World 예제 코드 반환"""
    return """
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

def get_loop_example_code() -> str:
    """카운터 예제 코드 반환"""
    return """
    # 루프 예제: 0-9 카운터
    # 셀 0에 10을 저장 (카운트다운 값)
    gga gga gga gga gga gga gga gga gga gga # 10
    
    # 셀 1로 이동하여 48 저장 (ASCII '0')
    gugu
    gga gga gga gga gga gga gga gga gga gga # 10
    gga gga gga gga gga gga gga gga gga gga # 20
    gga gga gga gga gga gga gga gga gga gga # 30
    gga gga gga gga gga gga gga gga gga gga # 40
    gga gga gga gga gga gga gga gga # 48
    
    # 셀 0으로 돌아가기
    gugugga
    
    # 루프 시작 - 셀 0이 0이 될 때까지 반복
    galanglang
      # 셀 1로 이동 (현재 ASCII 숫자)
      gugu
      # 현재 숫자 출력
      gguggaggugga
      # 셀 1 값 증가 (다음 ASCII 숫자)
      gga
      # 셀 0으로 돌아가기
      gugugga
      # 카운터 감소
      kka
    langlaggug
    """

def parse_arguments(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    명령줄 인자 파싱
    
    Args:
        args: 명령줄 인자 (None이면 sys.argv 사용)
        
    Returns:
        파싱된 인자
    """
    parser = argparse.ArgumentParser(description='Ggaggalang 인터프리터')
    parser.add_argument('-f', '--file', help='실행할 Ggaggalang 코드 파일')
    parser.add_argument('-d', '--debug', action='store_true', help='디버그 모드 활성화')
    parser.add_argument('-t', '--text', help='Ggaggalang 코드로 변환할 텍스트')
    parser.add_argument('-e', '--example', choices=['hello', 'loop'], 
                      help='실행할 예제 코드 (hello: Hello World, loop: 루프 예제)')
    
    return parser.parse_args(args)

def run_from_args(args: Optional[argparse.Namespace] = None) -> None:
    """
    명령줄 인자로 인터프리터 실행
    
    Args:
        args: 파싱된 인자 (None이면 파싱 수행)
    """
    if args is None:
        args = parse_arguments()
    
    # 텍스트-코드 변환 모드
    if args.text:
        code = string_to_ggaggalang(args.text)
        print(f"## 다음 텍스트를 출력하는 Ggaggalang 코드:\n## \"{args.text}\"\n")
        print(code)
        return
    
    # 파일에서 코드 불러오기
    if args.file:
        code = load_code_from_file(args.file)
        if not code:
            return
    # 예제 코드 사용
    elif args.example == 'hello':
        code = get_hello_world_code()
    elif args.example == 'loop':
        code = get_loop_example_code()
    else:
        # 기본값: Hello World 예제
        code = get_hello_world_code()
    
    # 인터프리터 실행
    interpreter = GgaggalangInterpreter(debug=args.debug)
    interpreter.execute(code)
    print()  # 줄바꿈 추가

def main() -> None:
    """메인 함수"""
    # 명령줄 인자가 있으면 인자 기반으로 실행
    if len(sys.argv) > 1:
        run_from_args()
        return
    
    # 디버그 모드로 Hello World 실행
    print("=== Debug Mode ===")
    interpreter_debug = GgaggalangInterpreter(debug=True)
    interpreter_debug.execute(get_hello_world_code())
    print("\n")
    
    # 일반 모드로 Hello World 실행
    print("=== Normal Mode ===")
    interpreter = GgaggalangInterpreter(debug=False)
    interpreter.execute(get_hello_world_code())
    print()
    
    # 루프 예제 실행
    print("\n=== Loop Example ===")
    interpreter = GgaggalangInterpreter(debug=False)
    interpreter.execute(get_loop_example_code())
    print()

if __name__ == "__main__":
    main()
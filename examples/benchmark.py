#!/usr/bin/env python3
"""
Ggaggalang 인터프리터 성능 벤치마크
"""
import time
import argparse
from ggaggalang.interpreter import GgaggalangInterpreter
from ggaggalang.optimizer import GgaggalangOptimizer

def get_counter_code(n=100):
    """
    0부터 n-1까지 출력하는 코드 생성
    
    Args:
        n: 최대 숫자
        
    Returns:
        Ggaggalang 코드
    """
    code = f"""
    # 셀 0에 {n}을 저장 (카운트다운 값)
    {"gga " * n}
    
    # 셀 1로 이동하여 48 저장 (ASCII '0')
    gugu
    {"gga " * 48}
    
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
    return code

def get_memory_move_code(n=10000):
    """
    메모리 포인터를 n번 이동하는 코드 생성
    
    Args:
        n: 이동 횟수
        
    Returns:
        Ggaggalang 코드
    """
    return "gugu " * n

def run_benchmark(test_type, n, with_optimization=False):
    """
    벤치마크 실행
    
    Args:
        test_type: 테스트 유형 ('counter' 또는 'move')
        n: 반복 횟수
        with_optimization: 최적화 적용 여부
        
    Returns:
        실행 시간 (초)
    """
    interpreter = GgaggalangInterpreter(debug=False)
    
    if test_type == 'counter':
        code = get_counter_code(n)
    elif test_type == 'move':
        code = get_memory_move_code(n)
    else:
        raise ValueError(f"알 수 없는 테스트 유형: {test_type}")
    
    if with_optimization:
        # 코드 최적화
        commands = interpreter.parser.clean_code(code)
        optimized_commands = GgaggalangOptimizer.optimize(commands)
        code = " ".join(optimized_commands)
        precompiled = True
    else:
        precompiled = False
    
    # 실행 시간 측정
    start_time = time.time()
    interpreter.execute(code, precompiled=precompiled)
    end_time = time.time()
    
    return end_time - start_time

def main():
    parser = argparse.ArgumentParser(description='Ggaggalang 인터프리터 성능 벤치마크')
    parser.add_argument('--test', choices=['counter', 'move'], default='counter',
                      help='벤치마크 테스트 유형')
    parser.add_argument('-n', type=int, default=100,
                      help='반복 횟수 (카운터의 경우 최대 숫자, 이동의 경우 이동 횟수)')
    parser.add_argument('--optimize', action='store_true',
                      help='코드 최적화 사용')
    
    args = parser.parse_args()
    
    print(f"--- Ggaggalang 인터프리터 벤치마크 ---")
    print(f"테스트: {args.test}, 반복 횟수: {args.n}, 최적화: {'On' if args.optimize else 'Off'}")
    
    # 일반 실행
    print("실행 중...")
    time_taken = run_benchmark(args.test, args.n, args.optimize)
    
    print(f"실행 시간: {time_taken:.6f}초")
    
    if not args.optimize:
        # 최적화 모드와 비교
        print("\n최적화 모드와 비교 중...")
        opt_time = run_benchmark(args.test, args.n, True)
        print(f"최적화 실행 시간: {opt_time:.6f}초")
        
        speedup = time_taken / opt_time if opt_time > 0 else float('inf')
        print(f"속도 향상: {speedup:.2f}x")

if __name__ == "__main__":
    main()
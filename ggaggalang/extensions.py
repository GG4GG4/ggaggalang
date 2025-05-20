"""
Ggaggalang 언어 확장 기능 모듈

다음 기능을 추가합니다:
1. 함수 정의 및 호출
2. 조건부 분기
3. 수학 연산 확장
"""
from typing import Dict, List, Tuple, Optional, Any

class GgaggalangExtensions:
    """Ggaggalang 확장 기능"""
    
    # 추가 명령어 정의
    EXTENDED_COMMANDS = {
        # 함수 관련 명령어
        'gangga': 'FUNC_DEF',    # 함수 정의 시작
        'ggaggang': 'FUNC_END',  # 함수 정의 끝
        'gukku': 'FUNC_CALL',    # 함수 호출
        'kkuggu': 'FUNC_RET',    # 함수에서 반환
        
        # 조건부 분기 명령어
        'gagugug': 'IF_START',   # if 시작 (현재 셀이 0이 아니면 실행)
        'gugalang': 'IF_ELSE',   # else 시작
        'galanggu': 'IF_END',    # if-else 종료
        
        # 수학 연산 명령어
        'gaggug': 'MULTIPLY',    # 현재 셀과 다음 셀 값 곱하기
        'guggug': 'DIVIDE',      # 현재 셀 값을 다음 셀 값으로 나누기
        'kkakka': 'MOD',         # 현재 셀 값을 다음 셀 값으로 나눈 나머지
        
        # 메모리 조작 명령어
        'galang': 'COPY',        # 현재 셀 값을 다음 셀에 복사
        'ganggang': 'JUMP_TO',   # 포인터를 현재 셀 값 위치로 이동
        'gagagal': 'SET',        # 현재 셀 값을 직접 설정
    }
    
    def __init__(self):
        """GgaggalangExtensions 초기화"""
        self.function_table: Dict[int, Tuple[int, int]] = {}  # 함수 이름(셀 값) -> (시작 위치, 끝 위치)
        self.call_stack: List[int] = []  # 함수 호출 스택 (반환 위치)
        
    def register_function(self, name: int, start_pos: int, end_pos: int) -> None:
        """
        함수 등록
        
        Args:
            name: 함수 이름(셀 값)
            start_pos: 함수 시작 위치
            end_pos: 함수 종료 위치
        """
        self.function_table[name] = (start_pos, end_pos)
        
    def get_function(self, name: int) -> Optional[Tuple[int, int]]:
        """
        함수 정보 조회
        
        Args:
            name: 함수 이름(셀 값)
            
        Returns:
            (시작 위치, 끝 위치) 튜플 또는 None
        """
        return self.function_table.get(name)
        
    def push_call_stack(self, return_pos: int) -> None:
        """
        함수 호출 스택에 반환 위치 추가
        
        Args:
            return_pos: 함수 호출 후 돌아갈 위치
        """
        self.call_stack.append(return_pos)
        
    def pop_call_stack(self) -> Optional[int]:
        """
        함수 호출 스택에서 반환 위치 가져오기
        
        Returns:
            반환 위치 또는 None
        """
        if self.call_stack:
            return self.call_stack.pop()
        return None
        
    @staticmethod
    def scan_for_functions(commands: List[str]) -> Dict[int, Tuple[int, int]]:
        """
        코드에서 함수 정의 찾기
        
        Args:
            commands: 명령어 목록
            
        Returns:
            함수 테이블 (이름 -> (시작, 끝) 매핑)
        """
        functions: Dict[int, Tuple[int, int]] = {}
        func_start_stack: List[int] = []
        current_func_name: Optional[int] = None
        
        for i, cmd in enumerate(commands):
            if cmd == 'FUNC_DEF':  # 함수 정의 시작
                func_start_stack.append(i)
            elif cmd == 'FUNC_END':  # 함수 정의 끝
                if func_start_stack:
                    start_pos = func_start_stack.pop()
                    # 함수 이름은 시작 명령어 바로 앞 셀의 값이라고 가정
                    func_name = start_pos  # 실제로는 런타임에 메모리에서 찾아야 함
                    functions[func_name] = (start_pos + 1, i)
        
        return functions
        
    @staticmethod
    def scan_for_if_blocks(commands: List[str]) -> Dict[int, Tuple[int, int]]:
        """
        코드에서 if 블록 찾기
        
        Args:
            commands: 명령어 목록
            
        Returns:
            if 블록 테이블 (시작 -> 끝 매핑)
        """
        if_blocks: Dict[int, int] = {}  # if 시작 -> else 또는 if_end
        else_blocks: Dict[int, int] = {}  # else -> if_end
        if_stack: List[int] = []
        
        for i, cmd in enumerate(commands):
            if cmd == 'IF_START':  # if 시작
                if_stack.append(i)
            elif cmd == 'IF_ELSE':  # else
                if if_stack:
                    if_start = if_stack[-1]
                    if_blocks[if_start] = i
            elif cmd == 'IF_END':  # if/else 종료
                if if_stack:
                    if_start = if_stack.pop()
                    if if_start in if_blocks:  # else가 있는 경우
                        else_pos = if_blocks[if_start]
                        else_blocks[else_pos] = i
                    else:  # else가 없는 경우
                        if_blocks[if_start] = i
        
        # if, else, end 포인트 모두 결합
        result = {}
        for if_start, next_point in if_blocks.items():
            if next_point in else_blocks:
                result[if_start] = (next_point, else_blocks[next_point])
            else:
                result[if_start] = (next_point, next_point)
                
        return result
"""
Ggaggalang 파서 모듈
"""
from typing import List, Tuple, Dict, Optional
from .errors import GgaggalangSyntaxError
from .extensions import GgaggalangExtensions

class GgaggalangParser:
    """Ggaggalang 코드를 파싱하는 클래스"""
    
    # 기본 명령어 정의
    COMMANDS = {
        'gga': '+',          # 현재 포인터가 가리키는 메모리 셀의 값을 1 증가
        'kka': '-',          # 현재 포인터가 가리키는 메모리 셀의 값을 1 감소
        'gugu': '>',         # 메모리 포인터를 오른쪽으로 이동
        'gugugga': '<',      # 메모리 포인터를 왼쪽으로 이동
        'gguggaggugga': '.', # 현재 메모리 셀의 값을 ASCII 문자로 출력
        'ggalgga': ',',      # 사용자 입력을 받아 현재 메모리 셀에 저장
        'galanglang': '[',   # 현재 메모리 셀의 값이 0이면 대응하는 `langlaggug`로 이동
        'langlaggug': ']',   # 현재 메모리 셀의 값이 0이 아니면 대응하는 `galanglang`으로 이동
    }
    
    # 확장 명령어 결합
    COMMANDS.update(GgaggalangExtensions.EXTENDED_COMMANDS)
    
    def __init__(self, debug: bool = False):
        """
        GgaggalangParser 초기화
        
        Args:
            debug: 디버그 모드 활성화 여부
        """
        self.debug = debug
        self.original_code = ""
        self.lines = []
        self.pos_to_line_col = {}  # 위치 매핑 데이터
        
    def parse_command(self, code: str, pos: int) -> Tuple[Optional[str], int]:
        """
        현재 위치에서 시작하는 명령어를 파싱
        
        Args:
            code: 파싱할 코드
            pos: 현재 위치
            
        Returns:
            (명령어, 길이) 튜플, 명령어가 없으면 (None, 1)
        """
        # 가장 긴 명령어부터 순서대로 확인
        for cmd in sorted(self.COMMANDS.keys(), key=len, reverse=True):
            if code.startswith(cmd, pos):
                return (cmd, len(cmd))
        return (None, 1)
    
    def clean_code(self, code: str) -> List[str]:
        """
        코드에서 주석과 공백을 제거하고 명령어 목록을 반환
        
        Args:
            code: 원본 코드
            
        Returns:
            파싱된 명령어 목록
            
        Raises:
            GgaggalangSyntaxError: 문법 오류 발생 시
        """
        self.original_code = code
        self.lines = code.split('\n')
        
        # 주석 제거 및 줄 시작 위치 추적
        cleaned = ''
        line_start_pos = [0]  # 각 줄의 시작 위치를 추적
        current_pos = 0
        
        for i, line in enumerate(self.lines):
            if '#' in line:
                line = line[:line.index('#')]
            cleaned += line
            current_pos += len(line)
            if i < len(self.lines) - 1:
                line_start_pos.append(current_pos)
        
        # 위치 매핑을 위한 데이터 구조 생성
        self.pos_to_line_col = {}
        for i, start_pos in enumerate(line_start_pos):
            line = self.lines[i]
            for j in range(len(line)):
                if start_pos + j < len(cleaned):
                    self.pos_to_line_col[start_pos + j] = (i + 1, j + 1)  # 1-based line and column
            
        # 명령어 추출
        commands = []
        pos = 0
        while pos < len(cleaned):
            # 공백 건너뛰기
            if cleaned[pos].isspace():
                pos += 1
                continue
            
            # 명령어 매칭 시도
            command, length = self.parse_command(cleaned, pos)
            if command:
                commands.append(command)
            else:
                # 알 수 없는 명령어
                line, col = self.pos_to_line_col.get(pos, (0, 0))
                unknown_char = cleaned[pos] if pos < len(cleaned) else "EOF"
                raise GgaggalangSyntaxError(
                    f"알 수 없는 명령어: '{unknown_char}'", line, col
                )
            
            pos += length

        if self.debug:
            print(f"DEBUG: 파싱된 명령어: {' '.join(commands)}")
            
        return commands
    
    def check_bracket_matching(self, commands: List[str]) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        명령어 목록에서 괄호 짝이 맞는지 확인
        
        Args:
            commands: 명령어 목록
            
        Returns:
            (매칭 여부, 오류 위치, 오류 메시지) 튜플
        """
        stack = []
        for i, cmd in enumerate(commands):
            if cmd == 'galanglang':
                stack.append(i)
            elif cmd == 'langlaggug':
                if not stack:
                    return False, i, "닫는 괄호에 대응하는 여는 괄호가 없습니다"
                stack.pop()
        if stack:
            return False, stack[0], "여는 괄호에 대응하는 닫는 괄호가 없습니다"
        return True, None, None
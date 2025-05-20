"""
Ggaggalang 인터프리터 모듈
성능 개선을 위한 최적화 적용
"""
from typing import List, Optional, Dict, Any, Callable
import traceback
import array
from .errors import GgaggalangSyntaxError, GgaggalangRuntimeError
from .parser import GgaggalangParser
from .visualizer import MemoryVisualizer

class GgaggalangInterpreter:
    """Ggaggalang 인터프리터 클래스"""
    
    def __init__(self, debug: bool = False, memory_size: int = 30000):
        """
        GgaggalangInterpreter 초기화
        
        Args:
            debug: 디버그 모드 활성화 여부
            memory_size: 메모리 셀 개수
        """
        # 배열 타입 사용으로 메모리 효율 개선
        self.memory = array.array('B', [0] * memory_size)  # 부호 없는 바이트 배열로 메모리 최적화
        self.memory_size = memory_size
        self.pointer = 0
        self.debug = debug
        self.loop_stack = []
        self.current_command_index = 0
        self.commands = []
        self.parser = GgaggalangParser(debug=debug)
        
        # 명령어 처리 함수 매핑 (dispatcher) - 성능 개선
        self.command_handlers = {
            'gga': self.increment,
            'kka': self.decrement,
            'gugu': self.move_right,
            'gugugga': self.move_left,
            'gguggaggugga': self.output_byte,
            'ggalgga': self.input_byte,
            'galanglang': self.loop_start,
            'langlaggug': self.loop_end
        }
        
    def increment(self) -> None:
        """gga: 현재 포인터가 가리키는 메모리 셀의 값을 1 증가"""
        try:
            self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값을 1 증가: {self.memory[self.pointer]}")
        except IndexError:
            raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")

    def decrement(self) -> None:
        """kka: 현재 포인터가 가리키는 메모리 셀의 값을 1 감소"""
        try:
            self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값을 1 감소: {self.memory[self.pointer]}")
        except IndexError:
            raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")

    def move_right(self) -> None:
        """gugu: 메모리 포인터를 오른쪽으로 이동"""
        old_pointer = self.pointer
        if self.pointer == self.memory_size - 1:
            self.pointer = 0
            if self.debug:
                print(f"DEBUG: 포인터를 오른쪽으로 이동: {old_pointer} → {self.pointer} (메모리 순환)")
        else:
            self.pointer += 1
            if self.debug:
                print(f"DEBUG: 포인터를 오른쪽으로 이동: {old_pointer} → {self.pointer}")

    def move_left(self) -> None:
        """gugugga: 메모리 포인터를 왼쪽으로 이동"""
        old_pointer = self.pointer
        if self.pointer == 0:
            self.pointer = self.memory_size - 1
            if self.debug:
                print(f"DEBUG: 포인터를 왼쪽으로 이동: {old_pointer} → {self.pointer} (메모리 순환)")
        else:
            self.pointer -= 1
            if self.debug:
                print(f"DEBUG: 포인터를 왼쪽으로 이동: {old_pointer} → {self.pointer}")

    def output_byte(self) -> None:
        """gguggaggugga: 현재 메모리 셀의 값을 ASCII 문자로 출력"""
        try:
            if self.pointer < 0 or self.pointer >= len(self.memory):
                raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")
                
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값 출력: {self.memory[self.pointer]} ({chr(self.memory[self.pointer])})")
            print(chr(self.memory[self.pointer]), end='')
        except ValueError:
            # ASCII 범위를 벗어난 경우
            raise GgaggalangRuntimeError(f"출력 오류: 셀 {self.pointer}의 값 {self.memory[self.pointer]}은 유효한 ASCII 문자가 아닙니다.")

    def input_byte(self) -> None:
        """ggalgga: 사용자 입력을 받아 현재 메모리 셀에 저장"""
        try:
            if self.pointer < 0 or self.pointer >= len(self.memory):
                raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")
                
            user_input = input()
            if user_input:
                input_char = user_input[0]
                self.memory[self.pointer] = ord(input_char)
                if self.debug:
                    print(f"DEBUG: 입력 값 {ord(input_char)} ({input_char}) 저장 → 셀 {self.pointer}")
            else:
                self.memory[self.pointer] = 0
                if self.debug:
                    print(f"DEBUG: 빈 입력, 셀 {self.pointer}에 0 저장")
        except Exception as e:
            if self.debug:
                print(f"DEBUG: 입력 오류: {e}")
            raise GgaggalangRuntimeError(f"입력 오류: {str(e)}")
            
    def loop_start(self) -> None:
        """galanglang: 현재 메모리 셀의 값이 0이면 대응하는 langlaggug로 이동"""
        if self.memory[self.pointer] == 0:
            # 값이 0이면 대응하는 닫는 괄호로 이동
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값이 0, 루프 건너뛰기")
            loop_count = 1
            i = self.current_command_index + 1
            while loop_count > 0 and i < len(self.commands):
                if self.commands[i] == 'galanglang':
                    loop_count += 1
                elif self.commands[i] == 'langlaggug':
                    loop_count -= 1
                i += 1
            self.current_command_index = i - 1  # 닫는 괄호 다음 명령어 위치로 설정
        else:
            # 값이 0이 아니면 루프 진입
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값이 {self.memory[self.pointer]}, 루프 진입")
            self.loop_stack.append(self.current_command_index)

    def loop_end(self) -> None:
        """langlaggug: 현재 메모리 셀의 값이 0이 아니면 대응하는 galanglang으로 이동"""
        if self.memory[self.pointer] != 0:
            # 값이 0이 아니면 대응하는 여는 괄호로 이동
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값이 {self.memory[self.pointer]}, 루프 반복")
            if self.loop_stack:
                self.current_command_index = self.loop_stack[-1]  # 여는 괄호 위치로 이동
            else:
                if self.debug:
                    print("ERROR: 괄호 불일치 - 대응하는 여는 괄호가 없습니다")
        else:
            # 값이 0이면 루프 종료
            if self.debug:
                print(f"DEBUG: 셀 {self.pointer}의 값이 0, 루프 종료")
            if self.loop_stack:
                self.loop_stack.pop()
            else:
                if self.debug:
                    print("ERROR: 괄호 불일치 - 대응하는 여는 괄호가 없습니다")
                    
    def show_debug_memory_state(self) -> None:
        """메모리 상태를 시각적으로 표시"""
        if not self.debug:
            return
        MemoryVisualizer.print_memory_state(self.memory, self.pointer)

    def precompile_loops(self) -> Dict[int, int]:
        """
        루프 시작과 끝 위치 미리 계산 (성능 최적화)
        
        Returns:
            루프 시작/끝 위치 매핑 사전
        """
        loop_map = {}  # 시작 위치 -> 끝 위치, 끝 위치 -> 시작 위치 매핑
        stack = []     # 열린 대괄호 위치 저장
        
        for i, cmd in enumerate(self.commands):
            if cmd == 'galanglang':  # 루프 시작
                stack.append(i)
            elif cmd == 'langlaggug':  # 루프 끝
                if not stack:  # 이미 파서에서 검증됨
                    continue
                
                start_pos = stack.pop()
                end_pos = i
                
                # 양방향 매핑
                loop_map[start_pos] = end_pos
                loop_map[end_pos] = start_pos
                
        return loop_map
        
    def execute(self, code: str, precompiled: bool = False) -> None:
        """
        Ggaggalang 코드 실행
        
        Args:
            code: 실행할 코드
            precompiled: 사전 처리된 코드 여부 (True이면 파싱 단계 건너뜀)
        """
        try:
            # 초기화
            self.pointer = 0
            self.memory = array.array('B', [0] * self.memory_size)
            self.loop_stack = []
            
            # 코드 파싱 (precompiled가 False인 경우에만)
            if not precompiled:
                self.commands = self.parser.clean_code(code)
                
                # 괄호 매칭 확인
                brackets_match, error_pos, error_msg = self.parser.check_bracket_matching(self.commands)
                if not brackets_match:
                    if self.debug:
                        cmd_with_error = self.commands[error_pos] if error_pos < len(self.commands) else "<end of code>"
                        print(f"ERROR: {error_msg} at command {error_pos} ({cmd_with_error})")
                    raise GgaggalangSyntaxError(f"{error_msg}", 0, 0)
            else:
                # 이미 처리된 코드 (최적화 직후 실행 등)
                self.commands = code.split()
            
            # 루프 위치 미리 계산 (최적화)
            loop_map = self.precompile_loops()
            
            # 명령어 실행
            self.current_command_index = 0
            self.loop_stack = []
            
            if self.debug:
                print("DEBUG: 실행 시작")
                self.show_debug_memory_state()
                
            # 실행 루프 최적화
            while self.current_command_index < len(self.commands):
                cmd = self.commands[self.current_command_index]
                
                if self.debug:
                    print(f"DEBUG: 실행 중: {cmd} (명령어 #{self.current_command_index+1})")
                
                # 명령어 dispatcher 패턴 사용 (if-else 체인보다 빠름)
                # 최적화된 명령어 처리
                if cmd.startswith("ADD "):
                    # 최적화된 증가 명령어
                    value = int(cmd.split()[1])
                    self.memory[self.pointer] = (self.memory[self.pointer] + value) % 256
                    if self.debug:
                        print(f"DEBUG: Cell {self.pointer} 값 {value} 증가: {self.memory[self.pointer]}")
                elif cmd.startswith("SUB "):
                    # 최적화된 감소 명령어
                    value = int(cmd.split()[1])
                    self.memory[self.pointer] = (self.memory[self.pointer] - value) % 256
                    if self.debug:
                        print(f"DEBUG: Cell {self.pointer} 값 {value} 감소: {self.memory[self.pointer]}")
                elif cmd.startswith("RIGHT "):
                    # 최적화된 오른쪽 이동 명령어
                    value = int(cmd.split()[1])
                    self.pointer = (self.pointer + value) % self.memory_size
                    if self.debug:
                        print(f"DEBUG: 포인터 오른쪽으로 {value}칸 이동: {self.pointer}")
                elif cmd.startswith("LEFT "):
                    # 최적화된 왼쪽 이동 명령어
                    value = int(cmd.split()[1])
                    self.pointer = (self.pointer - value) % self.memory_size
                    if self.debug:
                        print(f"DEBUG: 포인터 왼쪽으로 {value}칸 이동: {self.pointer}")
                elif cmd == "CLEAR":
                    # 최적화된 셀 초기화 명령어
                    self.memory[self.pointer] = 0
                    if self.debug:
                        print(f"DEBUG: Cell {self.pointer} 값 초기화: 0")
                elif cmd in self.command_handlers:
                    # 루프 명령어 최적화 처리
                    if cmd == 'galanglang':  # 루프 시작
                        if self.memory[self.pointer] == 0:
                            # 값이 0이면 짝이 되는 닫는 괄호로 바로 점프
                            self.current_command_index = loop_map[self.current_command_index]
                        else:
                            # 루프 스택 관리는 기존 메서드가 담당
                            self.loop_start()
                    elif cmd == 'langlaggug':  # 루프 끝
                        if self.memory[self.pointer] != 0:
                            # 값이 0이 아니면 짝이 되는 여는 괄호로 바로 점프
                            self.current_command_index = loop_map[self.current_command_index]
                        else:
                            # 루프 스택 관리는 기존 메서드가 담당
                            self.loop_end()
                    else:
                        # 일반 명령어 실행
                        self.command_handlers[cmd]()
                
                if self.debug and (cmd == 'gga' or cmd == 'kka' or cmd == 'ggalgga'):
                    # 메모리 값이 변경되는 명령어 후에만 메모리 상태 표시
                    self.show_debug_memory_state()
                
                self.current_command_index += 1
                
            if self.debug:
                print("\nDEBUG: 실행 완료")
                self.show_debug_memory_state()
                
        except GgaggalangSyntaxError as e:
            print(f"문법 오류: {e}")
            if self.debug:
                print(f"디버그 정보: 줄 {e.line}, 열 {e.column}")
                
        except GgaggalangRuntimeError as e:
            print(f"실행 오류: {e}")
            if self.debug:
                print(f"디버그 정보: 명령어 #{self.current_command_index+1} ({self.commands[self.current_command_index]})")
                traceback.print_exc()
                
        except Exception as e:
            print(f"오류 발생: {e}")
            if self.debug:
                print(f"디버그 정보: 명령어 #{self.current_command_index+1} (알 수 없는 오류)")
                traceback.print_exc()
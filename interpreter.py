class GgaggalangError(Exception):
    """Ggaggalang 인터프리터 관련 예외 기본 클래스"""
    pass

class GgaggalangSyntaxError(GgaggalangError):
    """Ggaggalang 코드의 문법 오류"""
    def __init__(self, message, line=None, column=None):
        self.line = line
        self.column = column
        if line is not None and column is not None:
            message = f"{message} (위치: 줄 {line}, 열 {column})"
        super().__init__(message)
        
class GgaggalangRuntimeError(GgaggalangError):
    """Ggaggalang 코드 실행 중 발생한 오류"""
    pass

class GgaggalangInterpreter:
    def __init__(self, debug=False):
        self.memory = [0] * 30000  # 30,000 cells of memory
        self.pointer = 0  # Current memory cell pointer
        self.debug = debug  # Debug mode flag
        self.loop_stack = []  # Stack to track loop positions
        self.original_code = ""  # 원본 코드 저장
        self.lines = []  # 줄 단위로 저장된 코드
        self.current_line = 0  # 현재 처리 중인 코드 줄 번호
        self.current_column = 0  # 현재 처리 중인 코드 열 번호
        
    def increment(self):
        """gga: increment the byte at pointer"""
        try:
            self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            if self.debug:
                print(f"DEBUG: Cell {self.pointer} incremented to {self.memory[self.pointer]}")
        except IndexError:
            raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")

    def decrement(self):
        """kka: decrement the byte at pointer"""
        try:
            self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            if self.debug:
                print(f"DEBUG: Cell {self.pointer} decremented to {self.memory[self.pointer]}")
        except IndexError:
            raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")

    def move_right(self):
        """gugu: increment the data pointer"""
        old_pointer = self.pointer
        if self.pointer == 29999:
            self.pointer = 0
            if self.debug:
                print(f"DEBUG: Moved right from {old_pointer} to cell {self.pointer} (메모리 순환)")
        else:
            self.pointer += 1
            if self.debug:
                print(f"DEBUG: Moved right to cell {self.pointer}")

    def move_left(self):
        """gugugga: decrement the data pointer"""
        old_pointer = self.pointer
        if self.pointer == 0:
            self.pointer = 29999
            if self.debug:
                print(f"DEBUG: Moved left from {old_pointer} to cell {self.pointer} (메모리 순환)")
        else:
            self.pointer -= 1
            if self.debug:
                print(f"DEBUG: Moved left to cell {self.pointer}")

    def output_byte(self):
        """gguggaggugga: output the byte at pointer"""
        try:
            if self.pointer < 0 or self.pointer >= len(self.memory):
                raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")
                
            if self.debug:
                print(f"DEBUG: Outputting cell {self.pointer} with value {self.memory[self.pointer]} ({chr(self.memory[self.pointer])})")
            print(chr(self.memory[self.pointer]), end='')
        except ValueError:
            # ASCII 범위를 벗어난 경우
            raise GgaggalangRuntimeError(f"출력 오류: 셀 {self.pointer}의 값 {self.memory[self.pointer]}은 유효한 ASCII 문자가 아닙니다.")

    def input_byte(self):
        """ggalgga: input a byte and store it at pointer"""
        try:
            if self.pointer < 0 or self.pointer >= len(self.memory):
                raise GgaggalangRuntimeError(f"메모리 범위 초과: 인덱스 {self.pointer}가 유효하지 않습니다.")
                
            user_input = input()
            if user_input:
                input_char = user_input[0]
                self.memory[self.pointer] = ord(input_char)
                if self.debug:
                    print(f"DEBUG: Input value {ord(input_char)} ({input_char}) stored in cell {self.pointer}")
            else:
                self.memory[self.pointer] = 0
                if self.debug:
                    print(f"DEBUG: Empty input, stored 0 in cell {self.pointer}")
        except Exception as e:
            if self.debug:
                print(f"DEBUG: Error getting input: {e}")
            raise GgaggalangRuntimeError(f"입력 오류: {str(e)}")
            
    def loop_start(self):
        """galanglang: if the byte at pointer is zero, jump forward to the matching langlaggug"""
        if self.memory[self.pointer] == 0:
            # Skip to matching end loop
            if self.debug:
                print(f"DEBUG: Cell {self.pointer} is 0, skipping loop")
            loop_count = 1
            i = self.current_command_index + 1
            while loop_count > 0 and i < len(self.commands):
                if self.commands[i] == 'galanglang':
                    loop_count += 1
                elif self.commands[i] == 'langlaggug':
                    loop_count -= 1
                i += 1
            self.current_command_index = i - 1  # Set to the command after the matching end loop
        else:
            # Remember position of loop start
            if self.debug:
                print(f"DEBUG: Cell {self.pointer} is {self.memory[self.pointer]}, entering loop")
            self.loop_stack.append(self.current_command_index)

    def loop_end(self):
        """langlaggug: if the byte at pointer is nonzero, jump back to the matching galanglang"""
        if self.memory[self.pointer] != 0:
            # Jump back to matching loop start
            if self.debug:
                print(f"DEBUG: Cell {self.pointer} is {self.memory[self.pointer]}, repeating loop")
            if self.loop_stack:
                self.current_command_index = self.loop_stack[-1]  # Jump to matching loop start
            else:
                if self.debug:
                    print("ERROR: Mismatched loop brackets - no matching loop start found")
        else:
            # Exit loop - pop the matching loop start from stack
            if self.debug:
                print(f"DEBUG: Cell {self.pointer} is 0, exiting loop")
            if self.loop_stack:
                self.loop_stack.pop()
            else:
                if self.debug:
                    print("ERROR: Mismatched loop brackets - no matching loop start found")

    def parse_command(self, code, pos):
        """Parse a single command starting at the given position"""
        if code.startswith('gguggaggugga', pos):
            return ('gguggaggugga', 12)
        elif code.startswith('gugugga', pos):
            return ('gugugga', 7)
        elif code.startswith('gugu', pos):
            return ('gugu', 4)
        elif code.startswith('gga', pos):
            return ('gga', 3)
        elif code.startswith('kka', pos):
            return ('kka', 3)
        elif code.startswith('ggalgga', pos):
            return ('ggalgga', 7)
        elif code.startswith('galanglang', pos):
            return ('galanglang', 10)
        elif code.startswith('langlaggug', pos):
            return ('langlaggug', 10)
        return (None, 1)

    def clean_code(self, code):
        """Remove comments and whitespace from code"""
        self.original_code = code
        self.lines = code.split('\n')
        
        # First, remove comments and join all lines
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
        
        # 위치 매핑을 위한 데이터 구조
        self.pos_to_line_col = {}
        for i, start_pos in enumerate(line_start_pos):
            line = self.lines[i]
            for j in range(len(line)):
                if start_pos + j < len(cleaned):
                    self.pos_to_line_col[start_pos + j] = (i + 1, j + 1)  # 1-based line and column
            
        # Then extract commands
        commands = []
        pos = 0
        while pos < len(cleaned):
            # Skip whitespace
            if cleaned[pos].isspace():
                pos += 1
                continue
            
            # Try to match commands from longest to shortest
            command, length = self.parse_command(cleaned, pos)
            if command:
                commands.append(command)
            else:
                # 유효하지 않은 명령어 발견
                line, col = self.pos_to_line_col.get(pos, (0, 0))
                unknown_char = cleaned[pos] if pos < len(cleaned) else "EOF"
                raise GgaggalangSyntaxError(
                    f"알 수 없는 명령어: '{unknown_char}'", line, col
                )
            
            pos += length

        if self.debug:
            print(f"DEBUG: Parsed commands: {' '.join(commands)}")
        return ' '.join(commands)  # Commands are now space-separated

    def check_bracket_matching(self, commands):
        """Check if brackets in the code are properly matched"""
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
        
    def show_debug_memory_state(self, highlight_pointer=True):
        """메모리 상태를 시각적으로 표시하는 디버그 함수"""
        if not self.debug:
            return
            
        # 현재 포인터 주변의 메모리 영역만 표시 (최대 20개 셀)
        start = max(0, self.pointer - 10)
        end = min(len(self.memory), start + 20)
        
        print("\nDEBUG: 메모리 상태:")
        print("┌" + "─" * 77 + "┐")
        
        # 메모리 영역 헤더 - 인덱스 표시
        header = "│ "
        for i in range(start, end):
            cell_index = f"{i:4d}"  # 4자리로 맞춤
            header += f"{cell_index:<7s}"
        print(header + " │")
        
        # 구분선
        print("├" + "─" * 77 + "┤")
        
        # 메모리 값 표시
        values = "│ "
        for i in range(start, end):
            if highlight_pointer and i == self.pointer:
                # 현재 포인터 위치 강조
                cell_value = f"[{self.memory[i]:3d}]"
            else:
                cell_value = f" {self.memory[i]:3d} "
            values += f"{cell_value:<7s}"
        print(values + " │")
        
        # ASCII 값 표시
        ascii_values = "│ "
        for i in range(start, end):
            if self.memory[i] >= 32 and self.memory[i] <= 126:  # 출력 가능한 ASCII 범위
                char = chr(self.memory[i])
            else:
                char = "·"  # 출력 불가능한 문자는 점으로 표시
                
            if highlight_pointer and i == self.pointer:
                # 현재 포인터 위치 강조
                cell_char = f"[{char:1s}]  "
            else:
                cell_char = f" {char:1s}   "
            ascii_values += f"{cell_char:<7s}"
        print(ascii_values + " │")
        
        print("└" + "─" * 77 + "┘")

    def execute(self, code):
        """Execute the Ggaggalang code"""
        try:
            # 초기화
            self.pointer = 0
            self.memory = [0] * 30000
            self.loop_stack = []
            
            # Clean and parse code
            code = self.clean_code(code)
            if self.debug:
                print(f"DEBUG: Cleaned code: {code}")
            
            # Split code into commands
            self.commands = code.split()
            
            # Check for matching brackets
            brackets_match, error_pos, error_msg = self.check_bracket_matching(self.commands)
            if not brackets_match:
                if self.debug:
                    cmd_with_error = self.commands[error_pos] if error_pos < len(self.commands) else "<end of code>"
                    print(f"ERROR: {error_msg} at command {error_pos} ({cmd_with_error})")
                raise GgaggalangSyntaxError(f"{error_msg}", 0, 0)
            
            # Execute commands
            self.current_command_index = 0
            self.loop_stack = []
            
            if self.debug:
                print("DEBUG: 실행 시작")
                self.show_debug_memory_state()
                
            while self.current_command_index < len(self.commands):
                cmd = self.commands[self.current_command_index]
                
                if self.debug:
                    print(f"DEBUG: 실행 중: {cmd} (명령어 #{self.current_command_index+1})")
                
                if cmd == 'gguggaggugga':
                    self.output_byte()
                elif cmd == 'gugu':
                    self.move_right()
                elif cmd == 'gugugga':
                    self.move_left()
                elif cmd == 'gga':
                    self.increment()
                elif cmd == 'kka':
                    self.decrement()
                elif cmd == 'ggalgga':
                    self.input_byte()
                elif cmd == 'galanglang':
                    self.loop_start()
                elif cmd == 'langlaggug':
                    self.loop_end()
                    
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
                import traceback
                traceback.print_exc()
                
        except Exception as e:
            print(f"오류 발생: {e}")
            if self.debug:
                print(f"디버그 정보: 명령어 #{self.current_command_index+1} (알 수 없는 오류)")
                import traceback
                traceback.print_exc()
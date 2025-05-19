class GgaggalangInterpreter:
    def __init__(self, debug=False):
        self.memory = [0] * 30000  # 30,000 cells of memory
        self.pointer = 0  # Current memory cell pointer
        self.debug = debug  # Debug mode flag
        self.loop_stack = []  # Stack to track loop positions
        
    def increment(self):
        """gga: increment the byte at pointer"""
        self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
        if self.debug:
            print(f"DEBUG: Cell {self.pointer} incremented to {self.memory[self.pointer]}")

    def decrement(self):
        """kka: decrement the byte at pointer"""
        self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
        if self.debug:
            print(f"DEBUG: Cell {self.pointer} decremented to {self.memory[self.pointer]}")

    def move_right(self):
        """gugu: increment the data pointer"""
        if self.pointer == 29999:
            self.pointer = 0
        else:
            self.pointer += 1
        if self.debug:
            print(f"DEBUG: Moved right to cell {self.pointer}")

    def move_left(self):
        """gugugga: decrement the data pointer"""
        if self.pointer == 0:
            self.pointer = 29999
        else:
            self.pointer -= 1
        if self.debug:
            print(f"DEBUG: Moved left to cell {self.pointer}")

    def output_byte(self):
        """gguggaggugga: output the byte at pointer"""
        if self.debug:
            print(f"DEBUG: Outputting cell {self.pointer} with value {self.memory[self.pointer]} ({chr(self.memory[self.pointer])})")
        print(chr(self.memory[self.pointer]), end='')

    def input_byte(self):
        """ggalgga: input a byte and store it at pointer"""
        try:
            input_char = input()[0] if input() else '\0'
            self.memory[self.pointer] = ord(input_char)
            if self.debug:
                print(f"DEBUG: Input value {ord(input_char)} stored in cell {self.pointer}")
        except Exception as e:
            if self.debug:
                print(f"DEBUG: Error getting input: {e}")
            self.memory[self.pointer] = 0
            
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
        # First, remove comments and join all lines
        cleaned = ''
        for line in code.split('\n'):
            if '#' in line:
                line = line[:line.index('#')]
            cleaned += line
            
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
                    return False, i, "Closing bracket without matching opening bracket"
                stack.pop()
        if stack:
            return False, stack[0], "Opening bracket without matching closing bracket"
        return True, None, None

    def execute(self, code):
        """Execute the Ggaggalang code"""
        try:
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
                raise SyntaxError(f"{error_msg} at position {error_pos}")
            
            # Execute commands
            self.current_command_index = 0
            self.loop_stack = []
            while self.current_command_index < len(self.commands):
                cmd = self.commands[self.current_command_index]
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
                self.current_command_index += 1
        except Exception as e:
            print(f"Error executing code: {e}")
            if self.debug:
                import traceback
                traceback.print_exc()
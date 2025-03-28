class GgaggalangInterpreter:
    def __init__(self, debug=False):
        self.memory = [0] * 30000  # 30,000 cells of memory
        self.pointer = 0  # Current memory cell pointer
        self.debug = debug  # Debug mode flag
        
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

    def execute(self, code):
        """Execute the Ggaggalang code"""
        code = self.clean_code(code)
        if self.debug:
            print(f"DEBUG: Cleaned code: {code}")
        
        # Split code into commands and execute each
        commands = code.split()
        for cmd in commands:
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
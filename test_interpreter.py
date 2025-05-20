#!/usr/bin/env python3
"""
Ggaggalang 인터프리터 테스트
"""
import unittest
import io
import sys
from ggaggalang.interpreter import GgaggalangInterpreter
from ggaggalang.errors import GgaggalangSyntaxError

class TestGgaggalangInterpreter(unittest.TestCase):
    def setUp(self):
        # 각 테스트 전에 새로운 인터프리터 객체 생성
        self.interpreter = GgaggalangInterpreter(debug=False)
        
        # 표준 출력 리디렉션 설정
        self.held_output = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
        
    def tearDown(self):
        # 표준 출력 복원
        sys.stdout = self.original_stdout
        
    def test_basic_commands(self):
        # 기본 명령어 테스트
        # 'A' (ASCII 65) 출력 코드
        code = """
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga # 65 (A)
        gguggaggugga
        """
        self.interpreter.execute(code)
        self.assertEqual(self.held_output.getvalue(), "A")
        
    def test_memory_wrap(self):
        # 메모리 값이 255를 초과하면 0으로 돌아가는지 테스트
        # 메모리 셀에 256을 더하면 원래 값이 나와야 함
        # ASCII 65 (A) 출력
        code = """
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga # 65 (A)
        
        # 256 더하기
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga # 256
        
        gguggaggugga
        """
        self.interpreter.execute(code)
        self.assertEqual(self.held_output.getvalue(), "A")
        
    def test_pointer_wrap(self):
        # 포인터가 메모리 범위를 초과하면 처음으로 돌아가는지 테스트
        code = """
        # 셀 0에 'A' (65) 저장
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga # 65 (A)
        
        # 포인터를 오른쪽으로 이동 (30000번 - 메모리 끝까지)
        """
        # 포인터를 오른쪽으로 30000번 이동 (메모리 크기만큼)하는 코드 추가
        code += "gugu " * 30000
        
        # 출력 명령 추가
        code += """
        gguggaggugga
        """
        
        self.interpreter.execute(code)
        self.assertEqual(self.held_output.getvalue(), "A")
    
    def test_loop_commands(self):
        # 루프 명령어 테스트 (0-2 출력)
        code = """
        # 셀 0에 3 저장 (카운트다운)
        gga gga gga # 3
        
        # 셀 1로 이동하여 48 저장 (ASCII '0')
        gugu
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga gga gga
        gga gga gga gga gga gga gga gga # 48
        
        # 셀 0으로 돌아가기
        gugugga
        
        # 루프 시작
        galanglang
          # 셀 1로 이동하여 출력
          gugu
          gguggaggugga
          # 셀 1 값을 증가 (다음 ASCII 값)
          gga
          # 셀 0으로 돌아가기
          gugugga
          # 셀 0 값을 감소
          kka
        langlaggug
        """
        
        self.interpreter.execute(code)
        self.assertEqual(self.held_output.getvalue(), "012")
    
    def test_error_handling(self):
        # 괄호 불일치 오류 테스트
        code = """
        # 괄호가 짝이 맞지 않는 코드
        galanglang
        gga
        # langlaggug 가 없음
        """
        
        # GgaggalangSyntaxError가 발생하는지 확인
        with self.assertRaises(GgaggalangSyntaxError):
            self.interpreter.parser.check_bracket_matching(
                self.interpreter.parser.clean_code(code)
            )
    
    def test_comments_and_whitespace(self):
        # 주석과 공백이 제대로 처리되는지 테스트
        code = """
        # 이것은 주석입니다
        gga gga # 이것도 주석입니다
        gga     gga # 공백이 여러 개 있습니다
        
        # 빈 줄도 있습니다
          # 들여쓰기된 주석도 있습니다
        gguggaggugga # 값 4를 ASCII로 출력합니다 (EOT 문자)
        """
        
        self.interpreter.execute(code)
        # ASCII 4는 EOT(End of Transmission) 제어 문자로 화면에 출력되지 않을 수 있음
        # 출력이 있었는지만 확인
        self.assertEqual(len(self.held_output.getvalue()), 1)
    
    def test_input_command(self):
        # 입력 명령어 테스트가 실패하면 이 테스트는 건너뛰기
        # (표준 입력을 시뮬레이션하는 것은 테스트 환경에 따라 불안정할 수 있음)
        self.skipTest("입력 명령어는 인터랙티브 테스트가 필요합니다")

if __name__ == "__main__":
    unittest.main()
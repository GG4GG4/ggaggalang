"""
Ggaggalang 인터프리터 관련 예외 클래스들
"""

class GgaggalangError(Exception):
    """Ggaggalang 인터프리터 관련 예외 기본 클래스"""
    pass

class GgaggalangSyntaxError(GgaggalangError):
    """Ggaggalang 코드의 문법 오류"""
    def __init__(self, message: str, line: int = None, column: int = None):
        self.line = line
        self.column = column
        if line is not None and column is not None:
            message = f"{message} (위치: 줄 {line}, 열 {column})"
        super().__init__(message)
        
class GgaggalangRuntimeError(GgaggalangError):
    """Ggaggalang 코드 실행 중 발생한 오류"""
    pass
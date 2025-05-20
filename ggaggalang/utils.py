"""
Ggaggalang 유틸리티 함수 모듈
"""
from typing import List, Optional

def string_to_ggaggalang(text: str) -> str:
    """
    문자열을 Ggaggalang 코드로 변환
    
    Args:
        text: 변환할 문자열
        
    Returns:
        Ggaggalang 코드
    """
    result = []
    
    for char in text:
        ascii_val = ord(char)
        # 문자의 ASCII 값만큼 gga 반복
        code = "gga " * ascii_val + f"# {ascii_val} ({char})\ngguggaggugga\ngugu\n"
        result.append(code)
    
    return "\n".join(result)

def load_code_from_file(file_path: str) -> Optional[str]:
    """
    파일에서 Ggaggalang 코드 불러오기
    
    Args:
        file_path: 코드 파일 경로
        
    Returns:
        파일 내용 또는 오류 시 None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"오류: 파일을 찾을 수 없습니다: {file_path}")
        return None
    except Exception as e:
        print(f"파일 읽기 오류: {e}")
        return None
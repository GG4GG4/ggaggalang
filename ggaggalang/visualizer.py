"""
메모리 상태 시각화 모듈
"""
from typing import List, Optional

class MemoryVisualizer:
    """메모리 상태를 시각적으로 표현하는 클래스"""
    
    @staticmethod
    def visualize_memory(memory: List[int], pointer: int, 
                         start: Optional[int] = None, 
                         end: Optional[int] = None, 
                         highlight_pointer: bool = True) -> str:
        """
        메모리 상태를 시각적으로 표현하는 문자열 반환
        
        Args:
            memory: 메모리 배열
            pointer: 현재 포인터 위치
            start: 표시 시작 인덱스 (기본값: 포인터-10)
            end: 표시 종료 인덱스 (기본값: 시작+20)
            highlight_pointer: 포인터 위치 강조 여부
            
        Returns:
            시각화된 메모리 상태를 나타내는 문자열
        """
        if start is None:
            start = max(0, pointer - 10)
        if end is None:
            end = min(len(memory), start + 20)
            
        result = ["\nDEBUG: 메모리 상태:"]
        result.append("┌" + "─" * 77 + "┐")
        
        # 메모리 영역 헤더 - 인덱스 표시
        header = "│ "
        for i in range(start, end):
            cell_index = f"{i:4d}"  # 4자리로 맞춤
            header += f"{cell_index:<7s}"
        result.append(header + " │")
        
        # 구분선
        result.append("├" + "─" * 77 + "┤")
        
        # 메모리 값 표시
        values = "│ "
        for i in range(start, end):
            if highlight_pointer and i == pointer:
                # 현재 포인터 위치 강조
                cell_value = f"[{memory[i]:3d}]"
            else:
                cell_value = f" {memory[i]:3d} "
            values += f"{cell_value:<7s}"
        result.append(values + " │")
        
        # ASCII 값 표시
        ascii_values = "│ "
        for i in range(start, end):
            if memory[i] >= 32 and memory[i] <= 126:  # 출력 가능한 ASCII 범위
                char = chr(memory[i])
            else:
                char = "·"  # 출력 불가능한 문자는 점으로 표시
                
            if highlight_pointer and i == pointer:
                # 현재 포인터 위치 강조
                cell_char = f"[{char:1s}]  "
            else:
                cell_char = f" {char:1s}   "
            ascii_values += f"{cell_char:<7s}"
        result.append(ascii_values + " │")
        
        result.append("└" + "─" * 77 + "┘")
        
        return "\n".join(result)
        
    @staticmethod
    def print_memory_state(memory: List[int], pointer: int, 
                          start: Optional[int] = None, 
                          end: Optional[int] = None, 
                          highlight_pointer: bool = True) -> None:
        """
        메모리 상태를 시각적으로 출력
        
        Args:
            memory: 메모리 배열
            pointer: 현재 포인터 위치
            start: 표시 시작 인덱스 (기본값: 포인터-10)
            end: 표시 종료 인덱스 (기본값: 시작+20)
            highlight_pointer: 포인터 위치 강조 여부
        """
        print(MemoryVisualizer.visualize_memory(
            memory, pointer, start, end, highlight_pointer
        ))
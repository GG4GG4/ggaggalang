"""
Ggaggalang 코드 최적화 모듈
"""
from typing import List, Tuple, Dict, Set, Optional, Iterator

class GgaggalangOptimizer:
    """Ggaggalang 코드 최적화 클래스"""
    
    @staticmethod
    def count_consecutive_commands(commands: List[str], start_idx: int, cmd_type: str) -> int:
        """
        특정 위치에서 시작하는 동일한 명령어 연속 개수 계산
        
        Args:
            commands: 명령어 목록
            start_idx: 시작 인덱스
            cmd_type: 명령어 유형
            
        Returns:
            연속된 동일 명령어 개수
        """
        count = 0
        i = start_idx
        
        while i < len(commands) and commands[i] == cmd_type:
            count += 1
            i += 1
            
        return count
    
    @staticmethod
    def optimize_increments(commands: List[str]) -> List[str]:
        """
        증감(gga/kka) 명령어 최적화
        연속된 증감 명령어를 압축
        
        Args:
            commands: 원본 명령어 목록
            
        Returns:
            최적화된 명령어 목록
        """
        optimized = []
        i = 0
        
        while i < len(commands):
            cmd = commands[i]
            
            if cmd == 'gga' or cmd == 'kka':
                # 연속 증감 명령어 카운트
                count = GgaggalangOptimizer.count_consecutive_commands(commands, i, cmd)
                
                # 최적화: 연속 명령어를 한 번의 계산으로 압축
                if cmd == 'gga':
                    optimized.append(f"ADD {count % 256}")
                else:  # cmd == 'kka'
                    optimized.append(f"SUB {count % 256}")
                
                i += count
            else:
                optimized.append(cmd)
                i += 1
                
        return optimized
        
    @staticmethod
    def optimize_movements(commands: List[str]) -> List[str]:
        """
        이동(gugu/gugugga) 명령어 최적화
        연속된 이동 명령어를 압축
        
        Args:
            commands: 원본 명령어 목록
            
        Returns:
            최적화된 명령어 목록
        """
        optimized = []
        i = 0
        
        while i < len(commands):
            cmd = commands[i]
            
            if cmd == 'gugu' or cmd == 'gugugga':
                # 순방향/역방향 이동 계산
                right_count = 0
                j = i
                
                while j < len(commands):
                    if commands[j] == 'gugu':
                        right_count += 1
                    elif commands[j] == 'gugugga':
                        right_count -= 1
                    else:
                        break
                    j += 1
                
                # 최적화: 순방향/역방향 상쇄 후 최소 이동으로 압축
                if right_count > 0:
                    optimized.append(f"RIGHT {right_count}")
                elif right_count < 0:
                    optimized.append(f"LEFT {abs(right_count)}")
                
                i = j
            else:
                optimized.append(cmd)
                i += 1
                
        return optimized
                
    @staticmethod
    def optimize_clear_cells(commands: List[str]) -> List[str]:
        """
        셀 초기화 패턴 최적화
        [****] 패턴 감지 및 최적화
        
        Args:
            commands: 원본 명령어 목록
            
        Returns:
            최적화된 명령어 목록
        """
        optimized = []
        i = 0
        
        while i < len(commands):
            # 셀 초기화 패턴 감지: galanglang kka langlaggug
            if (i + 2 < len(commands) and
                commands[i] == 'galanglang' and
                commands[i+1] == 'kka' and
                commands[i+2] == 'langlaggug'):
                
                optimized.append("CLEAR")
                i += 3
            else:
                optimized.append(commands[i])
                i += 1
                
        return optimized
    
    @staticmethod
    def optimize(commands: List[str]) -> List[str]:
        """
        Ggaggalang 코드 최적화 (전체 과정)
        
        Args:
            commands: 원본 명령어 목록
            
        Returns:
            최적화된 명령어 목록
        """
        # 증감 명령어 최적화
        optimized = GgaggalangOptimizer.optimize_increments(commands)
        
        # 이동 명령어 최적화
        optimized = GgaggalangOptimizer.optimize_movements(optimized)
        
        # 셀 초기화 패턴 최적화
        optimized = GgaggalangOptimizer.optimize_clear_cells(optimized)
        
        return optimized
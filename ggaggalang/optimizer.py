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
                if count > 1:  # 2개 이상의 연속 명령어만 최적화
                    if cmd == 'gga':
                        optimized.append(f"ADD {count % 256}")
                    else:  # cmd == 'kka'
                        optimized.append(f"SUB {count % 256}")
                    
                    i += count
                else:
                    optimized.append(cmd)
                    i += 1
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
                if right_count > 1:
                    optimized.append(f"RIGHT {right_count}")
                    i = j
                elif right_count < -1:
                    optimized.append(f"LEFT {abs(right_count)}")
                    i = j
                elif right_count == 1:
                    optimized.append('gugu')
                    i = j
                elif right_count == -1:
                    optimized.append('gugugga')
                    i = j
                else:  # right_count == 0, 상쇄된 경우
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
            
            # 또 다른 초기화 패턴: galanglang gga langlaggug (셀 값을 0으로 설정 후 1씩 증가)
            elif (i + 2 < len(commands) and
                  commands[i] == 'galanglang' and
                  commands[i+1] == 'gga' and
                  commands[i+2] == 'langlaggug'):
                
                optimized.append("SET_1")  # 셀 값을 1로 설정
                i += 3
                
            else:
                optimized.append(commands[i])
                i += 1
                
        return optimized
    
    @staticmethod
    def optimize_copy_patterns(commands: List[str]) -> List[str]:
        """
        복사 패턴 최적화
        복사 패턴 (현재 셀 값을 0으로 만들고 다른 셀의 값을 복사) 감지 및 최적화
        
        Args:
            commands: 원본 명령어 목록
            
        Returns:
            최적화된 명령어 목록
        """
        optimized = []
        i = 0
        
        while i < len(commands):
            # 복사 패턴 검색 (여러 단계의 복사 패턴이 있을 수 있음)
            # 기본 패턴: 
            # 1. 셀을 0으로 초기화: [CLEAR 또는 비슷한 패턴]
            # 2. 다른 셀로 이동: [RIGHT 또는 LEFT]
            # 3. 루프로 값을 복사: [galanglang, kka, RIGHT/LEFT, gga, RIGHT/LEFT, langlaggug]
            
            # 간단한 복사 패턴 감지 예시 (실제로는 더 복잡한 패턴 검색이 필요)
            if (i + 7 < len(commands) and
                (commands[i] == "CLEAR" or commands[i].startswith("SET")) and
                (commands[i+1] == "RIGHT" or commands[i+1] == "LEFT" or 
                 commands[i+1] == "gugu" or commands[i+1] == "gugugga") and
                commands[i+2] == "galanglang" and
                commands[i+3] == "kka" and
                (commands[i+4] == "RIGHT" or commands[i+4] == "LEFT" or 
                 commands[i+4] == "gugu" or commands[i+4] == "gugugga") and
                commands[i+5] == "gga" and
                (commands[i+6] == "RIGHT" or commands[i+6] == "LEFT" or 
                 commands[i+6] == "gugu" or commands[i+6] == "gugugga") and
                commands[i+7] == "langlaggug"):
                
                # 복사 패턴을 단일 명령어로 대체
                # COPY_X_TO_Y: X 셀에서 Y 셀로 복사 (간소화를 위해 정확한 셀 계산은 생략)
                optimized.append("COPY_PATTERN")
                i += 8
            else:
                optimized.append(commands[i])
                i += 1
                
        return optimized
    
    @staticmethod
    def optimize_loop_invariants(commands: List[str]) -> List[str]:
        """
        루프 불변 코드 최적화
        루프 내부에서 변하지 않는 코드 패턴 추출
        
        Args:
            commands: 원본 명령어 목록
            
        Returns:
            최적화된 명령어 목록
        """
        # 루프 시작과 끝 위치 매핑 찾기
        loop_map = {}
        loop_stack = []
        
        for i, cmd in enumerate(commands):
            if cmd == 'galanglang':
                loop_stack.append(i)
            elif cmd == 'langlaggug':
                if loop_stack:
                    start = loop_stack.pop()
                    loop_map[start] = i
                    loop_map[i] = start
        
        # 루프 내부 최적화 적용
        optimized = commands.copy()
        
        # 루프별 분석 및 최적화 (간단한 예시)
        for start, end in sorted(loop_map.items()):
            if start < end:  # 시작점만 처리
                loop_body = commands[start+1:end]
                
                # 간단한 루프 패턴 최적화 예시
                if len(loop_body) == 1 and loop_body[0] == 'gga':
                    # [+] 패턴은 셀을 0으로 설정
                    optimized[start:end+1] = ["CLEAR"]
                    
                # 다른 루프 패턴도 필요에 따라 추가 가능
        
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
        
        # 복사 패턴 최적화
        optimized = GgaggalangOptimizer.optimize_copy_patterns(optimized)
        
        # 루프 불변 코드 최적화
        optimized = GgaggalangOptimizer.optimize_loop_invariants(optimized)
        
        return optimized
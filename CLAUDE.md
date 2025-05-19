# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

Ggaggalang은 Brainfuck 기반의 한국형 프로그래밍 언어입니다. 기본 Brainfuck 명령어를 한글 의성어로 대체했으며, 메모리 조작 기능을 제공합니다.

## 핵심 명령어

| 명령어 | Brainfuck | 설명 |
|--------|-----------|------|
| `gga` | + | 현재 포인터가 가리키는 메모리 셀의 값을 1 증가 |
| `kka` | - | 현재 포인터가 가리키는 메모리 셀의 값을 1 감소 |
| `gugu` | > | 메모리 포인터를 오른쪽으로 이동 |
| `gugugga` | < | 메모리 포인터를 왼쪽으로 이동 |
| `gguggaggugga` | . | 현재 메모리 셀의 값을 ASCII 문자로 출력 |

## 사용법

```python
# 코드 실행 방법
python main.py

# 디버그 모드로 실행 (interpreter.py에서 직접 사용할 경우)
from interpreter import GgaggalangInterpreter
interpreter = GgaggalangInterpreter(debug=True)
interpreter.execute(code)

# 일반 모드로 실행 (interpreter.py에서 직접 사용할 경우)
from interpreter import GgaggalangInterpreter
interpreter = GgaggalangInterpreter()
interpreter.execute(code)
```

## 프로젝트 구조

- `interpreter.py`: GgaggalangInterpreter 클래스가 정의된 핵심 파일
  - 명령어 파싱, 실행, 디버그 기능 포함
  - 메모리(30,000개 셀)와 포인터 관리
- `main.py`: 샘플 코드와 메인 실행 함수 포함
  - 디버그 모드와 일반 모드 실행 예제
  - Hello World 예제 코드
- `README.md`: 프로젝트 설명 및 예제 코드

## 코드 아키텍처

1. `GgaggalangInterpreter` 클래스
   - 메모리 관리: 30,000개의 8비트(0-255) 메모리 셀 배열
   - 포인터: 현재 작업 중인 메모리 셀 위치
   - 순환 메모리 구조 (마지막 셀 다음은 첫 번째 셀)
   - 디버그 모드: 실행 흐름 상세 출력

2. 명령어 처리 과정
   - `clean_code()`: 주석과 공백 제거, 유효한 명령어만 추출
   - `parse_command()`: 각 명령어 패턴 인식
   - `execute()`: 명령어 실행

3. 기본 메모리 조작 함수
   - `increment()`: 현재 셀 값 증가
   - `decrement()`: 현재 셀 값 감소  
   - `move_right()`: 포인터 오른쪽 이동
   - `move_left()`: 포인터 왼쪽 이동
   - `output_byte()`: 현재 셀 값을 ASCII 문자로 출력

## 개발 시 참고사항

1. 프로젝트는 표준 Python 라이브러리만 사용합니다.
2. 특별한 빌드 과정 없이 `python main.py`로 실행합니다.
3. 새로운 Ggaggalang 코드를 작성할 때는 README.md의 문법을 참고하세요.
4. Python 3.6 이상 버전에서 실행 가능합니다.
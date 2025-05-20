# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

Ggaggalang은 Brainfuck 기반의 한국형 프로그래밍 언어입니다. 기본 Brainfuck 명령어를 한글 의성어로 대체했으며, 확장 기능으로 함수형 프로그래밍과 조건문을 지원합니다.

## 개발 명령어

```bash
# 패키지 설치 (개발 모드)
pip install -e .

# 기본 실행
ggaggalang

# 파일 실행
ggaggalang -f examples/hello_world.gg

# 디버그 모드
ggaggalang -f examples/hello_world.gg -d

# 최적화 모드
ggaggalang -f examples/hello_world.gg -o

# 최적화된 코드 표시
ggaggalang -f examples/hello_world.gg -o -s

# 텍스트를 Ggaggalang 코드로 변환
ggaggalang -t "Hello World"

# 예제 코드 실행
ggaggalang -e hello
ggaggalang -e loop

# 확장 기능 비활성화 (기본 Brainfuck 호환 모드)
ggaggalang --no-extensions

# 테스트 실행
python -m pytest test_interpreter.py -v

# 특정 테스트 실행
python -m pytest test_interpreter.py::TestGgaggalangInterpreter::test_basic_commands -v

# 벤치마크 실행
python examples/benchmark.py
python examples/benchmark.py --optimize
python examples/benchmark.py --test move -n 10000
```

## 언어 명령어

### 기본 명령어
| 명령어 | Brainfuck | 설명 |
|--------|-----------|------|
| `gga` | + | 현재 포인터가 가리키는 메모리 셀의 값을 1 증가 |
| `kka` | - | 현재 포인터가 가리키는 메모리 셀의 값을 1 감소 |
| `gugu` | > | 메모리 포인터를 오른쪽으로 이동 |
| `gugugga` | < | 메모리 포인터를 왼쪽으로 이동 |
| `gguggaggugga` | . | 현재 메모리 셀의 값을 ASCII 문자로 출력 |
| `ggalgga` | , | 사용자 입력을 받아 현재 메모리 셀에 저장 |
| `galanglang` | [ | 현재 메모리 셀의 값이 0이면 대응하는 `langlaggug`로 이동 |
| `langlaggug` | ] | 현재 메모리 셀의 값이 0이 아니면 대응하는 `galanglang`으로 이동 |

### 확장 명령어
| 명령어 | 설명 |
|--------|------|
| `gangga` | 함수 정의 시작 (현재 셀 값을 함수 이름으로 사용) |
| `ggaggang` | 함수 정의 끝 |
| `gukku` | 함수 호출 (현재 셀 값의 함수 호출) |
| `kkuggu` | 함수에서 반환 |
| `gagugug` | if 시작 (현재 셀이 0이 아니면 실행) |
| `gugalang` | else 시작 |
| `galanggu` | if-else 종료 |
| `gaggug` | 현재 셀과 다음 셀 값 곱하기 |
| `guggug` | 현재 셀 값을 다음 셀 값으로 나누기 |
| `kkakka` | 현재 셀 값을 다음 셀 값으로 나눈 나머지 |
| `galang` | 현재 셀 값을 다음 셀에 복사 |
| `ganggang` | 포인터를 현재 셀 값 위치로 이동 |
| `gagagal` | 현재 셀 값을 다음 셀 값으로 설정 |

## 패키지 구조

```
ggaggalang/
├── __init__.py         # 패키지 초기화 파일
├── cli.py              # 명령줄 인터페이스
├── errors.py           # 예외 클래스
├── extensions.py       # 언어 확장 기능
├── interpreter.py      # 인터프리터 핵심 기능
├── optimizer.py        # 코드 최적화 기능
├── parser.py           # 코드 파서
├── utils.py            # 유틸리티 함수
├── visualizer.py       # 메모리 시각화
└── bin/                # 실행 스크립트
    └── ggaggalang      # 명령줄 실행 파일
```

## 코드 아키텍처

1. **인터프리터 (interpreter.py)**
   - 핵심 클래스: `GgaggalangInterpreter`
   - 메모리 관리: array 타입의 30,000개 메모리 셀 (8비트)
   - 명령어 실행 및 디버그 기능
   - command_handlers 딕셔너리를 통한 명령어 분배 처리
   - 최적화된 코드 실행 및 성능 향상 기능

2. **파서 (parser.py)**
   - 핵심 클래스: `GgaggalangParser`
   - 코드 파싱 및 문법 검증
   - 주석 및 공백 제거
   - 명령어 추출 및 검증
   - 괄호 짝 매칭 검사

3. **확장 기능 (extensions.py)**
   - 핵심 클래스: `GgaggalangExtensions`
   - 확장 명령어 정의: `EXTENDED_COMMANDS` 딕셔너리
   - 함수 테이블 및 호출 스택 관리
   - 함수 정의 및 호출 기능
   - 조건부 분기문 처리
   - 확장 수학 연산 기능

4. **최적화 (optimizer.py)**
   - 핵심 클래스: `GgaggalangOptimizer`
   - 연속된 증감 명령어 압축 (`optimize_increments`)
   - 이동 명령어 최적화 (`optimize_movements`)
   - 셀 초기화 패턴 감지 (`optimize_clear_cells`)
   - 복사 패턴 최적화 (`optimize_copy_patterns`)
   - 루프 불변 코드 최적화 (`optimize_loop_invariants`)

5. **CLI (cli.py)**
   - 명령줄 인터페이스 및 인자 파싱
   - 실행 모드 관리: 디버그, 최적화, 확장 기능 제어
   - 예제 코드 제공 및 파일 실행
   - 텍스트-코드 변환 기능

6. **시각화 (visualizer.py)**
   - 클래스: `MemoryVisualizer`
   - 메모리 상태 테이블 형태 시각화
   - ASCII 값 표시 기능
   - 포인터 위치 강조 표시

## API 사용법

```python
# 기본 모드로 실행
from ggaggalang import GgaggalangInterpreter
interpreter = GgaggalangInterpreter()
interpreter.execute(code)

# 디버그 모드로 실행
interpreter = GgaggalangInterpreter(debug=True)
interpreter.execute(code)

# 확장 기능 비활성화
interpreter = GgaggalangInterpreter(extensions=False)
interpreter.execute(code)

# 최적화를 통한 실행
from ggaggalang.optimizer import GgaggalangOptimizer
parsed_commands = interpreter.parser.clean_code(code)
optimized_commands = GgaggalangOptimizer.optimize(parsed_commands)
optimized_code = " ".join(optimized_commands)
interpreter.execute(optimized_code, precompiled=True)

# 텍스트를 Ggaggalang 코드로 변환
from ggaggalang.utils import string_to_ggaggalang
code = string_to_ggaggalang("Hello World")
```

## 고급 예제 코드

프로젝트에는 다음과 같은 예제 코드가 포함되어 있습니다:

1. `examples/hello_world.gg` - 기본 "Hello World" 출력
2. `examples/function_example.gg` - 함수 정의와 호출 예제
3. `examples/if_condition.gg` - 조건문 분기 처리 예제
4. `examples/math_operations.gg` - 수학 연산 명령어 활용 예제
5. `examples/fibonacci.gg` - 피보나치 수열 계산 알고리즘
6. `examples/bubble_sort.gg` - 버블 정렬 알고리즘

## 개발 시 참고사항

1. 테스트 실행 시 확장 기능을 비활성화해야 기존 테스트가 정상 작동합니다.
2. 최적화 모드를 사용하면 실행 속도가 크게 향상됩니다.
3. 예외 처리는 `errors.py`에 정의된 예외 클래스를 사용합니다.
4. 새로운 기능을 추가할 때는 `extensions.py`의 `EXTENDED_COMMANDS` 딕셔너리에 명령어를 추가해야 합니다.
5. 코드 변경 후에는 `python -m pytest test_interpreter.py -v` 명령으로 테스트를 실행해 기능 검증을 해야 합니다.
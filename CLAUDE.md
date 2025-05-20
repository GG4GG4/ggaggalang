# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

Ggaggalang은 Brainfuck 기반의 한국형 프로그래밍 언어입니다. 기본 Brainfuck 명령어를 한글 의성어로 대체했으며, 확장 기능으로 함수형 프로그래밍과 조건문을 지원합니다.

## 개발 명령어

```bash
# 기본 실행
python main.py

# 파일 실행
python main.py -f examples/hello_world.ggal

# 디버그 모드
python main.py -f examples/hello_world.ggal -d

# 최적화 모드
python main.py -f examples/hello_world.ggal -o

# 최적화된 코드 표시
python main.py -f examples/hello_world.ggal -o -s

# 텍스트를 Ggaggalang 코드로 변환
python main.py -t "Hello World"

# 예제 코드 실행
python main.py -e hello
python main.py -e loop

# 확장 기능 비활성화 (기본 Brainfuck 호환 모드)
python main.py --no-extensions

# 테스트 실행
python -m unittest test_interpreter.py

# 벤치마크 실행
python examples/benchmark.py
python examples/benchmark.py --optimize
python examples/benchmark.py --test move -n 10000
```

## 핵심 명령어

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
| `gangga` | 함수 정의 시작 |
| `ggaggang` | 함수 정의 끝 |
| `gukku` | 함수 호출 |
| `kkuggu` | 함수에서 반환 |
| `gagugug` | if 시작 (현재 셀이 0이 아니면 실행) |
| `gugalang` | else 시작 |
| `galanggu` | if-else 종료 |
| `gaggug` | 현재 셀과 다음 셀 값 곱하기 |
| `guggug` | 현재 셀 값을 다음 셀 값으로 나누기 |
| `kkakka` | 현재 셀 값을 다음 셀 값으로 나눈 나머지 |
| `galang` | 현재 셀 값을 다음 셀에 복사 |
| `ganggang` | 포인터를 현재 셀 값 위치로 이동 |
| `gagagal` | 현재 셀 값을 직접 설정 |

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
└── visualizer.py       # 메모리 시각화
```

## 코드 아키텍처

1. **인터프리터 (interpreter.py)**
   - 핵심 클래스: `GgaggalangInterpreter`
   - 메모리 관리: array 타입의 30,000개 메모리 셀 (8비트)
   - 명령어 실행 및 디버그 기능
   - 최적화된 코드 실행 및 성능 향상 기능

2. **파서 (parser.py)**
   - 핵심 클래스: `GgaggalangParser`
   - 코드 파싱 및 문법 검증
   - 주석 및 공백 제거
   - 명령어 추출 및 검증

3. **확장 기능 (extensions.py)**
   - 핵심 클래스: `GgaggalangExtensions`
   - 함수 정의 및 호출 기능
   - 조건부 분기문
   - 확장 수학 연산

4. **최적화 (optimizer.py)**
   - 핵심 클래스: `GgaggalangOptimizer`
   - 연속된 명령어 압축
   - 루프 최적화
   - 성능 향상 기능

5. **CLI (cli.py)**
   - 명령줄 인터페이스
   - 다양한 옵션 처리
   - 예제 코드 및 파일 실행

6. **시각화 (visualizer.py)**
   - 메모리 상태 시각화
   - 디버깅 도구

## API 사용법

```python
# 기본 모드로 실행
from ggaggalang.interpreter import GgaggalangInterpreter
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

## 개발 시 참고사항

1. 테스트 실행 시 확장 기능을 비활성화해야 테스트가 정상 작동합니다.
2. 최적화 모드를 사용하면 실행 속도가 크게 향상됩니다.
3. 예외 처리는 `errors.py`에 정의된 예외 클래스를 사용합니다.
4. 새로운 기능을 추가할 때는 `extensions.py`를 참고하세요.
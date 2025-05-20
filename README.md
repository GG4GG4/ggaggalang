# Ggaggalang

Brainfuck 기반의 한국형 프로그래밍 언어입니다.

## 기본 문법

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

## 확장 명령어

Ggaggalang은 기본 Brainfuck 명령어 외에 확장 기능을 제공합니다.

### 함수 관련 명령어

| 명령어 | 설명 |
|--------|------|
| `gangga` | 함수 정의 시작 (현재 셀 값을 함수 이름으로 사용) |
| `ggaggang` | 함수 정의 끝 |
| `gukku` | 함수 호출 (현재 셀 값의 함수 호출) |
| `kkuggu` | 함수에서 반환 |

### 조건부 분기 명령어

| 명령어 | 설명 |
|--------|------|
| `gagugug` | if 시작 (현재 셀이 0이 아니면 실행) |
| `gugalang` | else 시작 |
| `galanggu` | if-else 종료 |

### 수학 연산 명령어

| 명령어 | 설명 |
|--------|------|
| `gaggug` | 현재 셀과 다음 셀 값 곱하기 |
| `guggug` | 현재 셀 값을 다음 셀 값으로 나누기 |
| `kkakka` | 현재 셀 값을 다음 셀 값으로 나눈 나머지 |

### 메모리 조작 명령어

| 명령어 | 설명 |
|--------|------|
| `galang` | 현재 셀 값을 다음 셀에 복사 |
| `ganggang` | 포인터를 현재 셀 값 위치로 이동 |
| `gagagal` | 현재 셀 값을 다음 셀 값으로 설정 |

## 설치 및 사용법

### 설치

```bash
# 패키지 설치
pip install ggaggalang
```

또는 저장소를 직접 클론하여 사용할 수 있습니다:

```bash
git clone https://github.com/GG4GG4/ggaggalang.git
cd ggaggalang
pip install -e .
```

### 라이브러리 사용법

```python
from ggaggalang import GgaggalangInterpreter

# 기본 모드로 실행
interpreter = GgaggalangInterpreter()
interpreter.execute(code)

# 디버그 모드로 실행
interpreter = GgaggalangInterpreter(debug=True)
interpreter.execute(code)

# 확장 기능 비활성화 모드 (기본 Brainfuck 호환)
interpreter = GgaggalangInterpreter(extensions=False)
interpreter.execute(code)
```

### 명령줄 사용법

```bash
# 기본 실행 (Hello World 예제)
ggaggalang

# 파일 실행
ggaggalang -f examples/hello_world.gg

# 디버그 모드로 실행
ggaggalang -f examples/hello_world.gg -d

# 예제 실행
ggaggalang -e hello
ggaggalang -e loop

# 코드 최적화 활성화
ggaggalang -f examples/hello_world.gg -o

# 최적화된 코드 표시
ggaggalang -f examples/hello_world.gg -o -s

# 확장 기능 비활성화 (기본 Brainfuck 호환 모드)
ggaggalang -f examples/hello_world.gg --no-extensions

# 텍스트를 Ggaggalang 코드로 변환
ggaggalang -t "Hello, World!"
```

## 디버그 모드

디버그 모드를 활성화하면 다음과 같은 정보가 출력됩니다:
- 파싱된 명령어 목록
- 메모리 셀의 값 변화
- 포인터 이동
- 출력 문자의 ASCII 값
- 메모리 상태 시각화

## 예제

### Hello World!

```python
# H (72)
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga # 72
gguggaggugga

gugu # 다음 셀로 이동

# e (101)
gga gga gga gga gga gga gga gga gga gga # 10
# ... 이하 생략 ...
```

더 많은 예제는 `examples` 폴더를 참조하세요:
- `function_example.gg` - 함수 정의와 호출 예제
- `if_condition.gg` - 조건문 사용 예제
- `math_operations.gg` - 수학 연산 예제

## 특징

- 30,000개의 메모리 셀
- 각 셀은 0-255 범위의 값 저장 (8비트)
- 순환 메모리 구조 (마지막 셀 다음은 첫 번째 셀)
- 공백과 주석 무시
- 디버그 모드 지원
- 코드 최적화 기능
- 함수 정의 및 호출
- 조건부 분기(if-else)
- 고급 수학 연산 (곱셈, 나눗셈, 모듈로)
- 메모리 조작 확장 기능

## 프로젝트 구조

```
ggaggalang/
├── __init__.py - 패키지 초기화
├── interpreter.py - 메인 인터프리터
├── parser.py - 코드 파싱
├── errors.py - 예외 클래스
├── extensions.py - 확장 기능
├── optimizer.py - 코드 최적화
├── visualizer.py - 메모리 시각화
├── utils.py - 유틸리티 함수
├── cli.py - 명령줄 인터페이스
└── bin/ - 실행 스크립트
```

## 라이선스

MIT License
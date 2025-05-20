# Ggaggalang 사용 가이드

Ggaggalang(까딱까딱)은 Brainfuck 기반의 한국형 프로그래밍 언어입니다. 이 가이드는 언어의 사용법과 예제를 제공합니다.

## 목차
1. [소개 및 설치](#소개-및-설치)
2. [명령어 문법](#명령어-문법)
3. [사용 방법](#사용-방법)
4. [예제 코드](#예제-코드)
5. [디버깅](#디버깅)
6. [고급 사용법](#고급-사용법)
7. [문제 해결](#문제-해결)

## 소개 및 설치

Ggaggalang은 Brainfuck의 8개 명령어를 한글 의성어로 대체한 프로그래밍 언어입니다. 단순한 문법으로 메모리 조작을 통해 프로그래밍을 할 수 있습니다.

### 설치

```bash
git clone https://github.com/GG4GG4/ggaggalang.git
cd ggaggalang
```

## 명령어 문법

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

## 사용 방법

### 기본 실행

인터프리터를 사용하여 Ggaggalang 코드를 실행할 수 있습니다:

```bash
# 기본 예제 실행
python main.py

# 파일에서 코드 실행
python main.py -f examples/hello_world.ggal

# 디버그 모드 활성화
python main.py -f examples/hello_world.ggal -d

# 최적화 모드로 실행 (성능 향상)
python main.py -f examples/hello_world.ggal -o

# 최적화된 명령어 확인
python main.py -f examples/hello_world.ggal -o -s
```

### 명령줄 인터페이스 (CLI)

Ggaggalang은 다양한 명령줄 옵션을 제공합니다:

```bash
python main.py -h  # 도움말 표시

# 옵션:
# -f, --file FILE     실행할 Ggaggalang 코드 파일
# -d, --debug         디버그 모드 활성화
# -t, --text TEXT     Ggaggalang 코드로 변환할 텍스트
# -e, --example {hello,loop}  실행할 예제 코드
# -o, --optimize      코드 최적화 활성화 (성능 향상)
# -s, --show-optimized 최적화된 코드 표시
```

### 파이썬 API 사용

파이썬 코드에서 직접 인터프리터를 사용할 수 있습니다:

```python
from interpreter import GgaggalangInterpreter

# 기본 모드로 실행
interpreter = GgaggalangInterpreter()
interpreter.execute(code)

# 디버그 모드로 실행
interpreter = GgaggalangInterpreter(debug=True)
interpreter.execute(code)
```

## 예제 코드

### Hello World

```
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
...
```

전체 코드는 `examples/hello_world.ggal` 파일을 참조하세요.

### 카운터 (0-9)

```
# 셀 0에 10을 저장 (카운트다운 값)
gga gga gga gga gga gga gga gga gga gga # 10

# 셀 1로 이동하여 48 저장 (ASCII '0')
gugu
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga # 48

# 셀 0으로 돌아가기
gugugga

# 루프 시작 - 셀 0이 0이 될 때까지 반복
galanglang
  # 셀 1로 이동 (현재 ASCII 숫자)
  gugu
  # 현재 숫자 출력
  gguggaggugga
  # 셀 1 값 증가 (다음 ASCII 숫자)
  gga
  # 셀 0으로 돌아가기
  gugugga
  # 카운터 감소
  kka
langlaggug
```

### 입력 에코

사용자 입력을 그대로 출력하는 예제:

```
# 입력 받기
ggalgga
# 출력하기
gguggaggugga
```

더 많은 예제는 `examples/` 디렉토리에서 확인할 수 있습니다.

## 디버깅

디버그 모드를 활성화하면 코드 실행 과정과 메모리 상태를 상세히 확인할 수 있습니다:

```bash
python main.py -f examples/counter.ggal -d
```

디버그 모드에서 제공되는 정보:
- 파싱된 명령어 목록
- 메모리 셀의 값 변화
- 포인터 이동
- 출력 문자의 ASCII 값
- 메모리 상태 시각화

## 고급 사용법

### 텍스트를 Ggaggalang 코드로 변환

```bash
python main.py -t "Hello"
```

이 명령은 "Hello" 문자열을 출력하는 Ggaggalang 코드를 생성합니다.

### 코드 최적화

대용량 코드나 성능이 중요한 경우 코드 최적화 기능을 사용하세요:

```bash
# 최적화 모드로 실행
python main.py -f examples/hello_world.ggal -o

# 최적화된 명령어 확인
python main.py -f examples/hello_world.ggal -o -s
```

최적화는 다음과 같은 작업을 수행합니다:
- 연속된 증감 명령어(gga/kka) 압축
- 연속된 이동 명령어(gugu/gugugga) 압축
- 셀 초기화 패턴 감지 및 최적화
- 루프 접근 최적화

### 성능 벤치마크

```bash
# 기본 벤치마크 실행
python examples/benchmark.py

# 최적화 적용 벤치마크
python examples/benchmark.py --optimize

# 다양한 옵션 적용
python examples/benchmark.py --test move -n 10000
```

### 자체 프로그램 작성 팁

1. 루프를 사용할 때 괄호(`galanglang`, `langlaggug`)가 올바르게 짝을 이루는지 확인하세요.
2. 메모리 셀은 0에서 255 사이의 값만 저장할 수 있습니다 (8비트).
3. 포인터가 메모리 범위를 벗어나면 자동으로 반대쪽 끝으로 순환합니다.
4. 주석과 공백은 자유롭게 사용할 수 있습니다.

## 문제 해결

### 일반적인 오류

1. **문법 오류**: 괄호(`galanglang`, `langlaggug`)가 짝을 이루지 않는 경우
2. **실행 오류**: 메모리 범위를 벗어나거나 잘못된 ASCII 값이 출력될 때
3. **무한 루프**: 루프 종료 조건이 적절하지 않을 때

### 해결책

1. 디버그 모드(`-d` 옵션)를 활성화하여 실행 과정을 확인합니다.
2. 괄호 짝이 맞는지 확인합니다.
3. 메모리 포인터 위치와 값이 예상대로인지 확인합니다.

오류 메시지를 주의 깊게 확인하면 문제를 쉽게 찾을 수 있습니다.

---

## 더 알아보기

- [README.md](README.md): 프로젝트 개요 및 기본 정보
- [examples/](examples/): 다양한 예제 코드
- [test_interpreter.py](test_interpreter.py): 인터프리터 테스트 코드

문제나 제안 사항이 있으면 GitHub 이슈로 등록해 주세요.
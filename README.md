# Ggaggalang

Brainfuck 기반의 한국형 프로그래밍 언어입니다.

## 문법

| 명령어 | Brainfuck | 설명 |
|--------|-----------|------|
| `gga` | + | 현재 포인터가 가리키는 메모리 셀의 값을 1 증가 |
| `kka` | - | 현재 포인터가 가리키는 메모리 셀의 값을 1 감소 |
| `gugu` | > | 메모리 포인터를 오른쪽으로 이동 |
| `gugugga` | < | 메모리 포인터를 왼쪽으로 이동 |
| `gguggaggugga` | . | 현재 메모리 셀의 값을 ASCII 문자로 출력 |

## 사용법

```python
from interpreter import GgaggalangInterpreter

# 기본 모드로 실행
interpreter = GgaggalangInterpreter()
interpreter.execute(code)

# 디버그 모드로 실행
interpreter = GgaggalangInterpreter(debug=True)
interpreter.execute(code)
```

### 디버그 모드

디버그 모드를 활성화하면 다음과 같은 정보가 출력됩니다:
- 파싱된 명령어 목록
- 메모리 셀의 값 변화
- 포인터 이동
- 출력 문자의 ASCII 값

## 예제

### Hello World!

```python
# H (ASCII 72)
gga gga gga gga gga gga gga gga gga gga # 10
gga gga gga gga gga gga gga gga gga gga # 20
gga gga gga gga gga gga gga gga gga gga # 30
gga gga gga gga gga gga gga gga gga gga # 40
gga gga gga gga gga gga gga gga gga gga # 50
gga gga gga gga gga gga gga gga gga gga # 60
gga gga gga gga gga gga gga gga gga gga # 70
gga gga # 72
gguggaggugga
```

더 많은 예제는 `main.py`를 참조하세요.

## 특징

- 30,000개의 메모리 셀
- 각 셀은 0-255 범위의 값 저장 (8비트)
- 순환 메모리 구조 (마지막 셀 다음은 첫 번째 셀)
- 공백과 주석 무시
- 디버그 모드 지원

## 라이선스

MIT License

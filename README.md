# Gemini 기반 오늘의 기술 추천 자동화

이 저장소는 GitHub Actions와 Google Gemini API를 활용하여 매일 아침 .NET, AI, C++ 분야의 최신 기술 추천 포스트를 자동으로 생성합니다.

## 자동화 개요
- 매일 오전 6시(GMT+9)에 워크플로우가 실행됩니다.
- Gemini API로부터 각 분야별 추천, 참고 사이트, 코드, 실행 결과를 받아 `_posts/dotnet/`, `_posts/ai/`, `_posts/c++/`에 Jekyll 포스트 양식으로 저장합니다.

---

## 커스터마이징 방법

### 1. 추천 주제 추가/변경
- `.github/scripts/gemini_tech_today.py`의 `PROMPTS`와 `POST_DIRS` 딕셔너리에 원하는 주제를 추가하거나 수정하세요.
- 프롬프트를 원하는 언어나 주제로 바꿀 수 있습니다.

### 2. 마크다운 템플릿 변경
- 같은 파일의 `make_post` 함수를 수정하여 포스트의 YAML 헤더나 본문 구조를 자유롭게 바꿀 수 있습니다.

### 3. 워크플로우 실행 시간 변경
- `.github/workflows/gemini-tech-today.yml`의 `cron` 값을 수정하세요.
  - 예: 매일 오전 7시로 변경하려면 `0 22 * * *` (UTC 기준)

### 4. Gemini API 프롬프트 커스터마이징
- 각 주제별 프롬프트를 더 구체적으로 작성하거나, 원하는 정보(예: 더 많은 코드, 실무 예시 등)를 요청할 수 있습니다.

---

## 테스트 방법

### 1. 로컬 테스트
1. Python 3.10+ 및 `requests` 패키지 설치:
   ```bash
   pip install requests
   ```
2. [Google Gemini API 키](https://ai.google.dev/)를 발급받아 환경 변수로 등록:
   ```bash
   export GEMINI_API_KEY=발급받은_키
   ```
3. 스크립트 직접 실행:
   ```bash
   python .github/scripts/gemini_tech_today.py
   ```
4. `_posts/dotnet/`, `_posts/ai/`, `_posts/c++/`에 마크다운 파일이 생성되는지 확인하세요.

### 2. GitHub Actions 테스트
- 워크플로우 파일을 수정 후 커밋/푸시하면, Actions 탭에서 수동으로 실행(Dispatch)하거나, 다음 예약 실행을 기다릴 수 있습니다.

---

## 수동 실행 방법

### 1. 로컬에서 수동 실행
위의 "로컬 테스트" 방법과 동일하게 실행하면 됩니다.

### 2. GitHub Actions에서 수동 실행
1. GitHub 저장소의 **Actions** 탭으로 이동
2. **Gemini Tech Today** 워크플로우 선택
3. **Run workflow** 버튼 클릭하여 즉시 실행

---

## 환경 변수 및 시크릿 설정
- 반드시 저장소의 `Settings > Secrets and variables > Actions`에서 `GEMINI_API_KEY`를 등록해야 합니다.

---

## 참고
- Gemini API 사용량에 따라 요금이 발생할 수 있습니다.
- 생성된 포스트는 Jekyll 규칙에 따라 자동으로 블로그에 반영됩니다.

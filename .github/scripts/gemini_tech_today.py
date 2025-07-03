import os
import requests
import time
import re
import glob
from datetime import datetime

# 환경 변수에서 Gemini API 키를 읽음
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise RuntimeError('GEMINI_API_KEY 환경 변수가 설정되어 있지 않습니다.')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=' + GEMINI_API_KEY

# 각 주제별 프롬프트 (기존 기술 제외)
def get_prompt_with_exclusions(topic, excluded_techs):
    base_prompts = {
        'dotnet': f'''오늘의 .NET 최신 기술 트렌드 중 하나를 추천해 주세요. 
다음 기술들은 이미 다뤘으므로 제외해주세요: {', '.join(excluded_techs) if excluded_techs else '없음'}

응답 형식:
## 오늘의 {topic.upper()} 최신 기술 트렌드: **[구체적인 기술명]**

**1. 간단한 설명:**
[기술에 대한 설명]

**2. 참고할 만한 공식 사이트나 블로그 링크:**
[링크들]

**3. 간단한 코드 예시 (C#):**
[코드 예시]

**4. 코드 실행 결과 예시:**
[결과 예시]''',
        
        'ai': f'''오늘의 AI 최신 기술 트렌드 중 하나를 추천해 주세요.
다음 기술들은 이미 다뤘으므로 제외해주세요: {', '.join(excluded_techs) if excluded_techs else '없음'}

응답 형식:
## 오늘의 {topic.upper()} 최신 기술 트렌드: **[구체적인 기술명]**

**1. 간단한 설명:**
[기술에 대한 설명]

**2. 참고할 만한 공식 사이트나 블로그 링크:**
[링크들]

**3. 간단한 코드 예시 (Python):**
[코드 예시]

**4. 코드 실행 결과 예시:**
[결과 예시]''',
        
        'c++': f'''오늘의 C++ 최신 기술 트렌드 중 하나를 추천해 주세요.
다음 기술들은 이미 다뤘으므로 제외해주세요: {', '.join(excluded_techs) if excluded_techs else '없음'}

응답 형식:
## 오늘의 {topic.upper()} 최신 기술 트렌드: **[구체적인 기술명]**

**1. 간단한 설명:**
[기술에 대한 설명]

**2. 참고할 만한 공식 사이트나 블로그 링크:**
[링크들]

**3. 간단한 코드 예시 (C++):**
[코드 예시]

**4. 코드 실행 결과 예시:**
[결과 예시]'''
    }
    return base_prompts[topic]

# 각 주제별 저장 경로
POST_DIRS = {
    'dotnet': '_posts/dotnet',
    'ai': '_posts/ai',
    'c++': '_posts/c++'
}

# 이전 포스트들에서 다뤘던 기술들을 추출하는 함수
def get_previous_technologies(topic, days_back=30):
    """최근 days_back 일 동안 다뤘던 기술들을 추출"""
    post_dir = POST_DIRS[topic]
    if not os.path.exists(post_dir):
        return []
    
    technologies = []
    # 최근 포스트들 검색
    post_files = glob.glob(os.path.join(post_dir, "*.md"))
    
    for post_file in post_files:
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # 1. Jekyll frontmatter에서 title 추출 (우선순위 높음)
                title_match = re.search(r'^title: "(.+?)"', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip()
                    # "DOTNET - C# 12 Primary Constructors" 형태에서 기술명 추출
                    tech_match = re.search(r'^[A-Z\+]+\s*-\s*(.+)', title)
                    if tech_match:
                        tech_name = tech_match.group(1).strip()
                        technologies.append(tech_name)
                        continue
                
                # 2. 본문에서 "## 오늘의 [TOPIC] 최신 기술 트렌드: **[기술명]**" 패턴 추출 (fallback)
                match = re.search(r'## 오늘의 .+ 최신 기술 트렌드: \*\*(.+?)\*\*', content)
                if match:
                    tech_name = match.group(1).strip()
                    technologies.append(tech_name)
                    
        except Exception as e:
            print(f"파일 읽기 오류 {post_file}: {e}")
            continue
    
    return technologies

# 제목을 추출하는 함수
def extract_title_from_content(content):
    """Gemini 응답에서 기술명을 추출하여 제목 생성"""
    # "## 오늘의 [TOPIC] 최신 기술 트렌드: **[기술명]**" 패턴에서 기술명 추출
    match = re.search(r'## 오늘의 .+ 최신 기술 트렌드: \*\*(.+?)\*\*', content)
    if match:
        tech_name = match.group(1).strip()
        return tech_name
    
    # 패턴이 없으면 기본 제목 반환
    return "오늘의 최신 기술 추천"

# 더 나은 제목 생성 함수
def create_better_title(topic, tech_name):
    """주제와 기술명을 조합하여 더 나은 제목 생성"""
    topic_display = topic.upper()
    return f"{topic_display} - {tech_name}"
def make_post(title, date, category, content):
    return f'''---
title: "{title}"
date: {date} +0900
categories: {category}
tags: [{category}, 최신기술, 추천]
---
\n{content}\n'''

def fetch_gemini_content(prompt):
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except requests.exceptions.RequestException as e:
        # 503 등 오류 발생 시 1분 대기 후 1회만 재시도
        print(f"[fetch_gemini_content] 첫 호출 실패: {e}. 60초 대기 후 재시도...")
        time.sleep(60)
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['candidates'][0]['content']['parts'][0]['text']

def main():
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filenametoday = datetime.now().strftime('%Y-%m-%d')
    
    # 주제별로 처리
    topics = ['dotnet', 'ai', 'c++']
    
    for topic in topics:
        print(f"[{topic}] 처리 시작...")
        
        # 이전에 다뤘던 기술들 확인
        previous_techs = get_previous_technologies(topic)
        print(f"[{topic}] 이전에 다뤘던 기술들: {previous_techs}")
        
        # 프롬프트 생성
        prompt = get_prompt_with_exclusions(topic, previous_techs)
        
        # Gemini API 호출
        try:
            content = fetch_gemini_content(prompt)
        except Exception as e:
            print(f"[{topic}] Gemini API 호출 실패: {e}")
            continue
        
        # 제목 추출 및 생성
        extracted_tech = extract_title_from_content(content)
        post_title = create_better_title(topic, extracted_tech)
        
        # 중복 체크 (방금 추출한 기술이 이미 다뤄진 것인지 확인)
        if extracted_tech in previous_techs:
            print(f"[{topic}] 경고: '{extracted_tech}' 기술이 이미 다뤄진 것 같습니다. 그래도 진행합니다.")
        
        # 파일명 및 경로
        filename = f"{filenametoday}-{topic}-today.md"
        post_path = os.path.join(POST_DIRS[topic], filename)
        
        # 포스트 생성
        post_md = make_post(post_title, today, topic, content)
        
        # 폴더 없으면 생성
        os.makedirs(POST_DIRS[topic], exist_ok=True)
        
        # 파일 저장
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(post_md)
        print(f"[{topic}] 포스트 생성 완료: {post_path}")
        print(f"[{topic}] 제목: {post_title}")
        print(f"[{topic}] 추출된 기술: {extracted_tech}")

if __name__ == '__main__':
    main()
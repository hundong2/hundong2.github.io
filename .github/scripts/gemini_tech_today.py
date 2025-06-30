import os
import requests
from datetime import datetime

# 환경 변수에서 Gemini API 키를 읽음
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise RuntimeError('GEMINI_API_KEY 환경 변수가 설정되어 있지 않습니다.')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=' + GEMINI_API_KEY

# 각 주제별 프롬프트
PROMPTS = {
    'dotnet': '''오늘의 .NET 최신 기술 트렌드 중 하나를 추천해 주세요.\n- 추천 기술의 간단한 설명\n- 참고할 만한 공식 사이트나 블로그 링크\n- 간단한 코드 예시 (C#)\n- 코드 실행 결과 예시\n를 포함해 주세요.''',
    'ai': '''오늘의 AI 최신 기술 트렌드 중 하나를 추천해 주세요.\n- 추천 기술의 간단한 설명\n- 참고할 만한 공식 사이트나 블로그 링크\n- 간단한 코드 예시 (Python)\n- 코드 실행 결과 예시\n를 포함해 주세요.''',
    'c++': '''오늘의 C++ 최신 기술 트렌드 중 하나를 추천해 주세요.\n- 추천 기술의 간단한 설명\n- 참고할 만한 공식 사이트나 블로그 링크\n- 간단한 코드 예시 (C++)\n- 코드 실행 결과 예시\n를 포함해 주세요.'''
}

# 각 주제별 저장 경로
POST_DIRS = {
    'dotnet': '_posts/dotnet',
    'ai': '_posts/ai',
    'c++': '_posts/c++'
}

# Jekyll 포스트 템플릿
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
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['candidates'][0]['content']['parts'][0]['text']

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    for topic in PROMPTS:
        # Gemini API 호출
        try:
            content = fetch_gemini_content(PROMPTS[topic])
        except Exception as e:
            print(f"[{topic}] Gemini API 호출 실패: {e}")
            continue
        # 파일명 및 경로
        filename = f"{today}-{topic}-today.md"
        post_path = os.path.join(POST_DIRS[topic], filename)
        # 포스트 생성
        post_title = f"{topic.upper()} 오늘의 최신 기술 추천"
        post_md = make_post(post_title, today + ' 06:00:00', topic, content)
        # 폴더 없으면 생성
        os.makedirs(POST_DIRS[topic], exist_ok=True)
        # 파일 저장
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(post_md)
        print(f"[{topic}] 포스트 생성 완료: {post_path}")

if __name__ == '__main__':
    main() 
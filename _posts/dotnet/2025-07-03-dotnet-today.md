---
title: "DOTNET - Project Tye"
date: 2025-07-03 21:03:02 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, Project, Tye]
---

## 오늘의 DOTNET 최신 기술 트렌드: **Project Tye**

**1. 간단한 설명:**

Project Tye는 .NET 애플리케이션 개발, 테스트 및 배포를 간소화하기 위한 오픈 소스 도구입니다. 특히 마이크로서비스 아키텍처에서 여러 개의 서비스를 쉽게 관리하고 오케스트레이션할 수 있도록 설계되었습니다. 로컬 개발 환경에서 Docker 컨테이너를 사용한 실행, 의존성 관리, 서비스 검색, 로그 집계 등을 자동화하여 개발 생산성을 향상시키는 데 중점을 둡니다. Kubernetes 배포를 위한 설정 파일 생성도 지원합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **GitHub 저장소:** [https://github.com/dotnet/tye](https://github.com/dotnet/tye)
*   **Microsoft 블로그:** [https://devblogs.microsoft.com/dotnet/announcing-tye-a-developer-first-tool-for-microservice-and-distributed-application-development/](https://devblogs.microsoft.com/dotnet/announcing-tye-a-developer-first-tool-for-microservice-and-distributed-application-development/)
*   **Microsoft Learn (개념적으로만 남아있음):** [https://learn.microsoft.com/ko-kr/dotnet/architecture/tye/](https://learn.microsoft.com/ko-kr/dotnet/architecture/tye/)

**3. 간단한 코드 예시 (C#):**

Project Tye는 코드가 아니라 구성 파일 (`tye.yaml`)을 사용하여 애플리케이션을 정의합니다. 다음은 간단한 웹 API 애플리케이션을 위한 `tye.yaml` 예시입니다.

```yaml
name: my-app
services:
  webapi:
    project: ./MyWebApi/MyWebApi.csproj
    bindings:
      - port: 8080
```

**4. 코드 실행 결과 예시:**

`tye run` 명령어를 실행하면, Project Tye는 `tye.yaml`에 정의된 서비스를 Docker 컨테이너로 실행하고, 서비스 검색, 로그 집계 등을 자동으로 설정합니다.  터미널에 각 서비스의 endpoint 주소와 로그 스트림이 표시됩니다.  또한, Project Tye 대시보드 (일반적으로 `http://localhost:8000`)를 통해 실행 중인 서비스의 상태를 모니터링할 수 있습니다.  예를 들어, 터미널에는 다음과 비슷한 출력이 표시될 수 있습니다.

```
[14:15:30 INF] Starting Tye Host...
[14:15:31 INF] Binding webapi to http://localhost:8080
[14:15:31 INF] Service webapi is running at http://localhost:8080
[14:15:31 INF] Dashboard running on http://localhost:8000
```
그리고 localhost:8000으로 접속하면 webapi 서비스의 상태를 포함한 대시보드를 볼 수 있습니다.


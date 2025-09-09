---
title: "DOTNET - .NET의 Global Tool Manifests 및 Tool Manifest"
date: 2025-09-09 21:03:04 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Global, Tool, Manifests, Manifest]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Global Tool Manifests 및 Tool Manifest**

**1. 간단한 설명:**

.NET Global Tool Manifests 및 Tool Manifest는 .NET CLI 도구를 프로젝트 또는 시스템 레벨에서 관리하고 공유하기 위한 메커니즘입니다. Global Tool Manifests는 특정 .NET 프로젝트나 개발 환경에 필요한 도구를 명시적으로 정의하고 관리하여, 개발 환경의 일관성을 유지하고 팀 협업을 용이하게 합니다. Tool Manifest는 프로젝트 내에서 특정 도구를 사용하도록 지정하는 파일이며, Global Tool Manifests는 시스템 전반에 걸쳐 사용 가능한 도구를 정의합니다. 이를 통해 개발자는 필요한 도구를 쉽게 설치하고, 프로젝트의 종속성을 명확하게 관리할 수 있습니다.  이전에는 global tool을 설치하면 시스템 전체에 설치되어 다른 프로젝트와 충돌할 가능성이 있었지만, Tool Manifest를 사용하면 프로젝트별로 필요한 도구를 격리하여 관리할 수 있습니다.  또한, 도구 버전을 명시적으로 지정하여 환경 의존성 문제를 해결하고, 프로젝트 설정 및 협업을 단순화합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Tool Manifest 파일:** [https://learn.microsoft.com/en-us/dotnet/core/tools/tool-manifest](https://learn.microsoft.com/en-us/dotnet/core/tools/tool-manifest)
*   **.NET tools overview:** [https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools](https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools)
*   **dotnet tool install:** [https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-tool-install](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-tool-install)
*   **Manage local tools using tool manifests:** [https://devblogs.microsoft.com/dotnet/manage-local-tools-using-tool-manifests/](https://devblogs.microsoft.com/dotnet/manage-local-tools-using-tool-manifests/)

**3. 간단한 코드 예시 (C#):**

아래 예시는 프로젝트 내에서 `dotnet-format`이라는 도구를 사용하기 위한 설정 과정입니다.

1.  **Tool Manifest 생성:**

    ```bash
    dotnet new tool-manifest
    ```

    이 명령은 프로젝트 디렉토리에 `.config/dotnet-tools.json` 파일을 생성합니다. 이 파일은 프로젝트의 tool manifest 파일 역할을 합니다.

2.  **도구 설치:**

    ```bash
    dotnet tool install -g dotnet-format --version 6.0.4
    ```

    이 명령은 `dotnet-format` 도구를 global tool로 설치합니다.  하지만 tool manifest를 사용하는 경우 `-g` 플래그를 생략하고 local tool로 설치하는 것이 권장됩니다.

    ```bash
    dotnet tool install dotnet-format --version 6.0.4
    ```

    이 명령어는 현재 프로젝트의 tool manifest 파일 (`.config/dotnet-tools.json`)에 `dotnet-format` 도구를 추가합니다.

3.  **.config/dotnet-tools.json 파일 내용 예시:**

    ```json
    {
      "version": 1,
      "isRoot": true,
      "tools": {
        "dotnet-format": {
          "version": "6.0.4",
          "commands": [
            "dotnet-format"
          ]
        }
      }
    }
    ```

4.  **도구 실행:**

    ```bash
    dotnet tool restore  # 누락된 도구가 있는 경우, 복원
    dotnet format  # dotnet-format 실행 (csproj 파일이 있는 디렉토리에서 실행)
    ```

    `dotnet tool restore`는 `.config/dotnet-tools.json`에 정의된 도구를 설치합니다.

**4. 코드 실행 결과 예시:**

`dotnet format`을 실행하면 코드가 자동으로 포맷됩니다. 변경된 파일에 대한 정보가 콘솔에 출력됩니다. 예를 들어:

```
Formatting C:\path\to\your\project\Program.cs
```

`.config/dotnet-tools.json` 파일은 프로젝트에 필요한 도구와 버전을 명시적으로 지정하므로, 다른 개발자가 프로젝트를 체크아웃했을 때 `dotnet tool restore` 명령을 실행하여 필요한 도구를 자동으로 설치할 수 있습니다. 이를 통해 개발 환경의 일관성을 유지하고 팀 협업을 간소화할 수 있습니다.


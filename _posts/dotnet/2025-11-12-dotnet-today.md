---
title: "DOTNET - .NET의 향상된 Assembly Trimming"
date: 2025-11-12 21:03:39 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 향상된, Assembly, Trimming]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 향상된 Assembly Trimming**

**1. 간단한 설명:**

어셈블리 트리밍(Assembly Trimming)은 사용하지 않는 코드 및 종속성을 제거하여 애플리케이션의 크기를 줄이는 .NET의 기능입니다. 최근 .NET 버전에서는 어셈블리 트리밍의 정확성, 성능 및 구성 가능성이 크게 향상되었습니다. 특히, 트리밍 프로세스에 영향을 미치는 새로운 속성, 빌드 구성 옵션, 분석 기능 등이 추가되어 개발자가 AOT(Ahead-of-Time) 컴파일 환경 및 컨테이너 기반 배포에 더 적합한 더 작고 빠른 애플리케이션을 만들 수 있도록 지원합니다. 이는 트리밍된 애플리케이션이 런타임에 예상치 못한 동작을 일으키지 않도록 더 강력한 분석을 제공하며, 트리밍 프로세스를 세부적으로 조정할 수 있는 더 많은 옵션을 제공하여 달성됩니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET 어셈블리 트리밍 설명:** [https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/](https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/)
*   **릴리스 노트 및 블로그 게시물:** .NET 최신 버전의 릴리스 노트를 확인하여 어셈블리 트리밍 관련 변경 사항을 확인하세요.
*   **GitHub 리포지토리:** .NET 런타임 리포지토리에서 트리밍 관련 이슈 및 토론을 찾아볼 수 있습니다.

**3. 간단한 코드 예시 (C#):**

어셈블리 트리밍은 일반적으로 프로젝트 파일(.csproj)에서 빌드 구성을 통해 제어됩니다.  다음은 .csproj 파일에 추가하여 트리밍을 활성화하는 방법의 예입니다.

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <PublishTrimmed>true</PublishTrimmed>
    <TrimMode>link</TrimMode>
  </PropertyGroup>

</Project>
```

설명:

*   `PublishTrimmed`: 게시 프로세스에서 트리밍을 활성화합니다.
*   `TrimMode`: 트리밍 모드를 지정합니다.  `link`는 가장 적극적인 트리밍 모드이며, 사용되지 않는 코드를 삭제합니다. `copyused` 모드는 사용되는 어셈블리만 복사하지만 삭제하지는 않습니다.
    *   **TrimMode를 사용해야 하는 이유:** 런타임 시 코드가 제거되는 것을 방지합니다. 코드 트리밍은 시작 크기를 줄이는 데 도움이 될 수 있지만 애플리케이션의 동작에 영향을 미치지 않도록 올바르게 수행하는 것이 중요합니다.

**4. 코드 실행 결과 예시:**

트리밍을 활성화하고 애플리케이션을 게시한 후, 게시된 애플리케이션의 크기가 상당히 줄어들 것입니다. 정확한 크기 감소는 애플리케이션의 종속성과 코드 사용량에 따라 달라집니다. 예를 들어, 기본 ASP.NET Core 웹 API를 트리밍하면 게시된 출력 크기가 50% 이상 줄어들 수 있습니다. 트리밍은 크기 감소 외에도 로드 시간 단축 및 메모리 사용량 감소와 같은 성능 이점도 가져올 수 있습니다.


---
title: "DOTNET - .NET의 새로운 빌드 캐싱 기능 (Build Caching)"
date: 2025-11-09 21:03:00 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 새로운, 빌드, 캐싱, 기능, (Build, Caching)]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 새로운 빌드 캐싱 기능 (Build Caching)**

**1. 간단한 설명:**

.NET SDK는 빌드 속도를 향상시키기 위해 빌드 캐싱 기능을 제공합니다. 이 기능은 이전에 성공적으로 빌드된 프로젝트의 중간 빌드 결과물을 캐싱하여, 변경되지 않은 부분은 다시 빌드하지 않고 캐시된 결과를 재사용합니다. 특히 대규모 프로젝트나 여러 프로젝트로 구성된 솔루션에서 빌드 시간을 획기적으로 단축할 수 있습니다. 캐싱은 종속성 그래프 분석을 통해 변경되지 않은 프로젝트를 식별하고, 캐시된 컴파일, 종속성 및 기타 자산을 재사용함으로써 빌드 과정을 최적화합니다. 이 기능은 기본적으로 활성화되어 있으며, 프로젝트 속성 또는 환경 변수를 통해 구성하거나 비활성화할 수 있습니다.  빌드 캐싱은 incremental build와 유사하지만, 더 넓은 범위의 시나리오를 지원하고, 빌드 서버 환경에서도 효과적으로 작동하도록 설계되었습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Learn - 빌드 출력 캐싱:** [https://learn.microsoft.com/ko-kr/dotnet/core/project-sdk/build-output-caching](https://learn.microsoft.com/ko-kr/dotnet/core/project-sdk/build-output-caching)
*   **NuGet 블로그 - 패키지 캐싱:** (NuGet 패키지 캐싱도 관련이 있습니다) [https://devblogs.microsoft.com/nuget/improve-nuget-performance-with-package-caching-for-github-actions/](https://devblogs.microsoft.com/nuget/improve-nuget-performance-with-package-caching-for-github-actions/)

**3. 간단한 코드 예시 (C#):**

빌드 캐싱 자체는 코드 레벨에서 직접적인 변경을 요구하지 않습니다.  대신, 프로젝트 파일(.csproj)에서 빌드 캐싱 동작을 구성할 수 있습니다.  다음은 빌드 캐싱을 명시적으로 비활성화하는 예시입니다.

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <DisableBuildOutputInference>true</DisableBuildOutputInference> <!-- 빌드 출력 추론 비활성화 -->
    <DisableImplicitFrameworkReferences>true</DisableImplicitFrameworkReferences> <!-- 암시적 프레임워크 참조 비활성화 -->
    <UseArtifactsOutput>false</UseArtifactsOutput> <!-- artifacts output 비활성화 -->
  </PropertyGroup>

</Project>
```

**4. 코드 실행 결과 예시:**

빌드 캐싱의 효과는 눈에 띄는 빌드 시간 단축으로 나타납니다. 예를 들어, 변경사항이 거의 없는 솔루션을 빌드할 때, 빌드 캐싱이 활성화된 경우 빌드 시간이 50% 이상 단축될 수 있습니다.  빌드 출력 로그를 확인하면 캐시된 프로젝트와 다시 빌드된 프로젝트를 확인할 수 있습니다.  Visual Studio의 빌드 출력 창 또는 `dotnet build -v detailed` 명령을 사용하여 자세한 빌드 로그를 확인할 수 있습니다.  캐시 히트가 발생하면 "Restoring from cache"와 같은 메시지가 로그에 나타납니다.


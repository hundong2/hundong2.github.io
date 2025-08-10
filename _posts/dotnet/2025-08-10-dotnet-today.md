---
title: "DOTNET - .NET의 Source Link"
date: 2025-08-10 21:02:59 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Source, Link]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Source Link**

**1. 간단한 설명:**

Source Link는 NuGet 패키지 또는 실행 파일에서 소스 코드를 자동으로 다운로드하여 디버깅 경험을 향상시키는 기술입니다. 디버깅 시 호출 스택에서 외부 라이브러리의 코드를 클릭하면, Visual Studio가 해당 라이브러리의 소스 코드를 자동으로 다운로드하여 보여줍니다. 이를 통해 라이브러리의 내부 동작을 더욱 쉽게 이해하고, 문제를 진단하며, 디버깅 효율성을 높일 수 있습니다. Source Link는 .pdb 파일에 소스 코드 위치 정보를 포함시켜 작동하며, GitHub, GitLab, Azure DevOps 등 다양한 소스 코드 저장소를 지원합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - Source Link:** [https://learn.microsoft.com/en-us/dotnet/standard/library-guidance/sourcelink](https://learn.microsoft.com/en-us/dotnet/standard/library-guidance/sourcelink)
*   **Source Link GitHub Repository:** [https://github.com/dotnet/sourcelink](https://github.com/dotnet/sourcelink)
*   **Blog Post - Debugging .NET Libraries with Source Link:** [https://devblogs.microsoft.com/dotnet/debugging-net-libraries-with-source-link/](https://devblogs.microsoft.com/dotnet/debugging-net-libraries-with-source-link/)

**3. 간단한 코드 예시 (C#):**

Source Link 자체는 코드를 작성하는 것이 아니라, 프로젝트 설정과 NuGet 패키지 빌드 과정에서 활성화됩니다.  `.csproj` 파일에 다음 속성을 추가하여 활성화 할 수 있습니다.

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <GeneratePackageOnBuild>true</GeneratePackageOnBuild>
    <IncludeSourceRevisionInPackage>true</IncludeSourceRevisionInPackage>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.SourceLink.GitHub" Version="1.1.1" PrivateAssets="All" />
  </ItemGroup>

</Project>
```

설명:
*   `GeneratePackageOnBuild`: NuGet 패키지 빌드 옵션.
*   `IncludeSourceRevisionInPackage`: 패키지에 소스 리비전 정보를 포함합니다.
*   `Microsoft.SourceLink.GitHub`: GitHub 저장소를 사용하는 경우 추가합니다. GitLab, Azure DevOps 등 다른 저장소에 맞는 Source Link 패키지를 사용합니다.  예: `Microsoft.SourceLink.GitLab`

**4. 코드 실행 결과 예시:**

Source Link는 코드 실행 결과 자체를 변경하지 않습니다.  Source Link를 활성화한 후, NuGet 패키지를 빌드하고, 해당 패키지를 사용하는 프로젝트에서 디버깅 모드로 실행합니다.  호출 스택에서 Source Link가 활성화된 라이브러리의 코드를 클릭하면, Visual Studio가 소스 코드를 다운로드하여 보여줍니다. 별도의 결과 텍스트는 없으며 디버깅 환경에서만 확인 가능합니다.


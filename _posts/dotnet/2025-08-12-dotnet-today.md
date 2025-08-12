---
title: "DOTNET - .NET의 Central Package Management (CPM)"
date: 2025-08-12 21:03:09 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Central, Package, Management, (CPM)]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Central Package Management (CPM)**

**1. 간단한 설명:**

Central Package Management (CPM)는 NuGet 패키지 버전을 중앙에서 관리할 수 있도록 해주는 기능입니다. 기존에는 각 프로젝트 파일(.csproj)에서 개별적으로 NuGet 패키지 버전 관리를 해야 했지만, CPM을 사용하면 `Directory.Packages.props` 파일을 통해 패키지 버전을 한 곳에서 정의하고 관리할 수 있습니다. 이를 통해 프로젝트 전반에 걸쳐 일관된 패키지 버전을 유지하고, 버전 업데이트를 간소화할 수 있습니다.  특히 대규모 솔루션에서 패키지 버전 충돌 문제를 해결하고 유지보수성을 향상시키는 데 유용합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Learn - 중앙 패키지 관리:** [https://learn.microsoft.com/ko-kr/nuget/consume-packages/central-package-management](https://learn.microsoft.com/ko-kr/nuget/consume-packages/central-package-management)
*   **NuGet GitHub Repository:** [https://github.com/NuGet/NuGet.Client](https://github.com/NuGet/NuGet.Client) (관련 RFC 및 이슈 확인 가능)
*   **Example of migration to Central Package Management:** [https://github.com/castleproject/Core/pull/864](https://github.com/castleproject/Core/pull/864)

**3. 간단한 코드 예시 (C#):**

**Directory.Packages.props:**

```xml
<Project>
  <PropertyGroup>
    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
  </PropertyGroup>
  <ItemGroup>
    <PackageVersion Include="Newtonsoft.Json" Version="13.0.1" />
    <PackageVersion Include="Microsoft.Extensions.Logging" Version="6.0.0" />
  </ItemGroup>
</Project>
```

**.csproj (프로젝트 파일):**

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" />
    <PackageReference Include="Microsoft.Extensions.Logging" />
  </ItemGroup>

</Project>
```

**4. 코드 실행 결과 예시:**

위와 같이 설정하면, 프로젝트는 `Directory.Packages.props`에 정의된 `Newtonsoft.Json` 버전 13.0.1과 `Microsoft.Extensions.Logging` 버전 6.0.0을 사용하게 됩니다.  프로젝트 파일에는 버전 정보를 명시하지 않아도 되며, 필요한 경우 `Directory.Packages.props` 파일만 수정하여 전체 솔루션의 패키지 버전을 일괄적으로 변경할 수 있습니다.  `dotnet restore` 명령을 실행하면 지정된 버전으로 패키지가 설치됩니다.  만약 `Directory.Packages.props`에 정의되지 않은 패키지를 사용하려고 하면, 복원 시에 에러가 발생하여 중앙 관리되지 않은 패키지 사용을 방지할 수 있습니다.


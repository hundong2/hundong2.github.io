---
title: "DOTNET - Native AOT (Ahead-of-Time Compilation)"
date: 2025-07-03 15:37:41 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천]
---

## 오늘의 DOTNET 최신 기술 트렌드: **Native AOT (Ahead-of-Time Compilation)**

**1. 간단한 설명:**

Native AOT는 .NET 런타임 컴파일러인 RyuJIT를 사용하여 어플리케이션을 배포하기 전에 네이티브 코드로 미리 컴파일하는 기술입니다. 기존의 JIT(Just-In-Time) 컴파일 방식은 어플리케이션 실행 시에 코드를 컴파일하여 실행 속도 향상을 가져왔지만, 콜드 스타트 시간 지연 및 메모리 사용량 증가라는 단점이 있었습니다. Native AOT는 이러한 단점을 해결하고, 어플리케이션 시작 시간을 획기적으로 단축하며, 메모리 사용량을 줄이고, 크기가 작은 독립적인 실행 파일을 생성할 수 있도록 해줍니다. 특히 클라우드 환경, 서버리스 환경, 모바일 환경과 같이 빠른 시작 속도와 작은 Footprint가 중요한 환경에서 유용합니다. .NET 8부터 본격적으로 활용되기 시작하면서, 성능 및 배포 방식에 대한 새로운 가능성을 제시하고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Native AOT Deployment**: [https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/)
*   **Announcing .NET 8 Release Candidate 2**: [https://devblogs.microsoft.com/dotnet/announcing-dotnet-8-release-candidate-2/](https://devblogs.microsoft.com/dotnet/announcing-dotnet-8-release-candidate-2/)
*   **Native AOT: Bringing .NET to New Places**: [https://devblogs.microsoft.com/dotnet/native-aot/](https://devblogs.microsoft.com/dotnet/native-aot/)
*   **Exploring .NET 8's Native AOT**: [https://andrewlock.net/exploring-dotnet-8-native-aot-new-in-dotnet-8/](https://andrewlock.net/exploring-dotnet-8-native-aot-new-in-dotnet-8/)

**3. 간단한 코드 예시 (C#):**

Native AOT는 기존의 C# 코드를 변경하는 것이 아니라, 컴파일 과정에서 적용됩니다.  다음은 간단한 콘솔 애플리케이션 예시입니다.

```csharp
using System;

namespace NativeAOTExample
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, Native AOT!");
        }
    }
}
```

**4. 코드 실행 결과 예시:**

이 코드는 Native AOT로 컴파일되어 실행되면, 다음과 같은 결과를 콘솔에 출력합니다.

```
Hello, Native AOT!
```

**Native AOT로 컴파일하는 방법:**

1.  `.csproj` 파일에 `<PublishAot>true</PublishAot>`를 추가합니다.
2.  `dotnet publish -c Release -r <RID>` 명령어를 사용하여 컴파일합니다.  (`<RID>`는 런타임 식별자, 예를 들어 `linux-x64`, `win-x64`, `osx-x64` 등입니다.)

예시 (`.csproj` 파일):

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <PublishAot>true</PublishAot>
    <InvariantGlobalization>true</InvariantGlobalization>
  </PropertyGroup>

</Project>
```

컴파일 명령어:

```bash
dotnet publish -c Release -r linux-x64
```

이후 `bin/Release/net8.0/linux-x64/publish/` 폴더에서 네이티브 실행 파일을 확인할 수 있습니다.


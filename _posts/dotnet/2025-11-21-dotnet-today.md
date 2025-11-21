---
title: "DOTNET - .NET의 Native AOT Single-File Deployment 및 실행 파일 크기 최적화"
date: 2025-11-21 21:03:19 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Native, AOT, Single, File, Deployment, 실행, 파일, 크기, 최적화]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Native AOT Single-File Deployment 및 실행 파일 크기 최적화**

**1. 간단한 설명:**
Native AOT (Ahead-of-Time) 컴파일은 .NET 애플리케이션을 네이티브 코드로 직접 컴파일하여 시작 시간을 단축하고 메모리 사용량을 줄이는 기술입니다. Single-File Deployment는 애플리케이션과 필요한 모든 종속성을 하나의 실행 파일로 묶어 배포를 간소화합니다. 최근 .NET 업데이트에서는 Native AOT Single-File Deployment를 함께 사용하여 실행 파일의 크기를 더욱 줄이고 최적화하는 데 초점을 맞추고 있습니다. 이는 특히 클라우드 환경, IoT 디바이스, 모바일 앱과 같이 리소스 제약이 있는 환경에서 .NET 애플리케이션의 성능과 배포 용이성을 크게 향상시키는 데 기여합니다. 실행 파일 크기 최적화는 트리밍(Trimming) 및 링킹(Linking) 과정에서 사용하지 않는 코드를 제거하고, 불필요한 종속성을 제거하여 달성됩니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET 공식 블로그:** [https://devblogs.microsoft.com/dotnet/](https://devblogs.microsoft.com/dotnet/) (Native AOT 관련 포스팅 검색)
*   **.NET Native AOT 문서:** [https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/)
*   **.NET Single-File Deployment 문서:** [https://learn.microsoft.com/en-us/dotnet/core/deploying/single-file/](https://learn.microsoft.com/en-us/dotnet/core/deploying/single-file/)
*   **다양한 기술 블로그:** "dotnet native aot single file size" 검색

**3. 간단한 코드 예시 (C#):**

```csharp
// Program.cs
using System;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello, Native AOT Single-File!");
    }
}
```

```xml
<!-- .csproj 파일 -->
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <SelfContained>true</SelfContained>
    <PublishSingleFile>true</PublishSingleFile>
    <TrimMode>full</TrimMode>
    <InvariantGlobalization>true</InvariantGlobalization>
    <OptimizationPreference>Size</OptimizationPreference>
  </PropertyGroup>

</Project>
```

**4. 코드 실행 결과 예시:**

1.  **빌드:**
    ```bash
    dotnet publish -c Release -r linux-x64 # 적절한 런타임 ID로 변경
    ```

2.  **실행 (배포된 실행 파일):**

    빌드 후 `bin/Release/net8.0/linux-x64/publish` 디렉토리에 생성된 단일 실행 파일 (`Program` 또는 `Program.exe`)을 실행합니다. (실행 파일 이름은 프로젝트 이름에 따라 달라짐)

    ```bash
    ./Program  # 또는 Program.exe
    ```

3.  **출력:**

    ```
    Hello, Native AOT Single-File!
    ```

**참고:**

*   `<PublishAot>true</PublishAot>`는 Native AOT 컴파일을 활성화합니다.
*   `<SelfContained>true</SelfContained>`는 런타임 라이브러리를 실행 파일에 포함합니다.
*   `<PublishSingleFile>true</PublishSingleFile>`는 단일 파일 배포를 활성화합니다.
*   `<TrimMode>full</TrimMode>`은 트리밍을 최대한으로 설정하여 실행 파일 크기를 줄입니다.  이는 일부 코드가 런타임에 사용되지 않더라도 제거될 수 있으므로 주의해서 사용해야 합니다.  필요한 경우 `TrimMode`를 `link`로 설정하거나, 코드를 트리밍으로부터 보호하기 위해 `DynamicDependency` attribute를 사용할 수 있습니다.
*   `<InvariantGlobalization>true</InvariantGlobalization>`은 문화권 관련 데이터를 제거하여 실행 파일 크기를 줄입니다.  글로벌라이제이션이 필요하지 않은 애플리케이션에 적합합니다.
*   `<OptimizationPreference>Size</OptimizationPreference>` 는 컴파일러에게 코드 최적화 시 속도보다 크기를 우선시하도록 지시합니다.
*   Native AOT를 사용하면 일부 기능 (예: 리플렉션, 런타임 코드 생성)에 제한이 있을 수 있으므로, 코드 호환성을 확인해야 합니다.
*   실행 파일 크기는 종속성 및 코드 복잡성에 따라 달라집니다.

이러한 설정들을 적절하게 조절하여, 애플리케이션의 요구 사항에 맞는 최적의 실행 파일 크기를 얻을 수 있습니다. 특히, `<TrimMode>`의 설정은 신중하게 고려해야 합니다.


---
title: "DOTNET - .NET의 고급 타입 시스템 활용: Nullable Reference Types (NRT) 강화 및 Attribute 기반 Nullability 분석"
date: 2025-10-09 21:03:36 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 고급, 타입, 시스템, 활용:, Nullable, Reference, Types, (NRT), 강화, Attribute, 기반, Nullability, 분석]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 고급 타입 시스템 활용: Nullable Reference Types (NRT) 강화 및 Attribute 기반 Nullability 분석**

**1. 간단한 설명:**

.NET의 Nullable Reference Types (NRT)는 컴파일 시 null 참조 관련 오류를 방지하기 위해 도입되었습니다.  최근 트렌드는 NRT를 더욱 적극적으로 활용하고, Attribute 기반으로 Nullability 분석을 강화하여 런타임 예외 가능성을 줄이는 것입니다. 단순히 `string?` 처럼 nullable 여부를 명시하는 것을 넘어, `NotNullWhen`, `MaybeNullWhen` 같은 attribute를 사용하여 함수의 인자와 반환값의 nullability를 더욱 정밀하게 표현하고, 컴파일러가 이를 분석하여 더 정확한 경고를 생성하도록 유도합니다.  이는 개발자가 null 관련 문제에 더욱 집중하고, 코드의 안정성을 높이는 데 기여합니다. 또한, 제3자 라이브러리의 nullability를 명시적으로 지정하여 NRT의 효과를 전체 프로젝트로 확장하는 방식도 주목받고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   [Nullable Reference Types (C# Guide):](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references)
*   [Nullability Attributes (C# Reference):](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/attributes/nullable-analysis)
*   [Exploring .NET Nullable Reference Types (Community Article, Example Driven):](https://andrewlock.net/exploring-net-6-nullable-reference-types/)
*   [ASP.NET Core Nullable Reference Types Deep Dive (Community Article):](https://www.stevejgordon.co.uk/asp-net-core-6-nullable-reference-types-deep-dive)

**3. 간단한 코드 예시 (C#):**

```csharp
using System.Diagnostics.CodeAnalysis;

public class Example
{
    // Attribute를 사용하여 Nullability를 명시적으로 표현
    public bool TryGetValue(string key, [NotNullWhen(true)] out string? value)
    {
        if (key == "exists")
        {
            value = "found";
            return true;
        }
        value = null;
        return false;
    }

    public void Test()
    {
        if (TryGetValue("exists", out string? result))
        {
            // result는 null이 아님이 보장됨
            Console.WriteLine(result.Length);
        }
        else
        {
            // result는 null일 수 있음.
            Console.WriteLine("Key not found.");
        }
    }

    // 제3자 라이브러리 nullability 지정 (예: Microsoft.Extensions.Configuration)
    public void LoadConfiguration([AllowNull] string connectionString) {
      // connectionString이 null일 경우, ConfigurationBuilder를 통해 기본 설정 로드
      if (string.IsNullOrEmpty(connectionString)) {
        Console.WriteLine("No connection string provided, loading default configuration.");
        // 실제 ConfigurationBuilder를 사용하여 기본 설정을 로드하는 로직이 여기에 들어갑니다.
      } else {
        Console.WriteLine($"Using custom connection string: {connectionString}");
      }
    }

}
```

**4. 코드 실행 결과 예시:**

```
found
5
```

(TryGetValue에 "exists"를 전달했을 경우)
```
Key not found.
```

(TryGetValue에 "exists" 외 다른 값을 전달했을 경우)
```
No connection string provided, loading default configuration.
```

(LoadConfiguration에 null 또는 빈 문자열을 전달했을 경우)
```
Using custom connection string: MyConnectionString
```

(LoadConfiguration에 "MyConnectionString"을 전달했을 경우)


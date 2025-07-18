---
title: "DOTNET - C#의 Interceptors"
date: 2025-07-17 21:03:06 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, C#의, Interceptors]
---

## 오늘의 DOTNET 최신 기술 트렌드: **C#의 Interceptors**

**1. 간단한 설명:**

C# Interceptors는 컴파일 시간에 코드를 수정하거나 추가할 수 있는 강력한 기능입니다. Source Generators와 유사하지만, Interceptors는 기존 코드를 *수정*한다는 점에서 차이가 있습니다. 이를 통해 빌드 시점에 자동으로 코드를 생성하여 기존 코드의 동작을 변경하거나 확장할 수 있습니다. 예를 들어, 특정 메서드 호출을 가로채어 로깅, 보안 검사, 캐싱 등의 작업을 수행하는 코드를 삽입할 수 있습니다. 이는 AOP (Aspect-Oriented Programming)의 일부 개념을 구현하는 데 유용하게 사용될 수 있습니다.  Interceptors는 주로 라이브러리 개발자가 라이브러리의 동작 방식을 소비자의 코드 베이스에 맞게 사용자 정의할 수 있도록 설계되었습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **C# Interceptors Proposal:** [https://github.com/dotnet/roslyn/blob/main/docs/features/interceptors.md](https://github.com/dotnet/roslyn/blob/main/docs/features/interceptors.md)
*   **Intercepting Method Invocations in C# Source Generators:** [https://devblogs.microsoft.com/dotnet/intercepting-method-invocations-in-c-source-generators/](https://devblogs.microsoft.com/dotnet/intercepting-method-invocations-in-c-source-generators/)
*   **Explore C# Interceptors: Modifying Method Calls During Compilation (video):** [https://www.youtube.com/watch?v=V8H-G7mK2_0](https://www.youtube.com/watch?v=V8H-G7mK2_0)

**3. 간단한 코드 예시 (C#):**

```csharp
// Caller.cs
namespace MyNamespace;

public class Caller
{
    public void CallMe()
    {
        Console.WriteLine("Original CallMe method executed.");
    }
}

// Interceptor.cs
using System.Runtime.CompilerServices;

namespace MyNamespace;

public static class Interceptor
{
    [InterceptsLocation(@"/path/to/Caller.cs", 5, 17)] // Caller.cs 파일의 5번째 줄, 17번째 문자에서 인터셉트
    public static void ReplacementCallMe(this Caller caller)
    {
        Console.WriteLine("Interceptor replaced CallMe method!");
    }
}

// Interceptors.cs (최상위 파일, 컴파일러에게 인터셉터 사용을 알림)
namespace System.Runtime.CompilerServices
{
    [AttributeUsage(AttributeTargets.Method, AllowMultiple = true, Inherited = false)]
    internal sealed class InterceptsLocationAttribute : Attribute
    {
        public InterceptsLocationAttribute(string filePath, int lineNumber, int characterPosition)
        {
            FilePath = filePath;
            LineNumber = lineNumber;
            CharacterPosition = characterPosition;
        }

        public string FilePath { get; }
        public int LineNumber { get; }
        public int CharacterPosition { get; }
    }
}

// Program.cs
using MyNamespace;

Caller caller = new();
caller.CallMe();
```

**4. 코드 실행 결과 예시:**

```
Interceptor replaced CallMe method!
```

**설명:**

*   `Caller.cs`에는 원래 실행될 `CallMe` 메서드가 있습니다.
*   `Interceptor.cs`에는 `ReplacementCallMe` 메서드가 있습니다.  `InterceptsLocation` 어트리뷰트는 컴파일러에게 특정 위치에서 `CallMe` 호출을 `ReplacementCallMe`로 대체하라고 지시합니다.  `@"/path/to/Caller.cs"` 부분은 실제 파일 경로로 변경해야 합니다.
*   `Interceptors.cs` 파일은 컴파일러에게 인터셉터를 사용하도록 알려줍니다. 반드시 최상위 파일이어야 합니다. `System.Runtime.CompilerServices` 네임스페이스에 정의되어야 하며, 인터셉터 어트리뷰트가 정의되어야 합니다.
*   `Program.cs`에서 `caller.CallMe()`를 호출하면, 원래 `CallMe` 메서드 대신 `ReplacementCallMe` 메서드가 실행됩니다.

**주의 사항:**

*   `InterceptsLocation` 어트리뷰트의 파일 경로는 프로젝트 루트를 기준으로 하는 상대 경로 또는 절대 경로를 사용해야 합니다. 정확한 위치를 지정해야 인터셉터가 작동합니다.
*   Interceptor는 컴파일 시에 작동하므로, 런타임에 동적으로 변경할 수 없습니다.
*   Interceptor는 코드를 이해하기 어렵게 만들 수 있으므로, 신중하게 사용해야 합니다.  라이브러리 개발자가 API 변경 없이 기존 코드를 확장하거나 수정할 수 있도록 하는 데 특히 유용합니다.
*   Visual Studio 2022 버전 17.7 이상, .NET 8 이상부터 사용 가능합니다.


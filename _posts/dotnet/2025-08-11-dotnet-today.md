---
title: "DOTNET - C#의 AsyncMethodBuilder 속성 및 사용자 정의 AsyncMethodBuilder"
date: 2025-08-11 21:03:07 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, C#의, AsyncMethodBuilder, 속성, 사용자, 정의]
---

## 오늘의 DOTNET 최신 기술 트렌드: **C#의 AsyncMethodBuilder 속성 및 사용자 정의 AsyncMethodBuilder**

**1. 간단한 설명:**

`AsyncMethodBuilder`는 비동기 메서드의 실행을 관리하는 핵심 메커니즘입니다. C# 5.0에서 도입된 `async/await` 키워드 뒤에는 컴파일러가 자동으로 생성하는 `AsyncMethodBuilder`가 숨어있습니다.  기본적으로는 `AsyncTaskMethodBuilder<T>` 또는 `AsyncTaskMethodBuilder`가 사용되지만,  `AsyncMethodBuilder` 속성을 사용하면 특정 메서드에 대해 사용자 정의 빌더를 지정하여 메모리 할당 감소, 성능 향상, 특수한 비동기 실행 흐름 제어와 같은 고급 시나리오를 구현할 수 있습니다. 특히 고성능 어플리케이션, 게임 개발, 임베디드 환경 등에서 리소스 사용을 최적화하는 데 유용합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - AsyncMethodBuilderAttribute:** [https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.asyncmethodbuilderattribute?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.asyncmethodbuilderattribute?view=net-8.0)
*   **Stephen Toub's Blog - It's All About the Builders:**  (더 구체적인 내용은 관련 검색을 통해 찾을 수 있습니다. Stephen Toub은 .NET 성능 전문가로서 AsyncMethodBuilder에 대한 깊이 있는 분석을 제공했습니다.)
*   **기타 블로그 및 강좌 검색 키워드:** "C# AsyncMethodBuilder custom", ".NET async method builder performance"

**3. 간단한 코드 예시 (C#):**

```csharp
using System;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

// 사용자 정의 AsyncMethodBuilder
public struct ValueTaskMethodBuilder
{
    private AsyncTaskMethodBuilder _builder;

    public static ValueTaskMethodBuilder Create()
    {
        return new ValueTaskMethodBuilder { _builder = AsyncTaskMethodBuilder.Create() };
    }

    public void Start<TStateMachine>(ref TStateMachine stateMachine) where TStateMachine : IAsyncStateMachine
    {
        _builder.Start(ref stateMachine);
    }

    public void SetStateMachine(IAsyncStateMachine stateMachine)
    {
        _builder.SetStateMachine(stateMachine);
    }

    public void SetResult()
    {
        _builder.SetResult();
    }

    public void SetException(Exception exception)
    {
        _builder.SetException(exception);
    }

    public ValueTask Task => new ValueTask(_builder.Task); // Task를 ValueTask로 감쌈
}


// AsyncMethodBuilder 속성 적용
public static class MyAsyncMethods
{
    [AsyncMethodBuilder(typeof(ValueTaskMethodBuilder))]
    public static async ValueTask MyAsyncMethod()
    {
        Console.WriteLine("Async Method Running...");
        await Task.Delay(100); // Simulate some async work
        Console.WriteLine("Async Method Completed.");
    }
}


public class Example
{
    public static async Task Main()
    {
        Console.WriteLine("Starting...");
        await MyAsyncMethods.MyAsyncMethod();
        Console.WriteLine("Finished.");
    }
}

```

**4. 코드 실행 결과 예시:**

```
Starting...
Async Method Running...
Async Method Completed.
Finished.
```

**설명:** 위 예제는 `ValueTaskMethodBuilder`라는 사용자 정의 빌더를 만들고, `AsyncMethodBuilderAttribute`를 사용하여 `MyAsyncMethod`에 적용합니다.  `ValueTaskMethodBuilder`는 기본 `AsyncTaskMethodBuilder`를 사용하여 비동기 작업을 처리하지만, 최종 결과를 `Task`가 아닌 `ValueTask`로 반환하도록 합니다.  `ValueTask`는 메모리 할당을 줄일 수 있는 구조체 기반의 비동기 반환 타입입니다.  이 코드는 AsyncMethodBuilder를 사용하여 비동기 메서드의 동작을 제어하는 방법을 보여줍니다. 실제로 사용할 때는 빌더의 코드를 더욱 정밀하게 조정하여 특정 성능 목표를 달성해야 합니다.


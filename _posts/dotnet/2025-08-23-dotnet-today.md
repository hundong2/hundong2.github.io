---
title: "DOTNET - .NET의 ILoggerMessage를 활용한 고성능 로깅"
date: 2025-08-23 21:02:42 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, ILoggerMessage를, 활용한, 고성능, 로깅]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 ILoggerMessage를 활용한 고성능 로깅**

**1. 간단한 설명:**

`ILoggerMessage`는 .NET 6부터 도입된 기능으로, 고성능 로깅을 가능하게 합니다. 기존의 문자열 보간 또는 복합 형식 문자열을 사용하는 로깅 방식은 매번 문자열을 생성하고 파싱하는 오버헤드가 있었습니다. `ILoggerMessage`는 람다식을 사용하여 로그 메시지를 정의하고, 필요한 경우에만 문자열을 생성하므로 성능을 향상시킵니다. 이는 특히 빈번하게 발생하는 로깅 작업에서 큰 차이를 만들어낼 수 있습니다. `ILoggerMessage`는 강력한 형식 검사를 지원하며, 코드 가독성을 높이는 데도 기여합니다.  이 방법은 특히 고성능이 중요한 애플리케이션, 예를 들어 높은 트래픽을 처리하는 웹 애플리케이션이나, 데이터 분석 애플리케이션 등에서 유용하게 사용될 수 있습니다. 또한, 로깅 메시지를 템플릿으로 정의하고 재사용할 수 있도록 함으로써 코드의 중복을 줄이고 유지보수성을 향상시키는 데 도움을 줍니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Learn - ILogger 인터페이스:** [https://learn.microsoft.com/ko-kr/dotnet/api/microsoft.extensions.logging.ilogger?view=dotnet-8.0](https://learn.microsoft.com/ko-kr/dotnet/api/microsoft.extensions.logging.ilogger?view=dotnet-8.0) (기본 인터페이스)
*   **.NET 블로그 (엔트리 구조체 로깅 성능 개선에 대한 언급):**  (아쉽게도 공식적인 `ILoggerMessage`에 대한 .NET 블로그 문서는 찾기 어려우므로,  `LoggerMessage`를 활용한 성능 개선 관련 문서를 검색하는 것이 좋습니다.)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.Extensions.Logging;

public partial class MyService
{
    private readonly ILogger<MyService> _logger;

    public MyService(ILogger<MyService> logger)
    {
        _logger = logger;
    }

    public void DoSomething(string input, int value)
    {
        // ILoggerMessage를 사용하여 로그 메시지 정의
        LogInformation(_logger, input, value);

        // Some business logic
        Console.WriteLine($"Doing something with {input} and {value}");
    }

    // 로깅 메시지를 위한 메서드 (정적이고 partial로 선언)
    [LoggerMessage(
        EventId = 100,
        Level = LogLevel.Information,
        Message = "Doing something with input: {Input}, value: {Value}")]
    static partial void LogInformation(ILogger logger, string input, int value);
}

public class Program
{
    public static void Main(string[] args)
    {
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder.AddConsole(); // 콘솔에 로그 출력
            builder.SetMinimumLevel(LogLevel.Information);
        });

        var logger = loggerFactory.CreateLogger<MyService>();
        var myService = new MyService(logger);
        myService.DoSomething("Hello", 42);

    }
}

```

**4. 코드 실행 결과 예시:**

```
info: MyService[100]
      Doing something with input: Hello, value: 42
Doing something with Hello and 42
```

**추가 설명:**

위 코드에서 `LogInformation` 메서드는 `[LoggerMessage]` 어트리뷰트를 사용하여 정의됩니다. 이 어트리뷰트는 이벤트 ID, 로그 레벨 및 메시지 템플릿을 지정합니다.  `ILogger`의 `LogInformation` 확장 메서드는 메시지 템플릿과 매개변수를 사용하여 로그 메시지를 생성합니다. 이 방법은 문자열 보간을 사용하는 것보다 훨씬 효율적입니다. `LogInformation`은 정적이고 `partial`로 선언되어 JIT 컴파일러가 더 최적화된 코드를 생성할 수 있도록 합니다.


---
title: "DOTNET - .NET의 Minimal API의 필터(Filters) 및 미들웨어(Middleware) 지원 강화"
date: 2025-09-06 21:03:05 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Minimal, API의, 필터(Filters), 미들웨어(Middleware), 지원, 강화]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Minimal API의 필터(Filters) 및 미들웨어(Middleware) 지원 강화**

**1. 간단한 설명:**

.NET 6부터 도입된 Minimal API는 간단한 HTTP API를 빠르게 구축할 수 있도록 돕는 기술입니다. 초기에는 기능이 제한적이었지만, .NET 7과 8을 거치면서 필터(Filters)와 미들웨어(Middleware) 지원이 크게 강화되었습니다.  필터는 요청 처리 전후에 특정 로직을 실행하여 인증, 유효성 검사, 로깅 등을 수행할 수 있게 해주고, 미들웨어는 요청 파이프라인에 사용자 정의 로직을 추가하여 전역적인 요청 처리 흐름을 제어할 수 있도록 합니다.  이러한 기능 강화를 통해 Minimal API는 복잡한 애플리케이션의 요구사항도 충족할 수 있는 강력한 API 개발 방식으로 진화하고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Minimal APIs 공식 문서:** [https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis?view=aspnetcore-8.0)
*   **Minimal APIs 필터 (Filters) 관련 문서:** [https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/min-api-filters?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/min-api-filters?view=aspnetcore-8.0)
*   **Minimal APIs 미들웨어 (Middleware) 관련 문서:** 미들웨어는 ASP.NET Core의 핵심 개념이므로, 일반적인 ASP.NET Core 미들웨어 관련 문서를 참고하면 Minimal API에서도 동일하게 적용 가능합니다. 예를 들어: [https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-8.0)
*   **C# Interceptors를 활용한 Minimal API 필터링 (예시):** 위에 이미 Interceptors를 제외했으므로, 직접적인 Interceptors 활용 코드는 제공하지 않습니다. 하지만 개념적으로 필터링 로직을 모듈화하고 재사용 가능하게 만드는 데 활용될 수 있다는 점을 참고하세요.

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);

// 필터 정의
async Task<IResult> ValidateName(EndpointFilterInvocationContext context, EndpointFilterDelegate next)
{
    var name = context.GetArgument<string>(0); // 첫 번째 매개변수 (name) 가져오기
    if (string.IsNullOrEmpty(name))
    {
        return Results.BadRequest("Name is required.");
    }

    return await next(context);
}

var app = builder.Build();

// 미들웨어 정의 (간단한 로깅)
app.Use(async (context, next) =>
{
    Console.WriteLine("Request received at: " + DateTime.Now);
    await next(context);
    Console.WriteLine("Response sent at: " + DateTime.Now);
});

// 엔드포인트 정의 및 필터 적용
app.MapGet("/hello/{name}", ([FromRoute] string name) => $"Hello, {name}!")
    .AddEndpointFilter(ValidateName);

// 두 번째 엔드포인트 (필터 없이)
app.MapGet("/goodbye/{name}", ([FromRoute] string name) => $"Goodbye, {name}!");


app.Run();
```

**4. 코드 실행 결과 예시:**

1.  **`GET /hello/World`**:
    *   **출력:** `Hello, World!`
    *   **콘솔:**
        ```
        Request received at: [날짜 및 시간]
        Response sent at: [날짜 및 시간]
        ```

2.  **`GET /hello/` (이름 없이 호출)**:
    *   **출력:** `400 Bad Request` (본문: "Name is required.")
    *   **콘솔:**
        ```
        Request received at: [날짜 및 시간]
        Response sent at: [날짜 및 시간]
        ```

3.  **`GET /goodbye/World`**:
    *   **출력:** `Goodbye, World!`
    *   **콘솔:**
        ```
        Request received at: [날짜 및 시간]
        Response sent at: [날짜 및 시간]
        ```

**설명:**

*   `/hello/{name}` 엔드포인트에는 `ValidateName` 필터가 적용되어 이름이 비어 있으면 400 오류를 반환합니다.
*   미들웨어는 모든 요청의 전후에 시간을 로깅합니다.
*   `/goodbye/{name}` 엔드포인트는 필터가 적용되지 않아 이름 유효성 검사를 거치지 않습니다.

이 예제는 Minimal API의 필터와 미들웨어 기능을 간단하게 보여줍니다. 실제 사용 시에는 더욱 복잡한 로직을 필터와 미들웨어에 구현하여 API의 기능과 보안을 강화할 수 있습니다.


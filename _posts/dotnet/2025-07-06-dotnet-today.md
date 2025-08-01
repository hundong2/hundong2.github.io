---
title: "DOTNET - ASP.NET Core Rate Limiting"
date: 2025-07-06 21:02:48 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, "ASP.NET", Core, Rate, Limiting]
---

## 오늘의 DOTNET 최신 기술 트렌드: **ASP.NET Core Rate Limiting**

**1. 간단한 설명:**

ASP.NET Core Rate Limiting은 애플리케이션이 과도한 요청으로 인해 다운되는 것을 방지하고, API의 악의적인 사용을 제한하며, 서비스 품질을 유지하기 위해 특정 기간 동안의 요청 수를 제한하는 기능입니다.  ASP.NET Core 7.0부터 내장 미들웨어로 제공되며, 다양한 알고리즘(고정 윈도우, 슬라이딩 윈도우, 토큰 버킷 등)을 사용하여 유연하게 설정할 수 있습니다. 사용자는 IP 주소, 사용자 ID, API 키 등 다양한 식별자를 기준으로 Rate Limiting을 적용할 수 있으며, 정책 설정을 통해 특정 엔드포인트나 컨트롤러에 대해 차별화된 제한을 설정할 수 있습니다.  이 기능은 DoS 공격 방어, 서버 과부하 방지, API 남용 방지에 효과적입니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft 공식 문서:** [https://learn.microsoft.com/en-us/aspnet/core/security/rate-limit?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/security/rate-limit?view=aspnetcore-8.0)
*   **Steve Gordon 블로그 (Rate Limiting with ASP.NET Core 7.0):** [https://www.stevejgordon.co.uk/rate-limiting-with-asp-net-core-7-0](https://www.stevejgordon.co.uk/rate-limiting-with-asp-net-core-7-0)
*   **AspNetCoreRateLimit 라이브러리 (타사 라이브러리, 필요에 따라 사용):** [https://github.com/stefanprodan/AspNetCoreRateLimit](https://github.com/stefanprodan/AspNetCoreRateLimit)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.AspNetCore.RateLimiting;
using System.Threading.RateLimiting;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRateLimiter(options =>
{
    options.AddFixedWindowLimiter(policyName: "fixed", options =>
    {
        options.PermitLimit = 4;  // 최대 요청 수
        options.Window = TimeSpan.FromSeconds(10); // 시간 창
        options.QueueProcessingOrder = QueueProcessingOrder.OldestFirst;
        options.QueueLimit = 2;    // 대기 큐 길이
    });

    options.RejectionStatusCode = StatusCodes.Status429TooManyRequests;
});

var app = builder.Build();

app.UseRateLimiter();

app.MapGet("/api/data", () => Results.Ok("Data received!"))
    .RequireRateLimiting("fixed");  // policyName 지정

app.Run();
```

**4. 코드 실행 결과 예시:**

위 코드를 실행하고 `/api/data` 엔드포인트에 10초 안에 4번 이상 요청을 보내면 다음과 같은 결과가 나타납니다.

*   처음 4번의 요청: HTTP 200 OK (Data received!)
*   5번째, 6번째 요청: 큐에 쌓였다가 처리됨 (HTTP 200 OK, 10초 창 안에 요청 처리가 가능할 경우)
*   7번째 이후의 요청: HTTP 429 Too Many Requests

**설명:**

*   `AddRateLimiter`를 사용하여 Rate Limiting 미들웨어를 설정합니다.
*   `AddFixedWindowLimiter`를 사용하여 고정 윈도우 알고리즘을 정의하고 "fixed"라는 이름을 지정합니다.
*   `PermitLimit`는 윈도우 시간 동안 허용되는 최대 요청 수입니다.
*   `Window`는 Rate Limiting을 적용하는 시간 창입니다.
*   `QueueLimit`는 대기 큐에 쌓을 수 있는 최대 요청 수입니다. 이 수를 초과하면 429 오류가 발생합니다.
*   `RejectionStatusCode`는 Rate Limit에 걸렸을 때 반환될 HTTP 상태 코드입니다.
*   `app.UseRateLimiter()`를 통해 Rate Limiting 미들웨어를 파이프라인에 추가합니다.
*   `RequireRateLimiting("fixed")`를 사용하여 특정 엔드포인트에 Rate Limiting 정책을 적용합니다.


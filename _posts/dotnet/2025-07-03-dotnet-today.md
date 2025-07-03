---
title: "DOTNET - .NET Aspire"
date: 2025-07-03 15:24:52 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET Aspire**

**1. 간단한 설명:**
.NET Aspire는 클라우드 네이티브 애플리케이션 개발을 간소화하기 위한 Microsoft의 오피니언화된 스택입니다. 분산 애플리케이션 개발, 배포, 모니터링의 복잡성을 줄이는 데 중점을 두고 있습니다. Aspire는 런타임, 툴링, 구성 요소를 결합하여 개발자가 복잡한 분산 시스템을 보다 쉽게 구축하고 운영할 수 있도록 합니다. 특히 마이크로서비스 아키텍처를 사용하는 애플리케이션에 적합하며, 서비스 검색, 구성 관리, 관찰 가능성과 같은 기능을 기본적으로 제공합니다. .NET 8과 함께 본격적으로 사용하기에 용이하며, .NET 7에서도 프리뷰 버전으로 사용 가능합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Aspire 공식 문서:** [https://learn.microsoft.com/ko-kr/dotnet/aspire/](https://learn.microsoft.com/ko-kr/dotnet/aspire/)
*   **.NET 블로그 - Introducing .NET Aspire:** [https://devblogs.microsoft.com/dotnet/introducing-dotnet-aspire/](https://devblogs.microsoft.com/dotnet/introducing-dotnet-aspire/)
*   **.NET Aspire GitHub 저장소:** [https://github.com/dotnet/aspire](https://github.com/dotnet/aspire)

**3. 간단한 코드 예시 (C#):**

```csharp
// Program.cs (Aspire AppHost 프로젝트)

using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

// Redis 캐시 서비스 추가
builder.AddRedis("cache");

// 웹 API 서비스 추가 (cache 서비스를 의존성으로 가짐)
builder.AddProject<Projects.WebApp>("webapi")
    .WithReference(builder.GetResource<RedisResource>("cache"));

builder.Build().Run();
```

```csharp
// WebApp 프로젝트의 Program.cs (예시)

var builder = WebApplication.CreateBuilder(args);

// Redis 연결 설정 (Aspire에서 제공하는 연결 정보를 사용)
builder.Services.AddStackExchangeRedisCache(options =>
{
    options.Configuration = builder.Configuration["ConnectionStrings:cache"];
});

var app = builder.Build();

app.MapGet("/", async (IStackExchangeRedisCache cache) =>
{
    var cachedValue = await cache.GetStringAsync("myKey");
    if (cachedValue == null)
    {
        cachedValue = "Hello from .NET Aspire!";
        await cache.SetStringAsync("myKey", cachedValue);
    }
    return cachedValue;
});

app.Run();

```

**4. 코드 실행 결과 예시:**

위 코드를 실행하면 Aspire 대시보드를 통해 Redis 캐시 서비스와 Web API 서비스의 상태를 확인할 수 있습니다.  Web API에 접근하면 "Hello from .NET Aspire!" 라는 문자열이 반환되며, 해당 값은 Redis 캐시에 저장됩니다.  이후 동일한 API를 호출하면 Redis 캐시에서 값을 가져와 반환합니다. Aspire 대시보드를 통해 서비스 간의 의존성, 로그, 메트릭 등을 쉽게 모니터링할 수 있습니다.


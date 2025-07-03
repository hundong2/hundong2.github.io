---
title: "DOTNET - .NET Aspire"
date: 2025-07-03 15:47:52 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET, Aspire]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET Aspire**

**1. 간단한 설명:**

.NET Aspire는 분산 애플리케이션 개발을 간소화하기 위한 마이크로소프트의 클라우드 네이티브 스택입니다. Aspire는 개발자가 복잡한 분산 시스템을 더 쉽게 구축, 디버깅, 배포 및 관리를 할 수 있도록 설계되었습니다. 핵심적으로 Aspire는 클라우드 네이티브 애플리케이션에서 필요한 서비스 검색, 구성 관리, 텔레메트리, 서비스 간 통신 및 탄력성 패턴 구현과 같은 일반적인 문제들을 해결하는 데 중점을 둡니다. Aspire를 사용하면 개발자는 인프라 코드보다는 비즈니스 로직에 집중할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Aspire Overview (Microsoft Docs):** [https://learn.microsoft.com/en-us/dotnet/aspire/get-started/](https://learn.microsoft.com/en-us/dotnet/aspire/get-started/)
*   **.NET Aspire 샘플:** [https://github.com/dotnet/aspire/tree/main/samples](https://github.com/dotnet/aspire/tree/main/samples)
*   **.NET Aspire 블로그 (Microsoft .NET Blog):** [https://devblogs.microsoft.com/dotnet/tag/aspire/](https://devblogs.microsoft.com/dotnet/tag/aspire/)

**3. 간단한 코드 예시 (C#):**

다음은 .NET Aspire를 사용하여 Redis 캐시를 서비스로 등록하는 간단한 예제입니다.

```csharp
// Program.cs (Aspire Host)

using Aspire.StackExchangeRedis;

var builder = DistributedApplication.CreateBuilder(args);

// Redis 캐시를 서비스로 추가합니다.
builder.AddRedis("cache");

// HTTP API 프로젝트를 서비스로 추가하고, 캐시를 의존성으로 연결합니다.
builder.AddProject<Projects.WebApp>("webapp")
       .WithReference(builder.GetResource("cache"));

builder.Build().Run();

// WebApp 프로젝트 (WebApp.csproj) 내의 코드

using StackExchange.Redis;

var builder = WebApplication.CreateBuilder(args);

// Redis 연결 문자열을 가져옵니다. Aspire가 자동으로 연결 정보를 제공합니다.
string redisConnectionString = builder.Configuration.GetConnectionString("cache");

// Redis 연결을 설정합니다.
builder.Services.AddStackExchangeRedisCache(options =>
{
    options.Configuration = redisConnectionString;
});

var app = builder.Build();

app.MapGet("/", async (IConnectionMultiplexer redis) => {
    IDatabase db = redis.GetDatabase();
    await db.StringSetAsync("mykey", "Hello from Aspire!");
    return await db.StringGetAsync("mykey");
});

app.Run();

```

**4. 코드 실행 결과 예시:**

이 코드 예시를 실행하면, ASP.NET Core 웹 애플리케이션이 시작되고,  `/` 엔드포인트에 접근하면 Redis 캐시에 "mykey"라는 키로 "Hello from Aspire!"라는 값을 저장하고, 저장된 값을 반환합니다. Aspire 대시보드를 통해 서비스 연결 상태, 로그, 메트릭을 모니터링할 수 있습니다. 브라우저에서 `/` 엔드포인트를 호출하면 브라우저에 "Hello from Aspire!"가 표시됩니다.


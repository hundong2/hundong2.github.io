---
title: "DOTNET - .NET Aspire의 Service Defaults"
date: 2025-11-30 21:03:25 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET, Aspire의, Service, Defaults]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET Aspire의 Service Defaults**

**1. 간단한 설명:**
.NET Aspire의 Service Defaults는 분산 애플리케이션 개발 시 서비스 간의 통신, 구성, 로깅, 헬스 체크 등 공통적인 설정을 중앙 집중적으로 관리하고 재사용할 수 있도록 하는 기능입니다. 이를 통해 개발자는 각 서비스별로 반복적인 설정을 하지 않고도 일관성 있는 애플리케이션 동작을 보장할 수 있으며, 서비스 간의 의존성을 명확하게 정의하고 관리할 수 있습니다. Service Defaults는 애플리케이션의 구성 요소 간에 표준화된 설정을 적용하여 개발 생산성을 높이고 유지보수를 용이하게 합니다. 핵심은 중앙 집중식 구성, 자동 구성 적용, 타입 안정성 및 확장성에 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   .NET Aspire 공식 문서: [https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/service-defaults](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/service-defaults)
*   .NET 블로그의 .NET Aspire 관련 게시물 (예시): [https://devblogs.microsoft.com/dotnet/introducing-dotnet-aspire-preview-1/](https://devblogs.microsoft.com/dotnet/introducing-dotnet-aspire-preview-1/) (최신 버전의 .NET Aspire 소개글 참고)

**3. 간단한 코드 예시 (C#):**

```csharp
// Program.cs (호스트 프로젝트)

using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

// 서비스 정의 (예: Redis)
var redis = builder.AddRedis("redis");

// 프로젝트 추가
var apiservice = builder.AddProject<Projects.ApiService>("apiservice");

// 서비스 간 연결 구성 (예: apiservice가 redis에 의존)
apiservice.WithReference(redis);

builder.Build().Run();
```

```csharp
// ApiService 프로젝트의 Program.cs (API 서비스 프로젝트)
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

// 서비스 등록 (예: Redis 캐시)
builder.Services.AddStackExchangeRedisCache(options =>
{
    // 구성은 .NET Aspire에 의해 자동으로 설정됨
});

// ... 기타 API 서비스 구성 ...

var app = builder.Build();

// ... 미들웨어 설정 및 라우팅 ...

app.Run();
```

```csharp
// AppHost 프로젝트의 Service Defaults 설정 (AppHost.cs 또는 유사한 파일)
builder.Services.ConfigureDefaults(defaults =>
{
    // 예: gRPC 헬스 체크 활성화
    defaults.UseGrpcHealthChecks();

    // 예: OpenTelemetry 구성
    defaults.UseOpenTelemetry();

    // 사용자 정의 Service Defaults도 가능
    defaults.Add(builder =>
    {
        if (builder.Resource.Annotations.OfType<DaprResourceAnnotation>().Any())
        {
             builder.ConfigureContainer(properties =>
             {
                   properties.Environment.Add("DAPR_HTTP_MAX_REQUEST_SIZE", "100");
             });
        }
    });
});
```

**4. 코드 실행 결과 예시:**

코드를 실행하면 .NET Aspire는 다음과 같은 작업을 자동으로 처리합니다.

*   서비스 간의 연결 정보를 환경 변수로 설정하여 각 서비스가 서로를 찾을 수 있도록 합니다.
*   Redis 캐시와 같은 의존성을 필요한 서비스에 주입합니다.
*   각 서비스에 대해 헬스 체크 엔드포인트를 구성합니다.
*   OpenTelemetry를 구성하여 분산 트레이싱 및 메트릭 수집을 활성화합니다.

이러한 설정은 명시적인 코드 없이 .NET Aspire 프레임워크에 의해 자동으로 이루어지므로 개발자는 비즈니스 로직에 집중할 수 있습니다.  .NET Aspire 대시보드를 통해 서비스 상태, 로그, 메트릭 등을 모니터링할 수 있습니다.

**주의:** 위 예시는 .NET Aspire의 개념을 보여주기 위한 것이며, 실제 구현은 프로젝트 구조와 구성에 따라 달라질 수 있습니다.  최신 .NET Aspire 버전을 기준으로 작성되었으며, Preview 버전에서 API 변경이 있을 수 있습니다. 항상 공식 문서를 참조하십시오.


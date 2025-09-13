---
title: "DOTNET - .NET의 새로운 스레딩 프리미티브: `System.Threading.RateLimiter`"
date: 2025-09-13 21:03:02 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 새로운, 스레딩, 프리미티브:, `System.Threading.RateLimiter`]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 새로운 스레딩 프리미티브: `System.Threading.RateLimiter`**

**1. 간단한 설명:**
`System.Threading.RateLimiter`는 .NET 7부터 도입된 새로운 라이브러리로, 애플리케이션 또는 서비스의 처리량을 제어하는 데 사용됩니다. 특정 기간 동안 처리할 수 있는 요청 수를 제한하여 시스템 과부하를 방지하고, 서비스 품질을 유지하며, 악의적인 공격으로부터 보호하는 데 유용합니다. 다양한 제한 알고리즘(Token Bucket, Concurrency Limiter 등)을 제공하며, 확장 가능한 아키텍처를 통해 사용자 정의 제한 전략을 구현할 수 있습니다. 이는 특히 마이크로서비스 아키텍처에서 중요한 역할을 하며, 외부 API 호출을 제한하거나, 내부 처리량을 관리하는 데 효과적입니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Official Blog (관련 게시물):** 아쉽게도 .NET 블로그에 `RateLimiter`에 대한 독립적인 게시물은 찾기 어렵지만, .NET 7 릴리스 정보 및 관련 문서에서 찾을 수 있습니다.
*   **Microsoft Learn 문서:** [https://learn.microsoft.com/en-us/dotnet/api/system.threading.ratelimiter?view=net-7.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.ratelimiter?view=net-7.0)
*   **GitHub 샘플:** [https://github.com/dotnet/runtime/tree/main/src/libraries/System.Threading.RateLimiter](https://github.com/dotnet/runtime/tree/main/src/libraries/System.Threading.RateLimiter) (라이브러리 소스 코드 및 샘플)
*   **ASP.NET Core Rate Limiting Middleware:** [https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit?view=aspnetcore-8.0) (ASP.NET Core에서 사용하는 방법)

**3. 간단한 코드 예시 (C#):**

```csharp
using System;
using System.Threading;
using System.Threading.RateLimiter;
using System.Threading.Tasks;

public class RateLimiterExample
{
    public static async Task Main(string[] args)
    {
        // 초당 5개의 요청만 허용하는 TokenBucketRateLimiter 생성
        TokenBucketRateLimiterOptions options = new TokenBucketRateLimiterOptions
        {
            TokenLimit = 5,
            ReplenishmentPeriod = TimeSpan.FromSeconds(1),
            TokensPerPeriod = 5,
            AutoReplenishment = true
        };
        using TokenBucketRateLimiter limiter = new TokenBucketRateLimiter(options);

        for (int i = 0; i < 10; i++)
        {
            // 요청이 가능한지 확인
            RateLimitLease lease = await limiter.AcquireAsync(1); // 1개의 토큰 획득 시도
            if (lease.IsAcquired)
            {
                Console.WriteLine($"요청 {i + 1}: 허용됨");
                // 실제 작업 수행 (예: API 호출)
                await Task.Delay(100); // 간단한 지연
            }
            else
            {
                Console.WriteLine($"요청 {i + 1}: 제한됨");
                // 제한되었을 때 처리 (예: 재시도, 오류 처리)
            }
        }

        Console.WriteLine("완료.");
    }
}
```

**4. 코드 실행 결과 예시:**

```
요청 1: 허용됨
요청 2: 허용됨
요청 3: 허용됨
요청 4: 허용됨
요청 5: 허용됨
요청 6: 제한됨
요청 7: 제한됨
요청 8: 제한됨
요청 9: 제한됨
요청 10: 제한됨
완료.
```

**설명:**

위 코드에서는 `TokenBucketRateLimiter`를 사용하여 초당 5개의 요청으로 제한합니다. `AcquireAsync(1)` 메서드는 1개의 토큰을 획득하려고 시도합니다. 토큰을 획득하면 `lease.IsAcquired`가 `true`를 반환하고, 요청이 허용됩니다. 그렇지 않으면 요청이 제한됩니다. ReplenishmentPeriod와 TokensPerPeriod를 조절하여 요청 제한 정도를 변경할 수 있습니다.


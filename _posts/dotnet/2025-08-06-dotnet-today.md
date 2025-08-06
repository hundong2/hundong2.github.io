---
title: "DOTNET - .NET의 Resilience 및 Fault Tolerance 패턴 구현 (Polly 라이브러리)"
date: 2025-08-06 21:03:18 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Resilience, Fault, Tolerance, 패턴, 구현, (Polly, 라이브러리)]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Resilience 및 Fault Tolerance 패턴 구현 (Polly 라이브러리)**

**1. 간단한 설명:**

.NET 개발에서 애플리케이션의 안정성과 복원력을 향상시키는 것은 매우 중요합니다. Polly는 이러한 목표를 달성하기 위한 강력한 .NET 라이브러리입니다. Polly는 재시도, 서킷 브레이커, 폴백, 타임아웃, 캐싱 등 다양한 Resilience 및 Fault Tolerance 패턴을 구현하는 데 사용됩니다.  특히 분산 시스템, 마이크로서비스 아키텍처에서 외부 의존성에 대한 일시적인 오류(Transient Faults)를 효과적으로 처리하고, 전체 시스템의 안정성을 유지하는 데 핵심적인 역할을 합니다. Polly는 단순한 API를 제공하며, ConfigureAwait(false)를 준수하며, 다양한 로깅 및 메트릭 기능을 지원합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Polly GitHub:** [https://github.com/App-vNext/Polly](https://github.com/App-vNext/Polly)
*   **Polly Wiki:** [https://github.com/App-vNext/Polly/wiki](https://github.com/App-vNext/Polly/wiki)
*   **Microsoft Documentation:** [https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/) (마이크로서비스 아키텍처에서의 Resilience 관련 문서)
*   **Blog Post Example:** [https://www.exceptionnotfound.net/using-polly-in-asp-net-core-for-transient-fault-handling/](https://www.exceptionnotfound.net/using-polly-in-asp-net-core-for-transient-fault-handling/) (Polly와 ASP.NET Core 통합 예제)

**3. 간단한 코드 예시 (C#):**

```csharp
using Polly;
using Polly.Retry;

// 외부 API를 호출하는 예시 함수
async Task<string> CallExternalApiAsync()
{
    // 실제 API 호출 로직 (가정)
    Console.WriteLine("API 호출 시도...");
    await Task.Delay(100); // 잠시 대기 (네트워크 지연 시뮬레이션)
    Random rnd = new Random();
    if (rnd.Next(0, 10) < 3) // 30% 확률로 예외 발생 시뮬레이션
    {
        throw new HttpRequestException("API 호출 실패!");
    }
    return "API 호출 성공!";
}

public async Task RunPollyExample()
{
    // 재시도 정책 정의 (최대 3번 재시도, 지수 백오프 적용)
    RetryPolicy retryPolicy = Policy
        .Handle<HttpRequestException>() // HttpRequestException 예외 처리
        .WaitAndRetryAsync(3, retryAttempt =>
            TimeSpan.FromSeconds(Math.Pow(2, retryAttempt))); // 2^retryAttempt 초 대기

    try
    {
        // 정책 실행 및 API 호출
        string result = await retryPolicy.ExecuteAsync(async () => await CallExternalApiAsync());

        Console.WriteLine($"결과: {result}");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"오류 발생: {ex.Message}");
    }
}

// 메인 함수
public static async Task Main(string[] args)
{
    PollyExample example = new PollyExample();
    await example.RunPollyExample();
}

public class PollyExample
{
    public Task RunPollyExample()
    {
        throw new NotImplementedException();
    }
}
```

**4. 코드 실행 결과 예시:**

```
API 호출 시도...
API 호출 시도...
API 호출 시도...
오류 발생: API 호출 실패!
```

(위의 예시는 API 호출이 3번 실패하고, 그 이후 예외가 처리된 경우입니다. 성공할 경우 "결과: API 호출 성공!" 메시지가 출력됩니다.)

**설명:**

이 코드는 Polly 라이브러리를 사용하여 `HttpRequestException`이 발생할 경우, 최대 3번까지 재시도하는 로직을 보여줍니다. `WaitAndRetryAsync` 메서드를 사용하여 재시도 간에 지수 백오프(Exponential Backoff)를 적용했습니다. 즉, 재시도 횟수가 증가할수록 대기 시간이 늘어납니다. 이를 통해 일시적인 네트워크 문제 등으로 인한 오류를 효과적으로 처리하고, 애플리케이션의 복원력을 높일 수 있습니다. Polly는 이 외에도 서킷 브레이커, 타임아웃, 폴백 등 다양한 정책을 지원하여, 애플리케이션의 Resilience를 종합적으로 관리할 수 있도록 도와줍니다.


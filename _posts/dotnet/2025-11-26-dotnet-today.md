---
title: "DOTNET - .NET의 IHostedLifecycleService 인터페이스"
date: 2025-11-26 21:03:25 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, IHostedLifecycleService, 인터페이스]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 IHostedLifecycleService 인터페이스**

**1. 간단한 설명:**

`IHostedLifecycleService`는 .NET 6부터 도입된 인터페이스로, `IHostedService` 인터페이스를 확장하여 호스팅된 서비스의 생명주기 동안 더 세분화된 제어 지점을 제공합니다.  `IHostedService`가 `StartAsync`와 `StopAsync`만 제공하는 반면, `IHostedLifecycleService`는 다음과 같은 추가 메서드를 제공합니다.

*   `StartingAsync`: 서비스가 시작되기 직전에 호출됩니다.
*   `StartedAsync`: 서비스가 시작된 직후에 호출됩니다.
*   `StoppingAsync`: 서비스가 중지되기 직전에 호출됩니다.
*   `StoppedAsync`: 서비스가 중지된 직후에 호출됩니다.

이러한 추가 메서드를 통해 호스팅된 서비스의 시작 및 종료 과정에서 더 미세하게 제어하고, 로깅, 메트릭 수집, 사전 초기화 또는 정리 작업 등을 수행할 수 있습니다. 예를 들어, `StartingAsync`에서 구성 정보를 로드하거나, `StoppedAsync`에서 사용하지 않는 리소스를 해제할 수 있습니다. 이 인터페이스는 특히 백그라운드 작업, 데이터베이스 연결 관리, 캐싱 등의 시나리오에서 유용합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Documentation:** [https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostedlifecycleservice?view=dotnet-plat-ext-8.0](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostedlifecycleservice?view=dotnet-plat-ext-8.0)
*   **Stack Overflow:**  (Stack Overflow에서 `IHostedLifecycleService`에 대한 관련 질문 및 답변을 검색하여 참조할 만한 링크를 찾을 수 있습니다.)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System.Threading;
using System.Threading.Tasks;

public class MyLifecycleService : IHostedLifecycleService
{
    private readonly ILogger<MyLifecycleService> _logger;

    public MyLifecycleService(ILogger<MyLifecycleService> logger)
    {
        _logger = logger;
    }

    public Task StartingAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Service is starting.");
        return Task.CompletedTask;
    }

    public Task StartedAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Service has started.");
        return Task.CompletedTask;
    }

    public Task StoppingAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Service is stopping.");
        return Task.CompletedTask;
    }

    public Task StoppedAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Service has stopped.");
        return Task.CompletedTask;
    }

    public Task StartAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Service StartAsync called.");
        return Task.CompletedTask;
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Service StopAsync called.");
        return Task.CompletedTask;
    }
}

// Program.cs (또는 Startup.cs)
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

public class Program
{
    public static async Task Main(string[] args)
    {
        using IHost host = Host.CreateDefaultBuilder(args)
            .ConfigureServices(services =>
            {
                services.AddHostedService<MyLifecycleService>();
            })
            .Build();

        await host.RunAsync();
    }
}
```

**4. 코드 실행 결과 예시:**

콘솔 출력 (로깅 수준에 따라 다를 수 있음):

```
info: MyLifecycleService[0]
      Service is starting.
info: MyLifecycleService[0]
      Service StartAsync called.
info: MyLifecycleService[0]
      Service has started.
// ... (애플리케이션 실행 중) ...
info: MyLifecycleService[0]
      Service is stopping.
info: MyLifecycleService[0]
      Service StopAsync called.
info: MyLifecycleService[0]
      Service has stopped.
```

**요약:**

`IHostedLifecycleService`는 .NET에서 호스팅된 서비스의 생명주기를 보다 세밀하게 제어해야 할 때 매우 유용한 인터페이스입니다. 시작 및 종료 단계에서 추가적인 이벤트 핸들러를 제공하여, 서비스의 초기화 및 정리 작업을 보다 효율적으로 관리할 수 있게 해줍니다.


---
title: "DOTNET - .NET의 Microsoft Extensions Hosting"
date: 2025-09-17 21:03:27 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Microsoft, Extensions, Hosting]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Microsoft Extensions Hosting**

**1. 간단한 설명:**

Microsoft Extensions Hosting은 .NET 애플리케이션의 기본 아키텍처를 구성하는 데 사용되는 프레임워크입니다.  단순한 콘솔 앱부터 복잡한 웹 API, 백그라운드 서비스, 데스크톱 애플리케이션까지 다양한 유형의 애플리케이션에서 DI(Dependency Injection), 구성(Configuration), 로깅(Logging), 옵션(Options) 등의 기능을 중앙 집중적으로 관리할 수 있도록 해줍니다. 특히 .NET Aspire와 함께 사용될 때, 클라우드 네이티브 애플리케이션의 복잡성을 관리하는 데 핵심적인 역할을 합니다.  Hosting은 애플리케이션의 생명 주기를 제어하고, 다양한 서비스와 미들웨어를 통합하여 애플리케이션의 확장성과 유지보수성을 높입니다.  최근 트렌드는 .NET Aspire와의 연동을 통해 클라우드 네이티브 앱 개발을 더욱 용이하게 하고, 호스팅 환경 구성을 선언적으로 정의하여 코드 중복을 줄이고 재사용성을 높이는 방향으로 발전하고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs on .NET Generic Host:** [https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host](https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host)
*   **Microsoft Docs on Dependency Injection in .NET:** [https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection)
*   **Microsoft Docs on Configuration in .NET:** [https://learn.microsoft.com/en-us/dotnet/core/extensions/configuration](https://learn.microsoft.com/en-us/dotnet/core/extensions/configuration)
*   **Microsoft Docs on Logging in .NET:** [https://learn.microsoft.com/en-us/dotnet/core/extensions/logging](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging)
*   **.NET Aspire Documentation (Hosting Context):** [https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/hosting](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/hosting)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;

public class Program
{
    public static async Task Main(string[] args)
    {
        using IHost host = Host.CreateDefaultBuilder(args)
            .ConfigureAppConfiguration((hostingContext, config) =>
            {
                config.AddJsonFile("appsettings.json", optional: true, reloadOnChange: true);
                config.AddEnvironmentVariables(prefix: "APP_");
            })
            .ConfigureServices((context, services) =>
            {
                services.AddHostedService<Worker>();
                services.Configure<MyOptions>(context.Configuration.GetSection("MyOptions")); // Options Pattern 예시
            })
            .ConfigureLogging(logging =>
            {
                logging.AddConsole();
                logging.AddDebug();
            })
            .Build();

        await host.RunAsync();
    }
}

public class Worker : BackgroundService
{
    private readonly ILogger<Worker> _logger;

    public Worker(ILogger<Worker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);
            await Task.Delay(1000, stoppingToken);
        }
    }
}

public class MyOptions
{
    public string? Option1 { get; set; }
    public int Option2 { get; set; }
}
```

**4. 코드 실행 결과 예시:**

콘솔 애플리케이션을 실행하면 다음과 같은 출력을 볼 수 있습니다.

```
info: Worker[0]
      Worker running at: 2023-10-27T10:00:00.1234567+09:00
info: Worker[0]
      Worker running at: 2023-10-27T10:00:01.1234567+09:00
info: Worker[0]
      Worker running at: 2023-10-27T10:00:02.1234567+09:00
...
```

`appsettings.json` 파일 (있는 경우) 또는 환경 변수에 따라 구성된 옵션이 `MyOptions` 클래스에 바인딩되고, DI를 통해 `Worker` 클래스에서 사용할 수 있습니다.  로깅은 콘솔과 디버그 출력에 기록됩니다.  `.NET Aspire` 환경에서는 호스팅 구성이 더욱 간결해지며, 클라우드 리소스와의 통합이 쉬워집니다. 예를 들어, AppHost 프로젝트에서 선언적으로 서비스를 정의하고, 이를 Hosting 환경에 자동으로 연결할 수 있습니다.


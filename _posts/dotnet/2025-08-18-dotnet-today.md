---
title: "DOTNET - .NET의 Entity Framework Core의 Interceptors 활용"
date: 2025-08-18 21:03:03 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Entity, Framework, Core의, Interceptors, 활용]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Entity Framework Core의 Interceptors 활용**

**1. 간단한 설명:**

Entity Framework Core (EF Core) Interceptors는 EF Core가 데이터베이스와 상호 작용하는 동안 다양한 시점에서 코드를 실행할 수 있게 해주는 강력한 기능입니다.  데이터베이스 명령 실행 전후, 연결 열기/닫기 전후, 트랜잭션 관리 등 다양한 이벤트에 가로채기를 추가하여 로깅, 성능 측정, 명령 수정, 캐싱 등 다양한 작업을 수행할 수 있습니다. 이는 데이터베이스 상호 작용 로직을 애플리케이션 코드와 분리하여 유지보수성을 높이고, 횡단 관심사 (cross-cutting concerns)를 효과적으로 처리할 수 있도록 돕습니다.  EF Core 8에서는 Interceptors가 더욱 강력해졌으며, 복잡한 시나리오에 대한 지원이 향상되었습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - EF Core Interceptors:** [https://learn.microsoft.com/en-us/ef/core/logging-events-diagnostics/interceptors](https://learn.microsoft.com/en-us/ef/core/logging-events-diagnostics/interceptors)
*   **EF Core Power Tools:** (Interceptors를 쉽게 구현하고 관리하는 데 도움을 줄 수 있습니다.  공식 문서는 아니지만 유용한 도구입니다.) [https://marketplace.visualstudio.com/items?itemName=ErikEJ.EFCorePowerTools](https://marketplace.visualstudio.com/items?itemName=ErikEJ.EFCorePowerTools)
*   **Various blogs and articles on EF Core Interceptors:** 구글에서 "EF Core Interceptors"를 검색하면 많은 블로그 글과 예제를 찾을 수 있습니다. (예: "EF Core Interceptors tutorial")

**3. 간단한 코드 예시 (C#):**

다음은 데이터베이스 명령 실행 시간을 측정하는 간단한 Interceptor 예제입니다.

```csharp
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Diagnostics;
using System;
using System.Diagnostics;
using System.Threading;
using System.Threading.Tasks;

public class TimingInterceptor : DbCommandInterceptor
{
    private readonly ILogger<TimingInterceptor> _logger;
    private readonly Stopwatch _stopwatch;

    public TimingInterceptor(ILogger<TimingInterceptor> logger)
    {
        _logger = logger;
        _stopwatch = new Stopwatch();
    }

    public override InterceptionResult<DbDataReader> ReaderExecuting(
        DbCommand command,
        CommandEventData eventData,
        InterceptionResult<DbDataReader> result)
    {
        _stopwatch.Restart();
        return base.ReaderExecuting(command, eventData, result);
    }

    public override async ValueTask<InterceptionResult<DbDataReader>> ReaderExecutingAsync(
        DbCommand command,
        CommandEventData eventData,
        InterceptionResult<DbDataReader> result,
        CancellationToken cancellationToken = default)
    {
        _stopwatch.Restart();
        return await base.ReaderExecutingAsync(command, eventData, result, cancellationToken);
    }

    public override DbDataReader ReaderExecuted(
        DbCommand command,
        CommandExecutedEventData eventData,
        DbDataReader result)
    {
        _stopwatch.Stop();
        _logger.LogInformation($"Command '{command.CommandText}' executed in {_stopwatch.ElapsedMilliseconds}ms");
        return base.ReaderExecuted(command, eventData, result);
    }

    public override async ValueTask<DbDataReader> ReaderExecutedAsync(
        DbCommand command,
        CommandExecutedEventData eventData,
        DbDataReader result,
        CancellationToken cancellationToken = default)
    {
        _stopwatch.Stop();
        _logger.LogInformation($"Command '{command.CommandText}' executed in {_stopwatch.ElapsedMilliseconds}ms");
        return await base.ReaderExecutedAsync(command, eventData, result, cancellationToken);
    }
}

// DbContext 구성
public class MyDbContext : DbContext
{
    public MyDbContext(DbContextOptions<MyDbContext> options) : base(options)
    {
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.AddInterceptors(new TimingInterceptor(_logger)); // TimingInterceptor 등록
    }

    // ... DbSet 등 ...
}

// 로거를 주입받는 방법
public class SomeClass
{
    private readonly ILogger<SomeClass> _logger;
    private readonly MyDbContext _context;

    public SomeClass(ILogger<SomeClass> logger, MyDbContext context)
    {
        _logger = logger;
        _context = context;
    }

    public void SomeMethod()
    {
        // 데이터베이스 작업 수행
        var data = _context.SomeEntities.ToList();
    }
}
```

**4. 코드 실행 결과 예시:**

데이터베이스 쿼리가 실행될 때마다 다음과 같은 로그 메시지가 출력됩니다.

```
info: TimingInterceptor[0]
      Command 'SELECT [s].[Id], [s].[Name] FROM [SomeEntities] AS [s]' executed in 123ms
```

**설명:**

1.  **TimingInterceptor 클래스:** `DbCommandInterceptor`를 상속받아 구현됩니다.
2.  **ReaderExecuting/ReaderExecutingAsync:** 데이터베이스 명령 실행 전에 Stopwatch를 시작합니다.
3.  **ReaderExecuted/ReaderExecutedAsync:** 데이터베이스 명령 실행 후에 Stopwatch를 멈추고 실행 시간을 로그에 기록합니다.
4.  **DbContext 구성:** `OnConfiguring` 메서드에서 `AddInterceptors`를 사용하여 TimingInterceptor를 등록합니다.  ILogger를 주입받아 사용해야 하므로 DI 컨테이너에 등록하는 것이 좋습니다.
5.  **로거 주입 및 사용:** 실제 비즈니스 로직을 담은 클래스에서 `ILogger<SomeClass>` 와 `MyDbContext` 를 주입받아 사용합니다.

이 예제는 간단한 성능 측정 Interceptor이지만, 이 외에도 다양한 Interceptor를 구현하여 EF Core의 동작을 사용자 정의할 수 있습니다.  로깅, 캐싱, 명령 수정, 보안 검사 등에 Interceptors를 활용할 수 있습니다.


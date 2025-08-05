---
title: "DOTNET - .NET의 성능 분석 도구 PerfCollect 및 dotnet-counters 활용"
date: 2025-08-04 21:03:20 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 성능, 분석, 도구, PerfCollect, counters, 활용]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 성능 분석 도구 PerfCollect 및 dotnet-counters 활용**

**1. 간단한 설명:**

.NET 애플리케이션의 성능 문제를 진단하고 최적화하기 위해 PerfCollect 및 dotnet-counters와 같은 성능 분석 도구를 사용하는 것이 중요해지고 있습니다. PerfCollect는 Linux 환경에서 저수준 성능 데이터를 수집하는 데 유용한 스크립트이며, dotnet-counters는 .NET 애플리케이션의 실시간 성능 메트릭을 모니터링하는 CLI 도구입니다.  이 두 도구를 함께 사용하면 CPU 사용량, 메모리 할당, GC (Garbage Collection), JIT 컴파일 등에 대한 자세한 정보를 얻을 수 있어 성능 병목 현상을 식별하고 개선하는 데 도움을 줍니다. 특히 컨테이너 환경이나 클라우드 환경에서 실행되는 .NET 애플리케이션의 성능 모니터링 및 문제 해결에 유용합니다.  최근에는 Grafana, Prometheus와 같은 모니터링 시스템과의 연동도 강화되어 더욱 효율적인 성능 관리가 가능해지고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **PerfCollect:**
    *   [PerfCollect GitHub Repository](https://github.com/dotnet/performance/blob/main/docs/perfcollect.md): 공식 문서 및 사용법
    *   [Microsoft Docs - dotnet-counters](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-counters): dotnet-counters 설명
    *   [Performance Tips: dotnet-counters and dotnet-trace](https://devblogs.microsoft.com/dotnet/performance-tips-dotnet-counters-and-dotnet-trace/)

**3. 간단한 코드 예시 (C#):**

아래 코드는 예시일 뿐이며, 실제 성능 분석은 별도의 .NET 애플리케이션을 대상으로 수행해야 합니다. dotnet-counters는 실행 중인 .NET 프로세스의 PID를 인자로 받아 성능 메트릭을 모니터링합니다.

```csharp
// Example .NET application (simple CPU intensive task)
using System;
using System.Threading;

public class ExampleApp
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Starting ExampleApp...");

        while (true)
        {
            // Simulate CPU intensive work
            CalculatePrime(10000);
            Thread.Sleep(100);
        }
    }

    static bool IsPrime(int number)
    {
        if (number <= 1) return false;
        if (number <= 3) return true;

        if (number % 2 == 0 || number % 3 == 0) return false;

        for (int i = 5; i * i <= number; i = i + 6)
        {
            if (number % i == 0 || number % (i + 2) == 0)
                return false;
        }

        return true;
    }

    static void CalculatePrime(int limit)
    {
        for (int i = 2; i <= limit; i++)
        {
            IsPrime(i);
        }
    }
}
```

**4. 코드 실행 결과 예시:**

1.  `.NET 애플리케이션 실행:` 위 C# 코드를 컴파일하고 실행합니다. (예: `dotnet run`)
2.  `dotnet-counters 사용:`  별도의 터미널에서 dotnet-counters를 사용하여 실행 중인 애플리케이션의 PID를 지정하고 성능 메트릭을 모니터링합니다.
    ```bash
    dotnet-counters monitor --process-id <PID>
    ```

    `<PID>`는 실행 중인 .NET 애플리케이션의 프로세스 ID로 대체해야 합니다. (예: `dotnet-counters monitor --process-id 1234`)

3. 출력 결과 (예시):

```
Press p to pause, r to resume, q to quit.
  Metric                       Value
  --------------------------   -------
  cpu-usage (%)                15.53
  gen-0-gc-count               0
  gen-1-gc-count               0
  gen-2-gc-count               0
  heap-size (MB)               1.23
  working-set (MB)             25.67
```

PerfCollect는 Linux 환경에서 아래와 같이 사용할 수 있습니다. (관리자 권한 필요)

```bash
sudo ./perfcollect collect -d 30 -o /tmp/mytrace
```

위 명령어는 30초 동안 성능 데이터를 수집하여 `/tmp/mytrace` 디렉토리에 저장합니다.  수집된 데이터는 `dotnet-trace` 또는 Visual Studio Performance Profiler를 사용하여 분석할 수 있습니다.

**주의:**  PerfCollect는 리눅스 환경에서 사용 가능하며,  dotnet-counters는 Windows, macOS, Linux에서 모두 사용할 수 있습니다.  실행 권한 및 관리자 권한이 필요할 수 있습니다.


---
title: "DOTNET - .NET의 Metrics API (System.Diagnostics.Metrics)"
date: 2025-08-17 21:02:49 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Metrics, API, (System.Diagnostics.Metrics)]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Metrics API (System.Diagnostics.Metrics)**

**1. 간단한 설명:**

.NET 6부터 도입된 `System.Diagnostics.Metrics` API는 애플리케이션 성능 및 상태를 측정하고 수집하기 위한 표준화된 방법을 제공합니다. 기존의 카운터, 게이지, 히스토그램 등의 메트릭을 코드로 정의하고, 이를 다양한 모니터링 도구 (Prometheus, Grafana, Azure Monitor 등)로 내보내 애플리케이션의 동작을 심층적으로 분석하고 성능 문제를 진단하는 데 활용할 수 있습니다.  `System.Diagnostics.Metrics`는  OpenTelemetry 표준을 준수하여 다양한 백엔드 시스템과의 호환성을 보장합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - System.Diagnostics.Metrics:** [https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.metrics?view=net-7.0](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.metrics?view=net-7.0)
*   **.NET Blog - Introduction to Metrics in .NET 6:** [https://devblogs.microsoft.com/dotnet/introducing-metrics-in-dotnet-6/](https://devblogs.microsoft.com/dotnet/introducing-metrics-in-dotnet-6/)
*   **OpenTelemetry Official Website:** [https://opentelemetry.io/](https://opentelemetry.io/)

**3. 간단한 코드 예시 (C#):**

```csharp
using System;
using System.Diagnostics.Metrics;
using System.Threading;

public class ExampleMetrics
{
    private static readonly Meter MyMeter = new Meter("MyApplication.Metrics", "1.0");
    private static readonly Counter<long> RequestCounter = MyMeter.CreateCounter<long>("requests.count", "requests", "The number of requests received");
    private static readonly Histogram<double> RequestLatency = MyMeter.CreateHistogram<double>("requests.latency", "ms", "The latency of requests");

    public static void ProcessRequest()
    {
        // Record request start time
        var startTime = DateTime.UtcNow;

        // Simulate processing a request
        Thread.Sleep(new Random().Next(10, 100));

        // Calculate latency
        var latency = (DateTime.UtcNow - startTime).TotalMilliseconds;

        // Increment the request counter
        RequestCounter.Add(1);

        // Record the latency
        RequestLatency.Record(latency);
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("Starting metric generation...");

        for (int i = 0; i < 10; i++)
        {
            ProcessRequest();
            Thread.Sleep(500); // Simulate requests coming in every 0.5 seconds
        }

        Console.WriteLine("Metric generation complete.");

        // Keep the console window open to observe metrics if needed
        Console.ReadKey();
    }
}
```

**4. 코드 실행 결과 예시:**

이 코드를 직접 실행하면 콘솔에 별도의 결과가 출력되지는 않습니다.  대신,  `Meter` 객체를 생성하고, `Counter` 와 `Histogram` 메트릭을 정의하고 업데이트하여, 애플리케이션에서 메트릭 데이터를 생성합니다.  이 메트릭 데이터를 실제로 활용하려면, `MetricExporter`를 사용하여 Prometheus나 Azure Monitor와 같은 모니터링 시스템으로 데이터를 내보내야 합니다.

만약 Prometheus와 OpenTelemetry를 설정했다면, Prometheus UI에서 다음과 같은 이름으로 메트릭을 확인할 수 있습니다:

*   `myappication_metrics_requests_count`
*   `myappication_metrics_requests_latency`

그리고 Grafana와 같은 시각화 도구를 사용하여 해당 메트릭을 그래프로 표시하고 분석할 수 있습니다.

**추가 정보:**

*   **OpenTelemetry 설정:** 실제 애플리케이션에서 `System.Diagnostics.Metrics`를 사용하려면 OpenTelemetry SDK를 설치하고 구성하여 메트릭을 지정된 백엔드(예: Prometheus, Azure Monitor)로 내보내야 합니다.
*   **MetricExporter 구현:** 사용자 정의 메트릭을 특정 모니터링 시스템에 맞게 내보내려면,  `MetricExporter` 인터페이스를 구현해야 합니다.
*   **샘플 프로젝트:** Microsoft의 공식 GitHub 저장소에서 `System.Diagnostics.Metrics`를 사용하는 다양한 샘플 프로젝트를 찾아볼 수 있습니다.  "dotnet/runtime" 리포지토리를 검색하고 "Metrics" 키워드를 사용하여 관련 예제를 찾으십시오.


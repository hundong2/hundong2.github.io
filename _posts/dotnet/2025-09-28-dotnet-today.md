---
title: "DOTNET - .NET Aspire를 활용한 분산 애플리케이션의 Observability 향상"
date: 2025-09-28 21:03:01 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET, Aspire를, 활용한, 분산, 애플리케이션의, Observability, 향상]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET Aspire를 활용한 분산 애플리케이션의 Observability 향상**

**1. 간단한 설명:**
.NET Aspire는 마이크로 서비스 아키텍처를 쉽게 구축하고 배포, 관리할 수 있도록 도와주는 .NET 프레임워크입니다. 최근에는 .NET Aspire를 통해 구축된 분산 애플리케이션의 Observability를 더욱 향상시키는 데 초점이 맞춰지고 있습니다. 이는 애플리케이션의 상태, 성능, 동작을 더 잘 이해하고 문제를 신속하게 진단하고 해결하기 위한 노력의 일환입니다. 구체적으로는 OpenTelemetry를 활용하여 애플리케이션 전반의 메트릭, 로그, 트레이스를 수집하고, Grafana, Prometheus, Azure Monitor와 같은 도구를 통해 시각화하고 분석하는 기능이 강화되고 있습니다. 또한, .NET Aspire의 대시보드를 통해 더욱 직관적인 모니터링 환경을 제공하고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Aspire 공식 문서:** [https://learn.microsoft.com/ko-kr/dotnet/aspire/](https://learn.microsoft.com/ko-kr/dotnet/aspire/)
*   **OpenTelemetry:** [https://opentelemetry.io/](https://opentelemetry.io/)
*   **.NET 블로그 (Aspire 관련 게시물):** [https://devblogs.microsoft.com/dotnet/](https://devblogs.microsoft.com/dotnet/) (검색어로 "Aspire" 검색)
*   **Azure Monitor:** [https://azure.microsoft.com/ko-kr/products/monitor/](https://azure.microsoft.com/ko-kr/products/monitor/)
*   **Grafana:** [https://grafana.com/](https://grafana.com/)
*   **Prometheus:** [https://prometheus.io/](https://prometheus.io/)

**3. 간단한 코드 예시 (C#):**

```csharp
// Program.cs (ASP.NET Core Web API 프로젝트)
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

var builder = WebApplication.CreateBuilder(args);

// OpenTelemetry 구성 (메트릭, 트레이싱)
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics =>
    {
        metrics.SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("MyWebApi"));
        metrics.AddPrometheusExporter(); // Prometheus로 메트릭 내보내기
        metrics.AddMeter("Microsoft.AspNetCore.Hosting");
        metrics.AddMeter("Microsoft.AspNetCore.Server.Kestrel");
    })
    .WithTracing(tracing =>
    {
        tracing.SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("MyWebApi"));
        tracing.AddAspNetCoreInstrumentation();
        tracing.AddConsoleExporter(); // 콘솔에 트레이스 출력 (테스트용)
        tracing.AddOtlpExporter(); // Otlp exporter를 사용하여 Jaeger나 다른 백엔드로 전송
    });

builder.Services.AddControllers();

var app = builder.Build();

app.MapControllers();
app.MapPrometheusScrapingEndpoint();

app.Run();
```

**4. 코드 실행 결과 예시:**

이 코드를 실행하면 ASP.NET Core Web API 프로젝트가 OpenTelemetry를 사용하여 메트릭과 트레이스를 수집합니다.

*   **Prometheus:**  `http://localhost:<포트>/metrics` 엔드포인트에서 Prometheus 형식으로 메트릭 데이터를 확인할 수 있습니다.
*   **콘솔 출력 (트레이싱):**  트레이스 데이터가 콘솔에 출력됩니다.
*   **OtlpExporter:** OtlpExporter가 설정되어 있다면 지정된 Jaeger 또는 다른 백엔드에 트레이스 데이터가 전송됩니다.  Jaeger UI에서 트레이스를 시각화할 수 있습니다.
*   **.NET Aspire 대시보드:** .NET Aspire 대시보드 (아직 완전히 통합되지 않았을 수 있음, 향후 업데이트 기대)에서 애플리케이션의 전반적인 상태 및 메트릭을 시각적으로 확인할 수 있습니다.

**참고:**  위 예제는 기본적인 OpenTelemetry 설정이며, 실제 환경에서는 Jaeger, Azure Monitor 등 다양한 백엔드에 연결하고, 추가적인 구성 옵션을 설정해야 할 수 있습니다.  또한 .NET Aspire의 Observability 기능은 계속 진화하고 있으므로 최신 문서를 참고하는 것이 좋습니다.


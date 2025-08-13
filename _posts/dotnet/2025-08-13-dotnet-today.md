---
title: "DOTNET - .NET의 One-Click Publish to Azure Container Apps"
date: 2025-08-13 21:03:02 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, One, Click, Publish, to, Azure, Container, Apps]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 One-Click Publish to Azure Container Apps**

**1. 간단한 설명:**

Visual Studio 2022 버전 17.9부터 Azure Container Apps에 대한 One-Click Publish 기능이 추가되었습니다. 이 기능은 .NET 애플리케이션을 컨테이너화하고 Azure Container Apps 환경에 배포하는 과정을 획기적으로 간소화합니다. 개발자는 복잡한 Azure CLI 명령이나 Dockerfile 작성 없이, Visual Studio 내에서 몇 번의 클릭만으로 애플리케이션을 배포할 수 있습니다.  이 기능은 개발 생산성을 향상시키고, 컨테이너화 및 클라우드 네이티브 기술 도입의 장벽을 낮추는 데 기여합니다. 또한, Visual Studio는 자동으로 Dockerfile을 생성하고, 컨테이너 이미지를 빌드하고, Azure Container Registry에 푸시한 다음, Azure Container Apps에 배포하는 모든 단계를 처리합니다. Azure Container Apps는 서버리스 컴퓨팅 플랫폼으로, 컨테이너화된 애플리케이션을 쉽게 배포하고 확장할 수 있도록 지원합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET 블로그:** [https://devblogs.microsoft.com/dotnet/one-click-publish-to-azure-container-apps/](https://devblogs.microsoft.com/dotnet/one-click-publish-to-azure-container-apps/)
*   **Azure Container Apps 공식 문서:** [https://learn.microsoft.com/en-us/azure/container-apps/](https://learn.microsoft.com/en-us/azure/container-apps/)

**3. 간단한 코드 예시 (C#):**

실제 코드를 보여주는 것은 Visual Studio IDE를 통해 이루어지기 때문에,  간단한 ASP.NET Core 웹 API 프로젝트를 예시로 들어보겠습니다.  이 코드는 Azure Container Apps에 배포될 API의 기본 구조를 보여줍니다.

```csharp
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();

// Sample Controller
[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    private static readonly string[] Summaries = new[]
    {
        "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

    private readonly ILogger<WeatherForecastController> _logger;

    public WeatherForecastController(ILogger<WeatherForecastController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetWeatherForecast")]
    public IEnumerable<WeatherForecast> Get()
    {
        return Enumerable.Range(1, 5).Select(index => new WeatherForecast
        {
            Date = DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            TemperatureC = Random.Shared.Next(-20, 55),
            Summary = Summaries[Random.Shared.Next(Summaries.Length)]
        })
        .ToArray();
    }
}

public class WeatherForecast
{
    public DateOnly Date { get; set; }
    public int TemperatureC { get; set; }
    public string? Summary { get; set; }
}

```

**4. 코드 실행 결과 예시:**

위 API를 Azure Container Apps에 배포한 후, 해당 앱의 URL에 접근하면 다음과 같은 JSON 응답을 받을 수 있습니다.  (실제 값은 다를 수 있습니다.)

```json
[
    {
        "date": "2024-01-02",
        "temperatureC": 15,
        "summary": "Cool"
    },
    {
        "date": "2024-01-03",
        "temperatureC": -5,
        "summary": "Freezing"
    },
    {
        "date": "2024-01-04",
        "temperatureC": 28,
        "summary": "Warm"
    },
    {
        "date": "2024-01-05",
        "temperatureC": 8,
        "summary": "Chilly"
    },
    {
        "date": "2024-01-06",
        "temperatureC": 32,
        "summary": "Hot"
    }
]
```

Visual Studio 2022 내에서 Azure Container Apps에 게시할 때 Visual Studio가 생성한 컨테이너 이미지의 로그와, Azure Container Apps에 성공적으로 배포되었음을 나타내는 로그를 확인할 수 있습니다. Azure Portal에서도 배포된 Container App의 상태와 로그를 확인할 수 있습니다.


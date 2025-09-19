---
title: "DOTNET - .NET의 Configuration Validation"
date: 2025-09-19 21:03:21 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Configuration, Validation]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Configuration Validation**

**1. 간단한 설명:**

.NET Configuration Validation은 애플리케이션 구성 파일(예: appsettings.json)에 정의된 설정 값들이 예상대로 유효한지 확인하는 프로세스입니다. 이전에는 개발자가 수동으로 구성 값을 검증하거나 사용자 정의 유효성 검사 로직을 작성해야 했습니다. 하지만 최신 .NET 버전에서는 데이터 어노테이션(Data Annotations)과 IOptions 인터페이스를 활용하여 구성 값을 쉽게 검증할 수 있는 기능이 강화되었습니다. 이를 통해 잘못된 구성으로 인해 발생하는 런타임 오류를 방지하고 애플리케이션의 안정성을 높일 수 있습니다. 또한, FluentValidation과 같은 라이브러리를 활용하여 더 복잡하고 사용자 정의된 유효성 검사 규칙을 적용할 수도 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - Options pattern in ASP.NET Core:** [https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options?view=aspnetcore-8.0)
*   **Microsoft Docs - Data Annotations Attributes:** [https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations?view=net-8.0)
*   **FluentValidation:** [https://fluentvalidation.net/](https://fluentvalidation.net/)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System.ComponentModel.DataAnnotations;

// Configuration 설정 클래스 정의
public class AppSettings
{
    [Required(ErrorMessage = "Name is required.")]
    [StringLength(50, ErrorMessage = "Name cannot exceed 50 characters.")]
    public string Name { get; set; }

    [Range(1, 100, ErrorMessage = "Age must be between 1 and 100.")]
    public int Age { get; set; }

    [EmailAddress(ErrorMessage = "Invalid Email Address.")]
    public string Email { get; set; }
}

public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddValidatedSettings<T>(this IServiceCollection services, IConfiguration configuration, string sectionName) where T : class
    {
        services.Configure<T>(configuration.GetSection(sectionName));

        services.AddOptions<T>()
            .Bind(configuration.GetSection(sectionName))
            .ValidateDataAnnotations()
            .ValidateOnStart(); // 애플리케이션 시작 시 유효성 검사 수행

        return services;
    }
}

// Program.cs 또는 Startup.cs에서 사용 예시
public class Program
{
    public static void Main(string[] args)
    {
        var builder = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true);

        IConfigurationRoot configuration = builder.Build();

        var services = new ServiceCollection();

        // 설정 클래스 등록 및 유효성 검사 활성화
        services.AddValidatedSettings<AppSettings>(configuration, "AppSettings");

        // IOptions<AppSettings>를 통해 설정 값에 접근
        var serviceProvider = services.BuildServiceProvider();
        var settings = serviceProvider.GetRequiredService<IOptions<AppSettings>>().Value;

        Console.WriteLine($"Name: {settings.Name}");
        Console.WriteLine($"Age: {settings.Age}");
        Console.WriteLine($"Email: {settings.Email}");
    }
}

```

**appsettings.json 예시:**

```json
{
  "AppSettings": {
    "Name": "John Doe",
    "Age": 30,
    "Email": "john.doe@example.com"
  }
}
```

**4. 코드 실행 결과 예시:**

만약 `appsettings.json` 파일이 위의 예시와 같이 유효하다면, 콘솔에는 다음과 같은 결과가 출력됩니다.

```
Name: John Doe
Age: 30
Email: john.doe@example.com
```

만약 `appsettings.json` 파일에 유효하지 않은 값이 있다면, 애플리케이션 시작 시 `DataAnnotationsValidationException`이 발생하여 오류 메시지를 확인할 수 있습니다. 예를 들어, Name 필드를 비워두면 "Name is required."라는 오류 메시지가 표시됩니다.


---
title: "DOTNET - .NET의 Keyed Services"
date: 2025-09-15 21:02:55 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Keyed, Services]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Keyed Services**

**1. 간단한 설명:**

Keyed Services는 .NET 7부터 도입된 기능으로, Dependency Injection (DI) 컨테이너에 등록된 서비스들을 키(Key)를 사용하여 구별하고 주입할 수 있도록 해줍니다. 기존에는 타입(Type) 기반으로만 서비스를 구분했기 때문에, 동일한 인터페이스를 구현하는 여러 서비스가 필요한 경우 어려움이 있었습니다. Keyed Services를 사용하면 명확한 키를 통해 원하는 서비스를 선택적으로 주입할 수 있어, DI 컨테이너의 유연성과 유지보수성을 향상시킬 수 있습니다. 이는 특히 다양한 전략 패턴 구현, 다중 데이터베이스 연결 관리, 여러 버전의 API 지원 등과 같은 시나리오에서 유용합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs:** [https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-keyedad-services](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-keyedad-services)
*   **ASP.NET Core Updates in .NET 7:** [https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-dotnet-7/#keyed-services](https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-dotnet-7/#keyed-services)
*   **Keyed Dependency Injection in .NET 7:** [https://andrewlock.net/understanding-keyed-dependency-injection-in-dotnet-6/](https://andrewlock.net/understanding-keyed-dependency-injection-in-dotnet-6/) (Andrew Lock 블로그, .NET 6 기준으로 작성되었지만 개념은 동일)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.Extensions.DependencyInjection;

public interface IMessageWriter
{
    void Write(string message);
}

public class ConsoleMessageWriter : IMessageWriter
{
    public void Write(string message) => Console.WriteLine($"Console: {message}");
}

public class FileMessageWriter : IMessageWriter
{
    public void Write(string message) => File.WriteAllText("message.txt", $"File: {message}");
}

public class MessageProcessor
{
    private readonly IMessageWriter _writer;

    public MessageProcessor([FromKeyedServices("console")] IMessageWriter writer)
    {
        _writer = writer;
    }

    public void ProcessMessage(string message)
    {
        _writer.Write(message);
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        var services = new ServiceCollection();

        services.AddKeyedSingleton<IMessageWriter, ConsoleMessageWriter>("console");
        services.AddKeyedSingleton<IMessageWriter, FileMessageWriter>("file");
        services.AddTransient<MessageProcessor>();

        var serviceProvider = services.BuildServiceProvider();

        var processor = serviceProvider.GetRequiredService<MessageProcessor>();
        processor.ProcessMessage("Hello, Keyed Services!");
    }
}
```

**4. 코드 실행 결과 예시:**

콘솔에 다음과 같이 출력됩니다.

```
Console: Hello, Keyed Services!
```

그리고 `message.txt` 파일이 생성되고 다음 내용이 저장됩니다 (FileMessageWriter가 주입되었다면).

```
File: Hello, Keyed Services!
```
본 예시에서는 "console" 키를 사용하여 ConsoleMessageWriter를 주입했지만, 만약 `[FromKeyedServices("file")]`을 사용했다면 FileMessageWriter가 주입되어 message.txt 파일에 결과가 저장될 것입니다.


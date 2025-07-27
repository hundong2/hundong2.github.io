---
title: "DOTNET - .NET의 SignalR Backplane을 활용한 실시간 분산 애플리케이션 확장"
date: 2025-07-27 21:03:04 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, SignalR, Backplane을, 활용한, 실시간, 분산, 애플리케이션, 확장]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 SignalR Backplane을 활용한 실시간 분산 애플리케이션 확장**

**1. 간단한 설명:**

.NET SignalR은 실시간 양방향 통신을 쉽게 구현할 수 있도록 해주는 라이브러리입니다. 하지만 하나의 서버 인스턴스만으로는 대규모 사용자 트래픽을 감당하기 어려울 수 있습니다. SignalR Backplane은 여러 서버 인스턴스 간에 메시지를 동기화하여, 수평적 확장을 가능하게 해줍니다. 즉, 사용자가 어떤 서버에 연결되어 있든 상관없이 모든 사용자에게 동일한 실시간 정보를 제공할 수 있습니다.  주로 Redis, Azure Service Bus, 또는 SQL Server를 Backplane으로 활용합니다.  이를 통해 웹 소켓 연결의 상태를 여러 서버에서 공유하고, 특정 사용자에게 메시지를 보낼 때, 해당 사용자가 어떤 서버에 연결되어 있는지 몰라도 메시지를 안정적으로 전달할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft 공식 문서 - SignalR Scaleout with Azure Service Bus:** [https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-8.0&tabs=azure-service-bus](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-8.0&tabs=azure-service-bus)
*   **Microsoft 공식 문서 - SignalR Scaleout with Redis:** [https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-8.0&tabs=redis](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-8.0&tabs=redis)
*   **Microsoft 공식 문서 - SignalR Scaleout with SQL Server:** [https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-8.0&tabs=sql-server](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-8.0&tabs=sql-server)

**3. 간단한 코드 예시 (C#):**

```csharp
// Program.cs (ASP.NET Core)

using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.SignalR;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

// SignalR 서비스 추가
builder.Services.AddSignalR()
    // Redis Backplane 사용 (Azure Redis Cache 연결 문자열로 대체)
    .AddStackExchangeRedis("your_redis_connection_string", options => {
        options.ConfigurationOptions.AbortOnConnectFail = false; // Redis 연결 실패 시 재시도
    });

// CORS 설정 (개발 환경에 따라 조정)
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(
        policy =>
        {
            policy.WithOrigins("http://localhost:3000") // 클라이언트 앱 주소
                .AllowAnyMethod()
                .AllowAnyHeader()
                .AllowCredentials(); // 자격 증명 허용 (웹 소켓 연결에 필요)
        });
});


var app = builder.Build();

// 개발 환경에서 Swagger 추가
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}

// CORS 사용
app.UseCors();

app.UseRouting();

app.UseEndpoints(endpoints =>
{
    endpoints.MapHub<ChatHub>("/chatHub");
});

app.Run();


// ChatHub.cs
using Microsoft.AspNetCore.SignalR;

public class ChatHub : Hub
{
    public async Task SendMessage(string user, string message)
    {
        await Clients.All.SendAsync("ReceiveMessage", user, message);
    }
}
```

**4. 코드 실행 결과 예시:**

위 코드를 실행하고, 클라이언트 (예: JavaScript/TypeScript 기반 React 앱)에서 SignalR 연결을 맺고 메시지를 보내면, Redis Backplane을 통해 연결된 모든 서버의 클라이언트들에게 메시지가 실시간으로 전달됩니다.

예를 들어, 두 개의 ASP.NET Core 서버 인스턴스를 실행하고 Redis Backplane을 구성한 후, 한 서버에서 "User1"이 "Hello from Server 1!"이라는 메시지를 보내면, 다른 서버에 연결된 클라이언트에서도 해당 메시지를 즉시 받을 수 있습니다.  콘솔 또는 브라우저 개발자 도구에서 "ReceiveMessage: User1 says Hello from Server 1!" 과 같은 메시지를 확인할 수 있습니다.  서버를 여러 개로 늘려도 동일한 방식으로 작동하며, Redis가 메시지 브로커 역할을 수행하여 메시지 일관성을 보장합니다.


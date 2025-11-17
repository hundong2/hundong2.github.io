---
title: "DOTNET - .NET의 Application-Layer Protocol Negotiation (ALPN) 우선 순위 설정"
date: 2025-11-17 21:03:34 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Application, Layer, Protocol, Negotiation, (ALPN), 우선, 순위, 설정]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Application-Layer Protocol Negotiation (ALPN) 우선 순위 설정**

**1. 간단한 설명:**
ALPN (Application-Layer Protocol Negotiation)은 TLS 핸드셰이크 과정에서 클라이언트와 서버가 사용할 HTTP 버전을 협상하는 기술입니다. .NET 8부터는 Kestrel 웹 서버에서 ALPN 우선 순위를 설정할 수 있게 되었습니다. 이는 HTTP/3를 지원하는 서버에서 클라이언트가 HTTP/3를 선호하도록 설정하여 성능 향상을 도모할 수 있게 해줍니다. 기존에는 서버가 ALPN 목록의 순서를 결정했지만, 이제 애플리케이션에서 클라이언트가 HTTP/3를 먼저 시도하도록 명시적으로 구성할 수 있습니다. HTTP/3의 장점(향상된 신뢰성, 낮은 지연 시간 등)을 최대한 활용하기 위해 ALPN 협상 프로세스를 제어하는 것이 중요하며, 이 기능을 통해 개발자는 특정 환경에 맞춰 애플리케이션의 성능을 미세 조정할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft .NET 블로그:** (.NET 8 관련 ALPN 설정 정보가 포함된 내용을 찾아보세요.)
*   **ASP.NET Core 공식 문서:** (Kestrel configuration 관련 섹션에서 ALPN 우선 순위 설정 방법을 찾아보세요.)
*   **HTTP/3 관련 RFC:** (HTTP/3 및 QUIC 프로토콜에 대한 이해를 돕습니다.)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Server.Kestrel.Core;
using Microsoft.Extensions.Hosting;

public class Program
{
    public static void Main(string[] args)
    {
        CreateHostBuilder(args).Build().Run();
    }

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.ConfigureKestrel(serverOptions =>
                {
                    serverOptions.ConfigureEndpointDefaults(listenOptions =>
                    {
                        // HTTP/3 우선 순위 설정 (HTTP/3를 먼저 시도)
                        listenOptions.Protocols = HttpProtocols.Http1AndHttp2AndHttp3;
                        listenOptions.AlpnProtocols = new List<SslApplicationProtocol> {
                            SslApplicationProtocol.Http3,
                            SslApplicationProtocol.Http2,
                            SslApplicationProtocol.Http11
                        };
                    });
                });
                webBuilder.UseStartup<Startup>();
            });
}
```

**4. 코드 실행 결과 예시:**

이 코드를 실행하면 Kestrel 서버는 TLS 핸드셰이크 과정에서 클라이언트에게 HTTP/3를 가장 먼저 제안합니다. 클라이언트가 HTTP/3를 지원한다면, HTTP/3 연결이 설정됩니다. 만약 클라이언트가 HTTP/3를 지원하지 않는다면, HTTP/2나 HTTP/1.1과 같은 이전 버전의 HTTP로 연결이 설정됩니다.  실질적인 동작 확인은 브라우저의 개발자 도구 또는 `curl` 명령어 등을 사용하여 HTTP 버전 협상 결과를 확인해야 합니다.  (예: `curl -v --http3 https://your-server-address`)


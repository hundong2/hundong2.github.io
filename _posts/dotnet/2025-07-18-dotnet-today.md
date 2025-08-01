---
title: "DOTNET - .NET의 gRPC JSON transcoding"
date: 2025-07-18 21:03:06 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, ".NET의", gRPC, JSON, transcoding]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 gRPC JSON transcoding**

**1. 간단한 설명:**

gRPC JSON transcoding은 gRPC 서비스를 개발하고 HTTP JSON API를 통해 노출할 수 있도록 해주는 기술입니다. 즉, 하나의 gRPC 서비스 정의로부터 gRPC와 REST API를 동시에 제공할 수 있습니다.  gRPC의 효율성과 구조화된 메시지 정의의 장점은 유지하면서, HTTP 클라이언트가 쉽게 접근할 수 있도록 JSON 형태로 요청을 받고 응답을 변환해줍니다. 이는 클라이언트 호환성을 높이고 API 개발 및 관리를 간소화하는 데 도움이 됩니다. 예를 들어, gRPC를 지원하지 않는 웹 브라우저나 모바일 앱에서도 같은 서비스를 사용할 수 있게 됩니다.  .NET 7부터 이 기능이 더욱 개선되었고, .NET 8에서는 더욱 향상된 성능과 기능들을 제공합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - gRPC JSON transcoding in ASP.NET Core gRPC apps:** [https://learn.microsoft.com/en-us/aspnet/core/grpc/json-transcoding?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/grpc/json-transcoding?view=aspnetcore-8.0)
*   **ASP.NET Core gRPC JSON transcoding example:** [https://github.com/grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) (gRPC Gateway, 유사한 기능을 제공하는 외부 프로젝트)

**3. 간단한 코드 예시 (C#):**

```csharp
// .proto 파일 (예시: Greeter.proto)
syntax = "proto3";

package Greeter;

service GreeterService {
  rpc SayHello (HelloRequest) returns (HelloReply) {
     option (google.api.http) = {
      get: "/v1/greeter/{name}"
    };
  }
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}

// GreeterService.cs
using Grpc.Core;
using Greeter;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Authentication.JwtBearer;

namespace GrpcService.Services;

[Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme)]
public class GreeterService : Greeter.GreeterService.GreeterServiceBase
{
    private readonly ILogger<GreeterService> _logger;
    public GreeterService(ILogger<GreeterService> logger)
    {
        _logger = logger;
    }

    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloReply
        {
            Message = "Hello " + request.Name
        });
    }
}

// Program.cs (ASP.NET Core)
using GrpcService.Services;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi.Models;
using System.Text;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddGrpc();

builder.Services.AddGrpcReflection();

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidAudience = builder.Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Key"]))
        };
    });

builder.Services.AddAuthorization();

builder.Services.AddSwaggerGen(opt =>
{
    opt.SwaggerDoc("v1", new OpenApiInfo { Title = "MyAPI", Version = "v1" });
    opt.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        In = ParameterLocation.Header,
        Description = "Please enter token",
        Name = "Authorization",
        Type = SecuritySchemeType.Http,
        BearerFormat = "JWT",
        Scheme = "bearer"
    });

    opt.AddSecurityRequirement(new OpenApiSecurityRequirement
    {
        {
            new OpenApiSecurityScheme
            {
                Reference = new OpenApiReference
                {
                    Type = ReferenceType.SecurityScheme,
                    Id = "Bearer"
                }
            },
            new string[] {}
        }
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.UseGrpcWeb(new GrpcWebOptions { DefaultEnabled = true });
}
else
{
    app.UseHttpsRedirection();
}

app.UseRouting();

app.UseAuthentication();
app.UseAuthorization();

app.MapGrpcService<GreeterService>();

app.MapGrpcReflectionService();

app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
```

**4. 코드 실행 결과 예시:**

1.  **gRPC 요청:** gRPC 클라이언트를 사용하여 `SayHello` 메서드를 호출하면, gRPC 프로토콜로 메시지가 전달되고 "Hello [Name]"이라는 응답을 받습니다.

2.  **HTTP 요청 (JSON transcoding):**  `/v1/greeter/{name}`으로 HTTP GET 요청을 보내면, 서버는 gRPC JSON transcoding을 통해 요청을 gRPC 호출로 변환하고, 결과를 JSON 형태로 응답합니다.  예를 들어, `/v1/greeter/World`로 요청하면 다음과 같은 JSON 응답을 받게 됩니다.

```json
{
  "message": "Hello World"
}
```

**주의사항:**

*   `.proto` 파일에 `google.api.http` 옵션을 사용하여 HTTP 메서드와 경로를 지정해야 합니다.
*   ASP.NET Core 프로젝트에서 gRPC 서비스와 JSON transcoding을 활성화해야 합니다.
*   정확한 설정 및 사용법은 Microsoft Docs의 gRPC JSON transcoding 문서를 참고하는 것이 좋습니다.


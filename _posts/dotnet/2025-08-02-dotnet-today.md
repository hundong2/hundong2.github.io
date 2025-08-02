---
title: "DOTNET - .NET의 Entity Framework Core의 Compiled Models"
date: 2025-08-02 21:02:57 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Entity, Framework, Core의, Compiled, Models]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Entity Framework Core의 Compiled Models**

**1. 간단한 설명:**

Entity Framework Core (EF Core)의 Compiled Models은 EF Core가 런타임에 모델을 생성하는 대신, 빌드 시점에 미리 컴파일된 모델을 사용하는 방식입니다.  일반적으로 EF Core는 애플리케이션 시작 시 데이터베이스 스키마를 기반으로 모델을 생성하고 캐싱합니다. 그러나 Compiled Models을 사용하면 모델 생성 단계를 빌드 시간으로 옮겨, 애플리케이션 시작 시간을 단축하고 런타임 성능을 개선할 수 있습니다. 특히 모델이 복잡하고 많은 엔티티 및 관계를 포함하는 경우에 효과적입니다. EF Core 7부터 정식으로 지원되며, EF Core 8에서는 더욱 개선되었습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

* **Microsoft Docs - EF Core Compiled Models:** [https://learn.microsoft.com/en-us/ef/core/performance/compiled-models](https://learn.microsoft.com/en-us/ef/core/performance/compiled-models)
* **EF Core 7 What's New - Compiled Models:** (EF Core 7에 소개된 기능) - 웹 검색을 통해 찾아보세요.  Microsoft Docs에 EF Core 7의 "What's New" 페이지를 검색하거나 관련 블로그 게시글을 찾아볼 수 있습니다.
* **EF Core 8 What's New:** (EF Core 8에 추가적인 개선 사항) - 웹 검색을 통해 찾아보세요.  Microsoft Docs에 EF Core 8의 "What's New" 페이지를 검색하거나 관련 블로그 게시글을 찾아볼 수 있습니다.

**3. 간단한 코드 예시 (C#):**

먼저 EF Core 프로젝트에 `Microsoft.EntityFrameworkCore.Design` 패키지를 설치해야 합니다.

```csharp
// 1. DbContext 클래스 정의
public class MyContext : DbContext
{
    public DbSet<Blog> Blogs { get; set; }
    public DbSet<Post> Posts { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Data Source=blogging.db");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Blog>()
            .HasMany(b => b.Posts)
            .WithOne(p => p.Blog)
            .HasForeignKey(p => p.BlogId);
    }
}

public class Blog
{
    public int BlogId { get; set; }
    public string Url { get; set; }
    public List<Post> Posts { get; set; }
}

public class Post
{
    public int PostId { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }
    public int BlogId { get; set; }
    public Blog Blog { get; set; }
}

// 2. 모델 컴파일 (명령줄 또는 터미널 사용)
// dotnet ef migrations add InitialCreate
// dotnet ef database update
// dotnet ef dbcontext optimize --output-dir CompiledModels
```

위 명령어를 실행하면 `CompiledModels` 디렉토리에 컴파일된 모델 관련 코드가 생성됩니다.  이제 DbContext를 사용하는 코드를 수정하여 컴파일된 모델을 사용하도록 변경합니다.

```csharp
using Microsoft.EntityFrameworkCore;

public class MyContext : DbContext
{
    public DbSet<Blog> Blogs { get; set; }
    public DbSet<Post> Posts { get; set; }

    public MyContext(DbContextOptions<MyContext> options) : base(options)
    {
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Blog>()
            .HasMany(b => b.Posts)
            .WithOne(p => p.Blog)
            .HasForeignKey(p => p.BlogId);
    }
}


// Startup.cs 또는 Program.cs에서
using Microsoft.EntityFrameworkCore;

public class Program
{
    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        // 컴파일된 모델 사용 설정
        builder.Services.AddDbContext<MyContext>(options =>
            options.UseSqlite("Data Source=blogging.db",
                              b => b.UseModel(MyContextModel.Instance))); // MyContextModel은 CompiledModels 디렉토리에 생성된 클래스입니다.

        // ... 나머지 설정
        var app = builder.Build();
        // ... 나머지 설정
        app.Run();
    }
}

```

**4. 코드 실행 결과 예시:**

컴파일된 모델을 사용하면 애플리케이션 시작 시 DbContext의 초기화 시간이 크게 줄어듭니다. 특히 대규모 모델에서는 그 효과가 더욱 두드러집니다.  Visual Studio의 진단 도구 또는 로깅을 통해 시작 시간의 변화를 확인할 수 있습니다.  성능 테스트를 통해 실제로 얼마나 개선되었는지 측정하는 것이 좋습니다. 예를 들어, 동일한 코드를 컴파일된 모델을 사용하지 않은 경우와 사용한 경우 각각 실행하고 시작 시간을 비교할 수 있습니다.


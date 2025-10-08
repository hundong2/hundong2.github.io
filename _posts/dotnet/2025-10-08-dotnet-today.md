---
title: "DOTNET - .NET의 Blazor United"
date: 2025-10-08 21:03:33 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Blazor, United]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Blazor United**

**1. 간단한 설명:**

Blazor United는 ASP.NET Core 8에서 도입된 실험적인 기능으로, Blazor Server와 Blazor WebAssembly를 단일 프로그래밍 모델로 통합하는 것을 목표로 합니다.  이 기술은 클라이언트와 서버 간의 명확한 경계를 허물고, 개발자가 사용자 인터랙션 및 렌더링 방식을 유연하게 선택할 수 있도록 해줍니다.  개발자는 페이지별 또는 컴포넌트별로 렌더링 모드를 설정하여 최적의 성능과 사용자 경험을 제공할 수 있습니다. 예를 들어, 초기 로딩 속도가 중요한 페이지는 서버 렌더링을 사용하고, 사용자 인터랙션이 많은 컴포넌트는 WebAssembly에서 실행하도록 구성할 수 있습니다. Blazor United는 .NET 8의 가장 큰 혁신 중 하나이며, 웹 개발 패러다임을 변화시킬 잠재력을 가지고 있습니다. 정식 명칭은 **Blazor 통합 렌더링 모델**입니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **ASP.NET Core 업데이트 (영문):** [https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-dotnet-8/](https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-dotnet-8/) (Blazor 섹션 참조)
*   **MSDN Blazor 공식 문서:**  [https://learn.microsoft.com/ko-kr/aspnet/core/blazor/?view=aspnetcore-8.0](https://learn.microsoft.com/ko-kr/aspnet/core/blazor/?view=aspnetcore-8.0) (Blazor 통합 렌더링 모델 관련 섹션 업데이트 예상)
*   **초기 실험 단계 관련 블로그:** (Blazor United의 초기 실험적인 모습에 대한 정보) [https://blog.stevensanderson.com/2023/04/25/blazor-in-net-8-preview-unified-web-ui/](https://blog.stevensanderson.com/2023/04/25/blazor-in-net-8-preview-unified-web-ui/)

**3. 간단한 코드 예시 (C#):**

```csharp
@page "/"
@rendermode InteractiveAuto

<h1>Hello, world!</h1>

<p>Welcome to your new app.</p>

<SurveyPrompt Title="How is Blazor working for you?" />

@code {
    // InteractiveAuto는 서버와 WebAssembly 중 적절한 렌더링 방식을 자동으로 선택합니다.
}
```

**4. 코드 실행 결과 예시:**

브라우저에서 페이지를 처음 로드할 때, 서버에서 렌더링된 HTML이 먼저 표시됩니다. 이후 Blazor WebAssembly 런타임이 로드되면, 컴포넌트가 WebAssembly에서 실행되어 사용자 인터랙션을 처리합니다.  InteractiveAuto 렌더 모드를 사용하면 초기 로딩 속도와 클라이언트 측의 풍부한 사용자 경험을 모두 얻을 수 있습니다. 만약 `InteractiveServer`로 설정한다면 서버에서 모든 렌더링을 처리하고, `InteractiveWebAssembly`로 설정한다면 WebAssembly에서 모든 렌더링을 처리합니다. 이 렌더링 모드는 페이지 단위 뿐만 아니라 컴포넌트 단위로 설정이 가능합니다.


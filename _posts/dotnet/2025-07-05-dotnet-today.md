---
title: "DOTNET - Semantic Kernel"
date: 2025-07-05 21:03:01 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, Semantic, Kernel]
---

## 오늘의 DOTNET 최신 기술 트렌드: **Semantic Kernel**

**1. 간단한 설명:**

Semantic Kernel은 Microsoft에서 개발한 오픈 소스 SDK로, 개발자가 AI 모델(특히 대규모 언어 모델, LLM)을 기존 애플리케이션에 통합하는 것을 간소화합니다. 단순히 LLM을 호출하는 것을 넘어, 플러그인을 통해 LLM 기능을 확장하고, 플래너를 통해 LLM을 활용한 복잡한 작업 흐름을 자동화하는 기능을 제공합니다. 이를 통해 LLM을 마치 기존 코드와 통합된 것처럼 사용할 수 있으며, 자연어 기반의 인터페이스를 쉽게 구축할 수 있습니다. 예를 들어, 이메일 요약, 콘텐츠 생성, 데이터 분석, 코드 생성 등 다양한 작업을 자동화할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Semantic Kernel GitHub:** [https://github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)
*   **Semantic Kernel 공식 문서:** [https://learn.microsoft.com/en-us/semantic-kernel/](https://learn.microsoft.com/en-us/semantic-kernel/)
*   **Microsoft .NET 블로그 - Semantic Kernel 관련 글:** [https://devblogs.microsoft.com/dotnet/introducing-semantic-kernel-openai-sdk-for-net/](https://devblogs.microsoft.com/dotnet/introducing-semantic-kernel-openai-sdk-for-net/)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

// Kernel 초기화
KernelBuilder builder = new KernelBuilder();
builder.WithOpenAIChatCompletionService("gpt-3.5-turbo", "YOUR_OPENAI_API_KEY");
var kernel = builder.Build();

// Function 정의 (Prompt를 이용)
string prompt = @"
Summarize the following text:
{{$input}}
";

var summarizeFunction = kernel.CreateSemanticFunction(prompt);

// 입력 텍스트
string inputText = @"
Semantic Kernel is a new open-source SDK from Microsoft that integrates Large Language Models (LLMs) with conventional programming languages like C# and Python.
It enables developers to build intelligent applications by combining the power of LLMs with existing code.
Semantic Kernel provides a framework for creating plugins, planning, and executing complex tasks using LLMs.
";

// Function 실행
var result = await kernel.RunAsync(inputText, summarizeFunction);

// 결과 출력
Console.WriteLine(result);
```

**4. 코드 실행 결과 예시:**

```
Semantic Kernel is an open-source SDK from Microsoft that integrates Large Language Models (LLMs) with programming languages like C# and Python. It allows developers to create intelligent applications by combining LLMs with existing code, offering a framework for plugins, planning, and executing complex tasks.
```


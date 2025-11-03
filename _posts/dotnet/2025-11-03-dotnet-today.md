---
title: "DOTNET - .NET의 강화된 Source Generator 디버깅"
date: 2025-11-03 21:03:53 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 강화된, Source, Generator, 디버깅]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 강화된 Source Generator 디버깅**

**1. 간단한 설명:**

.NET 8부터 Source Generator 개발 및 디버깅 경험이 크게 향상되었습니다. 이전에는 Source Generator를 디버깅하기 위해 복잡한 설정과 프로세스가 필요했지만, 이제는 Visual Studio 내에서 Source Generator 코드를 직접 디버깅하고, 생성된 코드를 단계별로 실행하면서 변수 값을 확인할 수 있습니다. 이는 Source Generator를 개발하는 생산성을 크게 향상시키고, 오류를 쉽게 찾고 수정할 수 있도록 해줍니다. 특히, Source Generator가 생성하는 코드가 컴파일러에 어떻게 영향을 미치는지 시각적으로 확인할 수 있어 복잡한 코드 생성 로직을 이해하는 데 도움이 됩니다. 또한, Roslyn API를 사용하여 컴파일러의 동작을 분석하고 코드를 생성하는 Source Generator의 복잡성을 관리하는 데 유용합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET 8: Source Generator Debugging:** (예시 링크 - 실제 관련 자료가 있다면 업데이트 필요)
    [https://devblogs.microsoft.com/dotnet/your-example-blog-post-on-source-generator-debugging/](https://devblogs.microsoft.com/dotnet/your-example-blog-post-on-source-generator-debugging/)
*   **Roslyn Source Generators Documentation:** (예시 링크 - 실제 관련 자료가 있다면 업데이트 필요)
    [https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview)

**3. 간단한 코드 예시 (C#):**

```csharp
// Source Generator 코드 예시 (간단한 Hello World 생성기)
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.Text;

namespace MySourceGenerator
{
    [Generator]
    public class HelloWorldGenerator : ISourceGenerator
    {
        public void Execute(GeneratorExecutionContext context)
        {
            // 1. Find the main method
            var mainMethod = context.Compilation.EntryPoint;

            // 2. Get the namespace and class name
            var namespaceName = mainMethod.ContainingNamespace.ToString();
            var className = mainMethod.ContainingType.Name;

            // 3. Create the source code
            var sourceBuilder = new StringBuilder();
            sourceBuilder.AppendLine("using System;");
            sourceBuilder.AppendLine($"namespace {namespaceName}");
            sourceBuilder.AppendLine("{");
            sourceBuilder.AppendLine($"    public static partial class {className}");
            sourceBuilder.AppendLine("    {");
            sourceBuilder.AppendLine("        public static void GeneratedMethod()");
            sourceBuilder.AppendLine("        {");
            sourceBuilder.AppendLine("            Console.WriteLine(\"Hello from generated code!\");");
            sourceBuilder.AppendLine("        }");
            sourceBuilder.AppendLine("    }");
            sourceBuilder.AppendLine("}");

            // 4. Add the source code to the compilation
            context.AddSource("GeneratedCode.g.cs", sourceBuilder.ToString());
        }

        public void Initialize(GeneratorInitializationContext context)
        {
            // No initialization required for this generator.
        }
    }
}

// 소비하는 프로젝트 코드 (Program.cs)
using System;

namespace ConsoleApp1
{
    public partial class Program
    {
        static void Main(string[] args)
        {
            GeneratedMethod(); // Source Generator에 의해 생성된 메서드 호출
            Console.WriteLine("Hello from Main!");
        }
    }
}
```

**4. 코드 실행 결과 예시:**

```
Hello from generated code!
Hello from Main!
```

**설명:**

위 코드 예시에서 `HelloWorldGenerator`는 Source Generator입니다. 이 Source Generator는 `GeneratedMethod`라는 메서드를 생성하여 소비하는 프로젝트에 추가합니다.  .NET 8의 향상된 디버깅 기능을 사용하면 이 Generator의 `Execute` 메서드에 중단점을 설정하고, 변수 값을 검사하고, 생성된 코드를 단계별로 실행하면서 디버깅할 수 있습니다. 이전에는 생성된 코드를 직접 확인하기 어려웠지만, 이제는 훨씬 쉽게 문제를 해결할 수 있습니다.  디버깅 시에는 Source Generator 프로젝트를 시작 프로젝트로 설정하고 디버깅을 시작해야 합니다.  Visual Studio의 "디버그 -> 창 -> 모듈" 메뉴에서 Source Generator가 로드되었는지 확인하고, 생성된 코드를 탐색할 수 있습니다.

**주의:**

* 위 예시는 단순한 예시이며, 실제 Source Generator는 훨씬 복잡한 로직을 포함할 수 있습니다.
* .NET 8 이상에서 해당 기능을 사용하려면 Visual Studio 2022 버전 17.8 이상이 필요합니다.
* Source Generator 디버깅 기능을 사용하기 위한 특정 설정 (예: 디버거 연결)이 필요할 수 있습니다. (자세한 내용은 관련 문서를 참조)


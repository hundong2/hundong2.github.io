---
title: "DOTNET - .NET의 향상된 Reflection 기능 및 Source Generation 결합 활용"
date: 2025-09-16 21:03:19 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 향상된, Reflection, 기능, Source, Generation, 결합, 활용]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 향상된 Reflection 기능 및 Source Generation 결합 활용**

**1. 간단한 설명:**

.NET은 Reflection을 통해 런타임에 타입 정보를 얻고 동적으로 코드를 실행할 수 있게 해줍니다. Source Generation은 컴파일 타임에 코드를 생성하여 런타임 성능 저하를 줄일 수 있습니다. 최근 트렌드는 이 두 가지 기술을 결합하여 유연성과 성능이라는 두 마리 토끼를 잡는 것입니다. 컴파일 타임에 Reflection 관련 정보를 수집하여, 런타임에 필요한 Reflection 호출을 Source Generation을 통해 미리 생성된 코드로 대체하는 방식입니다. 이렇게 하면 Reflection의 유연성을 유지하면서도 런타임 오버헤드를 최소화할 수 있습니다.  특히, AOT (Ahead-of-Time) 컴파일 환경에서 Reflection 사용을 줄여 AOT 호환성을 높이는 데 중요한 역할을 합니다.  DI 컨테이너, ORM, 시리얼라이저 등 성능이 중요한 라이브러리에서 이러한 기법이 활발히 사용되고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Compiler Platform ("Roslyn") Overview:**  [https://github.com/dotnet/roslyn](https://github.com/dotnet/roslyn) (Roslyn을 이해하는 데 필수적인 저장소)
*   **.NET Source Generators:** [https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/](https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/) (Source Generator 소개)
*   **Reflection in .NET:** [https://learn.microsoft.com/en-us/dotnet/standard/reflection](https://learn.microsoft.com/en-us/dotnet/standard/reflection) (Reflection에 대한 Microsoft 공식 문서)
*   **기타 블로그 및 예제:** Google 검색이나 GitHub에서 ".NET Source Generation Reflection" 키워드로 검색하면 다양한 예제와 설명 자료를 찾을 수 있습니다.

**3. 간단한 코드 예시 (C#):**

```csharp
// 1. Source Generator 정의 (간략화된 예시)
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.Text;

namespace MySourceGenerator
{
    [Generator]
    public class MyGenerator : ISourceGenerator
    {
        public void Execute(GeneratorExecutionContext context)
        {
            // 2. 컴파일 시간에 Reflection 정보 수집
            var classDeclarations = context.Compilation.SyntaxTrees
                .SelectMany(tree => tree.GetRoot().DescendantNodes().OfType<ClassDeclarationSyntax>());

            foreach (var classDeclaration in classDeclarations)
            {
                var semanticModel = context.Compilation.GetSemanticModel(classDeclaration.SyntaxTree);
                var classSymbol = semanticModel.GetDeclaredSymbol(classDeclaration);

                if (classSymbol != null && classSymbol.GetAttributes().Any(a => a.AttributeClass?.Name == "MyAttribute"))
                {
                    // 3. Reflection 정보 기반으로 코드 생성
                    var className = classSymbol.Name;
                    var generatedCode = $@"
                    namespace MyGeneratedCode
                    {{
                        public static class {className}Helper
                        {{
                            public static string GetName() => ""{className}""; // 실제로는 Reflection 정보를 활용
                        }}
                    }}
                    ";

                    context.AddSource($"{className}Helper.g.cs", generatedCode);
                }
            }
        }

        public void Initialize(GeneratorInitializationContext context)
        {
        }
    }
}

// 4. Attribute 정의 (사용자 정의)
[AttributeUsage(AttributeTargets.Class)]
public class MyAttribute : Attribute
{
}

// 5. 코드 사용 예시
[MyAttribute]
public class MyClass
{
    // ...
}

public class Program
{
    public static void Main(string[] args)
    {
        // 6. 생성된 코드 사용
        Console.WriteLine(MyGeneratedCode.MyClassHelper.GetName());
    }
}
```

**4. 코드 실행 결과 예시:**

```
MyClass
```

**설명:**

1.  `MyGenerator`는 `ISourceGenerator`를 구현하는 Source Generator입니다.
2.  `Execute` 메서드에서 컴파일 시간에 코드를 분석하여 `MyAttribute`가 적용된 클래스를 찾습니다.  실제 구현에서는 Reflection API를 사용하여 더 많은 정보를 얻을 수 있습니다.
3.  찾은 클래스 정보를 기반으로  `GetName()` 메서드를 포함하는 헬퍼 클래스를 생성합니다. 이 메서드는 실제로는 Reflection을 통해 클래스 이름을 가져오는 로직을 Source Generation을 통해 미리 생성해둔 것입니다.
4.  `MyAttribute`는 예시를 위해 정의된 사용자 정의 Attribute입니다.
5.  `MyClass`는 Attribute가 적용된 클래스입니다.
6.  `Program.Main`에서는 생성된 `MyClassHelper.GetName()` 메서드를 호출하여 클래스 이름을 출력합니다.  이 호출은 런타임 Reflection 없이, 컴파일 타임에 생성된 코드를 직접 호출하므로 성능이 향상됩니다.

**핵심:** 이 예시는 매우 간략화된 것이지만, Source Generation과 Reflection을 결합하여 런타임 성능을 최적화하는 아이디어를 보여줍니다. 실제 프로젝트에서는 훨씬 복잡한 시나리오에 적용될 수 있습니다. 특히,  JSON 시리얼라이저, DI 컨테이너 등에서 Reflection을 많이 사용하는 경우, Source Generation을 통해 성능 향상을 기대할 수 있습니다. AOT 환경에서는 필수적인 최적화 기법이 될 수 있습니다.


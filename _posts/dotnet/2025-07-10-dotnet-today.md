---
title: "DOTNET - Incremental Source Generators"
date: 2025-07-10 21:03:12 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, Incremental, Source, Generators]
---

## 오늘의 DOTNET 최신 기술 트렌드: **Incremental Source Generators**

**1. 간단한 설명:**
Incremental Source Generators는 C# 컴파일러에 코드를 추가하거나 수정하는 데 사용되는 강력한 도구입니다. 기존의 Source Generators와 달리, Incremental Source Generators는 컴파일 과정에서 필요한 부분만 다시 생성하여 컴파일 시간을 단축하고 개발 생산성을 향상시킵니다. 특히 대규모 프로젝트나 자주 변경되는 코드베이스에서 유용하며, 분석 단계의 결과를 캐싱하여 변경되지 않은 부분에 대한 재분석을 피함으로써 성능을 최적화합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET Compiler Platform SDK - Incremental Generators:** [https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators/incremental](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators/incremental)
*   **Andrew Lock's Blog - Introduction to Incremental Source Generators:** [https://andrewlock.net/series/creating-a-source-generator/](https://andrewlock.net/series/creating-a-source-generator/) (이 시리즈는 기존 Source Generator부터 Incremental Source Generator까지 다룹니다.)
*   **.NET 블로그 - Announcing .NET 6 - Improvements in Compiler Platform:** [https://devblogs.microsoft.com/dotnet/announcing-net-6/](https://devblogs.microsoft.com/dotnet/announcing-net-6/) (Incremental Source Generator에 대한 간단한 소개가 포함되어 있습니다.)

**3. 간단한 코드 예시 (C#):**

```csharp
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.Collections.Immutable;

[Generator]
public class HelloSourceGenerator : IIncrementalGenerator
{
    public void Initialize(IncrementalGeneratorInitializationContext context)
    {
        // 구문 트리를 필터링하여 클래스 선언만 선택합니다.
        IncrementalValuesProvider<ClassDeclarationSyntax> classDeclarations = context.SyntaxProvider
            .CreateSyntaxProvider(
                predicate: static (s, _) => IsSyntaxTargetForGeneration(s),
                transform: static (ctx, _) => GetSemanticTargetForGeneration(ctx))
            .Where(static m => m is not null)!;

        // 클래스 선언에 기반하여 소스를 생성합니다.
        context.RegisterSourceOutput(classDeclarations,
            static (spc, source) => Execute(source, spc));
    }

    static bool IsSyntaxTargetForGeneration(SyntaxNode node)
        => node is ClassDeclarationSyntax m && m.AttributeLists.Count > 0;

    static ClassDeclarationSyntax? GetSemanticTargetForGeneration(GeneratorSyntaxContext context)
    {
        var classDeclarationSyntax = (ClassDeclarationSyntax)context.Node;

        foreach (AttributeListSyntax attributeListSyntax in classDeclarationSyntax.AttributeLists)
        {
            foreach (AttributeSyntax attributeSyntax in attributeListSyntax.Attributes)
            {
                if (context.SemanticModel.GetSymbolInfo(attributeSyntax).Symbol is not IMethodSymbol attributeSymbol)
                {
                    // 속성 이름을 확인할 수 없습니다.
                    continue;
                }

                INamedTypeSymbol attributeContainingTypeSymbol = attributeSymbol.ContainingType;
                string fullName = attributeContainingTypeSymbol.ToDisplayString();

                if (fullName == "MyNamespace.GenerateHelloAttribute") // 생성할 속성 이름
                {
                    return classDeclarationSyntax;
                }
            }
        }

        return null;
    }

    static void Execute(ClassDeclarationSyntax classDeclaration, SourceProductionContext context)
    {
        // 클래스 이름을 가져옵니다.
        string className = classDeclaration.Identifier.Text;

        // 소스 코드를 생성합니다.
        string sourceCode = $@"
using System;

namespace MyNamespace
{{
    public partial class {className}
    {{
        public void SayHello()
        {{
            Console.WriteLine(""Hello from {className}!"");
        }}
    }}
}}";

        // 소스 코드를 컴파일러에 추가합니다.
        context.AddSource($"{className}.g.cs", sourceCode);
    }
}

// 사용자가 작성해야 하는 속성
namespace MyNamespace
{
    [System.AttributeUsage(System.AttributeTargets.Class, AllowMultiple = false)]
    public class GenerateHelloAttribute : System.Attribute
    {
    }
}
```

**4. 코드 실행 결과 예시:**

위의 소스 생성기를 사용하려면 먼저 'MyNamespace.GenerateHelloAttribute'라는 속성을 정의하고, 소스 생성기를 적용할 클래스에 이 속성을 추가합니다.  예를 들어 다음과 같이 코드를 작성할 수 있습니다.

```csharp
using MyNamespace;

[GenerateHello]
public partial class MyClass
{
    // 이 클래스는 소스 생성기에 의해 확장됩니다.
}

public class Program
{
    public static void Main(string[] args)
    {
        MyClass myObject = new MyClass();
        myObject.SayHello(); // 소스 생성기에 의해 추가된 메서드 호출
    }
}
```

이 코드를 실행하면 콘솔에 "Hello from MyClass!"가 출력됩니다. 이는 Source Generator가 `MyClass`에 `SayHello()` 메서드를 추가했기 때문입니다.  Incremental Source Generators는 변경된 코드에 대해서만 소스를 다시 생성하므로 빌드 시간이 단축됩니다.


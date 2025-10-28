---
title: "DOTNET - .NET의 Source Code Generators"
date: 2025-10-28 21:03:42 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Source, Code, Generators]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Source Code Generators**

**1. 간단한 설명:**

Source Code Generators는 컴파일 과정에서 코드를 동적으로 생성하여 개발자의 생산성을 높이고 보일러플레이트 코드를 줄여주는 강력한 도구입니다. 컴파일러는 사용자가 작성한 코드를 컴파일하기 전에 Source Generators를 실행하고, 생성된 코드를 컴파일에 포함시킵니다.  이를 통해 어노테이션 기반 코드 생성, 리플렉션 방지, 성능 최적화 등 다양한 이점을 얻을 수 있습니다. Source Generators는 특히 다음과 같은 시나리오에서 유용합니다.

*   **어노테이션 기반 코드 생성:** 사용자 정의 어트리뷰트를 활용하여 특정 패턴에 맞는 코드를 자동으로 생성합니다.
*   **리플렉션 방지:** 런타임 리플렉션 대신 컴파일 타임에 코드를 생성하여 성능을 향상시킵니다.
*   **API 클라이언트 코드 생성:** API 정의(예: OpenAPI/Swagger)를 기반으로 클라이언트 코드를 자동으로 생성합니다.
*   **Serialization/Deserialization 코드 생성:** 특정 데이터 형식에 대한 serialization/deserialization 로직을 자동으로 생성합니다.
*   **Immutable 객체 생성:**  생성자, 속성, 메서드 등을 자동으로 생성하여 immutable 객체를 쉽게 만들 수 있습니다.

최근에는 다양한 라이브러리들이 Source Generators를 통해 성능과 개발 편의성을 향상시키고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - Source Generators:** [https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview)
*   **Andrew Lock - Source Generators:** [https://andrewlock.net/series/creating-a-source-generator/](https://andrewlock.net/series/creating-a-source-generator/)
*   **C# Source Generators - A Practical Guide:** [https://devblogs.microsoft.com/dotnet/a-practical-guide-to-c-source-generators/](https://devblogs.microsoft.com/dotnet/a-practical-guide-to-c-source-generators/)

**3. 간단한 코드 예시 (C#):**

```csharp
// Attribute 정의
[AttributeUsage(AttributeTargets.Class)]
public class GenerateToStringAttribute : Attribute { }

// 사용자 클래스
[GenerateToString]
public partial class Person
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public int Age { get; set; }
}

// Source Generator 코드 (간략화)
[Generator]
public class ToStringGenerator : ISourceGenerator
{
    public void Initialize(GeneratorInitializationContext context)
    {
        context.RegisterForSyntaxNotifications(() => new AttributeSyntaxReceiver());
    }

    public void Execute(GeneratorExecutionContext context)
    {
        if (!(context.SyntaxContextReceiver is AttributeSyntaxReceiver receiver))
        {
            return;
        }

        foreach (var classDeclaration in receiver.Classes)
        {
            var className = classDeclaration.Identifier.Text;
            var namespaceName = classDeclaration.Parent is NamespaceDeclarationSyntax namespaceDeclaration ? namespaceDeclaration.Name.ToString() : string.Empty;

            var sourceBuilder = new StringBuilder();
            sourceBuilder.AppendLine("using System;");
            if (!string.IsNullOrEmpty(namespaceName))
            {
                sourceBuilder.AppendLine($"namespace {namespaceName}");
                sourceBuilder.AppendLine("{");
            }

            sourceBuilder.AppendLine($"public partial class {className}");
            sourceBuilder.AppendLine("{");
            sourceBuilder.AppendLine($"    public override string ToString()");
            sourceBuilder.AppendLine("    {");
            sourceBuilder.AppendLine("        return $\"{");

            var properties = classDeclaration.Members.OfType<PropertyDeclarationSyntax>();
            foreach (var property in properties)
            {
                sourceBuilder.AppendLine($"            {property.Identifier.Text}: {{{property.Identifier.Text}}}, ");
            }

            sourceBuilder.AppendLine("        }\";");
            sourceBuilder.AppendLine("    }");
            sourceBuilder.AppendLine("}");

            if (!string.IsNullOrEmpty(namespaceName))
            {
                sourceBuilder.AppendLine("}");
            }


            context.AddSource($"{className}.g.cs", SourceText.From(sourceBuilder.ToString(), Encoding.UTF8));
        }
    }
}

// Attribute 를 찾기 위한 SyntaxReceiver
class AttributeSyntaxReceiver : ISyntaxContextReceiver
{
    public List<ClassDeclarationSyntax> Classes { get; } = new List<ClassDeclarationSyntax>();

    public void OnVisitSyntaxNode(GeneratorSyntaxContext context)
    {
        if (context.Node is ClassDeclarationSyntax classDeclaration &&
            classDeclaration.AttributeLists.Any(al => al.ToString().Contains("GenerateToString")))
        {
            Classes.Add(classDeclaration);
        }
    }
}
```

**4. 코드 실행 결과 예시:**

Source Generator가 실행되면 `Person` 클래스에 `ToString()` 메서드가 자동으로 추가됩니다. 따라서 다음과 같이 사용이 가능합니다.

```csharp
Person person = new Person { FirstName = "John", LastName = "Doe", Age = 30 };
Console.WriteLine(person.ToString());
```

**출력:**

```
{ FirstName: John,  LastName: Doe,  Age: 30, }
```

**Note:** Source Generator 구현은 복잡할 수 있으며, 제공된 예시는 개념을 설명하기 위해 간략화된 것입니다. 실제 구현에서는 더 많은 오류 처리 및 유효성 검사가 필요합니다.


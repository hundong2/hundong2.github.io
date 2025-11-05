---
title: "DOTNET - .NET의 향상된 코드 분석 및 리팩토링 도구 (Roslyn Analyzers and Code Fixes)"
date: 2025-11-05 21:03:31 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 향상된, 코드, 분석, 리팩토링, 도구, (Roslyn, Analyzers, and, Code, Fixes)]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 향상된 코드 분석 및 리팩토링 도구 (Roslyn Analyzers and Code Fixes)**

**1. 간단한 설명:**

Roslyn 기반의 코드 분석기(Analyzers)와 코드 수정(Code Fixes)은 .NET 개발자가 코드 품질을 개선하고, 코딩 표준을 준수하며, 잠재적인 문제를 사전에 발견하고 수정하는 데 도움을 주는 강력한 도구입니다.  최근에는 Roslyn API의 발전과 함께 이러한 분석기 및 수정 도구가 더욱 정교해지고, 사용자 정의 규칙을 쉽게 추가하고 적용할 수 있도록 발전하고 있습니다.  특히, 팀 협업 환경에서 일관된 코딩 스타일을 유지하고 프로젝트 전체의 코드 품질을 관리하는 데 매우 유용합니다.  또한, .NET 8 및 C# 12의 새로운 기능들을 활용하여 더 정확하고 효율적인 분석 및 수정이 가능해졌습니다.  최신 트렌드는 성능 개선, 복잡한 코드 패턴 인식, 그리고 자동 수정 기능의 강화에 초점을 맞추고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Roslyn SDK Documentation:** [https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/)
*   **Roslyn Analyzers on NuGet:** [https://www.nuget.org/packages?q=roslyn+analyzer](https://www.nuget.org/packages?q=roslyn+analyzer)
*   **.NET Compiler Platform ("Roslyn") Overview:** [https://github.com/dotnet/roslyn](https://github.com/dotnet/roslyn)
*   **Microsoft Code Analysis:** [https://learn.microsoft.com/en-us/visualstudio/code-quality/code-analysis-for-managed-code-overview?view=vs-2022](https://learn.microsoft.com/en-us/visualstudio/code-quality/code-analysis-for-managed-code-overview?view=vs-2022)

**3. 간단한 코드 예시 (C#):**

다음은 간단한 Roslyn Analyzer 및 Code Fix의 예시입니다. 이 예시는 사용되지 않는 (unused) 지역 변수를 찾아 제거하는 분석기입니다.

```csharp
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CodeActions;
using Microsoft.CodeAnalysis.CodeFixes;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.Diagnostics;
using System;
using System.Collections.Immutable;
using System.Linq;
using System.Threading.Tasks;

namespace UnusedVariableAnalyzer
{
    [DiagnosticAnalyzer(LanguageNames.CSharp)]
    public class UnusedVariableAnalyzer : DiagnosticAnalyzer
    {
        public const string DiagnosticId = "UnusedVariable";
        private static readonly LocalizableString Title = new LocalizableResourceString(nameof(Resources.AnalyzerTitle), Resources.ResourceManager, typeof(Resources));
        private static readonly LocalizableString MessageFormat = new LocalizableResourceString(nameof(Resources.AnalyzerMessageFormat), Resources.ResourceManager, typeof(Resources));
        private static readonly LocalizableString Description = new LocalizableResourceString(nameof(Resources.AnalyzerDescription), Resources.ResourceManager, typeof(Resources));

        private static readonly DiagnosticDescriptor Rule = new DiagnosticDescriptor(DiagnosticId, Title, MessageFormat, "Code Smell", DiagnosticSeverity.Warning, isEnabledByDefault: true, description: Description);

        public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics { get { return ImmutableArray.Create(Rule); } }

        public override void Initialize(AnalysisContext context)
        {
            context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
            context.EnableConcurrentExecution();

            context.RegisterSyntaxNodeAction(AnalyzeSymbol, SyntaxKind.LocalDeclarationStatement);
        }

        private static void AnalyzeSymbol(SyntaxNodeAnalysisContext context)
        {
            var localDeclaration = (LocalDeclarationStatementSyntax)context.Node;

            foreach (var variable in localDeclaration.Declaration.Variables)
            {
                var symbol = context.SemanticModel.GetDeclaredSymbol(variable, context.CancellationToken);

                if (symbol != null && !context.SemanticModel.LookupSymbols(localDeclaration.SpanStart, name: symbol.Name).Any(s => s.Equals(symbol)))
                {
                    var diagnostic = Diagnostic.Create(Rule, variable.Identifier.GetLocation(), variable.Identifier.Text);
                    context.ReportDiagnostic(diagnostic);
                }
            }
        }
    }

    [ExportCodeFixProvider(LanguageNames.CSharp, Name = nameof(UnusedVariableCodeFixProvider))]
    [Shared]
    public class UnusedVariableCodeFixProvider : CodeFixProvider
    {
        public sealed override ImmutableArray<string> FixableDiagnosticIds
        {
            get { return ImmutableArray.Create(UnusedVariableAnalyzer.DiagnosticId); }
        }

        public sealed override FixAllProvider GetFixAllProvider()
        {
            return WellKnownFixAllProviders.BatchFixer;
        }

        public sealed override async Task RegisterCodeFixesAsync(CodeFixContext context)
        {
            var diagnostic = context.Diagnostics.First();
            var diagnosticSpan = diagnostic.Location.SourceSpan;

            var root = await context.Document.GetSyntaxRootAsync(context.CancellationToken).ConfigureAwait(false);

            var localDeclaration = root.FindToken(diagnosticSpan.Start).Parent.AncestorsAndSelf().OfType<LocalDeclarationStatementSyntax>().FirstOrDefault();

            if (localDeclaration == null)
            {
                return;
            }

            context.RegisterCodeFix(
                CodeAction.Create(
                    title: CodeFixResources.CodeFixTitle,
                    createChangedSolution: c => RemoveVariableDeclaration(context.Document, localDeclaration, c),
                    equivalenceKey: nameof(CodeFixResources.CodeFixTitle)),
                diagnostic);
        }

        private async Task<Solution> RemoveVariableDeclaration(Document document, LocalDeclarationStatementSyntax localDeclaration, CancellationToken cancellationToken)
        {
            var root = await document.GetSyntaxRootAsync(cancellationToken).ConfigureAwait(false);
            var newRoot = root.RemoveNode(localDeclaration, SyntaxRemoveOptions.KeepNoTrivia);
            var newDocument = document.WithSyntaxRoot(newRoot);
            return newDocument.Project.Solution;
        }
    }
}

namespace UnusedVariableAnalyzer
{
    internal static class CodeFixResources
    {
        private static readonly System.Resources.ResourceManager resourceMan;

        private static System.Globalization.CultureInfo resourceCulture;

        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal CodeFixResources()
        {
        }

        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static System.Resources.ResourceManager ResourceManager
        {
            get
            {
                if ((resourceMan == null))
                {
                    System.Resources.ResourceManager temp = new System.Resources.ResourceManager("UnusedVariableAnalyzer.CodeFixResources", typeof(CodeFixResources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }

        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static System.Globalization.CultureInfo Culture
        {
            get
            {
                return resourceCulture;
            }
            set
            {
                resourceCulture = value;
            }
        }

        internal static string CodeFixTitle
        {
            get
            {
                return ResourceManager.GetString("CodeFixTitle", resourceCulture);
            }
        }
    }
}
```

(Resources.resx 에 아래 값들을 추가)
```xml
  <data name="AnalyzerTitle" xml:space="preserve">
    <value>Unused Variable</value>
  </data>
  <data name="AnalyzerMessageFormat" xml:space="preserve">
    <value>Variable '{0}' is declared but never used</value>
  </data>
  <data name="AnalyzerDescription" xml:space="preserve">
    <value>Variables declared but never used can be removed.</value>
  </data>
```

**4. 코드 실행 결과 예시:**

Visual Studio에서 위 분석기를 활성화하면, 사용되지 않는 변수가 있는 코드에 경고가 표시됩니다.  코드 수정(Code Fix) 기능을 사용하면 해당 변수를 선언한 줄이 자동으로 삭제됩니다.

**예시 코드:**

```csharp
public class MyClass
{
    public void MyMethod()
    {
        int unusedVariable = 10; // 경고 발생: Variable 'unusedVariable' is declared but never used
        int usedVariable = 20;
        Console.WriteLine(usedVariable);
    }
}
```

**수정 후 코드:**

```csharp
public class MyClass
{
    public void MyMethod()
    {
        int usedVariable = 20;
        Console.WriteLine(usedVariable);
    }
}
```

이 예제는 매우 단순하지만, 실제 프로젝트에서는 훨씬 복잡하고 유용한 코드 분석 및 수정 도구를 개발하여 생산성과 코드 품질을 크게 향상시킬 수 있습니다.


---
title: "DOTNET - .NET의 새로운 CodeGen 옵션: TieredPGO"
date: 2025-11-25 21:03:42 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 새로운, CodeGen, 옵션:, TieredPGO]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 새로운 CodeGen 옵션: TieredPGO**

**1. 간단한 설명:**
TieredPGO는 .NET 8에 도입된 새로운 프로파일 기반 최적화(PGO) 컴파일 기술입니다. 기존의 Dynamic PGO (프로그램 실행 중 수집된 프로필 데이터를 기반으로 최적화)를 더욱 발전시킨 형태로, Tiered Compilation과 결합하여 애플리케이션의 시작 성능과 최대 성능 모두를 향상시키는 것을 목표로 합니다. TieredPGO는 컴파일러가 런타임 데이터를 활용하여 가장 중요한 코드 영역을 식별하고, 해당 영역에 대해 더 많은 시간과 리소스를 투자하여 더욱 공격적인 최적화를 수행하도록 합니다. 이를 통해 애플리케이션은 초기 시작 단계에서 빠른 반응성을 유지하면서도, 장기적으로는 더 높은 처리량을 달성할 수 있습니다. TieredPGO는 .NET 8에서 기본적으로 활성화되어 있으며, 별도의 코드 변경 없이도 성능 향상을 기대할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET 8 Performance Improvements in .NET 8:** .NET 블로그의 .NET 8 성능 개선 관련 게시글에 TieredPGO에 대한 설명이 포함되어 있습니다.
    *   [https://devblogs.microsoft.com/dotnet/performance-improvements-in-dotnet-8/](https://devblogs.microsoft.com/dotnet/performance-improvements-in-dotnet-8/)
*   **.NET Documentation (Tiered Compilation):** Tiered Compilation 및 PGO에 대한 공식 문서.
    *   (공식 문서는 아직 특정 .NET 버전에 한정되지 않은 일반적인 설명 위주이므로, .NET 8 관련 내용은 블로그 글을 참고하는 것이 더 유용합니다.)

**3. 간단한 코드 예시 (C#):**

TieredPGO는 컴파일러 수준에서 동작하므로, 직접적으로 제어하거나 활성화/비활성화하는 코드는 없습니다.  .NET 8 이상 환경에서 빌드하면 기본적으로 활성화됩니다. 하지만 효과를 확인하기 위해 간단한 성능 측정 코드를 작성해볼 수 있습니다.

```csharp
using System;
using System.Diagnostics;

public class Program
{
    public static void Main(string[] args)
    {
        // 측정할 코드 블록 (예: 복잡한 계산 또는 데이터 처리)
        Stopwatch sw = Stopwatch.StartNew();
        for (int i = 0; i < 1000000; i++)
        {
            ComplexCalculation(i);
        }
        sw.Stop();
        Console.WriteLine($"Execution Time: {sw.ElapsedMilliseconds} ms");
    }

    private static double ComplexCalculation(int input)
    {
        double result = Math.Sqrt(input * input + 1);
        result = Math.Log(result + input);
        result = Math.Pow(result, 2.5);
        return result;
    }
}
```

**4. 코드 실행 결과 예시:**

위 코드를 .NET 7과 .NET 8 환경에서 실행하고, 각각의 실행 시간을 비교하여 TieredPGO의 효과를 간접적으로 확인할 수 있습니다.

**.NET 7 실행 결과 (예시):**

```
Execution Time: 1200 ms
```

**.NET 8 실행 결과 (예시):**

```
Execution Time: 1000 ms
```

(실제 결과는 하드웨어 환경, 워크로드, 컴파일러 최적화 수준에 따라 달라질 수 있습니다. 여러 번 실행하여 평균값을 비교하는 것이 좋습니다.)

**참고:** TieredPGO는 실행 시간 동안 프로필 데이터를 수집하고 최적화하기 때문에, 애플리케이션이 충분히 실행된 후에 성능 개선 효과가 더욱 뚜렷하게 나타납니다. 간단한 테스트 코드보다는 실제 애플리케이션 환경에서 성능 변화를 측정하는 것이 좋습니다. 또한,  성능 측정 시 Release 빌드 모드를 사용하고, 코드에서 불필요한 디버깅 관련 코드를 제거하여 정확도를 높이는 것이 중요합니다.


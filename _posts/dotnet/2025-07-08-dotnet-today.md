---
title: "DOTNET - C# 12의 Collection Expressions"
date: 2025-07-08 21:03:21 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, C#, 12의, Collection, Expressions]
---

## 오늘의 DOTNET 최신 기술 트렌드: **C# 12의 Collection Expressions**

**1. 간단한 설명:**
C# 12에 도입된 Collection Expressions는 배열, span, list 등 다양한 컬렉션 형식을 생성하는 간결하고 효율적인 방법을 제공합니다. 이전에는 배열 초기화, List.Add() 메서드 호출, Span<T> 생성자 호출 등 다양한 방법으로 컬렉션을 생성해야 했지만, Collection Expressions를 사용하면 `[element1, element2, element3]`와 같은 일관된 구문으로 컬렉션을 생성할 수 있습니다. 이 기능은 코드 가독성을 높이고 컬렉션 생성 코드를 더욱 간결하게 만들어줍니다. 또한, spread 연산자(`...`)를 사용하여 기존 컬렉션의 요소를 새로운 컬렉션에 쉽게 포함시킬 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - Collection expressions:** [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions)
*   **Jon Skeet's blog - Collection Expressions in C# 12:** (예시, 실제 Jon Skeet 블로그에 없을 수 있음. C# 관련 유명 블로거 검색하여 대체 가능)
*   **C# Language Design meeting notes:** (GitHub 저장소 링크, Collection Expressions 관련 회의록)

**3. 간단한 코드 예시 (C#):**

```csharp
using System;
using System.Collections.Generic;

public class CollectionExpressionsExample
{
    public static void Main(string[] args)
    {
        // 배열 생성
        int[] numbers = [1, 2, 3, 4, 5];
        Console.WriteLine($"Numbers: {string.Join(", ", numbers)}");

        // List 생성
        List<string> names = ["Alice", "Bob", "Charlie"];
        Console.WriteLine($"Names: {string.Join(", ", names)}");

        // Spread 연산자 사용
        int[] moreNumbers = [.. numbers, 6, 7];
        Console.WriteLine($"More Numbers: {string.Join(", ", moreNumbers)}");

        // 2차원 배열
        int[][] matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
        foreach (var row in matrix)
        {
            Console.WriteLine(string.Join(", ", row));
        }
    }
}
```

**4. 코드 실행 결과 예시:**

```
Numbers: 1, 2, 3, 4, 5
Names: Alice, Bob, Charlie
More Numbers: 1, 2, 3, 4, 5, 6, 7
1, 2, 3
4, 5, 6
7, 8, 9
```


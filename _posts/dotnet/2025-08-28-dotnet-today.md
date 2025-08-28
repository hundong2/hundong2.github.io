---
title: "DOTNET - .NET의 Native Memory API (System.Memory)"
date: 2025-08-28 21:03:08 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Native, Memory, API, (System.Memory)]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Native Memory API (System.Memory)**

**1. 간단한 설명:**

.NET의 `System.Memory` 네임스페이스는 언매니지드 메모리, 포인터 조작, 그리고 구조체를 복사 없이 안전하게 다루는 데 필요한 API들을 제공합니다. 이는 특히 고성능 애플리케이션, 게임 개발, 시스템 프로그래밍, 그리고 네이티브 라이브러리와의 상호 작용에서 매우 유용합니다. `System.Memory`의 핵심 요소는 다음과 같습니다:

*   **Span\<T>와 ReadOnlySpan\<T>:** 배열 또는 연속된 메모리 블록의 읽기/쓰기 (Span) 또는 읽기 전용 (ReadOnlySpan) 뷰를 나타냅니다. 이는 배열의 일부 또는 전체를 복사 없이 안전하게 접근할 수 있게 해줍니다.
*   **Memory\<T>와 ReadOnlyMemory\<T>:** `Span`과 유사하지만, 메모리 풀에 할당된 메모리 영역을 관리하는 데 사용됩니다. `Memory`는 소유권 개념을 포함하며, 더 긴 수명을 가질 수 있습니다.
*   **Unsafe:** 명칭에서 알 수 있듯이, C#에서 안전하지 않은(unsafe) 코드 블록을 사용하여 포인터를 직접 조작하고, 타입 캐스팅을 수행하며, 메모리에 직접 접근할 수 있게 해주는 클래스입니다. 주의해서 사용해야 하지만, 성능 critical한 시나리오에서 필수적입니다.

이러한 API를 활용하면 가비지 컬렉션의 부담을 줄이고, 메모리 복사를 최소화하여 애플리케이션의 성능을 크게 향상시킬 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - Span\<T> Structure:** [https://learn.microsoft.com/en-us/dotnet/api/system.span-1?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.span-1?view=net-8.0)
*   **Microsoft Docs - Memory\<T> Structure:** [https://learn.microsoft.com/en-us/dotnet/api/system.memory-1?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.memory-1?view=net-8.0)
*   **Microsoft Docs - Unsafe Class:** [https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.unsafe?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.unsafe?view=net-8.0)
*   **.NET Blog - Span\<T> and Memory\<T> Performance Improvements:** (가상의 링크, 실제 블로그 검색을 통해 관련 정보를 찾으세요.)

**3. 간단한 코드 예시 (C#):**

```csharp
using System;

public class SpanExample
{
    public static void Main(string[] args)
    {
        // 배열 생성
        int[] numbers = { 1, 2, 3, 4, 5 };

        // Span 생성 (전체 배열)
        Span<int> spanAll = numbers.AsSpan();

        // Span 생성 (배열의 일부)
        Span<int> spanPartial = numbers.AsSpan(1, 3); // 인덱스 1부터 3개 요소 (2, 3, 4)

        // Span을 통한 값 변경
        spanAll[0] = 10;

        // ReadOnlySpan 사용 예시
        ReadOnlySpan<int> readOnlySpan = numbers.AsSpan();
        // readOnlySpan[0] = 20; // 컴파일 에러! 읽기 전용이므로 변경 불가

        Console.WriteLine("Original Array: " + string.Join(", ", numbers));
        Console.WriteLine("Span (전체): " + string.Join(", ", spanAll.ToArray()));
        Console.WriteLine("Span (부분): " + string.Join(", ", spanPartial.ToArray()));
    }
}
```

**4. 코드 실행 결과 예시:**

```
Original Array: 10, 2, 3, 4, 5
Span (전체): 10, 2, 3, 4, 5
Span (부분): 2, 3, 4
```

**설명:**

*   `numbers` 배열을 생성하고, 전체 배열과 배열의 일부에 대한 `Span<int>`을 생성합니다.
*   `spanAll`을 통해 배열의 첫 번째 요소를 변경하면, 원본 배열 `numbers`도 함께 변경됩니다. (Span은 메모리의 뷰이기 때문)
*   `ReadOnlySpan`은 값을 변경할 수 없는 읽기 전용 뷰를 제공합니다.
*   `string.Join`과 `ToArray` 메서드를 사용하여 Span의 내용을 문자열로 출력합니다.


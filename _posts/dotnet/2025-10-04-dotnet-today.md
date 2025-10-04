---
title: "DOTNET - .NET의 신규 컬렉션 타입: `PriorityQueue<TElement, TPriority>`"
date: 2025-10-04 21:03:11 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, 신규, 컬렉션, 타입:, `PriorityQueue<TElement,, TPriority>`]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 신규 컬렉션 타입: `PriorityQueue<TElement, TPriority>`**

**1. 간단한 설명:**
`.NET 6`부터 도입된 `PriorityQueue<TElement, TPriority>`는 우선순위 큐 자료구조를 구현하는 컬렉션 타입입니다. 일반적인 큐(Queue)와 달리, 각 요소에 우선순위가 부여되어 우선순위가 높은 요소부터 먼저 dequeue 되는 특징을 가집니다. 이는 작업 스케줄링, 그래프 알고리즘(예: Dijkstra), 이벤트 처리 등 다양한 상황에서 효율적인 데이터 관리를 가능하게 합니다. `PriorityQueue`는 내부적으로 힙(Heap) 자료구조를 사용하여 구현되었으며, `enqueue`와 `dequeue` 연산의 시간 복잡도는 O(log n)입니다. .NET 7부터는 `TryDequeue` 메서드와 `EnqueueRange` 메서드가 추가되어 편의성이 더욱 향상되었습니다. .NET 8에서는 더욱 개선된 성능과 API를 제공합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - PriorityQueue\<TElement, TPriority> Class:** [https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.priorityqueue-2?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.priorityqueue-2?view=net-8.0)
*   **.NET Blog:** .NET의 공식 블로그에서 PriorityQueue 관련 업데이트나 사용 사례를 찾아볼 수 있습니다.
*   **GitHub - .NET Runtime Repository:**  PriorityQueue의 구현 내부를 살펴보고 싶다면 .NET Runtime repository (dotnet/runtime)에서 관련 코드를 찾아볼 수 있습니다.

**3. 간단한 코드 예시 (C#):**

```csharp
using System;
using System.Collections.Generic;

public class PriorityQueueExample
{
    public static void Main(string[] args)
    {
        // 우선순위 큐 생성 (string 요소, int 우선순위)
        PriorityQueue<string, int> priorityQueue = new();

        // 요소 추가 (이름, 우선순위)
        priorityQueue.Enqueue("Task C", 3);
        priorityQueue.Enqueue("Task A", 1);
        priorityQueue.Enqueue("Task B", 2);
        priorityQueue.Enqueue("Task D", 4);

        // 큐에서 요소 꺼내기 (우선순위가 높은 순서대로)
        Console.WriteLine("Tasks in priority order:");
        while (priorityQueue.Count > 0)
        {
            string task = priorityQueue.Dequeue();
            Console.WriteLine(task);
        }
    }
}
```

**4. 코드 실행 결과 예시:**

```
Tasks in priority order:
Task A
Task B
Task C
Task D
```


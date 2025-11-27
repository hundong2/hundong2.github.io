---
title: "DOTNET - .NET의 ConcurrentBag<T>.TryTakeAny()"
date: 2025-11-27 21:03:20 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, ConcurrentBag<T>.TryTakeAny()]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 ConcurrentBag<T>.TryTakeAny()**

**1. 간단한 설명:**

`.NET 7`부터 추가된 `ConcurrentBag<T>.TryTakeAny()` 메서드는 ConcurrentBag에서 **잠금 없이(lock-free) 임의의 항목을 효율적으로 제거**할 수 있도록 해줍니다. 기존의 `TryTake()` 메서드는 LIFO(Last-In-First-Out) 순서로 항목을 제거하려고 시도하기 때문에 특정 시나리오에서 성능 병목 현상을 유발할 수 있습니다. `TryTakeAny()`는 내부적으로 락을 사용하지 않으면서도 ConcurrentBag이 비어있지 않다면 하나의 항목을 제거합니다.  이 기능은 특히 **생산자-소비자 패턴**에서 여러 소비자가 동시에 작업을 처리해야 하는 경우 유용하며, 각 소비자는 백에서 사용할 수 있는 항목을 빠르게 가져와 작업을 시작할 수 있습니다. 즉, `TryTakeAny()`는 무작위 접근이 허용될 때 경쟁을 줄여 높은 동시성 및 성능을 제공합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - ConcurrentBag<T>.TryTakeAny Method:** [https://learn.microsoft.com/en-us/dotnet/api/system.collections.concurrent.concurrentbag-1.trytakeany?view=net-7.0](https://learn.microsoft.com/en-us/dotnet/api/system.collections.concurrent.concurrentbag-1.trytakeany?view=net-7.0)
*   **GitHub - Implementation of ConcurrentBag<T>.TryTakeAny:** [https://github.com/dotnet/runtime/blob/main/src/libraries/System.Collections.Concurrent/src/System/Collections/Concurrent/ConcurrentBag.cs](https://github.com/dotnet/runtime/blob/main/src/libraries/System.Collections.Concurrent/src/System/Collections/Concurrent/ConcurrentBag.cs)

**3. 간단한 코드 예시 (C#):**

```csharp
using System;
using System.Collections.Concurrent;
using System.Threading;
using System.Threading.Tasks;

public class ConcurrentBagExample
{
    public static void Main(string[] args)
    {
        ConcurrentBag<int> bag = new ConcurrentBag<int>();

        // 가방에 데이터 추가
        bag.Add(1);
        bag.Add(2);
        bag.Add(3);

        // TryTakeAny를 사용하여 데이터 가져오기
        if (bag.TryTakeAny(out int item))
        {
            Console.WriteLine($"가방에서 가져온 항목: {item}");
        }
        else
        {
            Console.WriteLine("가방이 비어 있습니다.");
        }

        // 여러 스레드에서 동시에 TryTakeAny를 시도
        Task[] tasks = new Task[3];
        for (int i = 0; i < 3; i++)
        {
            tasks[i] = Task.Run(() =>
            {
                if (bag.TryTakeAny(out int item))
                {
                    Console.WriteLine($"스레드 {Thread.CurrentThread.ManagedThreadId}: 가방에서 가져온 항목: {item}");
                }
                else
                {
                    Console.WriteLine($"스레드 {Thread.CurrentThread.ManagedThreadId}: 가방이 비어 있습니다.");
                }
            });
        }

        Task.WaitAll(tasks);
    }
}
```

**4. 코드 실행 결과 예시:**

```
가방에서 가져온 항목: 3
스레드 11: 가방에서 가져온 항목: 2
스레드 12: 가방에서 가져온 항목: 1
스레드 13: 가방이 비어 있습니다.
```

**설명:** 위의 코드는 ConcurrentBag에 데이터를 추가한 후 `TryTakeAny`를 사용하여 데이터를 가져오는 예시입니다. 여러 스레드에서 동시에 `TryTakeAny`를 호출하여 경쟁 상황을 시뮬레이션하고, 각 스레드가 성공적으로 데이터를 가져오거나 가방이 비어있음을 알리는 것을 보여줍니다. 결과는 스레드 실행 순서에 따라 달라질 수 있습니다.  ConcurrentBag은 항목이 추가된 순서를 보장하지 않으므로, `TryTakeAny`는 가방에 있는 항목 중 어떤 것이든 제거할 수 있습니다.


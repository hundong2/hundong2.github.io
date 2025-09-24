---
title: "DOTNET - .NET의 System.Runtime.InteropServices.Marshalling 네임스페이스 및 마샬링 최적화"
date: 2025-09-24 21:03:34 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, System.Runtime.InteropServices.Marshalling, 네임스페이스, 마샬링, 최적화]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 System.Runtime.InteropServices.Marshalling 네임스페이스 및 마샬링 최적화**

**1. 간단한 설명:**

.NET 7부터 도입되어 .NET 8에서 더욱 강화된 `System.Runtime.InteropServices.Marshalling` 네임스페이스는 네이티브 코드와의 상호 운용성(Interoperability)을 위한 마샬링 과정을 크게 개선하고 제어할 수 있도록 합니다. 기존의 Attributes 기반 마샬링 방식보다 훨씬 강력하고 사용자 정의가 가능하며, 성능 또한 향상되었습니다.  `CustomMarshallerAttribute`를 사용하여 마샬링 로직을 직접 구현하고, 다양한 마샬링 전략을 선택적으로 적용하여 managed/unmanaged 간의 데이터 변환 오버헤드를 줄일 수 있습니다.  또한 `[GeneratedComInterface]` 특성과 함께 사용하면 COM 인터페이스를 더욱 효율적으로 생성하고 사용할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft .NET Documentation:**  [`System.Runtime.InteropServices.Marshalling`](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshalling?view=net-8.0)
*   **.NET Blog:**  [Improvements in P/Invoke marshalling in .NET 7](https://devblogs.microsoft.com/dotnet/improvements-in-pinvoke-marshalling-in-net-7/)
*   **.NET Blog:** [Generated Com Wrappers](https://devblogs.microsoft.com/dotnet/generated-com-wrappers/)
*   **강력한 형식의 P/Invoke 마샬링에 대한 사용자 지정 마샬러** [https://learn.microsoft.com/ko-kr/dotnet/standard/native-interop/custom-marshallers](https://learn.microsoft.com/ko-kr/dotnet/standard/native-interop/custom-marshallers)

**3. 간단한 코드 예시 (C#):**

```csharp
using System.Runtime.InteropServices;
using System.Runtime.InteropServices.Marshalling;

// 사용자 정의 마샬러
[CustomMarshaller(typeof(MyStruct), MarshalMode.Default, typeof(MyStructMarshaller))]
public static class MyStructMarshaller
{
    public static unsafe IntPtr ConvertToUnmanaged(MyStruct managed, out int unmanagedSize)
    {
        // Unmanaged 메모리 할당 및 데이터 복사 로직 구현
        int size = sizeof(int) * 2;
        IntPtr unmanaged = Marshal.AllocHGlobal(size);
        unmanagedSize = size;
        Marshal.WriteInt32(unmanaged, managed.X);
        Marshal.WriteInt32(unmanaged, sizeof(int), managed.Y);
        return unmanaged;
    }

    public static unsafe MyStruct ConvertToManaged(IntPtr unmanaged)
    {
        // Unmanaged 메모리에서 Managed 객체로 데이터 복사 로직 구현
        return new MyStruct { X = Marshal.ReadInt32(unmanaged), Y = Marshal.ReadInt32(unmanaged, sizeof(int)) };
    }

    public static unsafe void Free(IntPtr unmanaged)
    {
        // Unmanaged 메모리 해제 로직 구현
        Marshal.FreeHGlobal(unmanaged);
    }
}

public struct MyStruct
{
    public int X;
    public int Y;
}

// P/Invoke 선언
internal static partial class NativeMethods
{
    [LibraryImport("mylibrary.dll")]
    internal static partial void ProcessMyStruct(MyStruct myStruct);
}

public class Example
{
    public static void UseMyStruct()
    {
        MyStruct data = new MyStruct { X = 10, Y = 20 };
        NativeMethods.ProcessMyStruct(data);
    }
}
```

**4. 코드 실행 결과 예시:**

위 코드는 `mylibrary.dll`의 `ProcessMyStruct` 함수에 `MyStruct` 구조체를 전달하는 예시입니다. `MyStructMarshaller` 클래스가 사용자 정의 마샬링 로직을 제공하며, 이 로직에 따라 managed `MyStruct` 데이터가 unmanaged 메모리에 복사되어 네이티브 함수에 전달됩니다.  `ProcessMyStruct` 함수 내부에서 전달된 데이터는 정상적으로 사용될 수 있습니다. (구체적인 실행 결과는 mylibrary.dll의 구현에 따라 달라집니다.)  만약 마샬링이 제대로 되지 않았다면, `ProcessMyStruct`는 잘못된 데이터 또는 예외를 발생시킬 수 있습니다.


---
title: "DOTNET - C# 12의 Primary Constructor"
date: 2025-07-16 21:03:25 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, C#, 12의, Primary, Constructor]
---

## 오늘의 DOTNET 최신 기술 트렌드: **C# 12의 Primary Constructor**

**1. 간단한 설명:**

C# 12에 도입된 Primary Constructor는 클래스, 구조체, 레코드에서 생성자를 더 간결하게 정의할 수 있게 해주는 기능입니다. 기존에는 필드 초기화 및 생성자 매개변수 전달을 위해 코드를 여러 번 반복해야 했지만, Primary Constructor를 사용하면 클래스 선언 시 매개변수를 정의하고, 이를 클래스 멤버처럼 직접 사용할 수 있습니다. 이를 통해 코드 양을 줄이고 가독성을 높일 수 있으며, 특히 DI (의존성 주입) 컨테이너를 사용하는 경우에 더욱 유용합니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - Primary Constructors:** [https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes#primary-constructors](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes#primary-constructors)
*   **C# 12: Primary Constructors:** [https://devblogs.microsoft.com/dotnet/new-c-12-features/#primary-constructors](https://devblogs.microsoft.com/dotnet/new-c-12-features/#primary-constructors)
*   **Exploring C# 12 Primary Constructors:** [https://www.youtube.com/watch?v=W-271uXgI-8](https://www.youtube.com/watch?v=W-271uXgI-8) (YouTube 영상)

**3. 간단한 코드 예시 (C#):**

```csharp
// C# 12 Primary Constructor 사용
public class Person(string firstName, string lastName)
{
    public string FullName => $"{firstName} {lastName}";

    public void Introduce()
    {
        Console.WriteLine($"Hello, my name is {FullName}.");
    }
}

// 레코드에서도 사용 가능
public record Product(string Name, decimal Price);

public class Example
{
    public static void Main(string[] args)
    {
        Person person = new Person("John", "Doe");
        person.Introduce();

        Product product = new Product("Laptop", 1200.00m);
        Console.WriteLine($"Product: {product.Name}, Price: {product.Price:C}");
    }
}
```

**4. 코드 실행 결과 예시:**

```
Hello, my name is John Doe.
Product: Laptop, Price: $1,200.00
```


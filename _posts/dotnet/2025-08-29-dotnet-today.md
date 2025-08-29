---
title: "DOTNET - .NET의 System.CommandLine 라이브러리 활용"
date: 2025-08-29 21:03:01 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, System.CommandLine, 라이브러리, 활용]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 System.CommandLine 라이브러리 활용**

**1. 간단한 설명:**

System.CommandLine은 .NET 기반 애플리케이션을 위한 현대적이고 유연한 명령줄 인터페이스 (CLI)를 구축하기 위한 강력한 라이브러리입니다. 과거 `Console.WriteLine()`으로 처리하던 명령줄 인자 파싱, 유효성 검사, 자동 완성, 도움말 생성 등의 복잡한 작업을 간소화하고, 사용자 친화적인 CLI 애플리케이션을 쉽게 개발할 수 있도록 지원합니다.  특히, 명령, 옵션, 인자 정의를 통해 구조화된 CLI를 만들고, 자동 완성, 오류 처리, 사용자 정의 헬프 메시지를 제공하여 사용성을 높일 수 있습니다. 최근에는 다양한 기능들이 추가되면서 더욱 강력해지고 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft System.CommandLine GitHub 저장소:** [https://github.com/dotnet/command-line-api](https://github.com/dotnet/command-line-api)
*   **System.CommandLine 개요:** [https://learn.microsoft.com/en-us/dotnet/standard/commandline/](https://learn.microsoft.com/en-us/dotnet/standard/commandline/)
*   **System.CommandLine 기반 도구 제작 예제:** [https://devblogs.microsoft.com/dotnet/modernize-your-net-tool-with-system-commandline/](https://devblogs.microsoft.com/dotnet/modernize-your-net-tool-with-system-commandline/)

**3. 간단한 코드 예시 (C#):**

```csharp
using System.CommandLine;

class Program
{
    static async Task<int> Main(string[] args)
    {
        // 루트 명령 생성
        var rootCommand = new RootCommand("간단한 파일 처리 도구");

        // 파일 경로 옵션 생성
        var fileOption = new Option<FileInfo?>(
            name: "--file",
            description: "처리할 파일 경로");
        fileOption.IsRequired = true; // 필수 옵션 지정
        rootCommand.AddOption(fileOption);

        // 텍스트 변환 옵션 생성
        var toUpperOption = new Option<bool>(
            name: "--to-upper",
            getDefaultValue: () => false,
            description: "텍스트를 대문자로 변환합니다.");
        rootCommand.AddOption(toUpperOption);

        // 명령 처리 핸들러 정의
        rootCommand.SetHandler(async (fileInfo, toUpper) =>
        {
            if (fileInfo is null)
            {
                Console.WriteLine("파일 경로가 지정되지 않았습니다.");
                return 1;
            }

            try
            {
                string content = await File.ReadAllTextAsync(fileInfo.FullName);

                if (toUpper)
                {
                    content = content.ToUpper();
                }

                Console.WriteLine($"파일 내용: {content}");
                return 0;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"오류 발생: {ex.Message}");
                return 1;
            }
        }, fileOption, toUpperOption);

        // 명령 파싱 및 실행
        return await rootCommand.InvokeAsync(args);
    }
}
```

**4. 코드 실행 결과 예시:**

**명령:**

```bash
dotnet run -- --file myfile.txt --to-upper
```

**myfile.txt 내용:**

```
Hello, world!
This is a test file.
```

**출력:**

```
파일 내용: HELLO, WORLD!
THIS IS A TEST FILE.
```

**에러 상황:**

**명령:**

```bash
dotnet run -- --to-upper
```

**출력:**

```
Option '--file' is required.
```

**명령:**

```bash
dotnet run -- --help
```

**출력:**

```
간단한 파일 처리 도구

Usage:
  [options]

Options:
  --file <file>          처리할 파일 경로
  --to-upper             텍스트를 대문자로 변환합니다.
  --version              Show version information
  -?, -h, --help       Show help and usage information
```


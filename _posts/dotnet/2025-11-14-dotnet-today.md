---
title: "DOTNET - .NET의 Enhanced Code Coverage"
date: 2025-11-14 21:03:25 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, Enhanced, Code, Coverage]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 Enhanced Code Coverage**

**1. 간단한 설명:**

.NET 8 이후, 코드 커버리지 기능이 크게 향상되었습니다.  특히, 이제는 플랫폼 간 코드 커버리지 데이터 병합이 가능해졌고, 브랜치 커버리지, 라인 커버리지, 함수 커버리지 등을 포함한 상세한 리포트를 생성할 수 있습니다.  `dotnet test` 명령어를 통해 쉽게 활성화할 수 있으며, OpenCover나 ReportGenerator와 같은 도구를 대체할 수 있는 수준으로 발전하고 있습니다. Visual Studio에서도 코드 커버리지 결과를 직접 확인할 수 있습니다. 이러한 기능 강화는 테스트 품질 향상 및 코드 유지보수 효율성을 높이는 데 기여합니다. 커버리지 데이터를 병합하여 다양한 환경에서 테스트된 코드의 커버리지를 종합적으로 분석할 수 있게 되었습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **.NET 공식 블로그:** 향상된 코드 커버리지에 대한 자세한 내용 및 업데이트를 확인 가능합니다. (예상 링크: Microsoft .NET Blog, 검색 키워드: ".NET code coverage enhancements")
*   **Microsoft Learn:** `dotnet test` 명령어를 사용한 코드 커버리지 활성화 및 구성 방법에 대한 공식 문서. (예상 링크: Microsoft Learn, 검색 키워드: "dotnet test code coverage")
*   **GitHub .NET Test SDK:** .NET Test SDK 저장소에서 관련 이슈 및 토론 내용을 확인할 수 있습니다. (예상 링크: GitHub .NET Test SDK, 검색 키워드: "Code Coverage")

**3. 간단한 코드 예시 (C#):**

```csharp
// Calculator.cs
public class Calculator
{
    public int Add(int a, int b)
    {
        if(a > 0 && b > 0){
            return a + b;
        }
        else
        {
            return 0;
        }
    }

    public int Subtract(int a, int b)
    {
        return a - b;
    }
}

// CalculatorTests.cs
using NUnit.Framework;

public class CalculatorTests
{
    [Test]
    public void Add_PositiveNumbers_ReturnsSum()
    {
        Calculator calculator = new Calculator();
        int result = calculator.Add(2, 3);
        Assert.AreEqual(5, result);
    }

    [Test]
    public void Subtract_Numbers_ReturnsDifference()
    {
        Calculator calculator = new Calculator();
        int result = calculator.Subtract(5, 2);
        Assert.AreEqual(3, result);
    }
}
```

**4. 코드 실행 결과 예시:**

1.  **테스트 실행:**

    ```bash
    dotnet test /p:CollectCoverage=true /p:CoverletOutputFormat=opencover
    ```

2.  **코드 커버리지 결과 (콘솔):**

    테스트 실행 후 콘솔에 표시되는 커버리지 요약 정보 (예시):

    ```
    Starting test execution, please wait...
    A total of 1 test files matched the specified pattern.
    Passed!  - Failed: 0, Passed: 2, Skipped: 0, Total: 2, Duration: < 1 ms - CalculatorTests.dll (net8.0)

    Generating code coverage report '/path/to/TestProject/TestResults/Coverage/coverage.opencover.xml'

    +---------+----------+--------+--------+--------+---------+
    | Module  | Assembly | Line   | Branch | Method | Class   |
    +---------+----------+--------+--------+--------+---------+
    | ConsoleApp1| ConsoleApp1 | 66.66% | 50%  | 100%  | 100%  |
    +---------+----------+--------+--------+--------+---------+
    ```

3.  **코드 커버리지 결과 (XML):**

    `coverage.opencover.xml` 파일에 저장된 상세 커버리지 정보 (일부):

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <CoverageSession>
      <Summary numSequencePoints="5" visitedSequencePoints="4" numBranchPoints="2" visitedBranchPoints="1" sequenceCoverage="80" branchCoverage="50" maxCyclomaticComplexity="1" minCyclomaticComplexity="1" visitedClasses="1" numClasses="1" visitedMethods="2" numMethods="2"/>
      <Modules>
        <Module hash="ABCDEF1234567890" path="/path/to/TestProject/bin/Debug/net8.0/ConsoleApp1.dll">
          <Summary numSequencePoints="5" visitedSequencePoints="4" numBranchPoints="2" visitedBranchPoints="1" sequenceCoverage="80" branchCoverage="50" maxCyclomaticComplexity="1" minCyclomaticComplexity="1" visitedClasses="1" numClasses="1" visitedMethods="2" numMethods="2"/>
          <Files>
            <File uid="1" path="/path/to/TestProject/Calculator.cs"/>
          </Files>
          <Classes>
            <Class name="Calculator" visibility="public" attributes="0">
              <Summary numSequencePoints="5" visitedSequencePoints="4" numBranchPoints="2" visitedBranchPoints="1" sequenceCoverage="80" branchCoverage="50" maxCyclomaticComplexity="1" minCyclomaticComplexity="1" visitedClasses="1" numClasses="1" visitedMethods="2" numMethods="2"/>
              <Methods>
                <Method name="Int32 Add(Int32, Int32)" signature="System.Int32 Add(System.Int32,System.Int32)" attributes="8" line="3" column="13" maxCyclomaticComplexity="1" minCyclomaticComplexity="1" sequenceCoverage="80" branchCoverage="50">
                  <Summary numSequencePoints="3" visitedSequencePoints="2" numBranchPoints="2" visitedBranchPoints="1" sequenceCoverage="66.66" branchCoverage="50"/>
                  <SequencePoints>
                    <SequencePoint ordinal="1" offset="0" sl="5" sc="13" el="5" ec="14" becol="0" becrow="0" visitCount="1" isBranchingPoint="False" vc="1" uspid="1"/>
                    <SequencePoint ordinal="2" offset="3" sl="6" sc="17" el="6" ec="32" becol="0" becrow="0" visitCount="1" isBranchingPoint="True" vc="1" uspid="1"/>
                    <SequencePoint ordinal="3" offset="6" sl="7" sc="21" el="7" ec="33" becol="0" becrow="0" visitCount="1" isBranchingPoint="False" vc="1" uspid="1"/>
                    <SequencePoint ordinal="4" offset="9" sl="10" sc="17" el="10" ec="25" becol="0" becrow="0" visitCount="0" isBranchingPoint="False" vc="0" uspid="1"/>
                  </SequencePoints>
                  <BranchPoints>
                    <BranchPoint offset="3" sl="6" path="0" ordinal="0" offsetPoint="9" visitCount="0" vc="0"/>
                    <BranchPoint offset="3" sl="6" path="1" ordinal="1" offsetPoint="6" visitCount="1" vc="1"/>
                  </BranchPoints>
                </Method>
                <Method name="Int32 Subtract(Int32, Int32)" signature="System.Int32 Subtract(System.Int32,System.Int32)" attributes="8" line="14" column="13" maxCyclomaticComplexity="1" minCyclomaticComplexity="1" sequenceCoverage="100" branchCoverage="100">
                  <Summary numSequencePoints="2" visitedSequencePoints="2" numBranchPoints="0" visitedBranchPoints="0" sequenceCoverage="100" branchCoverage="100"/>
                  <SequencePoints>
                    <SequencePoint ordinal="0" offset="0" sl="15" sc="13" el="15" ec="14" becol="0" becrow="0" visitCount="1" isBranchingPoint="False" vc="1" uspid="1"/>
                    <SequencePoint ordinal="1" offset="3" sl="16" sc="17" el="16" ec="29" becol="0" becrow="0" visitCount="1" isBranchingPoint="False" vc="1" uspid="1"/>
                  </SequencePoints>
                  <BranchPoints/>
                </Method>
              </Methods>
            </Class>
          </Classes>
        </Module>
      </Modules>
    </CoverageSession>
    ```

4.  **ReportGenerator를 사용하여 HTML 리포트 생성:**

    ```bash
    reportgenerator -reports:"/path/to/TestProject/TestResults/Coverage/coverage.opencover.xml" -targetdir:"/path/to/TestProject/CoverageReport"
    ```

이 HTML 리포트를 통해 시각적으로 보기 좋은 코드 커버리지 결과를 확인할 수 있습니다. 벤치 커버리지 정보도 포함됩니다. Add 함수에서 조건을 만족시키지 못하는 경우에 대한 테스트 케이스가 없으므로 해당 분기의 커버리지가 낮게 나온 것을 확인할 수 있습니다. 이를 통해 테스트 케이스를 추가하여 코드 커버리지를 높일 수 있습니다.


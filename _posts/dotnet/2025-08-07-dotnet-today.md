---
title: "DOTNET - .NET의 NuGet Package Signature Verification"
date: 2025-08-07 21:02:42 +0900
categories: dotnet
tags: [dotnet, 최신기술, 추천, DOTNET, .NET의, NuGet, Package, Signature, Verification]
---

## 오늘의 DOTNET 최신 기술 트렌드: **.NET의 NuGet Package Signature Verification**

**1. 간단한 설명:**

NuGet 패키지 서명 검증은 NuGet 클라이언트가 설치하려는 패키지가 게시자에 의해 실제로 서명되었고, 변경되지 않았음을 확인하는 기능입니다.  공개적으로 신뢰할 수 있는 인증서를 통해 NuGet 패키지의 무결성을 보장하고, 악성코드 삽입이나 변조로부터 개발자를 보호합니다. .NET 개발 환경의 보안을 강화하는 중요한 요소이며, 특히 오픈 소스 의존성이 높은 프로젝트에서 더욱 중요하게 다뤄집니다. 이 기능은 NuGet 6.0부터 도입되었고 지속적으로 개선되고 있습니다.  신뢰할 수 있는 서명자를 정의하고, NuGet이 해당 서명자를 통해 서명된 패키지만 설치하도록 구성하여 더욱 강력한 보안 정책을 적용할 수 있습니다.

**2. 참고할 만한 공식 사이트나 블로그 링크:**

*   **Microsoft Docs - NuGet Package Signing:** [https://learn.microsoft.com/en-us/nuget/concepts/package-signing](https://learn.microsoft.com/en-us/nuget/concepts/package-signing)
*   **Microsoft Docs - NuGet Trusted Signers:** [https://learn.microsoft.com/en-us/nuget/reference/cli-reference/nuget-config-file#trusted-signers](https://learn.microsoft.com/en-us/nuget/reference/cli-reference/nuget-config-file#trusted-signers)
*   **NuGet Blog - Package Signature Verification (Initial Announcement):** 공식 블로그에서 초기 도입 소식을 찾아볼 수 있습니다. 검색 엔진을 통해 찾아보시는 것을 추천드립니다.

**3. 간단한 코드 예시 (C#):**

NuGet 패키지 서명 검증은 코드 자체보다는 NuGet 구성 파일을 통해 관리됩니다. 아래는 `nuget.config` 파일의 예시입니다. 이 예시는 특정 인증서로 서명된 패키지만 허용하도록 설정하는 방법을 보여줍니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <configSections>
    <sectionGroup name="nuget">
      <section name="config" type="NuGet.Configuration.SectionHandler, NuGet.Configuration" />
    </sectionGroup>
  </configSections>
  <nuget>
    <config>
      <add key="signatureValidationMode" value="Require" />
    </config>
    <trustedSigners>
      <certificate fingerprint="AA BB CC DD EE FF 00 11 22 33 44 55 66 77 88 99 AA BB CC DD"
                   hashAlgorithm="SHA256"
                   allowUntrustedRoot="false" />
      <author name="Microsoft">
        <certificate fingerprint="FF EE DD CC BB AA 99 88 77 66 55 44 33 22 11 00 FF EE DD CC"
                     hashAlgorithm="SHA256" />
      </author>
    </trustedSigners>
  </nuget>
</configuration>
```

**설명:**

*   `<config>` 섹션에서 `signatureValidationMode`를 `Require`로 설정하면 서명된 패키지만 설치됩니다.
*   `<trustedSigners>` 섹션에서 신뢰할 수 있는 서명자를 정의합니다.
*   `<certificate>` 요소는 특정 인증서의 지문(fingerprint)과 해시 알고리즘을 지정합니다. `allowUntrustedRoot` 속성은 자체 서명된 인증서를 허용할지 여부를 나타냅니다. (보안상 false가 권장됩니다.)
*   `<author>` 요소는 특정 작성자를 지정하고, 해당 작성자의 인증서를 통해 서명된 패키지만 허용합니다.

**4. 코드 실행 결과 예시:**

위의 `nuget.config` 파일이 설정된 상태에서, Microsoft 또는 지정된 인증서로 서명되지 않은 NuGet 패키지를 설치하려고 하면 다음과 유사한 오류 메시지가 표시됩니다.

```
NU1008: The package 'My.Unsigned.Package' is not signed. Signature validation failed.
```

이 오류는 NuGet이 패키지의 서명을 검증하는 데 실패했음을 나타내며, 패키지 설치가 중단됩니다.


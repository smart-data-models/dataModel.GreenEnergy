<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 광전지 장치  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **데이터 모델은 *STC - 표준 테스트 조건* 및 *NOCT - 정상 작동 셀 온도*에 따라 태양광 패널의 기계적, 전기적 및 열적 특성을 설명하기 위한 것입니다. *주석* : 이 데이터 모델은 `태양광 장치`를 설명하는 주 엔터티로 직접 사용하거나 `refDevice` 속성의 참조를 사용하여 데이터 모델 `DEVICE`의 하위 엔터티로 사용할 수 있습니다. STC 및 NOCT에 대해 수행되는 측정값은 `Pmax`(최대 공칭 전력), `Umpp`(최적 작동 전압), `Impp`(최적 작동 전류), `Uoc`(개방 회로 전압), `Isc`(단락 전류)입니다. *데이터 모델에 대한 추가 정보 :* 이 데이터 모델은 장치[PHOTOVOLTAIC]를 설명하는 주 엔터티로 직접 사용하거나 `refDevice` 속성의 참조를 사용하여 데이터 모델[DEVICE]의 하위 엔터티로 사용할 수 있습니다.**  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `MaxPressureLoad[object]`: 최대 역학 패널에 가해지는 압력(전단, 탄성, 압축) 하중. 형식은 3가지 항목의 하위 속성으로 구성됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **PAL**은 파스칼을 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)	- `hail`:     
	- `snow`:     
	- `wind`:     
- `MaximumSystemVoltage[number]`: 모듈**에 허용되는 최대 시스템 전압입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **VLT**는 볼트를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `NominalPower[number]`: 패널**의 공칭 전력입니다. 모듈STC] 속성에 대한 [Pmax] 항목의 값과 동일합니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **WTT**는 와트를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `PanelNbModules[number]`: '패널' 당 '모듈' 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `application[array]`: 태양 전지판 유형에 관한 대상 애플리케이션(이 경우 '전기'). 고유 값. https://schema.org/Text. 열거형:'전기, 열, 기타'  - `applicationClass[array]`: 모듈과 관련된 잠재적 위험에 대한 평가입니다. 고유한 값입니다. 열거형:'A, B, C'  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaWeight[number]`: 면적 무게는 Kg/m² 단위로 측정됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **28**은 평방미터당 킬로그램을 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `brandName[string]`: 품목의 브랜드 이름  . Model: [https://schema.org/brand](https://schema.org/brand)- `cellDimension[object]`: 셀의 외부 치수입니다. 형식은 3개 항목의 하위 속성으로 구성됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MMT**는 밀리미터를 나타냅니다.  	- `length`:     
	- `thickness`:     
	- `width`:     
- `cellOperatingTemperature[object]`: 태양 에너지를 수집하는 셀의 공칭 작동 온도 범위입니다. 형식은 2개 항목의 하위 속성으로 구성됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **CEL**은 섭씨도를 나타냅니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `max`:     
	- `min`:     
- `cellType[array]`: 광전지 장치를 만드는 데 사용되는 셀의 종류. 2가지 기술 *`크리스탈린`* 또는 *`박막`*. 고유한 값입니다. 열거형: '비정질실리콘, CfTe, CIS, 단결정, 다결정, 기타'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateLastReported[date-time]`: 디바이스가 데이터를 성공적으로 보고한 마지막 시간을 나타내는 타임스탬프입니다. ISO8601 UTC 형식의 날짜 및 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `documentation[string]`: 기술 문서(설치/유지보수/사용)  . Model: [https://schema.org/Text](https://schema.org/Text)- `fireClass[array]`: 화재에 대한 평가(IEC 61730). 고유한 값입니다. 열거형:'A, B, C'  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `installationCondition[array]`: 다음 환경에서의 사용 조건 및 가능성. 조합. Enum:'사막, 먼지, 극한더위, 극한추위, 극한기후, 극한습도, 해양, 없음, 기타, 식염수, 모래, 지진'  . Model: [https://schema.org/Text](https://schema.org/Text)- `installationMode[array]`: 지상 기준 시스템과 관련된 장치의 위치입니다. 고유한 값입니다. 열거형: '접지, 기타, 기둥, 지붕, 벽'  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `manufacturerName[string]`: 품목의 제조업체 이름  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `modelName[string]`: 품목의 모델명  . Model: [https://schema.org/model](https://schema.org/model)- `moduleDimension[object]`:  모듈의 외부 치수입니다. 모듈은 1개에서 n개의 셀로 구성된 집합체일 수 있습니다. 형식은 3개 항목의 하위 속성으로 구성됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MMT**는 밀리미터를 나타냅니다.  	- `length`:     
	- `thickness`:     
	- `width`:     
- `moduleNOCT[object]`: 정상 작동 셀 온도 측정. 형식은 5가지 항목의 하위 속성으로 구성됩니다. Pmax(와트). Umpp(볼트). Impp(암페어). Uoc(볼트). Isc(암페어)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `Impp`:     
	- `Isc`:     
	- `Pmax`:     
	- `Umpp`:     
	- `Uoc`:     
- `moduleNbCells[number]`: '모듈' 당 '셀' 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `moduleSTC[object]`: 표준 테스트 조건 측정. 형식은 5가지 항목의 하위 속성으로 구성됩니다. Pmax(와트). Umpp(볼트). Impp(암페어). Uoc(볼트). Isc(암페어)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `Impp`:     
	- `Isc`:     
	- `Pmax`:     
	- `Umpp`:     
	- `Uoc`:     
- `moduleYieldRate[number]`: 지상 기준 시스템과 관련된 장치의 위치입니다. 고유한 가치  . Model: [https://schema.org/Number](https://schema.org/Number)- `nTCClass[number]`: 음의 온도 저항 계수(*NTC*)는 주어진 음의 온도 변화와 관련된 물리적 특성의 상대적 변화를 설명합니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어, **P1**은 퍼센트(%)를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pTCClass[number]`:  양온도 저항계수(*PTC*)는 주어진 양온도 변화와 관련된 물리적 특성의 상대적 변화를 설명합니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어, **P1**은 퍼센트(%)를 나타냅니다.  - `panelDimension[object]`: 패널의 외부 치수. 태양광 패널은 태양 광선으로부터 열을 모으는 여러 개의 셀로 구성된 1~n개의 모듈로 구성된 집합체일 수 있습니다. 형식은 3개 항목의 하위 속성으로 구성됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MMT**는 밀리미터를 나타냅니다.  	- `length`:     
	- `thickness`:     
	- `width`:     
- `panelLifetime[number]`: 패널의 평균 수명. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **ANN**은 연도를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `panelOperatingTemperature[object]`: 주변 작동 온도 범위. 패널을 사용하기 위한 최소 및 최대 추위와 열에 대한 저항력입니다. 형식은 두 가지 항목의 하위 속성으로 구성됩니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **CEL**은 섭씨도를 나타냅니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `max`:     
	- `min`:     
- `panelWeight[number]`: 패널의 무게(때때로 사용되는 기준은 Kg/㎡입니다). 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **KGM**은 킬로그램을 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `panelYieldCurve[array]`: 옵션 1. T0]의 [NominalPower] 및 [panelLifetime]에 따른 패널의 에너지 생산량 곡선. 목록에 제공된 측정값은 제조업체에서 제공한 정보에 따라 '단계'가 5년인 5년부터 시작하여 퍼센트로 표시되는 에너지 생산 능력의 시퀀스입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다. 예를 들어 **P1**은 퍼센트를 나타냅니다.  - `performanceLowIrradiance[number]`: 낮은 조도에서 성능에 대한 평균 상대적 수율. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **P1**은 퍼센트(%)를 나타냅니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `possibilityOfUse[array]`: 사용 가능성. 고유한 값입니다. Enum:'혼합, 모바일, 기타, 고정'  . Model: [https://schema.org/Text](https://schema.org/Text)- `protectionIP[string]`: 정션 박스에 대한 IP '침입 보호'. 이 등급은 국제전기기술위원회 표준(EN 60-529)에 따라 침입, 먼지, 우발적 접촉, 물로부터 기계식 케이스와 전기 인클로저가 제공하는 보호 수준을 분류하고 등급을 매깁니다. 첫 번째 숫자: 고체 입자 보호(단일 숫자: 0-6 또는 'X'). 두 번째 숫자: 액체 유입 보호(단일 숫자: 0-9 또는 'X' ).세 번째 숫자: 위험한 부품에 대한 접근으로부터 개인 보호(선택적 추가 문자). 네 번째 숫자: 기타 보호 기능(선택적 추가 문자)  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: 두 번째 링크로 사용되는 경우 메인 엔티티 [디바이스](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)에 대한 참조  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: 리포지토리와 연결된 [관심 지점](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)에 대한 참조  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `serialNumber[array]`: 제조업체에서 공급하고 단일 위치에서 작동 모드로 조립된 광전지 장치의 일련 번호 목록  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `temperatureCoefficient[object]`:  패널의 온도 영향 계수입니다. 형식은 3가지 항목의 하위 속성으로 구성됩니다. Pmax(와트). Uoc(볼트). Isc(암페어)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `Isc`:     
	- `Pmax`:     
	- `Uoc`:     
- `type[string]`: NGSI 엔티티 유형. PhotovoltaicDevice여야 합니다.  - `typeOfUse[array]`: 실내/실외 환경에서의 위치와 관련하여 허용된 용도. 고유한 값입니다. Enum:'실내, 실외, 혼합, 기타'  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `dateLastReported`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
STC 및 NOCT에 대해 수행되는 측정은 다음과 같습니다. [Pmax] **WTT**로 측정된 최대 공칭 전력은 와트를 나타냅니다. - Umpp] **VLT**로 측정된 최적 작동 전압은 볼트를 나타냅니다. - Impp] **AMP**로 측정된 최적 작동 전류는 암페어를 나타냅니다. - Uoc] **VLT**로 측정된 개방 회로 전압은 볼트를 나타냅니다. - Isc] **AMP**로 측정된 단락 전류는 암페어를 나타냅니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhotovoltaicDevice:    
  description: 'The Data Model is intended to describe the mechanical, electrical and thermal characteristics of photo-voltaic panels according to *STC - Standard Test Condition* and *NOCT - Normal Operating Cell Temperature*. *Remark* : This Data Model can be used directly as a main entity to describe the `Photovoltaic Device`  or as a sub-entity of the Data Model  `DEVICE` using a reference by the `refDevice` attribute. The measures performed for STC and NOCT are `Pmax` (Maximum Nominal Power), `Umpp` (Optimal operating voltage), `Impp` (Optimal Operating Current), `Uoc` (Open Circuit Voltage), `Isc` (Short Circuit Current). *Additional Information about Data Model:* This Data Model can be used directly as a main entity to describe the device [PHOTOVOLTAIC] or as a sub-entity of the Data Model [DEVICE] using a reference by the `refDevice` attribute.'    
  properties:    
    MaxPressureLoad:    
      description: 'aximum mechanics Pressure (shear, elasticity, compression) load on a Panel. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **PAL** represents Pascal'    
      properties:    
        hail:    
          minimum: 0    
          type: number    
        snow:    
          minimum: 0    
          type: number    
        wind:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Pascal    
    MaximumSystemVoltage:    
      description: 'Maximum system voltage permitted for the **module**. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    NominalPower:    
      description: 'Nominal Power for the **panel**. This is the same value of items [Pmax] for [moduleSTC] attribute. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **WTT** represents Watt'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: watts    
    PanelNbModules:    
      description: Number of 'Modules' per 'Panel'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    application:    
      description: 'Target application regarding the Type of Solar panel (In our case `electric`). A unique value. https://schema.org/Text. Enum:''electric, thermal, other'''    
      items:    
        enum:    
          - electric    
          - thermal    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    applicationClass:    
      description: 'Evaluation of the potential hazards associated with the module. A unique value. Enum:''A, B, C'''    
      items:    
        enum:    
          - A    
          - B    
          - C    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaWeight:    
      description: 'Area Weight measured in Kg/m². The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **28** represents Kilogram per square meter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilograms per square meter    
    brandName:    
      description: Brand Name of the item    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    cellDimension:    
      description: 'External dimension of a cell. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter'    
      properties:    
        length:    
          minimum: 0    
          type: number    
        thickness:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    cellOperatingTemperature:    
      description: 'This is the nominal operating temperature range of the cells in which it collects solar energy. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Degree Celsius    
    cellType:    
      description: 'Type of cells used to built the photo-voltaic unit. 2 kinds of Technologies *`Cristalline`* or  *`Thin layers`*. A unique value. Enum:''amorphousSilicon, CfTe, CIS, monocrystalline, polycrystalline, other'''    
      items:    
        enum:    
          - amorphousSilicon    
          - CfTe    
          - CIS    
          - monocrystalline    
          - polycrystalline    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastReported:    
      description: A timestamps which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    documentation:    
      description: Technical Documentation (Installation / maintenance / used)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fireClass:    
      description: 'Evaluation to the fire (IEC 61730). A unique value. Enum:''A, B, C'''    
      items:    
        enum:    
          - A    
          - B    
          - C    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    installationCondition:    
      description: 'Condition and possibility of use in the following environments. A combination. Enum:''desert, dust, extremeHeat, extremeCold, extremeClimate, extremeHumidity, marine, none, other, saline, sand, seismic'''    
      items:    
        enum:    
          - desert    
          - dust    
          - extremeHeat    
          - extremeCold    
          - extremeClimate    
          - extremeHumidity    
          - marine    
          - none    
          - other    
          - saline    
          - sand    
          - seismic    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    installationMode:    
      description: 'Positioning of the device in relation to a ground reference system. A unique value. Enum:''ground, other, pole, roofing, wall'''    
      items:    
        enum:    
          - ground    
          - other    
          - pole    
          - roofing    
          - wall    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    manufacturerName:    
      description: Manufacturer Name of the item    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    modelName:    
      description: Model Name of the item    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    moduleDimension:    
      description: ' External dimension of a module. A module can be an assembly of 1 to n cells. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter'    
      properties:    
        length:    
          minimum: 0    
          type: number    
        thickness:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
        units: Millimeters    
    moduleNOCT:    
      description: Normal Operating Cell Temperature measurements. The format is structured by a sub-property of 5 items. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere    
      properties:    
        Impp:    
          minimum: 0    
          type: number    
        Isc:    
          minimum: 0    
          type: number    
        Pmax:    
          minimum: 0    
          type: number    
        Umpp:    
          minimum: 0    
          type: number    
        Uoc:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    moduleNbCells:    
      description: Number of 'cells' per 'module'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    moduleSTC:    
      description: Standard Test Condition measurements. The format is structured by a sub-property of 5 items. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere    
      properties:    
        Impp:    
          minimum: 0    
          type: number    
        Isc:    
          minimum: 0    
          type: number    
        Pmax:    
          minimum: 0    
          type: number    
        Umpp:    
          minimum: 0    
          type: number    
        Uoc:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    moduleYieldRate:    
      description: Positioning of the device in relation to a ground reference system. A unique value    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    nTCClass:    
      description: 'The Negative Temperature Coefficient of resistance - *NTC*, describes the relative change of a physical property that is associated with a given change in negative temperature. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    pTCClass:    
      description: ' The Positive Temperature Coefficient of resistance - *PTC*, describes the relative change of a physical property that is associated with a given change in positive temperature. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    panelDimension:    
      description: 'External dimension of a Panel. A solar panel can be an assembly of 1 to n modules, which themselves are made of several cells which collect heat from the sun''s rays. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter'    
      properties:    
        length:    
          minimum: 0    
          type: number    
        thickness:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    panelLifetime:    
      description: 'Average lifetime of a panel. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **ANN** represents Year'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: year    
    panelOperatingTemperature:    
      description: 'Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat for using the panel. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: -50    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Degree Celsius    
    panelWeight:    
      description: 'Weight of a panel (Sometime the reference used is Kg / m²). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilogram'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilograms    
    panelYieldCurve:    
      description: 'Option 1. Energy production yield curve of the panel from its [NominalPower] at [T0] and along its [panelLifetime]. The Measurements provided in the list are a sequence of Energy Production Capacity represented in Percent starting at 5 years with a ''Step'' of 5 years according to the information provided by the manufacturer. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent. '    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    performanceLowIrradiance:    
      description: 'Average relative yield to Performance at Low Irradiance. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    possibilityOfUse:    
      description: 'Possibility of use. A unique value. Enum:''mixed, mobile, other, stationary'''    
      items:    
        enum:    
          - mixed    
          - mobile    
          - other    
          - stationary    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    protectionIP:    
      description: 'IP ''Ingress Protection'' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). First digit: Solid particle protection (Single numeral: 0–6 or ''X''). Second digit: Liquid ingress protection (Single numeral: 0–9 or ''X'' ).Third digit: Personal Protection  against access to dangerous parts (optional additional letter). Fourth digit: Other protections (optional additional letter)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    refDevice:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    serialNumber:    
      description: List of serial numbers of Photo-voltaic device supplied by the manufacturer and assembled in operating mode on a single location    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    temperatureCoefficient:    
      description: ' Temperature influence coefficient on the panel. The format is structured by a sub-property of 3 items. Pmax in Watt. Uoc in Volt. Isc in Ampere'    
      properties:    
        Isc:    
          minimum: 0    
          type: number    
        Pmax:    
          minimum: -1    
          type: number    
        Uoc:    
          minimum: -1    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PhotovoltaicDevice    
      enum:    
        - PhotovoltaicDevice    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfUse:    
      description: 'Accepted use regarding its positioning in an indoor / outdoor environment. A unique value. Enum:''indoor, outdoor, mixed, other'''    
      items:    
        enum:    
          - indoor    
          - outdoor    
          - mixed    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/PhotovoltaicDevice/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### PhotovoltaicDevice NGSI-v2 키값 예시  
다음은 키-값으로 JSON-LD 형식의 PhotovoltaicDevice의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
  "type": "PhotovoltaicDevice",  
  "name": "DEVICE-PV-T2-R-012",  
  "alternateName": "AirPort – global Observation",  
  "description": "Photo-voltaic Device description",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Roof 2 - Local  12"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:PV-T2-R-012",  
  "dateLastReported": "2020-05-17T09:47:00Z",  
  "brandName": "Canadian Solar",  
  "modelName": "CS6P-270P",  
  "manufacturerName": "Canadian Solar EMEA GmbH,",  
  "serialNumber": [  
    "CSPV270P-SN1804L6J34Z8742H",  
    "CSPV270P-SN1804L6J34Z8743H",  
    "CSPV270P-SN1804L6J34Z8744H",  
    "CSPV270P-SN1804L6J34Z8745H",  
    "CSPV270P-SN1804L6J34Z8746H"  
  ],  
  "application": ["electric"],  
  "cellType": ["polycrystalline"],  
  "installationMode": ["roofing"],  
  "installationCondition": [  
    "extremeHeat",  
    "extremeCold",  
    "extremeClimate",  
    "desert"  
  ],  
  "possibilityOfUsed": "stationary",  
  "integrationMode": "IAB",  
  "documentation": "https://www.myDevicePV.Cn",  
  "owners": [  
    "Airport-Division Maintenance"  
  ],  
  "cellDimension": {  
    "length": 16.0,  
    "width": 9.0,  
    "thickness": 2.3  
  },  
  "moduleNbCells": 60,  
  "moduleDimension": {  
    "length": 1600,  
    "width": 975,  
    "thickness": 3.75  
  },  
  "panelNbModules": 1,  
  "panelDimension": {  
    "length": 1638,  
    "width": 982,  
    "thickness": 40  
  },  
  "panelWeight": 18,  
  "arealWeight": 32,  
  "maxPressureLoad": {  
    "hail": 2500,  
    "snow": 5400,  
    "wind": 2400  
  },  
  "NominalPower": 270,  
  "MaximumSystemVoltage": 1000,  
  "applicationClass": ["A"],  
  "fireClass": ["C"],  
  "pTCClass": 92.1,  
  "nTCClass": 88.3,  
  "protectionIP": "IP67",  
  "moduleSTC": {  
    "Pmax": 270,  
    "Umpp": 30.8,  
    "Impp": 8.75,  
    "Uoc": 37.9,  
    "Isc": 9.32  
  },  
  "moduleNOCT": {  
    "Pmax": 196,  
    "Umpp": 28.1,  
    "Impp": 6.97,  
    "Uoc": 34.8,  
    "Isc": 7.55  
  },  
  "moduleYieldRate": 16.79,  
  "panelOperatingTemperature": {  
    "min": -40,  
    "max": 85  
  },  
  "cellOperatingTemperature": {  
    "min": 45,  
    "max": 2  
  },  
  "temperatureCoefficient": {  
    "Pmax": -0.41,  
    "Uoc": -0.31,  
    "Isc": 0.053  
  },  
  "performanceLowIrradiance": 96.5,  
  "panelLifetime": 30,  
  "panelYieldCurve": [  
    "95.0",  
    "92.5",  
    "90.0",  
    "87.5",  
    "85.0",  
    "80.0"  
  ],  
  "panelYieldRate": 0.5,  
  "panelTiltReference": {  
    "min": 28,  
    "max": 37  
  }  
}  
```  
</details>  
#### PhotovoltaicDevice NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PhotovoltaicDevice의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
  "type": "PhotovoltaicDevice",  
  "name": {  
    "type": "Property",  
    "value": "DEVICE-PV-T2-R-012"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort – global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Photo-voltaic Device description"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Roof 2 - Local  12"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Device:PV-T2-R-012"  
  },  
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-05-17T09:47:00Z"  
    }  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "Canadian Solar"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "CS6P-270P"  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "Canadian Solar EMEA GmbH,"  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": [  
      "CSPV270P-SN1804L6J34Z8742H",  
      "CSPV270P-SN1804L6J34Z8743H",  
      "CSPV270P-SN1804L6J34Z8744H",  
      "CSPV270P-SN1804L6J34Z8745H",  
      "CSPV270P-SN1804L6J34Z8746H"  
    ]  
  },  
  "application": {  
    "type": "Property",  
    "value": ["electric"]  
  },  
  "cellType": {  
    "type": "Property",  
    "value": ["polycrystalline"]  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": ["roofing"]  
  },  
  "installationCondition": {  
    "type": "Property",  
    "value": [  
      "extremeHeat",  
      "extremeCold",  
      "extremeClimate",  
      "desert"  
    ]  
  },  
  "possibilityOfUsed": {  
    "type": "Property",  
    "value": "stationary"  
  },  
  "integrationMode": {  
    "type": "Property",  
    "value": "IAB"  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myDevicePV.Cn"  
  },  
  "owners": {  
    "type": "Property",  
    "value": [  
      "Airport-Division Maintenance"  
    ]  
  },  
  "cellDimension": {  
    "type": "Property",  
    "value": {  
      "length": 16.0,  
      "width": 9.0,  
      "thickness": 2.3  
    }  
  },  
  "moduleNbCells": {  
    "type": "Property",  
    "value": 60  
  },  
  "moduleDimension": {  
    "type": "Property",  
    "value": {  
      "length": 1600,  
      "width": 975,  
      "thickness": 3.75  
    }  
  },  
  "panelNbModules": {  
    "type": "Property",  
    "value": 1  
  },  
  "panelDimension": {  
    "type": "Property",  
    "value": {  
      "length": 1638,  
      "width": 982,  
      "thickness": 40  
    }  
  },  
  "panelWeight": {  
    "type": "Property",  
    "value": 18  
  },  
  "arealWeight": {  
    "type": "Property",  
    "value": 32  
  },  
  "maxPressureLoad": {  
    "type": "Property",  
    "value": {  
      "hail": 2500,  
      "snow": 5400,  
      "wind": 2400  
    }  
  },  
  "NominalPower": {  
    "type": "Property",  
    "value": 270  
  },  
  "MaximumSystemVoltage": {  
    "type": "Property",  
    "value": 1000  
  },  
  "applicationClass": {  
    "type": "Property",  
    "value": ["A"]  
  },  
  "fireClass": {  
    "type": "Property",  
    "value": ["C"]  
  },  
  "pTCClass": {  
    "type": "Property",  
    "value": 92.1  
  },  
  "nTCClass": {  
    "type": "Property",  
    "value": 88.3  
  },  
  "protectionIP": {  
    "type": "Property",  
    "value": "IP67"  
  },  
  "moduleSTC": {  
    "type": "Property",  
    "value": {  
      "Pmax": 270,  
      "Umpp": 30.8,  
      "Impp": 8.75,  
      "Uoc": 37.9,  
      "Isc": 9.32  
    }  
  },  
  "moduleNOCT": {  
    "type": "Property",  
    "value": {  
      "Pmax": 196,  
      "Umpp": 28.1,  
      "Impp": 6.97,  
      "Uoc": 34.8,  
      "Isc": 7.55  
    }  
  },  
  "moduleYieldRate": {  
    "type": "Property",  
    "value": 16.79  
  },  
  "panelOperatingTemperature": {  
    "type": "Property",  
    "value": {  
      "min": -40,  
      "max": 85  
    }  
  },  
  "cellOperatingTemperature": {  
    "type": "Property",  
    "value": {  
      "min": 45,  
      "max": 2  
    }  
  },  
  "temperatureCoefficient": {  
    "type": "Property",  
    "value": {  
      "Pmax": -0.41,  
      "Uoc": -0.31,  
      "Isc": 0.053  
    }  
  },  
  "performanceLowIrradiance": {  
    "type": "Property",  
    "value": 96.5  
  },  
  "panelLifetime": {  
    "type": "Property",  
    "value": 30  
  },  
  "panelYieldCurve": {  
    "type": "Property",  
    "value": [  
      "95.0",  
      "92.5",  
      "90.0",  
      "87.5",  
      "85.0",  
      "80.0"  
    ]  
  },  
  "panelYieldRate": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "panelTiltReference": {  
    "type": "Property",  
    "value": {  
      "min": 28,  
      "max": 37  
    }  
  }  
}  
```  
</details>  
#### PhotovoltaicDevice NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 PhotovoltaicDevice의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
  "type": "PhotovoltaicDevice",  
  "name": "DEVICE-PV-T2-R-012",  
  "alternateName": "AirPort â€“ global Observation",  
  "description": "Photo-voltaic Device description",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Roof 2 - Local  12"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDevice": "urn:ngsi-ld:Device:PV-T2-R-012",  
  "dateLastReported": "2020-05-17T09:47:00Z",  
  "brandName": "Canadian Solar",  
  "modelName": "CS6P-270P",  
  "manufacturerName": "Canadian Solar EMEA GmbH,",  
  "serialNumber": [  
    "CSPV270P-SN1804L6J34Z8742H",  
    "CSPV270P-SN1804L6J34Z8743H",  
    "CSPV270P-SN1804L6J34Z8744H",  
    "CSPV270P-SN1804L6J34Z8745H",  
    "CSPV270P-SN1804L6J34Z8746H"  
  ],  
  "application": ["electric"],  
  "cellType": ["polycrystalline"],  
  "installationMode": ["roofing"],  
  "installationCondition": [  
    "extremeHeat",  
    "extremeCold",  
    "extremeClimate",  
    "desert"  
  ],  
  "possibilityOfUsed": "stationary",  
  "integrationMode": "IAB",  
  "documentation": "https://www.myDevicePV.Cn",  
  "owners": [  
    "Airport-Division Maintenance"  
  ],  
  "cellDimension": {  
    "length": 16.0,  
    "width": 9.0,  
    "thickness": 2.3  
  },  
  "moduleNbCells": 60,  
  "moduleDimension": {  
    "length": 1600,  
    "width": 975,  
    "thickness": 3.75  
  },  
  "panelNbModules": 1,  
  "panelDimension": {  
    "length": 1638,  
    "width": 982,  
    "thickness": 40  
  },  
  "panelWeight": 18,  
  "arealWeight": 32,  
  "maxPressureLoad": {  
    "hail": 2500,  
    "snow": 5400,  
    "wind": 2400  
  },  
  "NominalPower": 270,  
  "MaximumSystemVoltage": 1000,  
  "applicationClass": ["A"],  
  "fireClass": ["C"],  
  "pTCClass": 92.1,  
  "nTCClass": 88.3,  
  "protectionIP": "IP67",  
  "moduleSTC": {  
    "Pmax": 270,  
    "Umpp": 30.8,  
    "Impp": 8.75,  
    "Uoc": 37.9,  
    "Isc": 9.32  
  },  
  "moduleNOCT": {  
    "Pmax": 196,  
    "Umpp": 28.1,  
    "Impp": 6.97,  
    "Uoc": 34.8,  
    "Isc": 7.55  
  },  
  "moduleYieldRate": 16.79,  
  "panelOperatingTemperature": {  
    "min": -40,  
    "max": 85  
  },  
  "cellOperatingTemperature": {  
    "min": 45,  
    "max": 2  
  },  
  "temperatureCoefficient": {  
    "Pmax": -0.41,  
    "Uoc": -0.31,  
    "Isc": 0.053  
  },  
  "performanceLowIrradiance": 96.5,  
  "panelLifetime": 30,  
  "panelYieldCurve": [  
    "95.0",  
    "92.5",  
    "90.0",  
    "87.5",  
    "85.0",  
    "80.0"  
  ],  
  "panelYieldRate": 0.5,  
  "panelTiltReference": {  
    "min": 28,  
    "max": 37  
  },  
  "@context": [  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PhotovoltaicDevice NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PhotovoltaicDevice의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
  "type": "PhotovoltaicDevice",  
  "name": {  
    "type": "Property",  
    "value": "DEVICE-PV-T2-R-012"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort â€“ global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Photo-voltaic Device description"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Roof 2 - Local  12"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Device:PV-T2-R-012"  
  },  
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-05-17T09:47:00Z"  
    }  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "Canadian Solar"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "CS6P-270P"  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "Canadian Solar EMEA GmbH,"  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": [  
      "CSPV270P-SN1804L6J34Z8742H",  
      "CSPV270P-SN1804L6J34Z8743H",  
      "CSPV270P-SN1804L6J34Z8744H",  
      "CSPV270P-SN1804L6J34Z8745H",  
      "CSPV270P-SN1804L6J34Z8746H"  
    ]  
  },  
  "application": {  
    "type": "Property",  
    "value": ["electric"]  
  },  
  "cellType": {  
    "type": "Property",  
    "value": ["polycrystalline"]  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": ["roofing"]  
  },  
  "installationCondition": {  
    "type": "Property",  
    "value": [  
      "extremeHeat",  
      "extremeCold",  
      "extremeClimate",  
      "desert"  
    ]  
  },  
  "possibilityOfUsed": {  
    "type": "Property",  
    "value": "stationary"  
  },  
  "integrationMode": {  
    "type": "Property",  
    "value": "IAB"  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myDevicePV.Cn"  
  },  
  "owners": {  
    "type": "Property",  
    "value": [  
      "Airport-Division Maintenance"  
    ]  
  },  
  "cellDimension": {  
    "type": "Property",  
    "value": {  
      "length": 16.0,  
      "width": 9.0,  
      "thickness": 2.3  
    }  
  },  
  "moduleNbCells": {  
    "type": "Property",  
    "value": 60  
  },  
  "moduleDimension": {  
    "type": "Property",  
    "value": {  
      "length": 1600,  
      "width": 975,  
      "thickness": 3.75  
    }  
  },  
  "panelNbModules": {  
    "type": "Property",  
    "value": 1  
  },  
  "panelDimension": {  
    "type": "Property",  
    "value": {  
      "length": 1638,  
      "width": 982,  
      "thickness": 40  
    }  
  },  
  "panelWeight": {  
    "type": "Property",  
    "value": 18  
  },  
  "arealWeight": {  
    "type": "Property",  
    "value": 32  
  },  
  "maxPressureLoad": {  
    "type": "Property",  
    "value": {  
      "hail": 2500,  
      "snow": 5400,  
      "wind": 2400  
    }  
  },  
  "NominalPower": {  
    "type": "Property",  
    "value": 270  
  },  
  "MaximumSystemVoltage": {  
    "type": "Property",  
    "value": 1000  
  },  
  "applicationClass": {  
    "type": "Property",  
    "value": ["A"]  
  },  
  "fireClass": {  
    "type": "Property",  
    "value": ["C"]  
  },  
  "pTCClass": {  
    "type": "Property",  
    "value": 92.1  
  },  
  "nTCClass": {  
    "type": "Property",  
    "value": 88.3  
  },  
  "protectionIP": {  
    "type": "Property",  
    "value": "IP67"  
  },  
  "moduleSTC": {  
    "type": "Property",  
    "value": {  
      "Pmax": 270,  
      "Umpp": 30.8,  
      "Impp": 8.75,  
      "Uoc": 37.9,  
      "Isc": 9.32  
    }  
  },  
  "moduleNOCT": {  
    "type": "Property",  
    "value": {  
      "Pmax": 196,  
      "Umpp": 28.1,  
      "Impp": 6.97,  
      "Uoc": 34.8,  
      "Isc": 7.55  
    }  
  },  
  "moduleYieldRate": {  
    "type": "Property",  
    "value": 16.79  
  },  
  "panelOperatingTemperature": {  
    "type": "Property",  
    "value": {  
      "min": -40,  
      "max": 85  
    }  
  },  
  "cellOperatingTemperature": {  
    "type": "Property",  
    "value": {  
      "min": 45,  
      "max": 2  
    }  
  },  
  "temperatureCoefficient": {  
    "type": "Property",  
    "value": {  
      "Pmax": -0.41,  
      "Uoc": -0.31,  
      "Isc": 0.053  
    }  
  },  
  "performanceLowIrradiance": {  
    "type": "Property",  
    "value": 96.5  
  },  
  "panelLifetime": {  
    "type": "Property",  
    "value": 30  
  },  
  "panelYieldCurve": {  
    "type": "Property",  
    "value": [  
      "95.0",  
      "92.5",  
      "90.0",  
      "87.5",  
      "85.0",  
      "80.0"  
    ]  
  },  
  "panelYieldRate": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "panelTiltReference": {  
    "type": "Property",  
    "value": {  
      "min": 28,  
      "max": 37  
    }  
  },  
  "@context": [  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: SolarTracker  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
전역 설명: **솔라 트래커 데이터 모델 설명**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없으면 여러 유형이나 다른 형식/패턴을 가질 수 있습니다.</sub></sup>  
- `address[object]`: 우편 주소. 모델: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예: 스페인. 모델: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 지역. 모델: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 지역이 속한 지역. 모델: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 일부 국가에서 지역 정부가 관리하는 행정 구역 유형    
	- `postOfficeBoxNumber[string]`: 우체국 사서함 번호. 예: 03578. 모델: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호. 예: 24004. 모델: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 도로 주소. 모델: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로에서 특정 속성을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `altitude[number]`: 해수면 위의 설치 장소 고도. 이 값은 태양의 위치와 대기折射을 계산하기 위해 태양 알고리즘에서 사용됩니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: 서비스 또는 제공된 항목이 제공되는 지리적 영역. 모델: [https://schema.org/Text](https://schema.org/Text)- `backtracking[string]`: 열거형:'on','off'. 태양 트래커가 행간 그림자 방지 위해 최적의 태양각 위치에서 벗어나 백트래킹 모드인지 여부를 나타냅니다. 모델: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]`: 배터리의 현재 충전 수준을 총 용량의 백분율(0~100)로 표시합니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `boardDirection[string]`: 열거형:'-1','1'. 제어 보드의 물리적 방향을 지정합니다(동쪽을 향한 = 1, 서쪽을 향한 = -1). 모델: [https://schema.org/Text](https://schema.org/Text)- `currentAngle[number]`: 패널의 현재 각도 위치. 0은 패널이 수평(직접 위를 향함)임을 나타냅니다. 최소값은 동쪽 방향, 최대값은 서쪽 방향을 나타냅니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `currentPowerConsumption[number]`: 와트 단위로 측정된 실시간 전기 전력 수요. 모델: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티를 제공하는 공급자의 고유 식별자 시퀀스  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 보통 저장 플랫폼에서 할당됩니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프. 보통 저장 플랫폼에서 할당됩니다.  - `dateUpdate[date-time]`: 구성이 업데이트된 날짜. 모델: [http://schema.org/DateTime](http://schema.org/DateTime)- `description[string]`: 이 항목에 대한 설명  - `deviceCategory[string]`: 열거형:'PCU','FCU','SCU'. 시스템 내의 장치 분류를 지정합니다. 모델: [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`: 열거형:'Online','Offline'. 장치의 현재 작동 연결 상태를 나타냅니다. 모델: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `ipAddress[array]`: 장치의 IP 주소 목록. 값이 여러 개일 경우 쉼표로 구분된 목록일 수 있습니다. 모델: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 Geojson 참조. 점, 선, 다각형, 다중 점, 다중 선, 다중 다각형 중 하나일 수 있습니다.  - `maxAngleLimit[number]`: 서쪽으로 허용되는 최대 각도 위치. 이 소프트웨어 제한은 하드 상한으로 작용하며, 계산된 대상 각도가 더 큰 경우에도 패널은 이 값 이상으로 회전하지 않습니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `maxPowerRecorded[number]`: 마지막 이동 중에 기록된 활성 전기 전력 소비의最高 수준. 와트 단위로 측정됩니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `maxPowerThreshold[number]`: 모터 작동 중 전력 소비의 안전 한계. 전기 전력이 이 임계값을 초과하면 패널 이동이 즉시 중단되어 기계적 손상이나 모터 과부하를 방지합니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `minAngleLimit[number]`: 동쪽으로 허용되는 최소 각도 위치. 이 매개변수는 필수 작동 경계를 정의하며, 요청된 대상 위치와 관계없이 패널은 이 값 이상으로 동쪽으로 회전하지 않습니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `minPowerRecorded[number]`: 마지막 이동 중에 기록된 활성 전기 전력 소비의 최저 수준. 와트 단위로 측정됩니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `motorDirection[string]`: 열거형:'-1','1'. 모터의 물리적 마운팅 방향을 정의하며, 회전의 극성(동쪽을 향한 = 1, 서쪽을 향한 = -1)을 결정합니다. 모델: [https://schema.org/Text](https://schema.org/Text)- `movementInterval[string]`: 열거형:'5','10','15'. 패널이 자신의 위치를 조정하는 시간 빈도를 정의합니다. 값은 미리 정의된 간격 중 하나여야 합니다: 5, 10 또는 15분. 모델: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 이 항목의 이름  - `operatingMode[string]`: 열거형:'자동','수동','안전 눈','안전 눈 센서','안전 바람','안전 바람 센서','유지 보수'. 패널의 현재 기능 상태를 정의합니다. 이 모드에는 태양 알고리즘을 따르는지 또는 외부 오버라이드/안전 이벤트에 반응하는지 여부가 결정됩니다. 모델: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 고유 ID의 JSON으로 인코딩된 문자 시퀀스를 포함하는 목록  - `panelLength[number]`: 회전축에 수직인 축을 따라 측정된 패널의 치수. 이 값은 패널에 의해投影되는 그림자와 적절한 백트래킹 운동을 계산하는 데 중요합니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `restingAngle[number]`: 패널이 밤이나 지평선 아래에 있을 때 가정하는 특정 각도 위치. 이 위치는 트래커를 다음 일출까지 주차하는 데 사용됩니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URI 목록  - `snowSafetyAngle[number]`: 눈 이벤트 동안 패널이 채택해야 하는 특정 각도 위치. 이 각도는 눈이 쉽게 떨어지도록 설계되어 있으며, 트래커에 과도한 구조적 하중을 방지합니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 엔티티 데이터의 원래 출처를 URL로 제공하는 문자 시퀀스. 출처 공급자의 완전한 도메인 이름 또는 출처 개체의 URL을 추천합니다.  - `targetAngle[number]`: 패널 방향의 대상 각도 설정값. 0은 패널이 수평(직접 위를 향함)임을 나타냅니다. 최소값은 동쪽 방향, 최대값은 서쪽 방향을 나타냅니다. 모델: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: `SolarTracker`와 같아야 합니다.  - `windSafetyAngle[number]`: 바람 속도가 작동 임계값을 초과할 때 패널이 가정하는 안전 설정 각도. 이 위치는帆 효과를 최소화하고 바람의 상승이나 압력으로 인한 구조적 응력을 줄입니다. 모델: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `deviceCategory`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬됨 (자세한 정보를 위해 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>전체 yaml 세부 정보</strong></summary>    
```yaml  
SolarTracker:    
  description: 'Description of the data model SolarTracker '    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    altitude:    
      description: The elevation of the installation site above mean sea level. This value is used by the solar algorithm to refine the calculation of the sun's position and atmospheric refraction    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter (MTR)    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    backtracking:    
      description: Enum:'on','off'. Indicates whether the solar tracker is in backtracking mode to prevent row-to-row shadowing, deviating from the optimal sun-angle position    
      enum:    
        - 'on'    
        - 'off'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryLevel:    
      description: Represents the current charge level of the battery, expressed as a percentage of its total capacity (0 to 100)    
      maximum: 100    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: C62    
    boardDirection:    
      description: Enum:'-1','1'. Specifies the physical orientation of the control board based on the position of the emergency stop button (Eastward-facing = 1; Westward-facing = -1)    
      enum:    
        - '1'    
        - '-1'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    currentAngle:    
      description: The current angular position of the panel. A value of 0 indicates the panel is horizontal (facing directly upward). Minimum values represent an Eastward orientation, while maximum values represent a Westward orientation    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    currentPowerConsumption:    
      description: The real-time electrical power demand measured in Watts    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
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
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateUpdate:    
      description: The date when the configuration was updated    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceCategory:    
      description: Enum:'PCU','FCU','SCU'. Specifies the classification of the device within the system    
      enum:    
        - PCU    
        - FCU    
        - SCU    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceState:    
      description: Enum:'Online','Offline'. Indicates the current operational connectivity status of the device    
      enum:    
        - Online    
        - Offline    
      type: string    
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
        type: Relationship    
    ipAddress:    
      description: List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address    
      items:    
        anyOf:    
          - description: If the IP address meets the requirements of V4 IP address    
            format: ipv4    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          - description: If the IP address meets the requirements of V6 IP address    
            format: ipv6    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
        description: Every item in the list of IP address of the device    
        type: string    
        x-ngsi:    
          model: https://schema.org/Text    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    maxAngleLimit:    
      description: The maximum allowable angular position towards the West. This software limit acts as a hard ceiling; the panel will not rotate beyond this value even if the calculated target angle is greater    
      maximum: 90    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    maxPowerRecorded:    
      description: The highest level of active electrical power consumption recorded during the last movement, measured in Watts    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    maxPowerThreshold:    
      description: The safety limit for power consumption during motor operation. If the electrical power exceeds this threshold, the panel movement is immediately interrupted to prevent mechanical damage or motor overload    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    minAngleLimit:    
      description: The minimum allowable angular position towards the East. This parameter defines a mandatory operational boundary; the panel will not rotate further East than this value, regardless of the requested target position    
      maximum: 0    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    minPowerRecorded:    
      description: The lowest level of active electrical power consumption recorded during the last movement, measured in Watts    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    motorDirection:    
      description: Enum:'-1','1'. Defines the physical mounting orientation of the motor, which determines the polarity of the rotation (Eastward-facing = 1; Westward-facing = -1)    
      enum:    
        - '1'    
        - '-1'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    movementInterval:    
      description: 'Enum:''5'',''10'',''15''. Defines the time frequency at which the panel adjusts its position. The value must be one of the predefined intervals: 5, 10, or 15 minutes'    
      enum:    
        - '5'    
        - '10'    
        - '15'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operatingMode:    
      description: Enum:'automatic','manual','safesnow','safesnowsensor','safewind','safewindsensor','maintenance'. Defines the current functional state of the panel. This mode dictates whether the tracker follows the solar algorithm or responds to external overrides/safety events    
      enum:    
        - automatic    
        - manual    
        - safesnow    
        - safesnowsensor    
        - safewind    
        - safewindsensor    
        - maintenance    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    panelLength:    
      description: The dimension of the panel measured along the axis perpendicular to the axis of rotation. This value is critical for calculating the shadow cast by the panel and determining the appropriate backtracking movement    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter (MTR)    
    restingAngle:    
      description: The specific angular position the panel assumes during the night or when the sun is below the horizon. This position is used to park the tracker until the next sunrise    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
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
    snowSafetyAngle:    
      description: The specific angular position the panel must adopt during a snow event. This angle is designed to facilitate snow shedding and prevent excessive structural loading on the tracker    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    targetAngle:    
      description: The target angular setpoint for the panel's orientation. A value of 0 indicates the panel is horizontal (facing directly upward). Minimum values represent an Eastward orientation, while maximum values represent a Westward orientation    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    type:    
      description: It must be equal to `SolarTracker`    
      enum:    
        - SolarTracker    
      type: string    
      x-ngsi:    
        type: Property    
    windSafetyAngle:    
      description: The safety setpoint angle the panel assumes when wind speeds exceed the operational threshold. This position minimize the sail effect and reduce structural stress caused by wind uplift or pressure    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
  required:    
    - id    
    - type    
    - deviceCategory    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.SmartManufactoring/DigitalTwin/SolarTracker/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 예제 페이로드    
#### SolarTracker NGSI-v2 키-값 예제    
여기에서는 키-값으로 JSON 형식의 SolarTracker 예제를 보여줍니다. 이는 `options=keyValues`를 사용하여 개별 엔티티의 컨텍스트 데이터를 반환할 때 NGSI-v2와 호환됩니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1",  
  "type": "SolarTracker",  
  "deviceCategory": "PCU",  
  "ipAddress": ["10.13.13.3"],  
  "location": {  
    "type": "Point",  
    "coordinates": [16.563426, 40.850953]  
  }  
}  
```  
</details>  
#### SolarTracker NGSI-v2 정규화 예제    
여기에서는 정규화된 JSON 형식의 SolarTracker 예제를 보여줍니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1-FCU1-SCU1",  
  "type": "SolarTracker",  
  "dateUpdate": {  
    "type": "DateTime",  
    "value": "2026-01-29T00:00:00.000"  
  },  
  "altitude": {  
    "type": "Number",  
    "value": 436.6,  
    "unitCode": "MTR"  
  },  
  "currentPowerConsumption": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "maxPowerRecorded": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "minPowerRecorded": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "backtracking": {  
    "type": "Text",  
    "value": "on"  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": 85.34,  
    "unitCode": "C62"  
  },  
  "currentAngle": {  
    "type": "Number",  
    "value": -31.3,  
    "unitCode": "DD"  
  },  
  "deviceCategory": {  
    "type": "Text",  
    "value": "SCU"  
  },  
  "deviceState": {  
    "type": "Text",  
    "value": "Online"  
  },  
  "motorDirection": {  
    "type": "Text",  
    "value": "-1"  
  },  
  "boardDirection": {  
    "type": "Text",  
    "value": "1"  
  },  
  "targetAngle": {  
    "type": "Number",  
    "value": -29.3,  
    "unitCode": "DD"  
  },  
  "movementInterval": {  
    "type": "Text",  
    "value": "5"  
  },  
  "panelLength": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "MTR"  
  },  
  "maxPowerThreshold": {  
    "type": "Number",  
    "value": 10000,  
    "unitCode": "WTT"  
  },  
  "maxAngleLimit": {  
    "type": "Number",  
    "value": 55,  
    "unitCode": "DD"  
  },  
  "minAngleLimit": {  
    "type": "Number",  
    "value": -55,  
    "unitCode": "DD"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": ["urn:ngsi-ld:Device:PCU1-FCU1"]  
  },  
  "snowSafetyAngle": {  
    "type": "Number",  
    "value": 40,  
    "unitCode": "DD"  
  },  
  "windSafetyAngle": {  
    "type": "Number",  
    "value": 5,  
    "unitCode": "DD"  
  },  
  "restingAngle": {  
    "type": "Number",  
    "value": -5,  
    "unitCode": "DD"  
  },  
  "operatingMode": {  
    "type": "Text",  
    "value": "automatic"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [16.563436, 40.850453]  
    }  
  }  
}  
```  
</details>  
#### SolarTracker NGSI-LD 키-값 예제    
여기에서는 키-값으로 JSON-LD 형식의 SolarTracker 예제를 보여줍니다. 이는 `options=keyValues`를 사용하여 개별 엔티티의 컨텍스트 데이터를 반환할 때 NGSI-LD와 호환됩니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1-FCU1",  
  "type": "SolarTracker",  
  "backtracking": "off",  
  "deviceCategory": "FCU",  
  "owner": ["urn:ngsi-ld:Device:PCU1"],  
  "location": {  
    "type": "Point",  
    "coordinates": [16.563436, 40.850453]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SolarTracker NGSI-LD 정규화 예제    
여기에서는 정규화된 JSON-LD 형식의 SolarTracker 예제를 보여줍니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1-FCU1-SCU1",  
  "type": "SolarTracker",  
  "dateUpdate": {  
    "type": "Property",  
    "value": {  
      "@type":"DateTime",  
      "@value":"2026-01-29T00:00:00.000Z"  
    }  
  },  
  "altitude": {  
    "type": "Property",  
    "value": 436.6,  
    "unitCode": "MTR"  
  },  
  "currentPowerConsumption": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "maxPowerRecorded": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "minPowerRecorded": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "backtracking": {  
    "type": "Property",  
    "value": "on"  
  },  
  "batteryLevel": {  
    "type": "Property",  
    "value": 85.34,  
    "unitCode": "C62"  
  },  
  "currentAngle": {  
    "type": "Property",  
    "value": -31.3,  
    "unitCode": "DD"  
  },  
  "deviceCategory": {  
    "type": "Property",  
    "value": "SCU"  
  },  
  "deviceState": {  
    "type": "Property",  
    "value": "Online"  
  },  
  "motorDirection": {  
    "type": "Property",  
    "value": "-1"  
  },  
  "boardDirection": {  
    "type": "Property",  
    "value": "1"  
  },  
  "targetAngle": {  
    "type": "Property",  
    "value": -29.3,  
    "unitCode": "DD"  
  },  
  "movementInterval": {  
    "type": "Property",  
    "value": "5"  
  },  
  "panelLength": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "MTR"  
  },  
  "maxPowerThreshold": {  
    "type": "Property",  
    "value": 10000,  
    "unitCode": "WTT"  
  },  
  "maxAngleLimit": {  
    "type": "Property",  
    "value": 55,  
    "unitCode": "DD"  
  },  
  "minAngleLimit": {  
    "type": "Property",  
    "value": -55,  
    "unitCode": "DD"  
  },  
  "owner": {  
    "type": "Relationship",  
    "object": ["urn:ngsi-ld:Device:PCU1-FCU1"]  
  },  
  "snowSafetyAngle": {  
    "type": "Property",  
    "value": 40,  
    "unitCode": "DD"  
  },  
  "windSafetyAngle": {  
    "type": "Property",  
    "value": 5,  
    "unitCode": "DD"  
  },  
  "restingAngle": {  
    "type": "Property",  
    "value": -5,  
    "unitCode": "DD"  
  },  
  "operatingMode": {  
    "type": "Property",  
    "value": "automatic"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [16.563436, 40.850453]  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 크기 단위를 처리하는 방법에 대한 답변을 얻으십시오  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ太陽光発電測定  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicMeasurement/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**このデータモデルは、光起電力パネルからインバータ装置への連続電力を測定するためのものである。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `activePower[number]`: ここで phi は電圧に対する電流の位相シフトである。単位コード（テキスト）は UN/CEFACT_Common_Codes を用いて与えられる（最大 3 文字）。例えば、**KWT** はキロワットを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[number]`: 電流の電気的強度。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて示される。例えば、**AMP** はアンペアを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateEnergyMeteringStarted[date-time]`: ISO8601 UTCフォーマットでのエネルギー計測開始日  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObservedFrom[date-time]`: 観測期間：ISO8601 UTCフォーマットでの開始日時。この属性は、ハイライトされる時間間隔に対応する場合、'dateObserved 属性に加えて使用することができます。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: 観測期間：ISO8601 UTCフォーマットの終了日時。この属性は、ハイライトされる時間間隔に対応する場合、'dateObserved' 属性に加えて使用することができます。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `inverterStatus[array]`: ここで phi は電圧に対する電流の位相シフトである。単位コード（テキスト）は UN/CEFACT_Common_Codes を用いて与えられる（最大 3 文字）。例えば、**KWT** はキロワットを表す。Enum:'00-On sector, 01-Power failure / On battery, 02-Loss of communication, 03-Battery fault, 04-System shutdown, 05-Tension dip, 06-Overvoltage, 07-Voltage drop, 08-Voltage increase, 09-Line noise, 10-Frequency variation, 11-Transient distortion, 12-Harmonic distortion'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nominalPeakPowerGeneration[number]`: nominalPeakPowerGeneration は数値である。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**KWT** はキロワットを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `reactivePower[number]`: 回路が使用する無効電力。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて示される。例えば、**K5** はキロボルトアンペア無効電力を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPhotovoltaicDevice[*]`:   . Model: [Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL](Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL)- `refPointOfInterest[*]`: リポジトリとリンクしている[PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)への参照。  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `temperature[number]`: 装置の公称基準温度と比較した、観測時に記録された温度。単位コード（テキスト）は、[UN/CEFACT 共通コード](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) を用いて与えられる。例えば、**CEL**は摂氏を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI エンティティタイプ。これは、PhotovoltaicMeasurement でなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `dateEnergyMeteringStarted`  - `dateObserved`  - `id`  - `location`  - `refPhotovoltaicDevice`  - `temperature`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
以下の値を持つことができる。- 瞬間。特定の瞬間から - 平均。ある期間の平均値 - rms.     ある期間の二乗平均平方根 - 最大値。最大値。ある期間の最小値。  
average、rms、maximum、minimum]の値を使用する場合は、'measurementInterval'と呼ばれる別のMeta Data属性を使用して、測定期間の長さをSecondsで指定する必要があります。また、'timestamp'Meta Data属性は、測定期間の終了時刻とする。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhotovoltaicMeasurement:    
  description: The Data Model is intended to measure the continuous power transferred by the photo-voltaic panel to an Inverter Device.    
  properties:    
    activePower:    
      description: 'Active Power,where phi is the phase shift of the current compared to the voltage. The unit code (text) is given using the UN/CEFACT_Common_Codes (max 3 characters). For instance, For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilowatt    
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
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    current:    
      description: 'Electrical intensity of the current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
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
    dateEnergyMeteringStarted:    
      description: The starting date for metering energy in an ISO8601 UTC format    
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
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
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
    inverterStatus:    
      description: 'Active Power,where phi is the phase shift of the current compared to the voltage. The unit code (text) is given using the UN/CEFACT_Common_Codes (max 3 characters). For instance, For instance, **KWT** represents Kilowatt. Enum:''00-On sector, 01-Power failure / On battery, 02-Loss of communication,  03-Battery fault, 04-System shutdown, 05-Tension dip, 06-Overvoltage, 07-Voltage drop, 08-Voltage increase, 09-Line noise, 10-Frequency variation, 11-Transient distortion, 12-Harmonic distortion'''    
      items:    
        enum:    
          - 00-On sector    
          - 01-Power failure / On battery    
          - 02-Loss of communication    
          - 03-Battery fault    
          - 04-System shutdown    
          - 05-Tension dip    
          - 06-Overvoltage    
          - 07-Voltage drop    
          - 08-Voltage increase    
          - 09-Line noise    
          - 10-Frequency variation    
          - 11-Transient distortion    
          - 12-Harmonic distortion    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nominalPeakPowerGeneration:    
      description: 'nominalPeakPowerGeneration is a number. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilowatt    
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
    reactivePower:    
      description: 'Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    refPhotovoltaicDevice:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: ""    
      x-ngsi:    
        model: 'Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL'    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: degrees celsius    
    type:    
      description: NGSI Entity type. It has to be PhotovoltaicMeasurement    
      enum:    
        - PhotovoltaicMeasurement    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - refPhotovoltaicDevice    
    - dateEnergyMeteringStarted    
    - temperature    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/PhotovoltaicMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/PhotovoltaicMeasurement/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### PhotovoltaicMeasurement NGSI-v2 キー値の例  
JSON-LD形式のPhotovoltaicMeasurementのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
  "type": "PhotovoltaicMeasurement",  
  "dataProvider": "https://imredd.fr/en/home/",  
  "name": "Photovoltaic station IMREDD",  
  "description": "Photovoltaic data provided by the data logger ABB",  
  "seeAlso": "https://us.sunpower.com/products/solar-panels",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "61-63 Avenue Simone Veil"  
  },  
  "areaServed": "Nice",  
  "refPhotovoltaicDevice": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012",  
  "dateObserved": "2019-09-05T16:00:00.999Z",  
  "dateEnergyMeteringStarted": "2019-09-04T15:29:17.999Z",  
  "nominalPeakPowerGeneration": 179,  
  "temperature": 23.4  
}  
```  
</details>  
#### 太陽光発電測定 NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の PhotovoltaicMeasurement の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
  "type": "PhotovoltaicMeasurement",  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://imredd.fr/en/home/"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Photovoltaic station IMREDD"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Photovoltaic data provided by the data logger ABB"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://us.sunpower.com/products/solar-panels"  
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
      "streetAddress": "61-63 Avenue Simone Veil"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice"  
  },  
  "refPhotovoltaicDevice": {  
    "type": "Relationship",  
    "Object": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": "2019-09-05T16:00:00.999Z"  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": "2019-09-04T15:29:17.999Z"  
  },  
  "nominalPeakPowerGeneration": {  
    "type": "Property",  
    "value": 179  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 23.4  
  }  
}  
```  
</details>  
#### 太陽光発電測定 NGSI-LD キー値の例  
JSON-LD形式のPhotovoltaicMeasurementのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
    "type": "PhotovoltaicMeasurement",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "61-63 Avenue Simone Veil"  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://imredd.fr/en/home/"  
    },  
    "dateEnergyMeteringStarted": {  
        "type": "Property",  
        "value": "2019-09-04T15:29:17.999Z"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2019-09-05T16:00:00.999Z"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Photovoltaic data provided by the data logger ABB"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Photovoltaic station IMREDD"  
    },  
    "nominalPeakPowerGeneration": {  
        "type": "Property",  
        "value": 179  
    },  
    "refPhotovoltaicDevice": {  
        "type": "Relationship",  
        "Object": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://us.sunpower.com/products/solar-panels"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 23.4  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/common-schema.json",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 太陽光発電測定 NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の PhotovoltaicMeasurement の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
    "type": "PhotovoltaicMeasurement",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "61-63 Avenue Simone Veil"  
    },  
    "areaServed": "Nice",  
    "dataProvider": "https://imredd.fr/en/home/",  
    "dateEnergyMeteringStarted": "2019-09-04T15:29:17.999Z",  
    "dateObserved": "2019-09-05T16:00:00.999Z",  
    "description": "Photovoltaic data provided by the data logger ABB",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "name": "Photovoltaic station IMREDD",  
    "nominalPeakPowerGeneration": 179,  
    "refPhotovoltaicDevice": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012",  
    "seeAlso": "https://us.sunpower.com/products/solar-panels",  
    "temperature": 23.4,  
    "@context": [  
        "https://smart-data-models.github.io/data-models/common-schema.json",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

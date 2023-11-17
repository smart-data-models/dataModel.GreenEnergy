<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：绿色能源发电机    
==========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/GreenEnergyGenerator/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：可利用绿色能源发电的**通用发电站**    
版本： 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `generationSources[array]`: 用于发电的能源清单。Enum:'生物质、乙醇、地热、水电、太阳能'。  . Model: [https://schema.org/ItemList](https://schema.org/ItemList)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxBiomassMeasure[number]`: 可产生的最大生物质能的量度。使用 UN/CEFACT 通用代码给出的测量单位代码（文本）（最多 3 个字符）  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxEolicPowerMeasure[number]`: 可产生的最大能量的量度。使用 UN/CEFACT 通用代码给出的测量单位代码（文本）（最多 3 个字符）  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxGeothermalPowerGenerated[number]`: 可产生的最大地热能的量度。使用 UN/CEFACT 通用代码给出的测量单位代码（文本）（最多 3 个字符）  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxHydroPowerMeasure[number]`: 可产生的最大水电能量的度量。使用 UN/CEFACT 通用代码给出的测量单位代码（文本）（最多 3 个字符）  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxSolarPowerMeasure[number]`: 可产生的最大太阳能的量度。使用 UN/CEFACT 通用代码给出的测量单位代码（文本）（最多 3 个字符）  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `redistribution[boolean]`: 表示所产生的能量是否会倾泻到网络中  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `selfConsumption[boolean]`: 说明所产生的能源是否用于自身  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `status[string]`: 绿色能源发电机的状态。枚举："停用、有故障、工作中  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。必须是 GreenEnergyGenerator  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
绿色能源发电机的通用模型。利用太阳能或电能产生能量的设备。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
GreenEnergyGenerator:      
  description: A generic generator station which can generate energy from green energy      
  properties:      
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
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    generationSources:      
      description: 'A list of sources used for power generation. Enum:''biomass, eolic, geothermal, hydropower, solar'''      
      items:      
        enum:      
          - biomass      
          - eolic      
          - geothermal      
          - hydropower      
          - solar      
        type: string      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: https://schema.org/ItemList      
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
    maxBiomassMeasure:      
      description: A measure of maximum biomass energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: KWT      
    maxEolicPowerMeasure:      
      description: A measure of maximum eolic energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: KWT      
    maxGeothermalPowerGenerated:      
      description: A measure of maximum geothermal energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: KWT      
    maxHydroPowerMeasure:      
      description: A measure of maximum hydropower energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: KWT      
    maxSolarPowerMeasure:      
      description: A measure of maximum solar energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: KWT      
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
    redistribution:      
      description: Indicates whether the generated energy will be dumped into the network      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
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
    selfConsumption:      
      description: Indicate whether energy generated will use for self      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    status:      
      description: 'Status of the green energy generator. Enum:''outOfService, withIncidence, working'''      
      enum:      
        - outOfService      
        - withIncidence      
        - working      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity Type. It has to be GreenEnergyGenerator      
      enum:      
        - GreenEnergyGenerator      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/GreenEnergyGenerator/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.GreenEnergy/GreenEnergyGenerator/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### GreenEnergyGenerator NGSI-v2 密钥值示例    
下面是一个以 JSON-LD 格式作为键值的 GreenEnergyGenerator 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "type": "GreenEnergyGenerator",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.80356167695194,  
      43.46296641666926  
    ]  
  },  
  "source": "bike-in.com",  
  "dataProvider": "bike-in.com",  
  "name": "generator solar and eolic #9e46d",  
  "description": "mixed generator model ~004 with maximum power 22kw",  
  "status": "working",  
  "generationSources": [  
    "solar",  
    "eolic"  
  ],  
  "selfConsumption": true,  
  "redistribution": false,  
  "maxSolarPowerGenerated": 15,  
  "maxEolicPowerGenerated": 7,  
  "maxHydroPowerGenerated": 0,  
  "maxBiomassPowerGenerated": 0  
}  
```  
</details>    
#### GreenEnergyGenerator NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 GreenEnergyGenerator 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergy:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "type": "GreenEnergyGenerator",  
  "status": {  
    "type": "Text",  
    "value": "working"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.80356167695194,  
        43.46296641666926  
      ]  
    }  
  },  
  "selfConsumption": {  
    "type": "Boolean",  
    "value": true  
  },  
  "redistribution": {  
    "type": "Boolean",  
    "value": false  
  },  
  "generationSources": {  
    "type": "StructuredValue",  
    "value": [  
      "solar",  
      "eolic"  
    ]  
  },  
  "maxSolarPowerGenerated": {  
    "type": "Number",  
    "value": 20  
  },  
  "maxEolicPowerGenerated": {  
    "type": "Number",  
    "value": 10  
  }  
}  
```  
</details>    
#### GreenEnergyGenerator NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 GreenEnergyGenerator 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "type": "GreenEnergyGenerator",  
  "description": "mixed generator model ~004 with maximum power 22w",  
  "generationSources": [  
    "solar",  
    "eolic"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.80356167695194,  
      43.46296641666926  
    ]  
  },  
  "maxBiomassPowerGenerated": 0,  
  "maxEolicPowerGenerated": 7,  
  "maxHydroPowerGenerated": 0,  
  "maxSolarPowerGenerated": 15,  
  "name": "generator solar and eolic #9e46d",  
  "redistribution": false,  
  "selfConsumption": true,  
  "source": "bike-in.com",  
  "status": "working",  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### GreenEnergyGenerator NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 GreenEnergyGenerator 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:GreenEnergy:santander:GreenEnergy:greenEnergyGenerator:0001",  
    "type": "GreenEnergyGenerator",  
    "generationSources": {  
        "type": "Property",  
        "value": [  
            "solar",  
            "eolic"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.80356167695194,  
                43.46296641666926  
            ]  
        }  
    },  
    "maxEolicPowerGenerated": {  
        "type": "Property",  
        "value": 10  
    },  
    "maxSolarPowerGenerated": {  
        "type": "Property",  
        "value": 20  
    },  
    "redistribution": {  
        "type": "Property",  
        "value": false  
    },  
    "selfConsumption": {  
        "type": "Property",  
        "value": true  
    },  
    "status": {  
        "type": "Property",  
        "value": "working"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

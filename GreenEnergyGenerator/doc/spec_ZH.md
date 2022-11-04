<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。绿色能源发电公司  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/GreenEnergyGenerator/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**可以用绿色能源产生能量的通用发电机站**。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `generationSources[array]`: 用于发电的来源列表。Enum:'生物质、桉树、地热、水电、太阳能'  . Model: [https://schema.org/ItemList](https://schema.org/ItemList)- `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `maxBiomassMeasure[number]`: 可产生的最大生物质能的一种衡量标准。使用UN/CEFACT通用代码给出的计量单位代码（文本）（最多3个字符）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxEolicPowerMeasure[number]`: 可产生的最大新陈代谢能量的量度。使用UN/CEFACT通用代码给出的测量单位代码（文本）（最多3个字符）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxGeothermalPowerGenerated[number]`: 对可产生的最大地热能的衡量。使用UN/CEFACT通用代码给出的测量单位代码（文本）（最多3个字符）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxHydroPowerMeasure[number]`: 可产生的最大水电能量的衡量标准。使用UN/CEFACT通用代码给出的测量单位代码（文本）（最多3个字符）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxSolarPowerMeasure[number]`: 对可产生的最大太阳能的测量。使用UN/CEFACT通用代码给出的测量单位代码（文本）（最多3个字符）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `redistribution[boolean]`: 表示所产生的能量是否会被倾倒到网络中。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `selfConsumption[boolean]`: 说明所产生的能源是否将用于自身  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `status[string]`: 绿色能源发电机的状态。Enum:'outOfService, withIncidence, working' 枚举:'停用，发生，工作'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI实体类型。它必须是GreenEnergyGenerator。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
绿色能源发电机的通用模型。一个可以利用太阳能或欧洲绿色能源产生能量的设备。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GreenEnergyGenerator:    
  description: 'A generic generator station which can generate energy from green energy'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
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
      anyOf: &greenenergygenerator_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    maxBiomassMeasure:    
      description: 'A measure of maximum biomass energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    maxEolicPowerMeasure:    
      description: 'A measure of maximum eolic energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    maxGeothermalPowerGenerated:    
      description: 'A measure of maximum geothermal energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    maxHydroPowerMeasure:    
      description: 'A measure of maximum hydropower energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    maxSolarPowerMeasure:    
      description: 'A measure of maximum solar energy that can be generated. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *greenenergygenerator_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    redistribution:    
      description: 'Indicates whether the generated energy will be dumped into the network'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'Indicate whether energy generated will use for self'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'NGSI Entity Type. It has to be GreenEnergyGenerator'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ＃＃＃＃有效载荷的例子  
#### GreenEnergyGenerator NGSI-v2 关键值示例  
这里有一个GreenEnergyGenerator的例子，以JSON-LD格式作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "type": "GreenEnergyGenerator",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.80356167695194, 43.46296641666926]  
  },  
  "source": "bike-in.com",  
  "dataProvider": "bike-in.com",  
  "name": "generator solar and eolic #9e46d",  
  "description": "mixed generator model ~004 with maximum power 22kw",  
  "status":"working",  
  "generationSources":["solar","eolic"],  
  "selfConsumption":true,  
  "redistribution":false,  
  "maxSolarPowerGenerated": 15,  
  "maxEolicPowerGenerated": 7,  
  "maxHydroPowerGenerated": 0,  
  "maxBiomassPowerGenerated": 0  
}  
```  
</details>  
#### GreenEnergyGenerator NGSI-v2规范化实例  
下面是一个以JSON-LD格式规范化的GreenEnergyGenerator的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergy:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "type": "GreenEnergyGenerator",  
  "status": {  
    "type":"Text",  
    "value":"working"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.80356167695194,  
      43.46296641666926  
    ]  
  },  
  "selfConsumption":{  
    "type":"Boolean",  
    "value":true  
  },  
  "redistribution":{  
    "type":"Boolean",  
    "value":false  
  },  
  "generationSources":{  
    "type":"Array",  
    "value":[ "solar","eolic"]  
  },  
  "maxSolarPowerGenerated":{  
    "type":"Number",  
    "value": 20  
  },  
  "maxEolicPowerGenerated": {  
    "type":"Number",  
    "value":10  
  }  
}  
```  
</details>  
#### GreenEnergyGenerator NGSI-LD关键值示例  
这里有一个GreenEnergyGenerator的例子，以JSON-LD格式作为关键值。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GreenEnergy:santander:GreenEnergy:greenEnergyGenerator:0001",  
    "type": "GreenEnergyGenerator",  
    "generationSources": {  
        "type": "Array",  
        "value": [  
            "solar",  
            "eolic"  
        ]  
    },  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -3.80356167695194,  
            43.46296641666926  
        ]  
    },  
    "maxEolicPowerGenerated": {  
        "type": "Number",  
        "value": 10  
    },  
    "maxSolarPowerGenerated": {  
        "type": "Number",  
        "value": 20  
    },  
    "redistribution": {  
        "type": "Boolean",  
        "value": false  
    },  
    "selfConsumption": {  
        "type": "Boolean",  
        "value": true  
    },  
    "status": {  
        "type": "Text",  
        "value": "working"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GreenEnergyGenerator NGSI-LD规范化实例  
这里有一个GreenEnergyGenerator的例子，是以JSON-LD格式规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

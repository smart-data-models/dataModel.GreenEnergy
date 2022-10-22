<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。光电设备（PhotovoltaicDevice  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该数据模型旨在根据*STC-标准测试条件*和*NOCT-正常工作电池温度*来描述光电板的机械、电气和热特性。*备注* :该数据模型可直接作为描述 "光伏设备 "的主要实体，或作为数据模型 "DEVICE "的子实体，通过 "refDevice "属性进行参考。对STC和NOCT进行的测量是`Pmax`（最大额定功率），`Umpp`（最佳工作电压），`Impp`（最佳工作电流），`Uoc`（开路电压），`Isc`（短路电流）。*关于数据模型的附加信息：*该数据模型可以直接作为描述设备[PHOTOVOLTAIC]的主要实体，或者作为数据模型[DEVICE]的一个子实体，使用`refDevice`属性进行引用。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `MaxPressureLoad[object]`: 面板上的最大力学压力（剪切、弹性、压缩）载荷。该格式是由3个项目的子属性构成的。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**PAL**代表Pascal  . Model: [https://schema.org/Number](https://schema.org/Number)- `MaximumSystemVoltage[number]`: **模块**允许的最大系统电压。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**VLT**代表伏特  . Model: [https://schema.org/Number](https://schema.org/Number)- `NominalPower[number]`: 屏风的标称功率**。这与[moduleSTC]属性的项目[Pmax]的值相同。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**WTT**代表瓦特  . Model: [https://schema.org/Number](https://schema.org/Number)- `PanelNbModules[number]`: 每个 "面板 "的 "模块 "数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `application[array]`: 关于太阳能电池板类型的目标应用（在我们的例子中是 "电力"）。一个唯一的值。https://schema.org/Text。枚举：'电、热、其他  - `applicationClass[array]`: 评价与该模块有关的潜在危险。一个唯一的值。枚举:'A, B, C'  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaWeight[number]`: 面积 重量以公斤/平方米计算。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**28**代表每平方米公斤数。  . Model: [https://schema.org/Number](https://schema.org/Number)- `brandName[string]`: 项目的品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `cellDimension[object]`: 一个单元格的外部尺寸。该格式是由3个项目的子属性构成的。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MMT**代表毫米。  - `cellOperatingTemperature[object]`: 这是它收集太阳能的电池的额定工作温度范围。该格式是由2个项目的子属性构成的。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**CEL**代表摄氏度  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `cellType[array]`: 用于建造光电单元的电池类型。2种技术*"水晶石 "*或*"薄层 "*。一个独特的值。Enum:'amorphousSilicon, CfTe, CIS, monocrystalline, polycrystalline, other'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateLastReported[string]`: 表示设备成功报告数据的最后时间的时间戳。日期和时间采用ISO8601 UTC格式。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `documentation[string]`: 技术文件（安装/维护/使用）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `fireClass[array]`: 对火灾的评估（IEC 61730）。一个独特的值。枚举:'A, B, C'  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `installationCondition[array]`: 在以下环境中使用的条件和可能性。一个组合。Enum:'沙漠, 灰尘, 极热, 极冷, 极端气候, 极端湿度, 海洋, 无, 其他, 盐碱地, 沙地, 地震'  . Model: [https://schema.org/Text](https://schema.org/Text)- `installationMode[array]`: 设备相对于地面参考系统的定位。一个唯一的值。Enum:'地面，其他，杆，屋顶，墙'  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `manufacturerName[string]`: 制造商 项目名称  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `modelName[string]`: 项目的模型名称  . Model: [https://schema.org/model](https://schema.org/model)- `moduleDimension[object]`: 一个模块的外部尺寸。一个模块可以是1到n个单元的组合。该格式由3个项目的子属性构成。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MMT**代表毫米级  - `moduleNOCT[object]`: 正常工作电池温度测量。该格式由5个项目的子属性构成。Pmax（瓦特）。Umpp（伏特）。Impp，单位为安培。Uoc（伏特）。Isc（单位：安培  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `moduleNbCells[number]`: 每个 "模块 "的 "单元 "数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `moduleSTC[object]`: 标准测试条件测量。该格式由5个项目的子属性构成。Pmax（瓦特）。Umpp（伏特）。Impp（单位：安培）。Uoc（伏特）。Isc（单位：安培  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `moduleYieldRate[number]`: 设备相对于地面参考系统的定位。一个独特的值  . Model: [https://schema.org/Number](https://schema.org/Number)- `nTCClass[number]`: 负温度电阻系数 - *NTC*，描述了与给定的负温度变化相关的物理特性的相对变化。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**P1**代表百分比  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pTCClass[number]`: 电阻的正温度系数 - *PTC*，描述了与正温度的特定变化相关的物理特性的相对变化。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**P1**代表百分比。  - `panelDimension[object]`: 面板的外部尺寸。一个太阳能电池板可以是由1到n个模块组成的组件，这些模块本身是由几个电池组成的，从太阳光中收集热量。该格式由一个包含3个项目的子属性构成。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**MMT**代表毫米。  - `panelLifetime[number]`: 一个面板的平均寿命。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**ANN**代表年  . Model: [https://schema.org/Number](https://schema.org/Number)- `panelOperatingTemperature[object]`: 环境工作温度范围。这是使用面板的最低和最高耐寒和耐热性。该格式是由2个项目的子属性构成的。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**CEL**代表摄氏度  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `panelWeight[number]`: 板材的重量（有时使用的参考值是Kg/m²）。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**KGM**代表公斤。  . Model: [https://schema.org/Number](https://schema.org/Number)- `panelYieldCurve[array]`: 选项1.面板在[T0]时的[名义功率]和沿其[面板寿命]的能源生产收益曲线。列表中提供的测量值是根据制造商提供的信息，从5年开始，以5年为一个 "台阶"，用百分比表示的能源生产量序列。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**P1**代表百分比。  - `performanceLowIrradiance[number]`: 低辐照度下的平均相对产量与性能。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**P1**代表百分比  . Model: [https://schema.org/Number](https://schema.org/Number)- `possibilityOfUse[array]`: 使用的可能性。一个独特的值。Enum:'混合、移动、其他、固定'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `protectionIP[string]`: 接线盒的IP "入侵保护"。这是根据国际电工委员会标准（EN 60-529），对机械外壳和电气外壳提供的保护程度进行分类和评级，以防止入侵、灰尘、意外接触和水。第一个数字。固体颗粒保护（单一数字：0-6或'X'）。第二位数字。第三位数：液体进入保护（单个数字：0-9或'X'）。个人防护，防止接触危险部件（可选附加字母）。第四位数。其他保护措施（可选附加字母）  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: 如果作为第二链路使用，参考主要实体[设备](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: 对与存储库相连的[兴趣点](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)的引用。  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `serialNumber[array]`: 由制造商提供的、以运行模式装配在一个地方的光电池装置的序列号列表  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `temperatureCoefficient[object]`: 温度对面板的影响系数。该格式由3个项目的子属性构成。Pmax（瓦特）。Uoc（伏特）。Isc（单位：安培  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `type[string]`: NGSI实体类型。它必须是PhotovoltaicDevice  - `typeOfUse[array]`: 关于其在室内/室外环境中的定位，可接受使用。一个独特的值。Enum:'室内、室外、混合、其他'。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateLastReported`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
对STC和NOCT进行的测量是 - [Pmax] 以**WTT**表示瓦特的最大额定功率。- [Umpp] 以**VLT**衡量的最佳工作电压，代表伏特。- [Impp] 最佳工作电流，以**AMP**表示安培。- [Uoc] 以**VLT**衡量的开路电压，代表伏特。- [Isc] 短路电流，单位为**AMP**，代表安培。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
      description: 'Number of ''Modules'' per ''Panel'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      description: 'The geographic area where a service or offered item is provided'    
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
        units: 'kilograms per square meter'    
    brandName:    
      description: 'Brand Name of the item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    cellDimension:    
      description: 'External dimension of a cell. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter.'    
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
        units: 'Degree Celsius'    
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
    dateLastReported:    
      description: 'A timestamps which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    documentation:    
      description: 'Technical Documentation (Installation / maintenance / used)'    
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
      anyOf: &photovoltaicdevice_-_properties_-_owner_-_items_-_anyof    
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
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
    manufacturerName:    
      description: 'Manufacturer Name of the item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    modelName:    
      description: 'Model Name of the item'    
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
      description: 'Normal Operating Cell Temperature measurements. The format is structured by a sub-property of 5 items. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere'    
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
      description: 'Number of ''cells'' per ''module'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    moduleSTC:    
      description: 'Standard Test Condition measurements. The format is structured by a sub-property of 5 items. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere'    
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
      description: 'Positioning of the device in relation to a ground reference system. A unique value'    
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
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *photovoltaicdevice_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pTCClass:    
      description: ' The Positive Temperature Coefficient of resistance - *PTC*, describes the relative change of a physical property that is associated with a given change in positive temperature. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    panelDimension:    
      description: 'External dimension of a Panel. A solar panel can be an assembly of 1 to n modules, which themselves are made of several cells which collect heat from the sun''s rays. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter.'    
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
        units: 'Degree Celsius'    
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
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
    serialNumber:    
      description: 'List of serial numbers of Photo-voltaic device supplied by the manufacturer and assembled in operating mode on a single location'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'NGSI Entity type. It has to be PhotovoltaicDevice'    
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
## ＃＃＃＃有效载荷的例子  
#### PhotovoltaicDevice NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为关键值的PhotovoltaicDevice的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### PhotovoltaicDevice NGSI-v2规范化实例  
下面是一个以JSON-LD格式规范化的PhotovoltaicDevice的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
      "coordinates ": [  
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
    "value": "polycrystalline"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "roofing"  
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
    "value": "A"  
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
#### PhotovoltaicDevice NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为关键值的PhotovoltaicDevice的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
    "type": "PhotovoltaicDevice",  
    "MaximumSystemVoltage": {  
        "type": "Property",  
        "value": 1000  
    },  
    "NominalPower": {  
        "type": "Property",  
        "value": 270  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "Airport - Terminal 2 - Roof 2 - Local  12"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "AirPort \u2013 global Observation"  
    },  
    "application": {  
        "type": "Property",  
        "value": [  
            "electric"  
        ]  
    },  
    "applicationClass": {  
        "type": "Property",  
        "value": "A"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Aeroport"  
    },  
    "arealWeight": {  
        "type": "Property",  
        "value": 32  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Canadian Solar"  
    },  
    "cellDimension": {  
        "type": "Property",  
        "value": {  
            "length": 16.0,  
            "width": 9.0,  
            "thickness": 2.3  
        }  
    },  
    "cellOperatingTemperature": {  
        "type": "Property",  
        "value": {  
            "min": 45,  
            "max": 2  
        }  
    },  
    "cellType": {  
        "type": "Property",  
        "value": "polycrystalline"  
    },  
    "dateLastReported": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-05-17T09:47:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Photo-voltaic Device description"  
    },  
    "documentation": {  
        "type": "Property",  
        "value": "https://www.myDevicePV.Cn"  
    },  
    "fireClass": {  
        "type": "Property",  
        "value": [  
            "C"  
        ]  
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
    "installationMode": {  
        "type": "Property",  
        "value": "roofing"  
    },  
    "integrationMode": {  
        "type": "Property",  
        "value": "IAB"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates ": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "Canadian Solar EMEA GmbH,"  
    },  
    "maxPressureLoad": {  
        "type": "Property",  
        "value": {  
            "hail": 2500,  
            "snow": 5400,  
            "wind": 2400  
        }  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "CS6P-270P"  
    },  
    "moduleDimension": {  
        "type": "Property",  
        "value": {  
            "length": 1600,  
            "width": 975,  
            "thickness": 3.75  
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
    "moduleNbCells": {  
        "type": "Property",  
        "value": 60  
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
    "moduleYieldRate": {  
        "type": "Property",  
        "value": 16.79  
    },  
    "nTCClass": {  
        "type": "Property",  
        "value": 88.3  
    },  
    "name": {  
        "type": "Property",  
        "value": "DEVICE-PV-T2-R-012"  
    },  
    "owners": {  
        "type": "Property",  
        "value": [  
            "Airport-Division Maintenance"  
        ]  
    },  
    "pTCClass": {  
        "type": "Property",  
        "value": 92.1  
    },  
    "panelDimension": {  
        "type": "Property",  
        "value": {  
            "length": 1638,  
            "width": 982,  
            "thickness": 40  
        }  
    },  
    "panelLifetime": {  
        "type": "Property",  
        "value": 30  
    },  
    "panelNbModules": {  
        "type": "Property",  
        "value": 1  
    },  
    "panelOperatingTemperature": {  
        "type": "Property",  
        "value": {  
            "min": -40,  
            "max": 85  
        }  
    },  
    "panelTiltReference": {  
        "type": "Property",  
        "value": {  
            "min": 28,  
            "max": 37  
        }  
    },  
    "panelWeight": {  
        "type": "Property",  
        "value": 18  
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
    "performanceLowIrradiance": {  
        "type": "Property",  
        "value": 96.5  
    },  
    "possibilityOfUsed": {  
        "type": "Property",  
        "value": "stationary"  
    },  
    "protectionIP": {  
        "type": "Property",  
        "value": "IP67"  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:Device:PV-T2-R-012"  
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
    "temperatureCoefficient": {  
        "type": "Property",  
        "value": {  
            "Pmax": -0.41,  
            "Uoc": -0.31,  
            "Isc": 0.053  
        }  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PhotovoltaicDevice NGSI-LD归一化实例  
下面是一个以JSON-LD格式规范化的PhotovoltaicDevice的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
    "type": "PhotovoltaicDevice",  
    "MaximumSystemVoltage": 1000,  
    "NominalPower": 270,  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Airport - Terminal 2 - Roof 2 - Local  12"  
    },  
    "alternateName": "AirPort \u2013 global Observation",  
    "application": [  
        "electric"  
    ],  
    "applicationClass": [  
        "A"  
    ],  
    "areaServed": "Nice Aeroport",  
    "arealWeight": 32,  
    "brandName": "Canadian Solar",  
    "cellDimension": {  
        "length": 16.0,  
        "width": 9.0,  
        "thickness": 2.3  
    },  
    "cellOperatingTemperature": {  
        "min": 45,  
        "max": 2  
    },  
    "cellType": [  
        "polycrystalline"  
    ],  
    "dateLastReported": "2020-05-17T09:47:00Z",  
    "description": "Photo-voltaic Device description",  
    "documentation": "https://www.myDevicePV.Cn",  
    "fireClass": [  
        "C"  
    ],  
    "installationCondition": [  
        "extremeHeat",  
        "extremeCold",  
        "extremeClimate",  
        "desert"  
    ],  
    "installationMode": [  
        "roofing"  
    ],  
    "integrationMode": "IAB",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "manufacturerName": "Canadian Solar EMEA GmbH,",  
    "maxPressureLoad": {  
        "hail": 2500,  
        "snow": 5400,  
        "wind": 2400  
    },  
    "modelName": "CS6P-270P",  
    "moduleDimension": {  
        "length": 1600,  
        "width": 975,  
        "thickness": 3.75  
    },  
    "moduleNOCT": {  
        "Pmax": 196,  
        "Umpp": 28.1,  
        "Impp": 6.97,  
        "Uoc": 34.8,  
        "Isc": 7.55  
    },  
    "moduleNbCells": 60,  
    "moduleSTC": {  
        "Pmax": 270,  
        "Umpp": 30.8,  
        "Impp": 8.75,  
        "Uoc": 37.9,  
        "Isc": 9.32  
    },  
    "moduleYieldRate": 16.79,  
    "nTCClass": 88.3,  
    "name": "DEVICE-PV-T2-R-012",  
    "owners": [  
        "Airport-Division Maintenance"  
    ],  
    "pTCClass": 92.1,  
    "panelDimension": {  
        "length": 1638,  
        "width": 982,  
        "thickness": 40  
    },  
    "panelLifetime": 30,  
    "panelNbModules": 1,  
    "panelOperatingTemperature": {  
        "min": -40,  
        "max": 85  
    },  
    "panelTiltReference": {  
        "min": 28,  
        "max": 37  
    },  
    "panelWeight": 18,  
    "panelYieldCurve": [  
        "95.0",  
        "92.5",  
        "90.0",  
        "87.5",  
        "85.0",  
        "80.0"  
    ],  
    "panelYieldRate": 0.5,  
    "performanceLowIrradiance": 96.5,  
    "possibilityOfUsed": "stationary",  
    "protectionIP": "IP67",  
    "refDevice": "urn:ngsi-ld:Device:PV-T2-R-012",  
    "serialNumber": [  
        "CSPV270P-SN1804L6J34Z8742H",  
        "CSPV270P-SN1804L6J34Z8743H",  
        "CSPV270P-SN1804L6J34Z8744H",  
        "CSPV270P-SN1804L6J34Z8745H",  
        "CSPV270P-SN1804L6J34Z8746H"  
    ],  
    "temperatureCoefficient": {  
        "Pmax": -0.41,  
        "Uoc": -0.31,  
        "Isc": 0.053  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

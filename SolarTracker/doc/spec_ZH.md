<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：SolarTracker  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**数据模型SolarTracker的描述**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可以有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`：邮寄地址。模型：[https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`：国家。例如，西班牙。模型：[https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`：街道地址所在的地区，并且该地区位于该地区。模型：[https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`：该地区位于该国家的地区。模型：[https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`：一个区是一个类型的行政区划，在一些国家，由地方政府管理    
	- `postOfficeBoxNumber[string]`：用于PO箱地址的邮政信箱号码。例如，03578。模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`：邮政编码。例如，24004。模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`：街道地址。模型：[https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`：在公共街道上识别特定属性的编号    
- `alternateName[string]`：该项的替代名称  - `altitude[number]`：安装地点的海拔高度。该值用于太阳算法来细化太阳的位置和大气折射的计算。模型：[https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`：服务或提供的项目所提供的的地理区域。模型：[https://schema.org/Text](https://schema.org/Text)- `backtracking[string]`：枚举：'on'，'off'。指示太阳能跟踪器是否处于回溯模式，以防止行与行之间的阴影，偏离最佳太阳角度位置。模型：[https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]`：代表电池的当前充电水平，表示为其总容量的百分比（0至100）。模型：[https://schema.org/Number](https://schema.org/Number)- `boardDirection[string]`：枚举：'-1'，'1'。指定控制板的物理方向，基于紧急停止按钮的位置（朝东=1；朝西=-1）。模型：[https://schema.org/Text](https://schema.org/Text)- `currentAngle[number]`：面板的当前角度位置。值0表示面板是水平的（直接朝上）。最小值表示朝东的方向，而最大值表示朝西的方向。模型：[https://schema.org/Number](https://schema.org/Number)- `currentPowerConsumption[number]`：以瓦特为单位测量的实时电力需求。模型：[https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`：一系列字符，标识和谐数据实体的提供者  - `dateCreated[date-time]`：实体创建时间戳。这通常由存储平台分配  - `dateModified[date-time]`：实体最后修改的时间戳。这通常由存储平台分配  - `dateUpdate[date-time]`：配置更新的日期。模型：[http://schema.org/DateTime](http://schema.org/DateTime)- `description[string]`：此项的描述  - `deviceCategory[string]`：枚举：'PCU'，'FCU'，'SCU'。指定设备在系统中的分类。模型：[https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`：枚举：'Online'，'Offline'。指示设备的当前操作连接状态。模型：[https://schema.org/Text](https://schema.org/Text)- `id[*]`：实体的唯一标识符  - `ipAddress[array]`：设备的IP地址列表。如果设备有多个IP地址，可以是用逗号分隔的值列表。模型：[https://schema.org/Text](https://schema.org/Text)- `location[*]`：指向该项的Geojson引用。可以是点、线字符串、多边形、多点、多线字符串或多多边形  - `maxAngleLimit[number]`：允许朝西的最大角度位置。该软件限制作为硬性上限；面板不会超出该值，即使计算出的目标角度更大。模型：[https://schema.org/Number](https://schema.org/Number)- `maxPowerRecorded[number]`：最后一次移动期间记录的最高电力消耗水平，以瓦特为单位。模型：[https://schema.org/Number](https://schema.org/Number)- `maxPowerThreshold[number]`：电机运行期间的电力消耗安全限制。如果电力超过此阈值，面板运动将立即中断以防止机械损坏或电机过载。模型：[https://schema.org/Number](https://schema.org/Number)- `minAngleLimit[number]`：允许朝东的最小角度位置。该参数定义了一个强制性的操作边界；面板不会超出该值，无论请求的目标位置如何。模型：[https://schema.org/Number](https://schema.org/Number)- `minPowerRecorded[number]`：最后一次移动期间记录的最低电力消耗水平，以瓦特为单位。模型：[https://schema.org/Number](https://schema.org/Number)- `motorDirection[string]`：枚举：'-1'，'1'。定义电机的物理安装方向，该方向决定了旋转的极性（朝东=1；朝西=-1）。模型：[https://schema.org/Text](https://schema.org/Text)- `movementInterval[string]`：枚举：'5'，'10'，'15'。定义面板调整其位置的时间频率。该值必须是以下预定义间隔之一：5、10或15分钟。模型：[https://schema.org/Text](https://schema.org/Text)- `name[string]`：此项的名称  - `operatingMode[string]`：枚举：'自动'，'手动'，'safesnow'，'safesnowsensor'，'safewind'，'safewindsensor'，'maintenance'。定义面板的当前功能状态。该模式决定了跟踪器是否遵循太阳算法或响应外部覆盖/安全事件。模型：[https://schema.org/Text](https://schema.org/Text)- `owner[array]`：包含对所有者（们）的唯一ID的JSON编码字符序列的列表  - `panelLength[number]`：面板沿着与旋转轴垂直的轴测量的尺寸。该值对于计算面板投射的阴影和确定适当的回溯运动至关重要。模型：[https://schema.org/Number](https://schema.org/Number)- `restingAngle[number]`：面板在夜间或太阳在地平线以下时假定的特定角度位置。该位置用于停放跟踪器，直到下一次日出。模型：[https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`：指向该项的其他资源的URI列表  - `snowSafetyAngle[number]`：面板在雪事件期间必须采取的特定角度位置。该角度旨在促进雪的排放并防止跟踪器上的过度结构负载。模型：[https://schema.org/Number](https://schema.org/Number)- `source[string]`：实体数据的原始来源的URL序列。建议为源提供者的完全限定域名或源对象的URL  - `targetAngle[number]`：面板方向的目标角度设定值。值0表示面板是水平的（直接朝上）。最小值表示朝东的方向，而最大值表示朝西的方向。模型：[https://schema.org/Number](https://schema.org/Number)- `type[string]`：必须等于`SolarTracker`  - `windSafetyAngle[number]`：面板在风速超过操作阈值时假定的安全角度设定值。该位置最小化了帆的效果并降低了由风抬起或压力引起的结构应力。模型：[https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `deviceCategory`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 数据模型属性描述  
按字母顺序排序（单击查看详细信息）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完整的YAML详细信息</strong></summary>    
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
## 示例有效载荷    
#### SolarTracker NGSI-v2 键值示例    
这是一个SolarTracker在JSON格式中的键值示例。该示例与NGSI-v2兼容，当使用`options=keyValues`时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### SolarTracker NGSI-v2 规范化示例    
这是一个SolarTracker在JSON格式中的规范化示例。该示例与NGSI-v2兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### SolarTracker NGSI-LD 键值示例    
这是一个SolarTracker在JSON-LD格式中的键值示例。该示例与NGSI-LD兼容，当使用`options=keyValues`时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### SolarTracker NGSI-LD 规范化示例    
这是一个SolarTracker在JSON-LD格式中的规范化示例。该示例与NGSI-LD兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
请参阅[FAQ 10](https://smartdatamodels.org/index.php/faqs/)，以了解如何处理数量单位  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

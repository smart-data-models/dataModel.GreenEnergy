<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: SolarTracker  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Description of the data model SolarTracker **  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `altitude[number]`: The elevation of the installation site above mean sea level. This value is used by the solar algorithm to refine the calculation of the sun's position and atmospheric refraction  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `backtracking[string]`: Enum:'on','off'. Indicates whether the solar tracker is in backtracking mode to prevent row-to-row shadowing, deviating from the optimal sun-angle position  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]`: Represents the current charge level of the battery, expressed as a percentage of its total capacity (0 to 100)  . Model: [https://schema.org/Number](https://schema.org/Number)- `boardDirection[string]`: Enum:'-1','1'. Specifies the physical orientation of the control board based on the position of the emergency stop button (Eastward-facing = 1; Westward-facing = -1)  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentAngle[number]`: The current angular position of the panel. A value of 0 indicates the panel is horizontal (facing directly upward). Minimum values represent an Eastward orientation, while maximum values represent a Westward orientation  . Model: [https://schema.org/Number](https://schema.org/Number)- `currentPowerConsumption[number]`: The real-time electrical power demand measured in Watts  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateUpdate[date-time]`: The date when the configuration was updated  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `description[string]`: A description of this item  - `deviceCategory[string]`: Enum:'PCU','FCU','SCU'. Specifies the classification of the device within the system  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`: Enum:'Online','Offline'. Indicates the current operational connectivity status of the device  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `ipAddress[array]`: List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxAngleLimit[number]`: The maximum allowable angular position towards the West. This software limit acts as a hard ceiling; the panel will not rotate beyond this value even if the calculated target angle is greater  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPowerRecorded[number]`: The highest level of active electrical power consumption recorded during the last movement, measured in Watts  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPowerThreshold[number]`: The safety limit for power consumption during motor operation. If the electrical power exceeds this threshold, the panel movement is immediately interrupted to prevent mechanical damage or motor overload  . Model: [https://schema.org/Number](https://schema.org/Number)- `minAngleLimit[number]`: The minimum allowable angular position towards the East. This parameter defines a mandatory operational boundary; the panel will not rotate further East than this value, regardless of the requested target position  . Model: [https://schema.org/Number](https://schema.org/Number)- `minPowerRecorded[number]`: The lowest level of active electrical power consumption recorded during the last movement, measured in Watts  . Model: [https://schema.org/Number](https://schema.org/Number)- `motorDirection[string]`: Enum:'-1','1'. Defines the physical mounting orientation of the motor, which determines the polarity of the rotation (Eastward-facing = 1; Westward-facing = -1)  . Model: [https://schema.org/Text](https://schema.org/Text)- `movementInterval[string]`: Enum:'5','10','15'. Defines the time frequency at which the panel adjusts its position. The value must be one of the predefined intervals: 5, 10, or 15 minutes  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: The name of this item  - `operatingMode[string]`: Enum:'automatic','manual','safesnow','safesnowsensor','safewind','safewindsensor','maintenance'. Defines the current functional state of the panel. This mode dictates whether the tracker follows the solar algorithm or responds to external overrides/safety events  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `panelLength[number]`: The dimension of the panel measured along the axis perpendicular to the axis of rotation. This value is critical for calculating the shadow cast by the panel and determining the appropriate backtracking movement  . Model: [https://schema.org/Number](https://schema.org/Number)- `restingAngle[number]`: The specific angular position the panel assumes during the night or when the sun is below the horizon. This position is used to park the tracker until the next sunrise  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `snowSafetyAngle[number]`: The specific angular position the panel must adopt during a snow event. This angle is designed to facilitate snow shedding and prevent excessive structural loading on the tracker  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `targetAngle[number]`: The target angular setpoint for the panel's orientation. A value of 0 indicates the panel is horizontal (facing directly upward). Minimum values represent an Eastward orientation, while maximum values represent a Westward orientation  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: It must be equal to `SolarTracker`  - `windSafetyAngle[number]`: The safety setpoint angle the panel assumes when wind speeds exceed the operational threshold. This position minimize the sail effect and reduce structural stress caused by wind uplift or pressure  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `deviceCategory`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
notes appearing at the beginning of the spec  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
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
notes appearing in the middle of the spec  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### SolarTracker NGSI-v2 key-values Example    
Here is an example of a SolarTracker in JSON format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
#### SolarTracker NGSI-v2 normalized Example    
Here is an example of a SolarTracker in JSON format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
#### SolarTracker NGSI-LD key-values Example    
Here is an example of a SolarTracker in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
#### SolarTracker NGSI-LD normalized Example    
Here is an example of a SolarTracker in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
notes appearing in the footer of the spec  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

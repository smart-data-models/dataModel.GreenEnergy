<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
Entity: SolarTracker  
====================<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60) 
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
Globale Beschreibung: **Beschreibung des Datenmodells SolarTracker **  
Version: 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

## Liste der Eigenschaften  

 
<sup><sub>[*] Wenn in einem Attribut kein Typ angegeben ist, kann es mehrere Typen oder unterschiedliche Formate/Muster haben</sub></sup>  
- `address[object]`: Die Postanschrift. Modell: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien. Modell: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der die Straßenadresse liegt und die in der Region liegt. Modell: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der die Ortschaft liegt und die im Land liegt. Modell: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel 03578. Modell: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel 24004. Modell: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenadresse. Modell: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Eine Nummer, die ein bestimmtes Grundstück auf einer öffentlichen Straße identifiziert    
- `alternateName[string]`: Ein alternativer Name für dieses Element  
- `altitude[number]`: Die Höhe der Installationsstelle über dem mittleren Meeresspiegel. Dieser Wert wird vom Solalgorithmus verwendet, um die Berechnung der Sonnenposition und der atmosphärischen Refraktion zu verfeinern. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `areaServed[string]`: Das geografische Gebiet, in dem ein Dienst oder ein angebotenes Element bereitgestellt wird. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `backtracking[string]`: Enum:'on','off'. Gibt an, ob der Solarsucher im Backtracking-Modus ist, um Row-to-Row-Shadowing zu vermeiden und von der optimalen Sonnenposition abzuweichen. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `batteryLevel[number]`: Stellt den aktuellen Ladezustand des Akkus dar, ausgedrückt als Prozentsatz seiner Gesamtkapazität (0 bis 100). Modell: [https://schema.org/Number](https://schema.org/Number)  
- `boardDirection[string]`: Enum:'-1','1'. Legt die physische Ausrichtung der Steuerung auf der Grundlage der Position des Notausschalters fest (ostwärts gerichtet = 1; westwärts gerichtet = -1). Modell: [https://schema.org/Text](https://schema.org/Text)  
- `currentAngle[number]`: Die aktuelle Winkelposition des Panels. Ein Wert von 0 zeigt an, dass das Panel horizontal (direkt nach oben gerichtet) ist. Mindestwerte stellen eine ostwärts gerichtete Ausrichtung dar, während Maximalwerte eine westwärts gerichtete Ausrichtung darstellen. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `currentPowerConsumption[number]`: Die Echtzeit-Elektrizitätsnachfrage, gemessen in Watt. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `dataProvider[string]`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Datenentität identifiziert  
- `dateCreated[date-time]`: Zeitstempel der Erstellung der Entität. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `dateUpdate[date-time]`: Das Datum, an dem die Konfiguration aktualisiert wurde. Modell: [http://schema.org/DateTime](http://schema.org/DateTime)  
- `description[string]`: Eine Beschreibung dieses Elements  
- `deviceCategory[string]`: Enum:'PCU','FCU','SCU'. Legt die Klassifizierung des Geräts im System fest. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `deviceState[string]`: Enum:'Online','Offline'. Gibt den aktuellen Betriebszustand des Geräts an. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `id[*]`: Eindeutige Identifikation der Entität  
- `ipAddress[array]`: Liste der IP-Adressen des Geräts. Es kann eine durch Kommas getrennte Liste von Werten sein, wenn das Gerät mehrere IP-Adressen hat. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `location[*]`: Geojson-Referenz zum Element. Es kann ein Punkt, eine Linie, ein Polygon, MultiPunkt, MultiLinie oder MultiPolygon sein  
- `maxAngleLimit[number]`: Der maximal zulässige Winkel zur Westseite. Diese Softwarebegrenzung fungiert als harte Obergrenze; das Panel wird nicht über diesen Wert hinaus rotieren, auch wenn der berechnete Zielwinkel größer ist. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `maxPowerRecorded[number]`: Der höchste aktive elektrische Leistungsverbrauch, der während der letzten Bewegung aufgezeichnet wurde, gemessen in Watt. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `maxPowerThreshold[number]`: Die Sicherheitsbegrenzung für den Leistungsverbrauch während des Motorbetriebs. Wenn die elektrische Leistung diesen Schwellenwert überschreitet, wird die Panelbewegung sofort unterbrochen, um mechanische Schäden oder Motorüberlastung zu vermeiden. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `minAngleLimit[number]`: Der minimal zulässige Winkel zur Ostseite. Dieser Parameter definiert eine obligatorische Betriebsgrenze; das Panel wird nicht weiter östlich als diesen Wert rotieren, unabhängig von der angeforderten Zielposition. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `minPowerRecorded[number]`: Der niedrigste aktive elektrische Leistungsverbrauch, der während der letzten Bewegung aufgezeichnet wurde, gemessen in Watt. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `motorDirection[string]`: Enum:'-1','1'. Definiert die physische Montageorientierung des Motors, die die Polarität der Rotation bestimmt (ostwärts gerichtet = 1; westwärts gerichtet = -1). Modell: [https://schema.org/Text](https://schema.org/Text)  
- `movementInterval[string]`: Enum:'5','10','15'. Definiert die Zeitfrequenz, mit der das Panel seine Position anpasst. Der Wert muss einer der vordefinierten Intervalle sein: 5, 10 oder 15 Minuten. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Der Name dieses Elements  
- `operatingMode[string]`: Enum:'automatisch','manuell','safesnow','safesnowsensor','safewind','safewindsensor','wartung'. Definiert den aktuellen Funktionszustand des Panels. Dieser Modus bestimmt, ob der Sucher dem Solalgorithmus folgt oder auf externe Überschreibungen/Sicherheitsevents reagiert. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: Eine Liste, die eine JSON-codierte Folge von Zeichen enthält, die auf die eindeutigen IDs der Eigentümer verweisen  
- `panelLength[number]`: Die Dimension des Panels, gemessen entlang der Achse senkrecht zur Drehachse. Dieser Wert ist entscheidend für die Berechnung des Schattens, den das Panel wirft, und für die Bestimmung der geeigneten Rückverfolgungsbewegung. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `restingAngle[number]`: Die spezifische Winkelposition, die das Panel während der Nacht oder wenn die Sonne unter dem Horizont ist, einnimmt. Diese Position wird verwendet, um den Sucher bis zum nächsten Sonnenaufgang zu parken. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen zu diesem Element verweisen  
- `snowSafetyAngle[number]`: Die spezifische Winkelposition, die das Panel während eines Schneereignisses einnehmen muss. Dieser Winkel ist so konzipiert, dass er das Abwerfen von Schnee erleichtert und übermäßige strukturelle Belastungen auf den Sucher vermeidet. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angeben. Es wird empfohlen, den vollständig qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden  
- `targetAngle[number]`: Der Zielwinkel für die Ausrichtung des Panels. Ein Wert von 0 zeigt an, dass das Panel horizontal (direkt nach oben gerichtet) ist. Mindestwerte stellen eine ostwärts gerichtete Ausrichtung dar, während Maximalwerte eine westwärts gerichtete Ausrichtung darstellen. Modell: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: Es muss gleich `SolarTracker` sein  
- `windSafetyAngle[number]`: Der Sicherheitszielwinkel, den das Panel einnimmt, wenn die Windgeschwindigkeit den Betriebsgrenzwert überschreitet. Diese Position minimiert den Segelleffekt und reduziert den strukturellen Stress, der durch Windaufzug oder -druck verursacht wird. Modell: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
Erforderliche Eigenschaften  
- `deviceCategory`  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## Beschreibung des Datenmodells der Eigenschaften  
 
Sortiert alphabetisch (klicken für Details)  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>Vollständige YAML-Details</strong></summary>    
 
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
 
## Beispieldaten    
 
#### SolarTracker NGSI-v2 Schlüssel-Wert-Beispiel    
 
Hier ist ein Beispiel für einen SolarTracker im JSON-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
#### SolarTracker NGSI-v2 normalisiertes Beispiel    
 
Hier ist ein Beispiel für einen SolarTracker im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
#### SolarTracker NGSI-LD Schlüssel-Wert-Beispiel    
 
Hier ist ein Beispiel für einen SolarTracker im JSON-LD-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
#### SolarTracker NGSI-LD normalisiertes Beispiel    
 
Hier ist ein Beispiel für einen SolarTracker im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort darauf zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
 
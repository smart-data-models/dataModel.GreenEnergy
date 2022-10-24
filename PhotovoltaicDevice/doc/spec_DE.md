<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: PhotovoltaicDevice  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell dient zur Beschreibung der mechanischen, elektrischen und thermischen Eigenschaften von Photovoltaikmodulen gemäß *STC - Standard Test Condition* und *NOCT - Normal Operating Cell Temperature*. *Bemerkung* : Dieses Datenmodell kann direkt als Hauptentität zur Beschreibung des `Photovoltaic Device` oder als Unterentität des Datenmodells `DEVICE` unter Verwendung eines Verweises durch das Attribut `refDevice` verwendet werden. Die für STC und NOCT durchgeführten Messungen sind `Pmax` (maximale Nennleistung), `Umpp` (optimale Betriebsspannung), `Impp` (optimaler Betriebsstrom), `Uoc` (Leerlaufspannung), `Isc` (Kurzschlussstrom). *Zusätzliche Informationen zum Datenmodell:* Dieses Datenmodell kann direkt als Hauptentität zur Beschreibung des Geräts [PHOTOVOLTAIC] oder als Unterentität des Datenmodells [DEVICE] unter Verwendung eines Verweises durch das Attribut `refDevice` verwendet werden.**  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `MaxPressureLoad[object]`: aximale mechanische Druckbelastung (Scherung, Elastizität, Kompression) auf eine Platte. Das Format ist durch eine Untereigenschaft mit 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel, **PAL** steht für Pascal  . Model: [https://schema.org/Number](https://schema.org/Number)- `MaximumSystemVoltage[number]`: Maximal zulässige Systemspannung für das **Modul**. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `NominalPower[number]`: Nennleistung für das **Panel**. Dies ist derselbe Wert wie bei den Positionen [Pmax] für das Attribut [moduleSTC]. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **WTT** für Watt  . Model: [https://schema.org/Number](https://schema.org/Number)- `PanelNbModules[number]`: Anzahl der 'Module' pro 'Panel'  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `application[array]`: Zielanwendung in Bezug auf den Typ des Solarmoduls (in unserem Fall "elektrisch"). Ein eindeutiger Wert. https://schema.org/Text. Enum:'elektrisch, thermisch, andere'  - `applicationClass[array]`: Bewertung der potenziellen Gefahren, die mit dem Modul verbunden sind. Ein eindeutiger Wert. Enum:'A, B, C'  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaWeight[number]`: Fläche Gewicht gemessen in kg/m². Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **28** für Kilogramm pro Quadratmeter  . Model: [https://schema.org/Number](https://schema.org/Number)- `brandName[string]`: Markenname des Artikels  . Model: [https://schema.org/brand](https://schema.org/brand)- `cellDimension[object]`: Externe Dimension einer Zelle. Das Format ist durch eine Untereigenschaft mit 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MMT** für Millimeter.  - `cellOperatingTemperature[object]`: Dies ist der Nennbetriebstemperaturbereich der Zellen, in dem sie Sonnenenergie sammeln. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CEL** für Grad Celsius  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `cellType[array]`: Art der Zellen, die für den Bau der Photovoltaikanlage verwendet werden. 2 Arten von Technologien *`Kristalline`* oder *`Dünne Schichten`*. Ein eindeutiger Wert. Enum:'amorphesSilizium, CfTe, CIS, monokristallin, polykristallin, andere'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateLastReported[string]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem das Gerät erfolgreich Daten gemeldet hat. Datum und Uhrzeit im ISO8601 UTC-Format.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `documentation[string]`: Technische Dokumentation (Installation / Wartung / Gebrauch)  . Model: [https://schema.org/Text](https://schema.org/Text)- `fireClass[array]`: Bewertung für das Feuer (IEC 61730). Ein eindeutiger Wert. Enum:'A, B, C'  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `installationCondition[array]`: Bedingung und Möglichkeit der Verwendung in den folgenden Umgebungen. Eine Kombination. Enum:'Wüste, Staub, extremeHitze, extremeKälte, extremeKlima, extremeFeuchtigkeit, marine, keine, andere, salzhaltig, Sand, seismisch'  . Model: [https://schema.org/Text](https://schema.org/Text)- `installationMode[array]`: Positionierung des Geräts in Bezug auf ein Bodenreferenzsystem. Ein eindeutiger Wert. Enum:'Boden, Sonstiges, Mast, Dach, Wand'  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manufacturerName[string]`: Hersteller Name des Artikels  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `modelName[string]`: Modell Name des Artikels  . Model: [https://schema.org/model](https://schema.org/model)- `moduleDimension[object]`:  Äußere Abmessung eines Moduls. Ein Modul kann eine Baugruppe von 1 bis n Zellen sein. Das Format wird durch eine Untereigenschaft mit 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MMT** für Millimeter  - `moduleNOCT[object]`: Messungen der normalen Betriebstemperatur der Zelle. Das Format ist durch eine Untereigenschaft mit 5 Elementen strukturiert. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `moduleNbCells[number]`: Anzahl der "Zellen" pro "Modul  . Model: [https://schema.org/Number](https://schema.org/Number)- `moduleSTC[object]`: Messungen der Standard-Testbedingungen. Das Format ist durch eine Untereigenschaft mit 5 Elementen strukturiert. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `moduleYieldRate[number]`: Positionierung des Geräts in Bezug auf ein Bodenreferenzsystem. Ein eindeutiger Wert  . Model: [https://schema.org/Number](https://schema.org/Number)- `nTCClass[number]`: Der negative Temperaturkoeffizient des Widerstands - *NTC*, beschreibt die relative Änderung einer physikalischen Eigenschaft, die mit einer bestimmten negativen Temperaturänderung verbunden ist. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pTCClass[number]`:  Der positive Temperaturkoeffizient des Widerstands - *PTC* - beschreibt die relative Änderung einer physikalischen Eigenschaft, die mit einer bestimmten Änderung der positiven Temperatur verbunden ist. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  - `panelDimension[object]`: Äußere Abmessungen eines Paneels. Ein Solarmodul kann aus 1 bis n Modulen bestehen, die ihrerseits aus mehreren Zellen zusammengesetzt sind, die die Wärme der Sonnenstrahlen aufnehmen. Das Format ist durch eine Untereigenschaft mit 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MMT** für Millimeter.  - `panelLifetime[number]`: Durchschnittliche Lebensdauer einer Platte. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **ANN** für Jahr  . Model: [https://schema.org/Number](https://schema.org/Number)- `panelOperatingTemperature[object]`: Umgebungstemperaturbereich für den Betrieb. Dies ist die minimale und maximale Beständigkeit gegen Kälte und Hitze bei der Verwendung des Panels. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CEL** für Grad Celsius  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `panelWeight[number]`: Gewicht eines Paneels (manchmal wird das Gewicht in kg / m² angegeben). Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel, **KGM** steht für Kilogramm  . Model: [https://schema.org/Number](https://schema.org/Number)- `panelYieldCurve[array]`: Möglichkeit 1. Energieproduktionsertragskurve des Panels ausgehend von seiner [Nennleistung] bei [T0] und entlang seiner [Panel-Lebensdauer]. Die in der Liste angegebenen Messwerte sind eine Abfolge von Energieerzeugungskapazitäten in Prozent, beginnend bei 5 Jahren mit einem "Schritt" von 5 Jahren gemäß den vom Hersteller bereitgestellten Informationen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  - `performanceLowIrradiance[number]`: Durchschnittlicher relativer Ertrag zur Leistung bei niedriger Bestrahlungsstärke. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Percent  . Model: [https://schema.org/Number](https://schema.org/Number)- `possibilityOfUse[array]`: Die Möglichkeit der Nutzung. Ein eindeutiger Wert. Enum:'gemischt, mobil, sonstiges, stationär'  . Model: [https://schema.org/Text](https://schema.org/Text)- `protectionIP[string]`: IP 'Ingress Protection' (Schutz gegen Eindringen) für die Junction Box. Diese Stufe klassifiziert und bewertet den Grad des Schutzes, den mechanische und elektrische Gehäuse gegen Eindringen, Staub, versehentliche Berührung und Wasser gemäß der Norm der Internationalen Elektrotechnischen Kommission (EN 60-529) bieten. Erste Ziffer: Schutz gegen feste Partikel (einzelne Ziffer: 0-6 oder 'X'). Zweite Ziffer: Schutz gegen das Eindringen von Flüssigkeiten (Einzelne Ziffer: 0-9 oder 'X'), dritte Ziffer: Personenschutz gegen den Zugang zu gefährlichen Teilen (optionaler Zusatzbuchstabe). Vierte Ziffer: Sonstige Schutzmaßnahmen (optionaler Zusatzbuchstabe)  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[*]`: Verweis auf die Haupteinheit [Gerät] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) bei Verwendung als zweite Verbindung  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[*]`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit dem Repository verknüpft ist.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `serialNumber[array]`: Liste der Seriennummern der vom Hersteller gelieferten und in Betrieb befindlichen Photovoltaikanlage an einem einzigen Standort  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `temperatureCoefficient[object]`:  Koeffizient des Temperatureinflusses auf die Platte. Das Format ist durch eine Untereigenschaft mit 3 Elementen strukturiert. Pmax in Watt. Uoc in Volt. Isc in Ampere  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `type[string]`: NGSI-Entitätstyp. Es muss PhotovoltaicDevice sein.  - `typeOfUse[array]`: Akzeptierte Verwendung hinsichtlich der Positionierung in einer Innen-/Außenumgebung. Ein eindeutiger Wert. Enum:'innen, außen, gemischt, andere'  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateLastReported`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Die für STC und NOCT durchgeführten Messungen sind - [Pmax] Maximale Nennleistung gemessen in **WTT** steht für Watt. - Umpp] Optimale Betriebsspannung gemessen in **VLT** steht für Volt. - Impp] Optimaler Betriebsstrom gemessen in **AMP** steht für Ampere. - Uoc] Leerlaufspannung gemessen in **VLT** steht für Volt. - Isc] Kurzschlussstrom, gemessen in **AMP**, entspricht Ampere.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### PhotovoltaicDevice NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein PhotovoltaicDevice im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### PhotovoltaicDevice NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein PhotovoltaicDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### PhotovoltaicDevice NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein PhotovoltaicDevice im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### PhotovoltaicDevice NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein PhotovoltaicDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

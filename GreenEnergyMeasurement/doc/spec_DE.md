Entität: GreenEnergyMeasurement  
===============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/GreenEnergyMeasurement/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein Momentanwert der Stromerzeugung aus grünen Energiequellen**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `biomassPowerGenerated`: Gibt die Menge an Strom an, die unter Verwendung von Energie aus Biomasse erzeugt wurde. Der Code der Maßeinheit (Text) wird unter Verwendung des UN/CEFACT Common Code angegeben (max. 3 Zeichen).  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `eolicPowerGenerated`: Gibt die Menge an Strom an, die mit Hilfe von Sonnenenergie erzeugt wurde. Der Einheitencode (Text) der Messung wird unter Verwendung des UN/CEFACT Common Code angegeben (max. 3 Zeichen).  - `geothermalPowerGenerated`: Gibt die Menge des mit geothermischer Energie erzeugten Stroms an. Der Code der Maßeinheit (Text) wird unter Verwendung des UN/CEFACT Common Code angegeben (max. 3 Zeichen).  - `hydroPowerGenerated`: Gibt die Menge der aus Wasserkraft erzeugten Energie an. Der Einheitencode (Text) der Messung wird unter Verwendung des UN/CEFACT Common Code angegeben (max. 3 Zeichen).  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refGreenEnergyGenerator`: Ein Verweis auf die Entität `GreenEnergyGenerator`, zu der die Messung gehört.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `solarPowerGenerated`: Gibt die mit Solarenergie erzeugte Strommenge an. Der Einheitencode (Text) der Messung wird unter Verwendung des UN/CEFACT Common Code angegeben (max. 3 Zeichen).  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI-Entitätstyp: Es muss GreenEnergyMeasurement sein    
Erforderliche Eigenschaften  
- `id`  - `refGreenEnergyGenerator`  - `type`    
Generisches Modell für eine Momentaufnahme zur Messung der Energie, die mit einer oder mehreren grünen Energiequellen erzeugt wurde. Daher kann eine Entität vom Typ "GreenEnergyMeasurement" nicht ohne eine zugehörige Entität vom Typ "GreenEnergyGenerator" existieren.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GreenEnergyMeasurement:    
  description: 'A instantaneous measure of power generation using green energy sources'    
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
    biomassPowerGenerated:    
      description: 'Specifies the amount of power generated using biomass energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
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
    eolicPowerGenerated:    
      description: 'Specifies the amount of power generated using eolic energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    geothermalPowerGenerated:    
      description: 'Specifies the amount of power generated using geothermal energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    hydroPowerGenerated:    
      description: 'Specifies the amount of power generated using hydropower energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    id:    
      anyOf: &greenenergymeasurement_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *greenenergymeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refGreenEnergyGenerator:    
      anyOf:    
        - format: uri    
          type: string    
        - anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
      description: 'A reference to the entity `GreenEnergyGenerator` which it belongs the measurement.'    
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
    solarPowerGenerated:    
      description: 'Specifies the amount of power generated using solar energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KWT    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be GreenEnergyMeasurement'    
      type: string    
      value: GreenEnergyMeasurement    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refGreenEnergyGenerator    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/GreenEnergyMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GreenEnergy/GreenEnergyMeasurement/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Beispiel-Nutzlasten  
#### GreenEnergyMeasurement NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine GreenEnergyMeasurement im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyMeasurement:santander:GreenEnergyMeasurement:Generator:a34f24b",  
  "type": "GreenEnergyMeasurement",  
  "source": "bike-in.com",  
  "dataProvider": "bike-in.com",  
  "dateCreated": "2019-01-01T12:00:00Z",  
  "dateModified": "2020-07-22T12:00:00Z",  
  "solarPowerGenerated":1.2,  
  "eolicPowerGenerated":3,  
  "hydroPowerGenerated":0,  
  "biomassPowerGenerated":0,  
  "geothermalPowerGenerated":0,  
  "refGreenEnergyGenerator":"urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001"  
}  
```  
#### GreenEnergyMeasurement NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein GreenEnergyMeasurement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyMeasurement:santander:GreenEnergyMeasurement-Generator:a34f24b",  
  "type": "GreenEnergyMeasurement",  
  "solarPowerGenerated":{  
    "type":"Number",  
    "value":5.1  
  },  
  "eolicPowerGenerated":{  
    "type":"Number",  
    "value":2.1  
  },  
  "hydroPowerGenerated":{  
    "type":"Number",  
    "value":0  
  },  
  "biomassPowerGenerated":{  
    "type":"Number",  
    "value":0  
  },  
  "geothermalPowerGenerated":{  
    "type":"Number",  
    "value":0  
  },  
  "refGreenEnergyGenerator":{  
    "type":"Relationship",  
    "value":"urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001"  
  }  
}  
```  
#### GreenEnergyMeasurement NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine GreenEnergyMeasurement im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyMeasurement:santander:GreenEnergyMeasurement-Generator:a34f24b",  
  "type": "GreenEnergyMeasurement",  
  "solarPowerGenerated": {  
    "type": "Number",  
    "value": 5.1  
  },  
  "eolicPowerGenerated": {  
    "type": "Number",  
    "value": 2.1  
  },  
  "hydroPowerGenerated": {  
    "type": "Number",  
    "value": 2.1  
  },  
  "biomassPowerGenerated": {  
    "type": "Number",  
    "value": 2.1  
  },  
  "geothermalPowerGenerated": {  
    "type": "Number",  
    "value": 2.1  
  },  
  "refGreenEnergyGenerator": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GreenEnergyMeasurement NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine GreenEnergyMeasurement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GreenEnergyMeasurement:santander:GreenEnergyMeasurement:Generator:a34f24b",  
  "type": "GreenEnergyMeasurement",  
  "source": "bike-in.com",  
  "dataProvider": "bike-in.com",  
  "dateCreated": "2019-01-01T12:00:00Z",  
  "dateModified": "2020-07-22T12:00:00Z",  
  "solarPowerGenerated": 1.2,  
  "eolicPowerGenerated": 3,  
  "hydroPowerGenerated": 0,  
  "biomassPowerGenerated": 0,  
  "geothermalPowerGenerated": 0,  
  "refGreenEnergyGenerator": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht
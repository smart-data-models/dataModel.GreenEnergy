Entity: GreenEnergyMeasurement  
==============================  
[Open License](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/GreenEnergyMeasurement/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **A instantaneous measure of power generation using green energy sources**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `biomassPowerGenerated`: Specifies the amount of power generated using biomass energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `eolicPowerGenerated`: Specifies the amount of power generated using eolic energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).  - `geothermalPowerGenerated`: Specifies the amount of power generated using geothermal energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).  - `hydroPowerGenerated`: Specifies the amount of power generated using hydropower energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refGreenEnergyGenerator`: A reference to the entity `GreenEnergyGenerator` which it belongs the measurement.  - `seeAlso`: list of uri pointing to additional resources about the item  - `solarPowerGenerated`: Specifies the amount of power generated using solar energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity Type: It has to be GreenEnergyMeasurement    
Required properties  
- `id`  - `refGreenEnergyGenerator`  - `type`    
Generic model for a snapshot measure of energy generated using one or more green energy sources. Thus, an entity of type `GreenEnergyMeasurement` cannot exist without an accompanying Entity of Type GreenEnergyGenerator.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### GreenEnergyMeasurement NGSI-v2 key-values Example    
Here is an example of a GreenEnergyMeasurement in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GreenEnergyMeasurement NGSI-v2 normalized Example    
Here is an example of a GreenEnergyMeasurement in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### GreenEnergyMeasurement NGSI-LD key-values Example    
Here is an example of a GreenEnergyMeasurement in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GreenEnergyMeasurement NGSI-LD normalized Example    
Here is an example of a GreenEnergyMeasurement in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units
Entität: GreenEnergyMeasurement  
===============================







- `id`  



<details><summary><strong>full yaml details</strong></summary>    

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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    biomassPowerGenerated:    
      description: 'Specifies the amount of power generated using biomass energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KWT    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    eolicPowerGenerated:    
      description: 'Specifies the amount of power generated using eolic energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KWT    
    geothermalPowerGenerated:    
      description: 'Specifies the amount of power generated using geothermal energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KWT    
    hydroPowerGenerated:    
      description: 'Specifies the amount of power generated using hydropower energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *greenenergymeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    solarPowerGenerated:    
      description: 'Specifies the amount of power generated using solar energy. The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KWT    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be GreenEnergyMeasurement'    
      type: Property    
      value: GreenEnergyMeasurement    
  required:    
    - id    
    - type    
    - refGreenEnergyGenerator    
  type: object    
```  
</details>    





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
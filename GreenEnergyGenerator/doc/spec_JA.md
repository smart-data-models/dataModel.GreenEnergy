[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

======================









- `id`  



<details><summary><strong>full yaml details</strong></summary>    

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
        "https://smart-data-models.github.io/data-models/context.jsonld"  
    ]  
}  
```  

Entity: GreenEnergyMeasurement  
==============================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **A instantaneous measure of power generation using green energy sources**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided.  - `biomassPowerGenerated`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `eolicPowerGenerated`:   - `geothermalPowerGenerated`:   - `hydroPowerGenerated`:   - `id`:   - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refGreenEnergyGenerator`:   - `seeAlso`:   - `solarPowerGenerated`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type    
Required properties  
- `id`  - `refGreenEnergyGenerator`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GreenEnergyMeasurement:    
  description: 'A instantaneous measure of power generation using green energy sources'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    biomassPowerGenerated:    
      minimum: 0    
      type: number    
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
      minimum: 0    
      type: number    
    geothermalPowerGenerated:    
      minimum: 0    
      type: number    
    hydroPowerGenerated:    
      minimum: 0    
      type: number    
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
      type: Property    
    refGreenEnergyGenerator:    
      anyOf:    
        - format: uri    
          type: string    
        - anyOf: *greenenergymeasurement_-_properties_-_owner_-_items_-_anyof    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    solarPowerGenerated:    
      minimum: 0    
      type: number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      type: string    
      value: GreenEnergyMeasurement    
  required:    
    - id    
    - type    
    - refGreenEnergyGenerator    
  type: object    
```  
</details>    
## Example payloads    
#### GreenEnergyMeasurement NGSI V2 key-values Example    
Here is an example of a GreenEnergyMeasurement in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GreenEnergyMeasurement NGSI V2 normalized Example    
Here is an example of a GreenEnergyMeasurement in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
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
  "refGreenEnergyGenerator":"urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001",  
  "@context": ["https://smart-data-models.github.io/data-models/context.jsonld"]  
}  
```  
#### GreenEnergyMeasurement NGSI-LD normalized Example    
Here is an example of a GreenEnergyMeasurement in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

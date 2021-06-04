Entité : GreenEnergyMeasurement  
===============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/GreenEnergyMeasurement/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Mesure instantanée de la production d'électricité à partir de sources d'énergie vertes**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `biomassPowerGenerated`: Indique la quantité d'énergie produite à partir de la biomasse. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `eolicPowerGenerated`: Indique la quantité d'énergie produite à partir de l'énergie éolienne. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  - `geothermalPowerGenerated`: Indique la quantité d'énergie produite à partir de l'énergie géothermique. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  - `hydroPowerGenerated`: Indique la quantité d'énergie produite à partir de l'énergie hydroélectrique. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refGreenEnergyGenerator`: Une référence à l'entité `GreenEnergyGenerator` à laquelle il appartient la mesure.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `solarPowerGenerated`: Indique la quantité d'énergie produite à partir de l'énergie solaire. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI : Il doit s'agir de GreenEnergyMeasurement.    
Propriétés requises  
- `id`  - `refGreenEnergyGenerator`  - `type`    
Modèle générique pour une mesure instantanée de l'énergie générée à l'aide d'une ou plusieurs sources d'énergie verte. Ainsi, une entité de type `GreenEnergyMeasurement` ne peut exister sans une entité de type GreenEnergyGenerator qui l'accompagne.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      type: Geoproperty    
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
            format: uri    
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
## Exemples de charges utiles  
#### GreenEnergyMeasurement Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de GreenEnergyMeasurement au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Mesure de l'énergie verte NGSI-v2 normalisée Exemple  
Voici un exemple de GreenEnergyMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Valeurs-clés NGSI-LD de la mesure de l'énergie verte Exemple  
Voici un exemple de GreenEnergyMeasurement au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Mesure de l'énergie verte NGSI-LD normalisée Exemple  
Voici un exemple de GreenEnergyMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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

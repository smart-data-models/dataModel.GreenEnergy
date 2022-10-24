<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : GreenEnergyGenerator  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/GreenEnergyGenerator/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une station de générateur générique qui peut générer de l'énergie à partir de l'énergie verte**.  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `generationSources[array]`: Une liste des sources utilisées pour la production d'électricité. Enum : 'biomasse, éolien, géothermie, hydroélectricité, solaire'.  . Model: [https://schema.org/ItemList](https://schema.org/ItemList)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maxBiomassMeasure[number]`: Une mesure de l'énergie maximale de la biomasse qui peut être générée. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxEolicPowerMeasure[number]`: Mesure de l'énergie éolienne maximale qui peut être générée. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxGeothermalPowerGenerated[number]`: Mesure de l'énergie géothermique maximale qui peut être générée. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxHydroPowerMeasure[number]`: Mesure de l'énergie hydroélectrique maximale qui peut être produite. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxSolarPowerMeasure[number]`: Mesure de l'énergie solaire maximale qui peut être produite. Le code d'unité (texte) de mesure donné en utilisant le code commun du CEFACT-ONU (3 caractères maximum).  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `redistribution[boolean]`: Indique si l'énergie générée sera déversée dans le réseau.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `selfConsumption[boolean]`: Indiquez si l'énergie produite sera utilisée pour vous-même  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status[string]`: Statut du générateur d'énergie verte. Enum : 'outOfService, withIncidence, working' (hors service, avec incidence, en fonctionnement)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit être GreenEnergyGenerator.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Modèle générique de générateur d'énergie verte. Un dispositif qui peut générer de l'énergie en utilisant l'énergie verte solaire ou éolienne.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### GreenEnergyGenerator Exemple de valeurs-clés NGSI-v2  
Voici un exemple de GreenEnergyGenerator au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
</details>  
#### GreenEnergyGenerator NGSI-v2 normalisé Exemple  
Voici un exemple de GreenEnergyGenerator au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
</details>  
#### GreenEnergyGenerator Valeurs-clés NGSI-LD Exemple  
Voici un exemple de GreenEnergyGenerator au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
</details>  
#### GreenEnergyGenerator NGSI-LD normalisé Exemple  
Voici un exemple de GreenEnergyGenerator au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

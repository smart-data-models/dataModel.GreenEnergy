Entité : PhotovoltaicMeasurement  
================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicMeasurement/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le modèle de données est destiné à mesurer la puissance continue transférée par le panneau photo-voltaïque à un dispositif onduleur.**  

## Liste des propriétés  

- `activePower`: Puissance active, où phi est le déphasage du courant par rapport à la tension. Le code d'unité (texte) est donné en utilisant les UN/CEFACT_Common_Codes (3 caractères maximum). Par exemple, **KWT** représente le kilowatt.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `current`: Intensité électrique du courant. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **AMP** représente l'Ampère  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateEnergyMeteringStarted`: La date de début du comptage de l'énergie dans un format ISO8601 UTC.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObservedFrom`: Période d'observation : Date et heure de début dans un format ISO8601 UTC. Cet attribut peut être utilisé en complément de l'attribut 'dateObserved lorsqu'il correspond à un intervalle de temps à mettre en évidence.  - `dateObservedTo`: Période d'observation : Date et heure de fin dans un format ISO8601 UTC. Cet attribut peut être utilisé en complément de l'attribut "dateObserved" lorsqu'il correspond à un intervalle de temps à mettre en évidence.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `inverterStatus`: Puissance active, où phi est le déphasage du courant par rapport à la tension. Le code d'unité (texte) est donné en utilisant les UN/CEFACT_Common_Codes (3 caractères maximum). Par exemple, **KWT** représente le kilowatt. Enum : '00-Sur secteur, 01-Panne d'alimentation / Sur batterie, 02-Perte de communication, 03-Défaut de batterie, 04-Arrêt du système, 05-Perte de tension, 06-Surtension, 07-Chute de tension, 08-Elévation de tension, 09-Bruit de ligne, 10-Variation de fréquence, 11-Distorsion transitoire, 12-Distorsion harmonique'.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `nominalPeakPowerGeneration`: nominalPeakPowerGeneration est un nombre. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **KWT** représente un kilowatt.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `reactivePower`: Puissance réactive utilisée par les circuits. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **K5** représente le kilovolt-ampère-réactif.  - `refPhotovoltaicDevice`:   - `refPointOfInterest`: Référence à un [PointOfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) lié au Référentiel.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `temperature`: Température enregistrée au moment de l'observation par rapport à la température de référence nominale de l'appareil. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **CEL** représente le degré Celsius.  - `type`: Type d'entité NGSI. Il doit s'agir de PhotovoltaicMeasurement.    
Propriétés requises  
- `dateEnergyMeteringStarted`  - `dateObserved`  - `id`  - `location`  - `refPhotovoltaicDevice`  - `temperature`  - `type`    
Il peut avoir les valeurs suivantes. - instantané. De l'instant spécifique du temps - moyenne. La moyenne d'une période de temps - rms.     La moyenne quadratique d'une période de temps - maximum. Le maximum d'une période de temps - minimum. Le minimum d'une période de temps.  
Lorsque vous utilisez les valeurs [moyenne, rms, maximum, minimum], un autre attribut de métadonnées appelé "measurementInterval" doit être utilisé pour indiquer la durée de la période de mesure en secondes. De même, l'attribut de métadonnées "timestamp" doit correspondre à l'heure de fin de la période de mesure.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhotovoltaicMeasurement:    
  description: 'The Data Model is intended to measure the continuous power transferred by the photo-voltaic panel to an Inverter Device.'    
  properties:    
    activePower:    
      description: 'Active Power,where phi is the phase shift of the current compared to the voltage. The unit code (text) is given using the UN/CEFACT_Common_Codes (max 3 characters). For instance, For instance, **KWT** represents Kilowatt'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Kilowatt    
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
    current:    
      description: 'Electrical intensity of the current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Ampere    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateEnergyMeteringStarted:    
      description: 'The starting date for metering energy in an ISO8601 UTC format'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &photovoltaicmeasurement_-_properties_-_owner_-_items_-_anyof    
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
    inverterStatus:    
      description: 'Active Power,where phi is the phase shift of the current compared to the voltage. The unit code (text) is given using the UN/CEFACT_Common_Codes (max 3 characters). For instance, For instance, **KWT** represents Kilowatt. Enum:''00-On sector, 01-Power failure / On battery, 02-Loss of communication,  03-Battery fault, 04-System shutdown, 05-Tension dip, 06-Overvoltage, 07-Voltage drop, 08-Voltage increase, 09-Line noise, 10-Frequency variation, 11-Transient distortion, 12-Harmonic distortion'''    
      items:    
        enum:    
          - '00-On sector'    
          - '01-Power failure / On battery'    
          - '02-Loss of communication'    
          - '03-Battery fault'    
          - '04-System shutdown'    
          - '05-Tension dip'    
          - 06-Overvoltage    
          - '07-Voltage drop'    
          - '08-Voltage increase'    
          - '09-Line noise'    
          - '10-Frequency variation'    
          - '11-Transient distortion'    
          - '12-Harmonic distortion'    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
    nominalPeakPowerGeneration:    
      description: 'nominalPeakPowerGeneration is a number. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Kilowatt    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *photovoltaicmeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    reactivePower:    
      description: 'Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    refPhotovoltaicDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: ""    
      type: Relationship    
      x-ngsi:    
        model: 'Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL.'    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository.'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    temperature:    
      description: 'Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'degrees celsius'    
    type:    
      description: 'NGSI Entity type. It has to be PhotovoltaicMeasurement'    
      enum:    
        - PhotovoltaicMeasurement    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - refPhotovoltaicDevice    
    - dateEnergyMeteringStarted    
    - temperature    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### PhotovoltaicMeasurement Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de PhotovoltaicMeasurement au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
  "type": "PhotovoltaicMeasurement",  
  "dataProvider": "https://imredd.fr/en/home/",  
  "name": "Photovoltaic station IMREDD",  
  "description": "Photovoltaic data provided by the data logger ABB",  
  "seeAlso": "https://us.sunpower.com/products/solar-panels",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "61-63 Avenue Simone Veil"  
  },  
  "areaServed": "Nice",  
  "refPhotovoltaicDevice": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012",  
  "dateObserved": "2019-09-05T16:00:00.999Z",  
  "dateEnergyMeteringStarted": "2019-09-04T15:29:17.999Z",  
  "nominalPeakPowerGeneration": 179,  
  "temperature": 23.4  
}  
```  
#### PhotovoltaicMeasurement NGSI-v2 normalisé Exemple  
Voici un exemple de PhotovoltaicMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
  "type": "PhotovoltaicMeasurement",  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://imredd.fr/en/home/"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Photovoltaic station IMREDD"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Photovoltaic data provided by the data logger ABB"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://us.sunpower.com/products/solar-panels"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
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
      "streetAddress": "61-63 Avenue Simone Veil"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice"  
  },  
  "refPhotovoltaicDevice": {  
    "type": "Relationship",  
    "Object": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": "2019-09-05T16:00:00.999Z"  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": "2019-09-04T15:29:17.999Z"  
  },  
  "nominalPeakPowerGeneration": {  
    "type": "Property",  
    "value": 179  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 23.4  
  }  
}  
```  
#### Mesure du photovoltaïque Valeurs clés NGSI-LD Exemple  
Voici un exemple de PhotovoltaicMeasurement au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
  "type": "PhotovoltaicMeasurement",  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://imredd.fr/en/home/"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Photovoltaic station IMREDD"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Photovoltaic data provided by the data logger ABB"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://us.sunpower.com/products/solar-panels"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "61-63 Avenue Simone Veil"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice"  
  },  
  "refPhotovoltaicDevice": {  
    "type": "Relationship",  
    "Object": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": "2019-09-05T16:00:00.999Z"  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": "2019-09-04T15:29:17.999Z"  
  },  
  "nominalPeakPowerGeneration": {  
    "type": "Property",  
    "value": 179  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 23.4  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/common-schema.json",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### PhotovoltaicMeasurement NGSI-LD normalisé Exemple  
Voici un exemple de PhotovoltaicMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
  "type": "PhotovoltaicMeasurement",  
  "dataProvider": "https://imredd.fr/en/home/",  
  "name": "Photovoltaic station IMREDD",  
  "description": "Photovoltaic data provided by the data logger ABB",  
  "seeAlso": "https://us.sunpower.com/products/solar-panels",  
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
    "streetAddress": "61-63 Avenue Simone Veil"  
  },  
  "areaServed": "Nice",  
  "refPhotovoltaicDevice": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012",  
  "dateObserved": "2019-09-05T16:00:00.999Z",  
  "dateEnergyMeteringStarted": "2019-09-04T15:29:17.999Z",  
  "nominalPeakPowerGeneration": 179,  
  "temperature": 23.4,  
  "@context": [  
    "https://smart-data-models.github.io/data-models/common-schema.json",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  

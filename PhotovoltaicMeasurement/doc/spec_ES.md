<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: FotovoltaicaMedición  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicMeasurement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El modelo de datos está destinado a medir la potencia continua transferida por el panel fotovoltaico a un dispositivo inversor.**  
versión: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `activePower[number]`: Potencia activa, donde phi es el desfase de la corriente respecto a la tensión. El código de la unidad (texto) se da utilizando los UN/CEFACT_Common_Codes (máximo 3 caracteres). Por ejemplo, **KWT** representa el kilovatio  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[number]`: Intensidad eléctrica de la corriente. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **AMP** representa el amperio  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateEnergyMeteringStarted[string]`: La fecha de inicio de la medición de energía en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObservedFrom[string]`: Período de observación: Fecha y hora de inicio en un formato ISO8601 UTC. El atributo puede utilizarse además del atributo 'dateObserved cuando corresponde a un intervalo de tiempo que debe destacarse  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[string]`: Período de observación: Fecha y hora de finalización en un formato ISO8601 UTC. El atributo puede utilizarse además del atributo "dateObserved" cuando corresponde a un intervalo de tiempo que debe destacarse  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `inverterStatus[array]`: Potencia activa, donde phi es el desfase de la corriente respecto a la tensión. El código de la unidad (texto) se da utilizando los UN/CEFACT_Common_Codes (máximo 3 caracteres). Por ejemplo, **KWT** representa el kilovatio. Enum:'00-Sector, 01-Fallo de alimentación / En batería, 02-Pérdida de comunicación, 03-Fallo de batería, 04-Apagado del sistema, 05-Bajo de tensión, 06-Sobretensión, 07-Caída de tensión, 08-Aumento de tensión, 09-Ruido de línea, 10-Variación de frecuencia, 11-Distorsión transitoria, 12-Distorsión armónica'  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `nominalPeakPowerGeneration[number]`: nominalPeakPowerGeneration es un número. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **KWT** representa el kilovatio  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `reactivePower[number]`: Potencia reactiva utilizada por los circuitos. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **K5** representa el kilovoltio-amperio-reactivo  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPhotovoltaicDevice[*]`:   . Model: [Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL](Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL)- `refPointOfInterest[*]`: Referencia a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) vinculado con el Repositorio.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `temperature[number]`: Temperatura registrada en el momento de la Observación comparada con la temperatura nominal de referencia del dispositivo. El código de la unidad (texto) se indica utilizando los [Códigos comunes de la ONU/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **CEL** representa el grado Celsius  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Tiene que ser PhotovoltaicMeasurement  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateEnergyMeteringStarted`  - `dateObserved`  - `id`  - `location`  - `refPhotovoltaicDevice`  - `temperature`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Puede tener los siguientes valores. - instantáneo. Del instante concreto del tiempo - media. La media de un periodo de tiempo - rms.     La raíz cuadrada media de un período de tiempo - máximo. El máximo de un periodo de tiempo - mínimo. El mínimo de un período de tiempo.  
Cuando se utilicen los valores [promedio, rms, máximo, mínimo] debe utilizarse otro atributo de metadatos denominado 'measurementInterval' para indicar la duración del periodo de medición en segundos. Además, el atributo de metadatos "timestamp" debe ser la hora de finalización del periodo de medición.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PhotovoltaicMeasurement:    
  description: 'The Data Model is intended to measure the continuous power transferred by the photo-voltaic panel to an Inverter Device.'    
  properties:    
    activePower:    
      description: 'Active Power,where phi is the phase shift of the current compared to the voltage. The unit code (text) is given using the UN/CEFACT_Common_Codes (max 3 characters). For instance, For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    current:    
      description: 'Electrical intensity of the current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
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
    dateEnergyMeteringStarted:    
      description: 'The starting date for metering energy in an ISO8601 UTC format'    
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
    dateObservedFrom:    
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateObservedTo:    
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the ''dateObserved'' attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nominalPeakPowerGeneration:    
      description: 'nominalPeakPowerGeneration is a number. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KWT** represents Kilowatt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilowatt    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *photovoltaicmeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    reactivePower:    
      description: 'Reactive Power used by circuits. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **K5** represents kilovolt-ampere-reactive'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        model: 'Reference to a [Photovoltaic Device](https://github.com/smart-data-models/dataModel.Energy/PhotovoltaicDevice/doc/spec.md) which captured this observation, if the entity is used https://schema.org/URL'    
        type: Relationship    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature recorded at the time of Observation compared to the  nominal reference temperature of the device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'degrees celsius'    
    type:    
      description: 'NGSI Entity type. It has to be PhotovoltaicMeasurement'    
      enum:    
        - PhotovoltaicMeasurement    
      type: string    
      x-ngsi:    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/PhotovoltaicMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/PhotovoltaicMeasurement/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### PhotovoltaicMeasurement NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un PhotovoltaicMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### PhotovoltaicMeasurement NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un PhotovoltaicMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### PhotovoltaicMeasurement NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un PhotovoltaicMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
    "type": "PhotovoltaicMeasurement",  
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
    "dataProvider": {  
        "type": "Property",  
        "value": "https://imredd.fr/en/home/"  
    },  
    "dateEnergyMeteringStarted": {  
        "type": "Property",  
        "value": "2019-09-04T15:29:17.999Z"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2019-09-05T16:00:00.999Z"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Photovoltaic data provided by the data logger ABB"  
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
    "name": {  
        "type": "Property",  
        "value": "Photovoltaic station IMREDD"  
    },  
    "nominalPeakPowerGeneration": {  
        "type": "Property",  
        "value": 179  
    },  
    "refPhotovoltaicDevice": {  
        "type": "Relationship",  
        "Object": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://us.sunpower.com/products/solar-panels"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 23.4  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/common-schema.json",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PhotovoltaicMeasurement NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un PhotovoltaicMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "PhotovoltaicMeasurement:ENERGY-IMREDD-PV-0001",  
    "type": "PhotovoltaicMeasurement",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "61-63 Avenue Simone Veil"  
    },  
    "areaServed": "Nice",  
    "dataProvider": "https://imredd.fr/en/home/",  
    "dateEnergyMeteringStarted": "2019-09-04T15:29:17.999Z",  
    "dateObserved": "2019-09-05T16:00:00.999Z",  
    "description": "Photovoltaic data provided by the data logger ABB",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "name": "Photovoltaic station IMREDD",  
    "nominalPeakPowerGeneration": 179,  
    "refPhotovoltaicDevice": "urn:ngsi-ld:PhotovoltaicDevice:PV-T2-R-012",  
    "seeAlso": "https://us.sunpower.com/products/solar-panels",  
    "temperature": 23.4,  
    "@context": [  
        "https://smart-data-models.github.io/data-models/common-schema.json",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

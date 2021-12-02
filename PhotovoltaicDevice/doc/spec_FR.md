Entité : PhotovoltaicDevice  
===========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le modèle de données est destiné à décrire les caractéristiques mécaniques, électriques et thermiques des panneaux photo-voltaïques selon *STC - Standard Test Condition* et *NOCT - Normal Operating Cell Temperature*. *Remarque* : Ce modèle de données peut être utilisé directement comme entité principale pour décrire le `Photovoltaic Device` ou comme sous-entité du modèle de données `DEVICE` en utilisant une référence par l'attribut `refDevice`. Les mesures effectuées pour STC et NOCT sont `Pmax` (Puissance nominale maximale), `Umpp` (Tension de fonctionnement optimale), `Impp` (Courant de fonctionnement optimal), `Uoc` (Tension en circuit ouvert), `Isc` (Courant en court-circuit). *Informations supplémentaires sur le modèle de données : Ce modèle de données peut être utilisé directement comme entité principale pour décrire le dispositif [PHOTOVOLTAÏQUE] ou comme sous-entité du modèle de données [DEVICE] en utilisant une référence par l'attribut `refDevice`.  

## Liste des propriétés  

- `MaxPressureLoad`: a charge mécanique maximale de pression (cisaillement, élasticité, compression) sur un panneau. Le format est structuré par une sous-propriété de 3 éléments. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **PAL** représente Pascal  - `MaximumSystemVoltage`: Tension maximale du système autorisée pour le **module**. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **VLT** représente Volt  - `NominalPower`: Puissance nominale pour le **panneau**. Il s'agit de la même valeur que les éléments [Pmax] de l'attribut [moduleSTC]. Le code d'unité (texte) est donné à l'aide des [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **WTT** représente le Watt  - `PanelNbModules`: Nombre de "modules" par "panneau".  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `application`: Application cible concernant le type de panneau solaire (dans notre cas `électrique`). Une valeur unique. https://schema.org/Text. Enum : 'électrique, thermique, autre'.  - `applicationClass`: Évaluation des risques potentiels associés au module. Une valeur unique. Enum : 'A, B, C'.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `areaWeight`: Surface Poids mesuré en Kg/m². Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **28** représente le kilogramme par mètre carré.  - `brandName`: Nom de la marque de l'article  - `cellDimension`: Dimension externe d'une cellule. Le format est structuré par une sous-propriété de 3 éléments. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MMT** représente le millimètre.  - `cellOperatingTemperature`: Il s'agit de la plage de température nominale de fonctionnement des cellules dans lesquelles il collecte l'énergie solaire. Le format est structuré par une sous-propriété de 2 éléments. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **CEL** représente un degré Celsius.  - `cellType`: Type de cellules utilisées pour construire l'unité photo-voltaïque. 2 types de technologies *`Cristalline`* ou *`Couches minces`*. Une valeur unique. Enum : 'amorphousSilicon, CfTe, CIS, monocristallin, polycristallin, autre'.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastReported`: Un horodatage qui indique la dernière fois que le dispositif a transmis des données avec succès. Date et heure dans un format ISO8601 UTC.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `documentation`: Documentation technique (installation / maintenance / utilisation)  - `fireClass`: Évaluation au feu (IEC 61730). Une valeur unique. Enum : 'A, B, C'.  - `id`: Identifiant unique de l'entité  - `installationCondition`: Condition et possibilité d'utilisation dans les environnements suivants. Une combinaison. Enum : 'désert, poussière, chaleur extrême, froid extrême, climat extrême, humidité extrême, marin, aucun, autre, salin, sable, sismique'.  - `installationMode`: Positionnement de l'appareil par rapport à un système de référence au sol. Une valeur unique. Enum : 'ground, other, pole, roofing, wall' (sol, autre, poteau, toiture, mur)  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `manufacturerName`: Fabricant Nom de l'article  - `modelName`: Nom du modèle de l'article  - `moduleDimension`:  Dimension extérieure d'un module. Un module peut être un assemblage de 1 à n cellules. Le format est structuré par une sous-propriété de 3 éléments. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MMT** représente le millimètre.  - `moduleNOCT`: Mesures de la température normale de fonctionnement de la cellule. Le format est structuré par une sous-propriété de 5 éléments. Pmax en Watt. Umpp en Volt. Impp en Ampère. Uoc en Volt. Isc en Ampère  - `moduleNbCells`: Nombre de "cellules" par "module".  - `moduleSTC`: Mesures standard des conditions d'essai. Le format est structuré par une sous-propriété de 5 éléments. Pmax en Watt. Umpp en Volt. Impp en Ampère. Uoc en Volt. Isc en Ampère  - `moduleYieldRate`: Positionnement de l'appareil par rapport à un système de référence au sol. Une valeur unique  - `nTCClass`: Le coefficient de résistance à la température négative - *NTC*, décrit le changement relatif d'une propriété physique qui est associé à un changement donné de la température négative. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **P1** représente le Pourcentage  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pTCClass`:  Le coefficient de température positive de la résistance - *PTC*, décrit le changement relatif d'une propriété physique qui est associé à un changement donné de température positive. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **P1** représente le pourcentage.  - `panelDimension`: Dimension extérieure d'un panneau. Un panneau solaire peut être un assemblage de 1 à n modules, eux-mêmes composés de plusieurs cellules qui captent la chaleur des rayons du soleil. Le format est structuré par une sous-propriété de 3 éléments. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MMT** représente le millimètre.  - `panelLifetime`: Durée de vie moyenne d'un panneau. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **ANN** représente l'année  - `panelOperatingTemperature`: Plage de températures de fonctionnement ambiantes. Il s'agit de la résistance minimale et maximale au froid et à la chaleur pour l'utilisation du panneau. Le format est structuré par une sous-propriété de 2 éléments. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **CEL** représente le degré Celsius.  - `panelWeight`: Poids d'un panneau (la référence utilisée est parfois Kg / m²). Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **KGM** représente le kilogramme.  - `panelYieldCurve`: Option 1. Courbe de rendement de la production d'énergie du panneau à partir de sa [puissance nominale] à [T0] et tout au long de sa [durée de vie du panneau]. Les mesures fournies dans la liste sont une séquence de la capacité de production d'énergie représentée en pourcentage à partir de 5 ans avec un "pas" de 5 ans selon les informations fournies par le fabricant. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **P1** représente le pourcentage.  - `performanceLowIrradiance`: Rendement relatif moyen par rapport à la performance à faible irradiation. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **P1** représente le Pourcentage  - `possibilityOfUse`: Possibilité d'utilisation. Une valeur unique. Enum : 'mixte, mobile, autre, stationnaire'.  - `protectionIP`: IP "Ingress Protection" pour la boîte de jonction. Il s'agit du niveau qui classe et évalue le degré de protection offert par les boîtiers mécaniques et les enveloppes électriques contre les intrusions, la poussière, les contacts accidentels et l'eau, conformément à la norme de la Commission électrotechnique internationale (EN 60-529). Premier chiffre : Protection contre les particules solides (chiffre unique : 0-6 ou 'X'). Deuxième chiffre : Protection contre la pénétration de liquides (chiffre unique : 0-9 ou 'X'). Troisième chiffre : Troisième chiffre : protection personnelle contre l'accès aux parties dangereuses (lettre supplémentaire facultative). Quatrième chiffre : Autres protections (lettre supplémentaire facultative)  - `refDevice`: Référence à l'entité principale [dispositif] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) si elle est utilisée comme deuxième lien.  - `refPointOfInterest`: Référence à un [PointOfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) lié au Référentiel.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `serialNumber`: Liste des numéros de série des dispositifs photo-voltaïques fournis par le fabricant et assemblés en mode de fonctionnement sur un seul site.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `temperatureCoefficient`:  Coefficient d'influence de la température sur le panneau. Le format est structuré par une sous-propriété de 3 éléments. Pmax en Watt. Uoc en Volt. Isc en Ampère  - `type`: Type d'entité NGSI. Il doit être PhotovoltaicDevice.  - `typeOfUse`: Utilisation acceptée quant à son positionnement dans un environnement intérieur / extérieur. Une valeur unique. Enum : 'indoor, outdoor, mixed, other' (intérieur, extérieur, mixte, autre)    
Propriétés requises  
- `dateLastReported`  - `id`  - `location`  - `type`    
Les mesures effectuées pour STC et NOCT sont - [Pmax] Puissance nominale maximale mesurée en **WTT** représente Watt. - Umpp] Tension de fonctionnement optimale mesurée en **VLT** représente le Volt. - Impp] Courant de fonctionnement optimal mesuré en **AMP** représente l'Ampère. - Uoc] Tension de circuit ouvert mesurée en **VLT** représente le Volt. - Isc] Courant de court-circuit mesuré en **AMP** représente Ampère.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
        model: https://schema.org/Number.    
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
        model: https://schema.org/Text.    
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
        model: https://schema.org/StructuredValue.    
        type: Property    
    moduleNbCells:    
      description: 'Number of ''cells'' per ''module'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
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
        model: https://schema.org/StructuredValue.    
        type: Property    
    moduleYieldRate:    
      description: 'Positioning of the device in relation to a ground reference system. A unique value'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    nTCClass:    
      description: 'The Negative Temperature Coefficient of resistance - *NTC*, describes the relative change of a physical property that is associated with a given change in negative temperature. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
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
        model: https://schema.org/StructuredValue.    
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
        model: https://schema.org/Number.    
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
        model: https://schema.org/Text.    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/PhotovoltaicDevice/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### PhotovoltaicDevice NGSI-v2 key-values Exemple  
Voici un exemple d'un PhotovoltaicDevice au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### PhotovoltaicDevice NGSI-v2 normalisé Exemple  
Voici un exemple d'un PhotovoltaicDevice au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### PhotovoltaicDevice NGSI-LD key-values Exemple  
Voici un exemple d'un PhotovoltaicDevice au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "value": "AirPort \u2013 global Observation"  
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
    "value": [  
      "electric"  
    ]  
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
    "value": [  
      "C"  
    ]  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Dispositif photovoltaïque normalisé NGSI-LD Exemple  
Voici un exemple d'un PhotovoltaicDevice au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:PhotovoltaicDevice:PhotovoltaicDevice:MNCA-PV-T2-R-012",  
  "type": "PhotovoltaicDevice",  
  "name": "DEVICE-PV-T2-R-012",  
  "alternateName": "AirPort \u2013 global Observation",  
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
  "application": [  
    "electric"  
  ],  
  "cellType": [  
    "polycrystalline"  
  ],  
  "installationMode": [  
    "roofing"  
  ],  
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
  "applicationClass": [  
    "A"  
  ],  
  "fireClass": [  
    "C"  
  ],  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude
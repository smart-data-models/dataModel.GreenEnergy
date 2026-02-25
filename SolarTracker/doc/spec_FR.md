<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SolarTracker  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Description du modèle de données SolarTracker **  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modes</sub></sup>  
- `address[object]` : L'adresse postale  . Modèle : [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]` : Le pays. Par exemple, l'Espagne  . Modèle : [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]` : La localité dans laquelle se trouve l'adresse de la rue, et qui se trouve dans la région  . Modèle : [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]` : La région dans laquelle se trouve la localité, et qui se trouve dans le pays  . Modèle : [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]` : Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local    
	- `postOfficeBoxNumber[string]` : Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578  . Modèle : [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]` : Le code postal. Par exemple, 24004  . Modèle : [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]` : L'adresse de la rue  . Modèle : [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]` : Numéro identifiant une propriété spécifique sur une rue publique    
- `alternateName[string]` : Un nom alternatif pour cet élément  - `altitude[number]` : L'altitude du site d'installation par rapport au niveau moyen de la mer. Cette valeur est utilisée par l'algorithme solaire pour affiner le calcul de la position du soleil et de la réfraction atmosphérique  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]` : La zone géographique où un service ou un élément est fourni  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `backtracking[string]` : Enum:'on','off'. Indique si le suiveur solaire est en mode de suivi inverse pour prévenir l'ombrage entre les rangées, en déviant de la position d'angle solaire optimale  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]` : Représente le niveau de charge actuel de la batterie, exprimé en pourcentage de sa capacité totale (0 à 100)  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `boardDirection[string]` : Enum:'-1','1'. Spécifie l'orientation physique de la carte de contrôle en fonction de la position du bouton d'arrêt d'urgence (orienté vers l'est = 1 ; orienté vers l'ouest = -1)  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `currentAngle[number]` : La position angulaire actuelle du panneau. Une valeur de 0 indique que le panneau est horizontal (faisant face directement vers le haut). Les valeurs minimales représentent une orientation vers l'est, tandis que les valeurs maximales représentent une orientation vers l'ouest  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `currentPowerConsumption[number]` : La puissance électrique demandée en temps réel, mesurée en watts  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]` : Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée  - `dateCreated[date-time]` : Horodatage de la création de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateModified[date-time]` : Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateUpdate[date-time]` : La date à laquelle la configuration a été mise à jour  . Modèle : [http://schema.org/DateTime](http://schema.org/DateTime)- `description[string]` : Une description de cet élément  - `deviceCategory[string]` : Enum:'PCU','FCU','SCU'. Spécifie la classification de l'appareil dans le système  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]` : Enum:'Online','Offline'. Indique l'état de connectivité opérationnel actuel de l'appareil  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `id[*]` : Identifiant unique de l'entité  - `ipAddress[array]` : Liste des adresses IP de l'appareil. Il peut s'agir d'une liste de valeurs séparées par des virgules si l'appareil a plus d'une adresse IP  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `location[*]` : Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un multi-point, d'un multi-ligne ou d'un multi-polygone  - `maxAngleLimit[number]` : La position angulaire maximale autorisée vers l'ouest. Cette limite logicielle agit comme un plafond dur ; le panneau ne tournera pas au-delà de cette valeur, même si l'angle cible calculé est supérieur  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `maxPowerRecorded[number]` : Le niveau le plus élevé de consommation de puissance électrique active enregistré lors du dernier mouvement, mesuré en watts  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `maxPowerThreshold[number]` : La limite de sécurité pour la consommation de puissance pendant le fonctionnement du moteur. Si la puissance électrique dépasse ce seuil, le mouvement du panneau est immédiatement interrompu pour prévenir les dommages mécaniques ou la surcharge du moteur  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `minAngleLimit[number]` : La position angulaire minimale autorisée vers l'est. Ce paramètre définit une limite opérationnelle obligatoire ; le panneau ne tournera pas plus à l'est que cette valeur, quelle que soit la position cible demandée  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `minPowerRecorded[number]` : Le niveau le plus bas de consommation de puissance électrique active enregistré lors du dernier mouvement, mesuré en watts  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `motorDirection[string]` : Enum:'-1','1'. Définit l'orientation physique de montage du moteur, qui détermine la polarité de la rotation (orienté vers l'est = 1 ; orienté vers l'ouest = -1)  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `movementInterval[string]` : Enum:'5','10','15'. Définit la fréquence temporelle à laquelle le panneau ajuste sa position. La valeur doit être l'une des intervalles prédéfinis : 5, 10 ou 15 minutes  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `name[string]` : Le nom de cet élément  - `operatingMode[string]` : Enum:'automatique','manuel','safesnow','safesnowsensor','safewind','safewindsensor','maintenance'. Définit l'état fonctionnel actuel du panneau. Ce mode dicte si le suiveur suit l'algorithme solaire ou répond à des événements/sécurité externes  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `owner[array]` : Une liste contenant une séquence de caractères codés en JSON référençant les identifiants uniques des propriétaires  - `panelLength[number]` : La dimension du panneau mesurée le long de l'axe perpendiculaire à l'axe de rotation. Cette valeur est critique pour calculer l'ombre projetée par le panneau et déterminer le mouvement de suivi inverse approprié  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `restingAngle[number]` : La position angulaire spécifique que le panneau adopte pendant la nuit ou lorsque le soleil est en dessous de l'horizon. Cette position est utilisée pour stationner le suiveur jusqu'au prochain lever du soleil  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]` : liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `snowSafetyAngle[number]` : La position angulaire spécifique que le panneau doit adopter pendant un événement de neige. Cet angle est conçu pour faciliter l'élimination de la neige et prévenir les charges structurelles excessives sur le suiveur  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `source[string]` : Une séquence de caractères indiquant la source d'origine des données de l'entité sous la forme d'une URL. Il est recommandé d'être le nom de domaine pleinement qualifié du fournisseur source ou l'URL de l'objet source  - `targetAngle[number]` : Le point de référence angulaire cible pour l'orientation du panneau. Une valeur de 0 indique que le panneau est horizontal (faisant face directement vers le haut). Les valeurs minimales représentent une orientation vers l'est, tandis que les valeurs maximales représentent une orientation vers l'ouest  . Modèle : [https://schema.org/Number](https://schema.org/Number)- `type[string]` : Il doit être égal à `SolarTracker`  - `windSafetyAngle[number]` : Le point de référence de sécurité pour l'angle que le panneau adopte lorsque les vitesses du vent dépassent le seuil opérationnel. Cette position minimise l'effet de voile et réduit les contraintes structurelles causées par la poussée ou la pression du vent  . Modèle : [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `deviceCategory`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Description du modèle de données des propriétés  
Classées par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>détails yaml complets</strong></summary>    
```yaml  
SolarTracker:    
  description: 'Description of the data model SolarTracker '    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    altitude:    
      description: The elevation of the installation site above mean sea level. This value is used by the solar algorithm to refine the calculation of the sun's position and atmospheric refraction    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter (MTR)    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    backtracking:    
      description: Enum:'on','off'. Indicates whether the solar tracker is in backtracking mode to prevent row-to-row shadowing, deviating from the optimal sun-angle position    
      enum:    
        - 'on'    
        - 'off'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryLevel:    
      description: Represents the current charge level of the battery, expressed as a percentage of its total capacity (0 to 100)    
      maximum: 100    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: C62    
    boardDirection:    
      description: Enum:'-1','1'. Specifies the physical orientation of the control board based on the position of the emergency stop button (Eastward-facing = 1; Westward-facing = -1)    
      enum:    
        - '1'    
        - '-1'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    currentAngle:    
      description: The current angular position of the panel. A value of 0 indicates the panel is horizontal (facing directly upward). Minimum values represent an Eastward orientation, while maximum values represent a Westward orientation    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    currentPowerConsumption:    
      description: The real-time electrical power demand measured in Watts    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateUpdate:    
      description: The date when the configuration was updated    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceCategory:    
      description: Enum:'PCU','FCU','SCU'. Specifies the classification of the device within the system    
      enum:    
        - PCU    
        - FCU    
        - SCU    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceState:    
      description: Enum:'Online','Offline'. Indicates the current operational connectivity status of the device    
      enum:    
        - Online    
        - Offline    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    ipAddress:    
      description: List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address    
      items:    
        anyOf:    
          - description: If the IP address meets the requirements of V4 IP address    
            format: ipv4    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          - description: If the IP address meets the requirements of V6 IP address    
            format: ipv6    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
        description: Every item in the list of IP address of the device    
        type: string    
        x-ngsi:    
          model: https://schema.org/Text    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    maxAngleLimit:    
      description: The maximum allowable angular position towards the West. This software limit acts as a hard ceiling; the panel will not rotate beyond this value even if the calculated target angle is greater    
      maximum: 90    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    maxPowerRecorded:    
      description: The highest level of active electrical power consumption recorded during the last movement, measured in Watts    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    maxPowerThreshold:    
      description: The safety limit for power consumption during motor operation. If the electrical power exceeds this threshold, the panel movement is immediately interrupted to prevent mechanical damage or motor overload    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    minAngleLimit:    
      description: The minimum allowable angular position towards the East. This parameter defines a mandatory operational boundary; the panel will not rotate further East than this value, regardless of the requested target position    
      maximum: 0    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    minPowerRecorded:    
      description: The lowest level of active electrical power consumption recorded during the last movement, measured in Watts    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt (WTT)    
    motorDirection:    
      description: Enum:'-1','1'. Defines the physical mounting orientation of the motor, which determines the polarity of the rotation (Eastward-facing = 1; Westward-facing = -1)    
      enum:    
        - '1'    
        - '-1'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    movementInterval:    
      description: 'Enum:''5'',''10'',''15''. Defines the time frequency at which the panel adjusts its position. The value must be one of the predefined intervals: 5, 10, or 15 minutes'    
      enum:    
        - '5'    
        - '10'    
        - '15'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operatingMode:    
      description: Enum:'automatic','manual','safesnow','safesnowsensor','safewind','safewindsensor','maintenance'. Defines the current functional state of the panel. This mode dictates whether the tracker follows the solar algorithm or responds to external overrides/safety events    
      enum:    
        - automatic    
        - manual    
        - safesnow    
        - safesnowsensor    
        - safewind    
        - safewindsensor    
        - maintenance    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    panelLength:    
      description: The dimension of the panel measured along the axis perpendicular to the axis of rotation. This value is critical for calculating the shadow cast by the panel and determining the appropriate backtracking movement    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meter (MTR)    
    restingAngle:    
      description: The specific angular position the panel assumes during the night or when the sun is below the horizon. This position is used to park the tracker until the next sunrise    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    snowSafetyAngle:    
      description: The specific angular position the panel must adopt during a snow event. This angle is designed to facilitate snow shedding and prevent excessive structural loading on the tracker    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    targetAngle:    
      description: The target angular setpoint for the panel's orientation. A value of 0 indicates the panel is horizontal (facing directly upward). Minimum values represent an Eastward orientation, while maximum values represent a Westward orientation    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
    type:    
      description: It must be equal to `SolarTracker`    
      enum:    
        - SolarTracker    
      type: string    
      x-ngsi:    
        type: Property    
    windSafetyAngle:    
      description: The safety setpoint angle the panel assumes when wind speeds exceed the operational threshold. This position minimize the sail effect and reduce structural stress caused by wind uplift or pressure    
      maximum: 90    
      minimum: -90    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree Angle (DD)    
  required:    
    - id    
    - type    
    - deviceCategory    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.GreenEnergy/blob/master/SolarTracker/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.SmartManufactoring/DigitalTwin/SolarTracker/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles    
#### Exemple de clés-valeurs SolarTracker NGSI-v2    
Voici un exemple de SolarTracker au format JSON en tant que clés-valeurs. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1",  
  "type": "SolarTracker",  
  "deviceCategory": "PCU",  
  "ipAddress": ["10.13.13.3"],  
  "location": {  
    "type": "Point",  
    "coordinates": [16.563426, 40.850953]  
  }  
}  
```  
</details>  
#### Exemple de SolarTracker NGSI-v2 normalisé    
Voici un exemple de SolarTracker au format JSON en tant que normalisé. Cela est compatible avec NGSI-v2 lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1-FCU1-SCU1",  
  "type": "SolarTracker",  
  "dateUpdate": {  
    "type": "DateTime",  
    "value": "2026-01-29T00:00:00.000"  
  },  
  "altitude": {  
    "type": "Number",  
    "value": 436.6,  
    "unitCode": "MTR"  
  },  
  "currentPowerConsumption": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "maxPowerRecorded": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "minPowerRecorded": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "backtracking": {  
    "type": "Text",  
    "value": "on"  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": 85.34,  
    "unitCode": "C62"  
  },  
  "currentAngle": {  
    "type": "Number",  
    "value": -31.3,  
    "unitCode": "DD"  
  },  
  "deviceCategory": {  
    "type": "Text",  
    "value": "SCU"  
  },  
  "deviceState": {  
    "type": "Text",  
    "value": "Online"  
  },  
  "motorDirection": {  
    "type": "Text",  
    "value": "-1"  
  },  
  "boardDirection": {  
    "type": "Text",  
    "value": "1"  
  },  
  "targetAngle": {  
    "type": "Number",  
    "value": -29.3,  
    "unitCode": "DD"  
  },  
  "movementInterval": {  
    "type": "Text",  
    "value": "5"  
  },  
  "panelLength": {  
    "type": "Number",  
    "value": 0,  
    "unitCode": "MTR"  
  },  
  "maxPowerThreshold": {  
    "type": "Number",  
    "value": 10000,  
    "unitCode": "WTT"  
  },  
  "maxAngleLimit": {  
    "type": "Number",  
    "value": 55,  
    "unitCode": "DD"  
  },  
  "minAngleLimit": {  
    "type": "Number",  
    "value": -55,  
    "unitCode": "DD"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": ["urn:ngsi-ld:Device:PCU1-FCU1"]  
  },  
  "snowSafetyAngle": {  
    "type": "Number",  
    "value": 40,  
    "unitCode": "DD"  
  },  
  "windSafetyAngle": {  
    "type": "Number",  
    "value": 5,  
    "unitCode": "DD"  
  },  
  "restingAngle": {  
    "type": "Number",  
    "value": -5,  
    "unitCode": "DD"  
  },  
  "operatingMode": {  
    "type": "Text",  
    "value": "automatic"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [16.563436, 40.850453]  
    }  
  }  
}  
```  
</details>  
#### Exemple de clés-valeurs SolarTracker NGSI-LD    
Voici un exemple de SolarTracker au format JSON-LD en tant que clés-valeurs. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1-FCU1",  
  "type": "SolarTracker",  
  "backtracking": "off",  
  "deviceCategory": "FCU",  
  "owner": ["urn:ngsi-ld:Device:PCU1"],  
  "location": {  
    "type": "Point",  
    "coordinates": [16.563436, 40.850453]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Exemple de SolarTracker NGSI-LD normalisé    
Voici un exemple de SolarTracker au format JSON-LD en tant que normalisé. Cela est compatible avec NGSI-LD lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarTracker:PCU1-FCU1-SCU1",  
  "type": "SolarTracker",  
  "dateUpdate": {  
    "type": "Property",  
    "value": {  
      "@type":"DateTime",  
      "@value":"2026-01-29T00:00:00.000Z"  
    }  
  },  
  "altitude": {  
    "type": "Property",  
    "value": 436.6,  
    "unitCode": "MTR"  
  },  
  "currentPowerConsumption": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "maxPowerRecorded": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "minPowerRecorded": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "WTT"  
  },  
  "backtracking": {  
    "type": "Property",  
    "value": "on"  
  },  
  "batteryLevel": {  
    "type": "Property",  
    "value": 85.34,  
    "unitCode": "C62"  
  },  
  "currentAngle": {  
    "type": "Property",  
    "value": -31.3,  
    "unitCode": "DD"  
  },  
  "deviceCategory": {  
    "type": "Property",  
    "value": "SCU"  
  },  
  "deviceState": {  
    "type": "Property",  
    "value": "Online"  
  },  
  "motorDirection": {  
    "type": "Property",  
    "value": "-1"  
  },  
  "boardDirection": {  
    "type": "Property",  
    "value": "1"  
  },  
  "targetAngle": {  
    "type": "Property",  
    "value": -29.3,  
    "unitCode": "DD"  
  },  
  "movementInterval": {  
    "type": "Property",  
    "value": "5"  
  },  
  "panelLength": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "MTR"  
  },  
  "maxPowerThreshold": {  
    "type": "Property",  
    "value": 10000,  
    "unitCode": "WTT"  
  },  
  "maxAngleLimit": {  
    "type": "Property",  
    "value": 55,  
    "unitCode": "DD"  
  },  
  "minAngleLimit": {  
    "type": "Property",  
    "value": -55,  
    "unitCode": "DD"  
  },  
  "owner": {  
    "type": "Relationship",  
    "object": ["urn:ngsi-ld:Device:PCU1-FCU1"]  
  },  
  "snowSafetyAngle": {  
    "type": "Property",  
    "value": 40,  
    "unitCode": "DD"  
  },  
  "windSafetyAngle": {  
    "type": "Property",  
    "value": 5,  
    "unitCode": "DD"  
  },  
  "restingAngle": {  
    "type": "Property",  
    "value": -5,  
    "unitCode": "DD"  
  },  
  "operatingMode": {  
    "type": "Property",  
    "value": "automatic"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [16.563436, 40.850453]  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.GreenEnergy/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de gérer les unités de grandeur  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

Entità: PhotovoltaicDevice  
==========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.GreenEnergy/blob/master/PhotovoltaicDevice/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Il modello di dati è destinato a descrivere le caratteristiche meccaniche, elettriche e termiche dei pannelli fotovoltaici secondo *STC - Standard Test Condition* e *NOCT - Normal Operating Cell Temperature*. *Nota* : Questo modello di dati può essere utilizzato direttamente come entità principale per descrivere il `dispositivo fotovoltaico` o come sotto-entità del modello di dati `DEVICE` utilizzando un riferimento tramite l'attributo `refDevice`. Le misure eseguite per STC e NOCT sono `Pmax` (potenza nominale massima), `Umpp` (tensione operativa ottimale), `Impp` (corrente operativa ottimale), `Uoc` (tensione a circuito aperto), `Isc` (corrente di corto circuito). *Informazioni aggiuntive sul modello di dati:* Questo modello di dati può essere usato direttamente come entità principale per descrivere il dispositivo [PHOTOVOLTAIC] o come sotto-entità del modello di dati [DEVICE] usando un riferimento tramite l'attributo `refDevice`.  

## Elenco delle proprietà  

- `MaxPressureLoad`: aximum mechanics Pressure (shear, elasticity, compression) load on a Panel. Il formato è strutturato da una sottoproprietà di 3 elementi. Il codice dell'unità (testo) è dato utilizzando i [codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **PAL** rappresenta Pascal  - `MaximumSystemVoltage`: Tensione massima di sistema consentita per il **modulo**. Il codice dell'unità (testo) è dato usando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **VLT** rappresenta Volt  - `NominalPower`: Potenza nominale per il **pannello**. Questo è lo stesso valore degli elementi [Pmax] per l'attributo [moduleSTC]. Il codice dell'unità (testo) è dato usando i [codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **WTT** rappresenta i Watt  - `PanelNbModules`: Numero di "moduli" per "pannello  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `application`: Applicazione target riguardante il tipo di pannello solare (nel nostro caso `elettrico`). Un valore unico. https://schema.org/Text. Enum:'elettrico, termico, altro'.  - `applicationClass`: Valutazione dei potenziali pericoli associati al modulo. Un valore unico. Enum:'A, B, C'.  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `areaWeight`: Area Peso misurato in Kg/m². Il codice dell'unità (testo) è dato usando il [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **28** rappresenta il chilogrammo per metro quadrato  - `brandName`: Nome della marca dell'articolo  - `cellDimension`: Dimensione esterna di una cella. Il formato è strutturato da una sotto-proprietà di 3 elementi. Il codice dell'unità (testo) è dato utilizzando i [codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **MMT** rappresenta il millimetro.  - `cellOperatingTemperature`: Questo è l'intervallo di temperatura nominale di funzionamento delle celle in cui raccoglie l'energia solare. Il formato è strutturato da una sottoproprietà di 2 elementi. Il codice dell'unità (testo) è dato utilizzando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **CEL** rappresenta i gradi Celsius  - `cellType`: Tipo di celle utilizzate per costruire l'unità fotovoltaica. 2 tipi di tecnologie *`Cristalline`* o *`Strati sottili`*. Un valore unico. Enum:'amorphousSilicon, CfTe, CIS, monocristallino, policristallino, altro'.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateLastReported`: Un timestamp che denota l'ultima volta in cui il dispositivo ha riportato con successo dei dati. Data e ora in formato ISO8601 UTC.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `documentation`: Documentazione tecnica (installazione / manutenzione / usato)  - `fireClass`: Valutazione al fuoco (IEC 61730). Un valore unico. Enum:'A, B, C'.  - `id`: Identificatore unico dell'entità  - `installationCondition`: Condizione e possibilità di utilizzo nei seguenti ambienti. Una combinazione. Enum:'deserto, polvere, caldo estremo, freddo estremo, clima estremo, umidità estrema, marino, nessuno, altro, salino, sabbia, sismico'  - `installationMode`: Posizionamento del dispositivo rispetto a un sistema di riferimento a terra. Un valore unico. Enum:'terra, altro, palo, tetto, muro'.  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `manufacturerName`: Nome del produttore dell'articolo  - `modelName`: Nome del modello dell'articolo  - `moduleDimension`:  Dimensione esterna di un modulo. Un modulo può essere un insieme da 1 a n celle. Il formato è strutturato da una sotto-proprietà di 3 elementi. Il codice dell'unità (testo) è dato utilizzando i [codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **MMT** rappresenta il millimetro  - `moduleNOCT`: Misure della temperatura normale di funzionamento della cella. Il formato è strutturato da una sotto-proprietà di 5 elementi. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere  - `moduleNbCells`: Numero di 'celle' per 'modulo  - `moduleSTC`: Misure di condizioni di prova standard. Il formato è strutturato da una sottoproprietà di 5 elementi. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere  - `moduleYieldRate`: Posizionamento del dispositivo rispetto a un sistema di riferimento a terra. Un valore unico  - `nTCClass`: Il coefficiente di resistenza alla temperatura negativa - *NTC*, descrive il cambiamento relativo di una proprietà fisica che è associato a un dato cambiamento di temperatura negativo. Il codice dell'unità (testo) è dato usando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **P1** rappresenta Percentuale  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `pTCClass`:  Il coefficiente di resistenza alla temperatura positiva - *PTC*, descrive il cambiamento relativo di una proprietà fisica che è associato a un dato cambiamento di temperatura positiva. Il codice dell'unità (testo) è dato usando il [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **P1** rappresenta la percentuale.  - `panelDimension`: Dimensione esterna di un pannello. Un pannello solare può essere un insieme da 1 a n moduli, che a loro volta sono composti da diverse celle che raccolgono il calore dei raggi solari. Il formato è strutturato da una sotto-proprietà di 3 elementi. Il codice dell'unità (testo) è dato utilizzando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **MMT** rappresenta il millimetro.  - `panelLifetime`: Durata media di un pannello. Il codice dell'unità (testo) è dato usando i [codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **ANN** rappresenta l'anno  - `panelOperatingTemperature`: Intervallo di temperatura operativa ambientale. Si tratta della resistenza minima e massima al freddo e al caldo per l'utilizzo del pannello. Il formato è strutturato da una sottoproprietà di 2 elementi. Il codice dell'unità (testo) è dato utilizzando i [Codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **CEL** rappresenta il grado Celsius  - `panelWeight`: Peso di un pannello (a volte il riferimento utilizzato è Kg / m²). Il codice dell'unità (testo) è dato usando i [codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **KGM** rappresenta il chilogrammo  - `panelYieldCurve`: Opzione 1. Curva di rendimento della produzione di energia del pannello dalla sua [NominalPower] a [T0] e lungo la sua [panelLifetime]. Le misure fornite nell'elenco sono una sequenza di capacità di produzione di energia rappresentata in percentuale a partire da 5 anni con un 'Passo' di 5 anni secondo le informazioni fornite dal produttore. Il codice dell'unità (testo) è dato utilizzando i [Codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **P1** rappresenta la percentuale.  - `performanceLowIrradiance`: Rendimento medio relativo al rendimento a basso irraggiamento. Il codice dell'unità (testo) è dato usando il [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Per esempio, **P1** rappresenta Percentuale  - `possibilityOfUse`: Possibilità di utilizzo. Un valore unico. Enum:'misto, mobile, altro, fisso'.  - `protectionIP`: IP 'Ingress Protection' per la Junction Box. Questo è il livello che classifica e valuta il grado di protezione fornito dagli involucri meccanici e dagli involucri elettrici contro l'intrusione, la polvere, il contatto accidentale e l'acqua secondo lo standard della Commissione Elettrotecnica Internazionale (EN 60-529). Prima cifra: Protezione dalle particelle solide (numero unico: 0-6 o "X"). Seconda cifra: Protezione dall'ingresso di liquidi (numero singolo: 0-9 o 'X' ).Terza cifra: Protezione personale contro l'accesso a parti pericolose (lettera aggiuntiva opzionale). Quarta cifra: Altre protezioni (lettera aggiuntiva opzionale)  - `refDevice`: Riferimento all'entità principale [Dispositivo](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) se usato come secondo collegamento  - `refPointOfInterest`: Riferimento a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) collegato al Repository.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `serialNumber`: Elenco dei numeri di serie dei dispositivi fotovoltaici forniti dal fabbricante e montati in modalità di funzionamento su un'unica postazione  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `temperatureCoefficient`:  Coefficiente di influenza della temperatura sul pannello. Il formato è strutturato da una sotto-proprietà di 3 elementi. Pmax in Watt. Uoc in Volt. Isc in Ampere  - `type`: Tipo di entità NGSI. Deve essere PhotovoltaicDevice  - `typeOfUse`: Uso accettato per quanto riguarda il suo posizionamento in un ambiente interno/esterno. Un valore unico. Enum:'interno, esterno, misto, altro'.    
Proprietà richieste  
- `dateLastReported`  - `id`  - `location`  - `type`    
Le misure eseguite per STC e NOCT sono - [Pmax] Potenza nominale massima misurata in **WTT** rappresenta Watt. - Umpp] Tensione operativa ottimale misurata in **VLT** rappresenta Volt. - Impp] Corrente operativa ottimale misurata in **AMP** rappresenta gli Ampere. - Uoc] La tensione a circuito aperto misurata in **VLT** rappresenta il Volt. - Isc] Corrente di corto circuito misurata in **AMP** rappresenta l'Ampere.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempio di payloads  
#### PhotovoltaicDevice NGSI-v2 valori chiave Esempio  
Ecco un esempio di un PhotovoltaicDevice in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### PhotovoltaicDevice NGSI-v2 normalizzato Esempio  
Ecco un esempio di un PhotovoltaicDevice in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### PhotovoltaicDevice NGSI-LD valori chiave Esempio  
Ecco un esempio di PhotovoltaicDevice in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### PhotovoltaicDevice NGSI-LD normalizzato Esempio  
Ecco un esempio di un PhotovoltaicDevice in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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

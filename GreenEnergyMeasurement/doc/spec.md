# GreenEnergyMeasurement
## Description

Generic model for a snapshot measure of energy generated using one or more green energy sources.
Thus, an entity of type `GreenEnergyMeasurement` cannot exist without an accompanying Entity of Type GreenEnergyGenerator

## Data Model

+ `id`: Entity's unique identifier.
  + It shall be `urn:ngsi-ld:GreenEnergyMeasurement:<identifier>`.

+ `type`: Entity Type
  + It shall be equal to `GreenEnergyMeasurement`.

+ `source` : A sequence of characters giving the source of the entity data.
  + Attribute type: [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
  + Optional.

+ `dataProvider` : Specifies the URL to information about the provider of this
  information
  + Attribute type: [URL](https://schema.org/URL)
  + Optional.

+ `dateCreated` : Entity's creation timestamp.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated.

+ `dateModified` : Last update timestamp of this Entity.
  + Attribute type: [DateTime](https://schema.org/DateTime)
  + Read-Only. Automatically generated.

+ `solarPowerGenerated` : Specifies the amount of power generated using solar energy
  + Attribute type: [Number]
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).
  + Attribute metadata:
    timestamp : optional timestamp for the observed value. It can be omitted
      + Type: DateTime
  + Optional.

+ `eolicPowerGenerated` : Specifies the amount of power generated using eolic energy
  + Attribute type: [Number]
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).
  + Attribute metadata:
    timestamp : optional timestamp for the observed value. It can be omitted
      + Type: DateTime
  + Optional.

+ `hydroPowerGenerated` : Specifies the amount of power generated using hydropower energy
  + Attribute type: [Number]
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).
  + Attribute metadata:
    timestamp : optional timestamp for the observed value. It can be omitted
      + Type: DateTime
  + Optional.

+ `biomassPowerGenerated` : Specifies the amount of power generated using biomass energy
  + Attribute type: [Number]
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).
  + Attribute metadata:
    timestamp : optional timestamp for the observed value. It can be omitted
      + Type: DateTime
  + Optional.

+ `geothermalPowerGenerated` : Specifies the amount of power generated using geothermal energy
  + Attribute type: [Number]
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT Common Code (max. 3 characters).
  + Attribute metadata:
    timestamp : optional timestamp for the observed value. It can be omitted
      + Type: DateTime
  + Optional.

+ `refGreenEnergyGenerator` : A reference to the entity `GreenEnergyGenerator` which
  it belongs the measurement
  - Attribute type: Reference to entity of type
        [GreenEneryGenerator](../GreenEnergyGenerator/doc/spec.md)
  - Mandatory

## Examples

### Normalized Example

Normalized NGSI response

```json
{
  "id": "urn:ngsi-ld:GreenEnergyMeasurement:santander:GreenEnergyMeasurement-Generator:a34f24b",
  "type": "GreenEnergyMeasurement",
  "dataProvider":{
    "value":"es.smartciti",
  },
  "solarPowerGenerated":{
    "value":1.2
  },
  "eolicPowerGenerated":{
    "value":3
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
    "value":"urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001"
  }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
  "id": "urn:ngsi-ld:GreenEnergyMeasurement:santander:GreenEnergyMeasurement-Generator:a34f24b",
  "type": "GreenEnergyMeasurement",
  "dataProvider":"es.smartciti",
  "solarPowerGenerated":1.2,
  "eolicPowerGenerated":3,
  "hydroPowerGenerated":0,
  "biomassPowerGenerated":0,
  "geothermalPowerGenerated":0,
  "refGreenEnergyGenerator":"urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0042"
}
```

## Open issues

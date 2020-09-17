# GreenEnergyGenerator
## Description

Generic model for Green Energy Generator. A device which can generate energy using Solar or Eolic green energy.

## Data Model

+ `id`: Entity Id
  + It shall be `urn:ngsi-ld:GreenEnergyGenerator:<identifier>`.

+ `type`: Entity Type
  + It shall be equal to `GreenEnergyGenerator`.

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

+ `location` : Geolocation of the green energy generator site represented by a GeoJSON
  (Multi)Polygon or Point.
  + Attribute type: `geo:json`.
  + Normative References:
    [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
  + Mandatory if `address` is not defined.

+ `address` : Registered green energy generator address.
  + Normative References:
    [https://schema.org/address](https://schema.org/address)
  + Mandatory if `location` is not defined.

+ `name`: Name of the green energy generator.
  + Attribute type: [Text](https://schema.org/Text)
  + Optional.

+ `description`: Brief description of the green energy generator.
  + Attribute type: [Text](https://schema.org/Text)
  + Optional.

+ `status` : Status of the green energy generator.
  + Attribute type: [Text](https://schema.org/Text)
  + Allowed Values: one Of (`working`, `outOfService`, `withIncidence`)
  + Metadata:
    + `timestamp` : Timestamp which reflects the date when the attribute
      value was obtained.
      + Type: [DateTime](https://schema.org/DateTime)
      + Optional
  + Optional

+ `selfConsumption`: Indicate whether energy generated will use for self.
  + Attribute type: type: [Boolean](https://schema.org/Boolean)
  + Optional.

+ `redistribution`: Indicates whether the generated energy will be
  dumped into the network.
  + Attribute type: [Boolean](https://schema.org/Boolean)
  + Optional.

+ `generationSources`: A list of sources used for power generation.
  + Attribute type: [ItemList](https://schema.org/ItemList)
  + Allowed values: (`solar`,`eolic`,`hydropower`,`biomass`,`geothermal`)
  + Mandatory.

+ `maxSolarPowerGenerated`: A measure of maximum solar energy that can be generated
  + Attribute type: [Number](https://schema.org/Number)
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
    Common Code (max. 3 characters).
  + Optional.

+ `maxEolicPowerGenerated`: A measure of maximum eolic energy that can be generated
  + Attribute type: [Number](https://schema.org/Number)
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
    Common Code (max. 3 characters).
  + Optional.

+ `maxHydroPowerGenerated`: A measure of maximum hydropower energy that can be generated
  + Attribute type: [Number](https://schema.org/Number)
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
    Common Code (max. 3 characters).

+ `maxBiomassPowerGenerated`: A measure of maximum biomass energy that can be generated
  + Attribute type: [Number](https://schema.org/Number)
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
    Common Code (max. 3 characters).
  + Optional.

+ `maxGeothermalPowerGenerated`: A measure of maximum geothermal energy that can be generated
  + Attribute type: [Number](https://schema.org/Number)
  + Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
    Common Code (max. 3 characters).
  + Optional.

## Examples

### Normalized Example

Normalized NGSI response

```json
{
  "id": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:9e46d",
  "type": "GreenEnergyGenerator",
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [
        -4.747901,
        41.618265
      ]
    }
  },
  "name":{
    "value":"generator solar + eolic #9e46d"
  },
  "description":{
    "value": "mixed generator model ~004 with maximum power 22w"
  },
  "status":{
    "value":"working"
  },
  "generationSources":{
    "value":["solar","eolic"]
  },
  "selfConsumption":{
    "value":true
  },
  "redistribution":{
    "value":false
  },
  "maxSolarPowerGenerated":{
    "value":15
  },
  "maxEolicPowerGenerated":{
    "value":7
  },
  "maxHydroPowerGenerated":{
    "value":0
  },
  "maxBioMassPowerGenerated":{
    "value":0
  }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
  "id": "urn:ngsi-ld:GreenEnergyGenerator:santander:GreenEnergy:greenEnergyGenerator:0001",
  "type": "GreenEnergyGenerator",
  "location": {
    "type": "Point",
    "coordinates": [-3.80356167695194, 43.46296641666926]
  },
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

## Open issues


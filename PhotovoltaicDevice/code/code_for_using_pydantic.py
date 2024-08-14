from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class MaxPressureLoad(BaseModel):
    hail: Optional[confloat(ge=0.0)] = None
    snow: Optional[confloat(ge=0.0)] = None
    wind: Optional[confloat(ge=0.0)] = None


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class ApplicationEnum(Enum):
    electric = 'electric'
    thermal = 'thermal'
    other = 'other'


class ApplicationClas(Enum):
    A = 'A'
    B = 'B'
    C = 'C'


class CellDimension(BaseModel):
    length: Optional[confloat(ge=0.0)] = None
    thickness: Optional[confloat(ge=0.0)] = None
    width: Optional[confloat(ge=0.0)] = None


class CellOperatingTemperature(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class CellTypeEnum(Enum):
    amorphousSilicon = 'amorphousSilicon'
    CfTe = 'CfTe'
    CIS = 'CIS'
    monocrystalline = 'monocrystalline'
    polycrystalline = 'polycrystalline'
    other = 'other'


class FireClas(Enum):
    A = 'A'
    B = 'B'
    C = 'C'


class InstallationConditionEnum(Enum):
    desert = 'desert'
    dust = 'dust'
    extremeHeat = 'extremeHeat'
    extremeCold = 'extremeCold'
    extremeClimate = 'extremeClimate'
    extremeHumidity = 'extremeHumidity'
    marine = 'marine'
    none = 'none'
    other = 'other'
    saline = 'saline'
    sand = 'sand'
    seismic = 'seismic'


class InstallationModeEnum(Enum):
    ground = 'ground'
    other = 'other'
    pole = 'pole'
    roofing = 'roofing'
    wall = 'wall'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class ModuleDimension(BaseModel):
    length: Optional[confloat(ge=0.0)] = None
    thickness: Optional[confloat(ge=0.0)] = None
    width: Optional[confloat(ge=0.0)] = None


class ModuleNOCT(BaseModel):
    Impp: Optional[confloat(ge=0.0)] = None
    Isc: Optional[confloat(ge=0.0)] = None
    Pmax: Optional[confloat(ge=0.0)] = None
    Umpp: Optional[confloat(ge=0.0)] = None
    Uoc: Optional[confloat(ge=0.0)] = None


class ModuleSTC(BaseModel):
    Impp: Optional[confloat(ge=0.0)] = None
    Isc: Optional[confloat(ge=0.0)] = None
    Pmax: Optional[confloat(ge=0.0)] = None
    Umpp: Optional[confloat(ge=0.0)] = None
    Uoc: Optional[confloat(ge=0.0)] = None


class PanelDimension(BaseModel):
    length: Optional[confloat(ge=0.0)] = None
    thickness: Optional[confloat(ge=0.0)] = None
    width: Optional[confloat(ge=0.0)] = None


class PanelOperatingTemperature(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=-50.0)] = None


class PossibilityOfUseEnum(Enum):
    mixed = 'mixed'
    mobile = 'mobile'
    other = 'other'
    stationary = 'stationary'


class TemperatureCoefficient(BaseModel):
    Isc: Optional[confloat(ge=0.0)] = None
    Pmax: Optional[confloat(ge=-1.0)] = None
    Uoc: Optional[confloat(ge=-1.0)] = None


class Type6(Enum):
    PhotovoltaicDevice = 'PhotovoltaicDevice'


class TypeOfUseEnum(Enum):
    indoor = 'indoor'
    outdoor = 'outdoor'
    mixed = 'mixed'
    other = 'other'


class PhotovoltaicDevice(BaseModel):
    MaxPressureLoad: Optional[MaxPressureLoad] = Field(
        None,
        description='aximum mechanics Pressure (shear, elasticity, compression) load on a Panel. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **PAL** represents Pascal',
    )
    MaximumSystemVoltage: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum system voltage permitted for the **module**. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    NominalPower: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Nominal Power for the **panel**. This is the same value of items [Pmax] for [moduleSTC] attribute. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **WTT** represents Watt',
    )
    PanelNbModules: Optional[float] = Field(
        None, description="Number of 'Modules' per 'Panel'"
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    application: Optional[List[ApplicationEnum]] = Field(
        None,
        description="Target application regarding the Type of Solar panel (In our case `electric`). A unique value. https://schema.org/Text. Enum:'electric, thermal, other'",
    )
    applicationClass: Optional[List[ApplicationClas]] = Field(
        None,
        description="Evaluation of the potential hazards associated with the module. A unique value. Enum:'A, B, C'",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    areaWeight: Optional[float] = Field(
        None,
        description='Area Weight measured in Kg/m². The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **28** represents Kilogram per square meter',
    )
    brandName: Optional[str] = Field(None, description='Brand Name of the item')
    cellDimension: Optional[CellDimension] = Field(
        None,
        description='External dimension of a cell. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter',
    )
    cellOperatingTemperature: Optional[CellOperatingTemperature] = Field(
        None,
        description='This is the nominal operating temperature range of the cells in which it collects solar energy. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius',
    )
    cellType: Optional[List[CellTypeEnum]] = Field(
        None,
        description="Type of cells used to built the photo-voltaic unit. 2 kinds of Technologies *`Cristalline`* or  *`Thin layers`*. A unique value. Enum:'amorphousSilicon, CfTe, CIS, monocrystalline, polycrystalline, other'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastReported: Optional[AwareDatetime] = Field(
        None,
        description='A timestamps which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    documentation: Optional[str] = Field(
        None, description='Technical Documentation (Installation / maintenance / used)'
    )
    fireClass: Optional[List[FireClas]] = Field(
        None,
        description="Evaluation to the fire (IEC 61730). A unique value. Enum:'A, B, C'",
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    installationCondition: Optional[List[InstallationConditionEnum]] = Field(
        None,
        description="Condition and possibility of use in the following environments. A combination. Enum:'desert, dust, extremeHeat, extremeCold, extremeClimate, extremeHumidity, marine, none, other, saline, sand, seismic'",
    )
    installationMode: Optional[List[InstallationModeEnum]] = Field(
        None,
        description="Positioning of the device in relation to a ground reference system. A unique value. Enum:'ground, other, pole, roofing, wall'",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manufacturerName: Optional[str] = Field(
        None, description='Manufacturer Name of the item'
    )
    modelName: Optional[str] = Field(None, description='Model Name of the item')
    moduleDimension: Optional[ModuleDimension] = Field(
        None,
        description=' External dimension of a module. A module can be an assembly of 1 to n cells. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter',
    )
    moduleNOCT: Optional[ModuleNOCT] = Field(
        None,
        description='Normal Operating Cell Temperature measurements. The format is structured by a sub-property of 5 items. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere',
    )
    moduleNbCells: Optional[float] = Field(
        None, description="Number of 'cells' per 'module'"
    )
    moduleSTC: Optional[ModuleSTC] = Field(
        None,
        description='Standard Test Condition measurements. The format is structured by a sub-property of 5 items. Pmax in Watt. Umpp in Volt. Impp in Ampere. Uoc in Volt. Isc in Ampere',
    )
    moduleYieldRate: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Positioning of the device in relation to a ground reference system. A unique value',
    )
    nTCClass: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The Negative Temperature Coefficient of resistance - *NTC*, describes the relative change of a physical property that is associated with a given change in negative temperature. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    pTCClass: Optional[confloat(ge=0.0)] = Field(
        None,
        description=' The Positive Temperature Coefficient of resistance - *PTC*, describes the relative change of a physical property that is associated with a given change in positive temperature. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    panelDimension: Optional[PanelDimension] = Field(
        None,
        description="External dimension of a Panel. A solar panel can be an assembly of 1 to n modules, which themselves are made of several cells which collect heat from the sun's rays. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MMT** represents Millimeter",
    )
    panelLifetime: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Average lifetime of a panel. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **ANN** represents Year',
    )
    panelOperatingTemperature: Optional[PanelOperatingTemperature] = Field(
        None,
        description='Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat for using the panel. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius',
    )
    panelWeight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Weight of a panel (Sometime the reference used is Kg / m²). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilogram',
    )
    panelYieldCurve: Optional[List[str]] = Field(
        None,
        description="Option 1. Energy production yield curve of the panel from its [NominalPower] at [T0] and along its [panelLifetime]. The Measurements provided in the list are a sequence of Energy Production Capacity represented in Percent starting at 5 years with a 'Step' of 5 years according to the information provided by the manufacturer. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent. ",
    )
    performanceLowIrradiance: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Average relative yield to Performance at Low Irradiance. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    possibilityOfUse: Optional[List[PossibilityOfUseEnum]] = Field(
        None,
        description="Possibility of use. A unique value. Enum:'mixed, mobile, other, stationary'",
    )
    protectionIP: Optional[str] = Field(
        None,
        description="IP 'Ingress Protection' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). First digit: Solid particle protection (Single numeral: 0–6 or 'X'). Second digit: Liquid ingress protection (Single numeral: 0–9 or 'X' ).Third digit: Personal Protection  against access to dangerous parts (optional additional letter). Fourth digit: Other protections (optional additional letter)",
    )
    refDevice: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link',
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[List[str]] = Field(
        None,
        description='List of serial numbers of Photo-voltaic device supplied by the manufacturer and assembled in operating mode on a single location',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    temperatureCoefficient: Optional[TemperatureCoefficient] = Field(
        None,
        description=' Temperature influence coefficient on the panel. The format is structured by a sub-property of 3 items. Pmax in Watt. Uoc in Volt. Isc in Ampere',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be PhotovoltaicDevice'
    )
    typeOfUse: Optional[List[TypeOfUseEnum]] = Field(
        None,
        description="Accepted use regarding its positioning in an indoor / outdoor environment. A unique value. Enum:'indoor, outdoor, mixed, other'",
    )

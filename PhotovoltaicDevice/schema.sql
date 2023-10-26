/* (Beta) Export of data model PhotovoltaicDevice of the subject dataModel.GreenEnergy for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PhotovoltaicDevice_type AS ENUM ('PhotovoltaicDevice');
CREATE TABLE PhotovoltaicDevice (MaxPressureLoad JSON, MaximumSystemVoltage NUMERIC, NominalPower NUMERIC, PanelNbModules NUMERIC, address JSON, alternateName TEXT, application JSON, applicationClass JSON, areaServed TEXT, areaWeight NUMERIC, brandName TEXT, cellDimension JSON, cellOperatingTemperature JSON, cellType JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateLastReported TIMESTAMP, dateModified TIMESTAMP, description TEXT, documentation TEXT, fireClass JSON, id TEXT PRIMARY KEY, installationCondition JSON, installationMode JSON, location JSON, manufacturerName TEXT, modelName TEXT, moduleDimension JSON, moduleNOCT JSON, moduleNbCells NUMERIC, moduleSTC JSON, moduleYieldRate NUMERIC, nTCClass NUMERIC, name TEXT, owner JSON, pTCClass NUMERIC, panelDimension JSON, panelLifetime NUMERIC, panelOperatingTemperature JSON, panelWeight NUMERIC, panelYieldCurve JSON, performanceLowIrradiance NUMERIC, possibilityOfUse JSON, protectionIP TEXT, seeAlso JSON, serialNumber JSON, source TEXT, temperatureCoefficient JSON, type PhotovoltaicDevice_type, typeOfUse JSON);
/* (Beta) Export of data model SolarTracker of the subject dataModel.GreenEnergy 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE backtracking_type AS ENUM ('on', 'off');
CREATE TYPE boardDirection_type AS ENUM ('1', '-1');
CREATE TYPE deviceCategory_type AS ENUM ('PCU', 'FCU', 'SCU');
CREATE TYPE deviceState_type AS ENUM ('Online', 'Offline');
CREATE TYPE motorDirection_type AS ENUM ('1', '-1');
CREATE TYPE movementInterval_type AS ENUM ('5', '10', '15');
CREATE TYPE operatingMode_type AS ENUM ('automatic', 'manual', 'safesnow', 'safesnowsensor', 'safewind', 'safewindsensor', 'maintenance');
CREATE TYPE SolarTracker_type AS ENUM ('SolarTracker');

CREATE TABLE SolarTracker (
    address JSON,
    alternateName TEXT,
    altitude NUMERIC,
    areaServed TEXT,
    backtracking backtracking_type,
    batteryLevel NUMERIC,
    boardDirection boardDirection_type,
    currentAngle NUMERIC,
    currentPowerConsumption NUMERIC,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    dateUpdate TIMESTAMP,
    description TEXT,
    deviceCategory deviceCategory_type,
    deviceState deviceState_type,
    id TEXT PRIMARY KEY,
    ipAddress JSON,
    location JSON,
    maxAngleLimit NUMERIC,
    maxPowerRecorded NUMERIC,
    maxPowerThreshold NUMERIC,
    minAngleLimit NUMERIC,
    minPowerRecorded NUMERIC,
    motorDirection motorDirection_type,
    movementInterval movementInterval_type,
    name TEXT,
    operatingMode operatingMode_type,
    owner JSON,
    panelLength NUMERIC,
    restingAngle NUMERIC,
    seeAlso JSON,
    snowSafetyAngle NUMERIC,
    source TEXT,
    targetAngle NUMERIC,
    type SolarTracker_type,
    windSafetyAngle NUMERIC
);
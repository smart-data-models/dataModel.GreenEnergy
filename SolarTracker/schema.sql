/* (Beta) Export of data model SolarTracker of the subject dataModel.GreenEnergy for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SolarTracker_backtracking_type AS ENUM ('on', 'off');
CREATE TYPE SolarTracker_boardDirection_type AS ENUM ('1', '-1');
CREATE TYPE SolarTracker_deviceCategory_type AS ENUM ('PCU', 'FCU', 'SCU');
CREATE TYPE SolarTracker_deviceState_type AS ENUM ('Online', 'Offline');
CREATE TYPE SolarTracker_motorDirection_type AS ENUM ('1', '-1');
CREATE TYPE SolarTracker_movementInterval_type AS ENUM ('5', '10', '15');
CREATE TYPE SolarTracker_operatingMode_type AS ENUM ('automatic', 'manual', 'safesnow', 'safesnowsensor', 'safewind', 'safewindsensor', 'maintenance');
CREATE TYPE SolarTracker_type AS ENUM ('SolarTracker');
CREATE TABLE SolarTracker (
  "address" JSON,
  "alternateName" TEXT,
  "altitude" NUMERIC,
  "areaServed" TEXT,
  "backtracking" SolarTracker_backtracking_type,
  "batteryLevel" NUMERIC,
  "boardDirection" SolarTracker_boardDirection_type,
  "currentAngle" NUMERIC,
  "currentPowerConsumption" NUMERIC,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "dateUpdate" TIMESTAMP,
  "description" TEXT,
  "deviceCategory" SolarTracker_deviceCategory_type,
  "deviceState" SolarTracker_deviceState_type,
  "id" TEXT PRIMARY KEY,
  "ipAddress" JSON,
  "location" JSON,
  "maxAngleLimit" NUMERIC,
  "maxPowerRecorded" NUMERIC,
  "maxPowerThreshold" NUMERIC,
  "minAngleLimit" NUMERIC,
  "minPowerRecorded" NUMERIC,
  "motorDirection" SolarTracker_motorDirection_type,
  "movementInterval" SolarTracker_movementInterval_type,
  "name" TEXT,
  "operatingMode" SolarTracker_operatingMode_type,
  "owner" JSON,
  "panelLength" NUMERIC,
  "restingAngle" NUMERIC,
  "seeAlso" JSON,
  "snowSafetyAngle" NUMERIC,
  "source" TEXT,
  "targetAngle" NUMERIC,
  "type" SolarTracker_type,
  "windSafetyAngle" NUMERIC
);
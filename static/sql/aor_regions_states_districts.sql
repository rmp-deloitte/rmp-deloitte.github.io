-- Area of Operations --
INSERT INTO AreaOfOperations (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aorId)
VALUES ('East', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1)
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aorId = 1;

INSERT INTO AreaOfOperations (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aorId)
VALUES ('West', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2)
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aorId = 2;

-- Regions --
INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Atlantic', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 'East')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 1, aor_id = 'East';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Capital', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2, 'East')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 2, aor_id = 'East';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Central', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3, 'East')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 3, aor_id = 'East';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('HQ', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4, 'East')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 4, aor_id = 'East';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Midwest', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5, 'West')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 5, aor_id = 'West';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Mountain', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6, 'West')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 6, aor_id = 'West';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Northeast', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7, 'East')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 7, aor_id = 'East';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Pacific', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8, 'West')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 8, aor_id = 'West';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Southeast', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9, 'East')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 9, aor_id = 'East';

INSERT INTO regions (name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, regionId, aor_id)
VALUES ('Southwest', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10, 'West')
ON DUPLICATE KEY UPDATE centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, regionId = 10, aor_id = 'West';

-- States --
INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Alaska', 'AK', 2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Pacific', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'AK', stateId = 2, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Pacific', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Alabama', 'AL', 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'AL', stateId = 1, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Arkansas', 'AR', 5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'AR', stateId = 5, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Arizona', 'AZ', 4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'AZ', stateId = 4, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('California', 'CA', 6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Pacific', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'CA', stateId = 6, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Pacific', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Colorado', 'CO', 8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'CO', stateId = 8, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Connecticut', 'CT',9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'CT', stateId = 9, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('District of Columbia', 'DC', 11, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'DC', stateId = 11, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Delaware', 'DE', 10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'DE', stateId = 10, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Florida', 'FL', 12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'FL', stateId = 12, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Georgia', 'GA', 13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'GA', stateId = 13, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Hawaii', 'HI', 15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Pacific', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'HI', stateId = 15, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Pacific', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Iowa', 'IA', 19, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Midwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'IA', stateId = 19, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Midwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Idaho', 'ID', 16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Midwest', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'ID', stateId = 16, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Midwest', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Illinois', 'IL', 17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'IL', stateId = 17, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Indiana', 'IN', 18, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'IN', stateId = 18, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Kansas', 'KS', 20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Midwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'KS', stateId = 20, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Midwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Kentucky', 'KY', 21, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'KY', stateId = 21, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Louisiana', 'LA', 22, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'LA', stateId = 22, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Massachusetts', 'MA', 25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'MA', stateId = 25, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Maryland', 'MD', 24, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'MD', stateId = 24, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Maine', 'ME', 23, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'ME', stateId = 23, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Michigan', 'MI', 26, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'MI', stateId = 26, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Minnesota', 'MN', 27, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Midwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'MN', stateId = 27, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Midwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Missouri', 'MO', 29, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Midwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'MO', stateId = 29, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Midwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Mississippi', 'MS', 28, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'MS', stateId = 28, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Montana', 'MN', 30, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'MT', stateId = 30, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('North Carolina', 'NC', 37, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'NC', stateId = 37, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('North Dakota', 'ND', 38, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'AK', stateId = 38, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('New Hampshire', 'NH', 33, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'NH', stateId = 33, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Nebraska', 'NE', 31, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Midwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'NE', stateId = 31, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Midwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('New Jersey', 'NJ', 34, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'NJ', stateId = 34, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('New Mexico', 'NM', 35, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'NM', stateId = 35, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('North Dakota', 'ND', 38, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'ND', stateId = 38, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Nevada', 'NV', 32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'NV', stateId = 32, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('New York', 'NY', 36, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'NY', stateId = 36, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Ohio', 'OH', 39, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'OH', stateId = 39, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Oklahoma', 'OK', 40, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Southwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'OK', stateId = 40, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Southwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Oregon', 'OR', 41, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Pacific', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'OR', stateId = 41, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Pacific', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Pennsylvania', 'PA', 42, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'PA', stateId = 42, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Puerto Rico', 'PR', 72, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Southeast', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'PR', stateId = 72, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Southeast', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Rhode Island', 'RI', 44, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'RI', stateId = 44, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('South Carolina', 'SC', 45, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'SC', stateId = 45, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('South Dakota', 'SD', 46, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'No Office/No Service')
ON DUPLICATE KEY UPDATE abbv = 'SD', stateId = 46, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'No Office/No Service';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Tennessee', 'TN', 47, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'TN', stateId = 47, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Texas', 'TX', 48, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Southwest', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'TX', stateId = 48, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Southwest', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Utah', 'UT', 49, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'UT', stateId = 49, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Virginia', 'VA', 51, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Atlantic', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'VA', stateId = 51, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Atlantic', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Vermont', 'VT', 50, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Northeast', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'VT', stateId = 50, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Northeast', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Washington', 'WA', 53, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Pacific', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'WA', stateId = 53, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Pacific', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Wisconsin', 'WI', 55, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'Operational')
ON DUPLICATE KEY UPDATE abbv = 'WI', stateId = 55, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'Operational';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('West Virginia', 'WV', 54, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'East', 'Central', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'WV', stateId = 54, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'East', region_id = 'Central', serviceStatus = 'No Office';

INSERT INTO states (name, abbv, stateId, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, serviceStatus)
VALUES ('Wyoming', 'WY', 56, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'West', 'Mountain', 'No Office')
ON DUPLICATE KEY UPDATE abbv = 'WY', stateId = 56, centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = 'West', region_id = 'Mountain', serviceStatus = 'No Office';

-- Districts --
INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Alabama') * 1000 + 1, 'MAL', 'Middle District of Alabama', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Alabama'), (SELECT states.region_id FROM states WHERE name = 'Alabama'), 'Alabama')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Alabama') * 1000 + 1, name = 'Middle District of Alabama', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Alabama'), region_id = (SELECT states.region_id FROM states WHERE name = 'Alabama'), state_id = 'Alabama';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Alabama') * 1000 + 2, 'NAL', 'Northern District of Alabama', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Alabama'), (SELECT states.region_id FROM states WHERE name = 'Alabama'), 'Alabama')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Alabama') * 1000 + 2, name = 'Northern District of Alabama', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Alabama'), region_id = (SELECT states.region_id FROM states WHERE name = 'Alabama'), state_id = 'Alabama';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Alabama') * 1000 + 3, 'SAL', 'Southern District of Alabama', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Alabama'), (SELECT states.region_id FROM states WHERE name = 'Alabama'), 'Alabama')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Alabama') * 1000 + 3, name = 'Southern District of Alabama', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Alabama'), region_id = (SELECT states.region_id FROM states WHERE name = 'Alabama'), state_id = 'Alabama';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Alaska') * 1000 + 1, 'AK', 'District of Alaska', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Alaska'), (SELECT states.region_id FROM states WHERE name = 'Alaska'), 'Alaska')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Alaska') * 1000 + 1,name = 'District of Alaska', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Alaska'), region_id = (SELECT states.region_id FROM states WHERE name = 'Alaska'), state_id = 'Alaska';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Arizona') * 1000 + 1, 'AZ', 'District of Arizona', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Arizona'), (SELECT states.region_id FROM states WHERE name = 'Arizona'), 'Arizona')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Arizona') * 1000 + 1, name = 'District of Arizona', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Arizona'), region_id = (SELECT states.region_id FROM states WHERE name = 'Arizona'), state_id = 'Arizona';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Arkansas') * 1000 + 1, 'EAR', 'Eastern District of Arkansas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Arkansas'), (SELECT states.region_id FROM states WHERE name = 'Arkansas'), 'Arkansas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Arkansas') * 1000 + 1, name = 'Eastern District of Arkansas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Arkansas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Arkansas'), state_id = 'Arkansas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Arkansas') * 1000 + 2, 'WAR', 'Western District of Arkansas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Arkansas'), (SELECT states.region_id FROM states WHERE name = 'Arkansas'), 'Arkansas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Arkansas') * 1000 + 2, name = 'Western District of Arkansas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Arkansas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Arkansas'), state_id = 'Arkansas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 1, 'CCA', 'Central District of California', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'California'), (SELECT states.region_id FROM states WHERE name = 'California'), 'California')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 1, name = 'Central District of California', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'California'), region_id = (SELECT states.region_id FROM states WHERE name = 'California'), state_id = 'California';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 2, 'ECA', 'Eastern District of California', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'California'), (SELECT states.region_id FROM states WHERE name = 'California'), 'California')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 2, name = 'Eastern District of California', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'California'), region_id = (SELECT states.region_id FROM states WHERE name = 'California'), state_id = 'California';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 3, 'NCA', 'Northern District of California', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'California'), (SELECT states.region_id FROM states WHERE name = 'California'), 'California')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 +3, name = 'Northern District of California', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'California'), region_id = (SELECT states.region_id FROM states WHERE name = 'California'), state_id = 'California';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 4, 'SCA', 'Southern District of California', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'California'), (SELECT states.region_id FROM states WHERE name = 'California'), 'California')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 4, name = 'Southern District of California', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'California'), region_id = (SELECT states.region_id FROM states WHERE name = 'California'), state_id = 'California';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 5, 'WCA', 'Western District of California', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'California'), (SELECT states.region_id FROM states WHERE name = 'California'), 'California')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='California') * 1000 + 5, name = 'Western District of California', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'California'), region_id = (SELECT states.region_id FROM states WHERE name = 'California'), state_id = 'California';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Colorado') * 1000 + 1, 'CO', 'District of Colorado', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Colorado'), (SELECT states.region_id FROM states WHERE name = 'Colorado'), 'Colorado')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Colorado') * 1000 + 1, name = 'District of Colorado', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Colorado'), region_id = (SELECT states.region_id FROM states WHERE name = 'Colorado'), state_id = 'Colorado';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Connecticut') * 1000 + 1, 'CT', 'District of Connecticut', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Connecticut'), (SELECT states.region_id FROM states WHERE name = 'Connecticut'), 'Connecticut')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Connecticut') * 1000 + 1, name = 'District of Connecticut', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Connecticut'), region_id = (SELECT states.region_id FROM states WHERE name = 'Connecticut'), state_id = 'Connecticut';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Delaware') * 1000 + 1, 'DE', 'District of Delaware', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Delaware'), (SELECT states.region_id FROM states WHERE name = 'Delaware'), 'Delaware')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Delaware') * 1000 + 1,  name = 'District of Delaware', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Delaware'), region_id = (SELECT states.region_id FROM states WHERE name = 'Delaware'), state_id = 'Delaware';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='District of Columbia') * 1000 + 1, 'DC', 'District of Columbia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'District of Columbia'), (SELECT states.region_id FROM states WHERE name = 'District of Columbia'), 'District of Columbia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='District of Columbia') * 1000 + 1,  name = 'District of Columbia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'District of Columbia'), region_id = (SELECT states.region_id FROM states WHERE name = 'District of Columbia'), state_id = 'District of Columbia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Florida') * 1000 + 1, 'MFL', 'Middle District of Florida', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Florida'), (SELECT states.region_id FROM states WHERE name = 'Florida'), 'Florida')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Florida') * 1000 + 1, name = 'Middle District of Florida', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Florida'), region_id = (SELECT states.region_id FROM states WHERE name = 'Florida'), state_id = 'Florida';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Florida') * 1000 + 2, 'NFL', 'Northern District of Florida', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Florida'), (SELECT states.region_id FROM states WHERE name = 'Florida'), 'Florida')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Florida') * 1000 + 2, name = 'Northern District of Florida', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Florida'), region_id = (SELECT states.region_id FROM states WHERE name = 'Florida'), state_id = 'Florida';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Florida') * 1000 + 3, 'SFL', 'Southern District of Florida', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Florida'), (SELECT states.region_id FROM states WHERE name = 'Florida'), 'Florida')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Florida') * 1000 + 3, name = 'Southern District of Florida', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Florida'), region_id = (SELECT states.region_id FROM states WHERE name = 'Florida'), state_id = 'Florida';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Georgia') * 1000 + 1, 'MGA', 'Middle District of Georgia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Georgia'), (SELECT states.region_id FROM states WHERE name = 'Georgia'), 'Georgia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Georgia') * 1000 + 1, name = 'Middle District of Georgia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Georgia'), region_id = (SELECT states.region_id FROM states WHERE name = 'Georgia'), state_id = 'Georgia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Georgia') * 1000 + 2, 'NGA', 'Northern District of Georgia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Georgia'), (SELECT states.region_id FROM states WHERE name = 'Georgia'), 'Georgia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Georgia') * 1000 + 2, name = 'Northern District of Georgia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Georgia'), region_id = (SELECT states.region_id FROM states WHERE name = 'Georgia'), state_id = 'Georgia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Georgia') * 1000 + 3, 'SGA', 'Southern District of Georgia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Georgia'), (SELECT states.region_id FROM states WHERE name = 'Georgia'), 'Georgia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Georgia') * 1000 + 3, name = 'Southern District of Georgia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Georgia'), region_id = (SELECT states.region_id FROM states WHERE name = 'Georgia'), state_id = 'Georgia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Hawaii') * 1000 + 1, 'HI', 'District of Hawaii', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Hawaii'), (SELECT states.region_id FROM states WHERE name = 'Hawaii'), 'Hawaii')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Hawaii') * 1000 + 1, name = 'District of Hawaii', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Hawaii'), region_id = (SELECT states.region_id FROM states WHERE name = 'Hawaii'), state_id = 'Hawaii';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Idaho') * 1000 + 1, 'ID', 'District of Idaho', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Idaho'), (SELECT states.region_id FROM states WHERE name = 'Idaho'), 'Idaho')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Idaho') * 1000 + 1, name = 'District of Idaho', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Idaho'), region_id = (SELECT states.region_id FROM states WHERE name = 'Idaho'), state_id = 'Idaho';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Illinois') * 1000 + 1, 'CIL', 'Central District of Illinois', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Illinois'), (SELECT states.region_id FROM states WHERE name = 'Illinois'), 'Illinois')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Illinois') * 1000 + 1, name = 'Central District of Illinois', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Illinois'), region_id = (SELECT states.region_id FROM states WHERE name = 'Illinois'), state_id = 'Illinois';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Illinois') * 1000 + 2, 'NIL', 'Northern District of Illinois', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Illinois'), (SELECT states.region_id FROM states WHERE name = 'Illinois'), 'Illinois')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Illinois') * 1000 + 2, name = 'Northern District of Illinois', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Illinois'), region_id = (SELECT states.region_id FROM states WHERE name = 'Illinois'), state_id = 'Illinois';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Illinois') * 1000 + 3, 'SIL', 'Southern District of Illinois', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Illinois'), (SELECT states.region_id FROM states WHERE name = 'Illinois'), 'Illinois')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Illinois') * 1000 + 3, name = 'Southern District of Illinois', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Illinois'), region_id = (SELECT states.region_id FROM states WHERE name = 'Illinois'), state_id = 'Illinois';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Indiana') * 1000 + 1, 'NIN', 'Northern District of Indiana', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Indiana'), (SELECT states.region_id FROM states WHERE name = 'Indiana'), 'Indiana')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Indiana') * 1000 + 1, name = 'Northern District of Indiana', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Indiana'), region_id = (SELECT states.region_id FROM states WHERE name = 'Indiana'), state_id = 'Indiana';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Indiana') * 1000 + 2, 'SIN', 'Southern District of Indiana', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Indiana'), (SELECT states.region_id FROM states WHERE name = 'Indiana'), 'Indiana')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Indiana') * 1000 + 2, name = 'Southern District of Indiana', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Indiana'), region_id = (SELECT states.region_id FROM states WHERE name = 'Indiana'), state_id = 'Indiana';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Iowa') * 1000 + 1, 'NIA', 'Northern District of Iowa', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Iowa'), (SELECT states.region_id FROM states WHERE name = 'Iowa'), 'Iowa')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Iowa') * 1000 + 1, name = 'Northern District of Iowa', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Iowa'), region_id = (SELECT states.region_id FROM states WHERE name = 'Iowa'), state_id = 'Iowa';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Iowa') * 1000 + 2, 'SIA', 'Southern District of Iowa', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Iowa'), (SELECT states.region_id FROM states WHERE name = 'Iowa'), 'Iowa')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Iowa') * 1000 + 2, name = 'Southern District of Iowa', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Iowa'), region_id = (SELECT states.region_id FROM states WHERE name = 'Iowa'), state_id = 'Iowa';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Kansas') * 1000 + 1, 'KS', 'District of Kansas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Kansas'), (SELECT states.region_id FROM states WHERE name = 'Kansas'), 'Kansas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Kansas') * 1000 + 1, name = 'District of Kansas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Kansas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Kansas'), state_id = 'Kansas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Kentucky') * 1000 + 1, 'EKY', 'Eastern District of Kentucky', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Kentucky'), (SELECT states.region_id FROM states WHERE name = 'Kentucky'), 'Kentucky')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Kentucky') * 1000 + 1,  name = 'Eastern District of Kentucky', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Kentucky'), region_id = (SELECT states.region_id FROM states WHERE name = 'Kentucky'), state_id = 'Kentucky';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Kentucky') * 1000 + 2, 'WKY', 'Western District of Kentucky', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Kentucky'), (SELECT states.region_id FROM states WHERE name = 'Kentucky'), 'Kentucky')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Kentucky') * 1000 + 2,  name = 'Western District of Kentucky', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Kentucky'), region_id = (SELECT states.region_id FROM states WHERE name = 'Kentucky'), state_id = 'Kentucky';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Louisiana') * 1000 + 1, 'ELA', 'Eastern District of Louisiana', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Louisiana'), (SELECT states.region_id FROM states WHERE name = 'Louisiana'), 'Louisiana')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Louisiana') * 1000 + 1, name = 'Eastern District of Louisiana', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Louisiana'), region_id = (SELECT states.region_id FROM states WHERE name = 'Louisiana'), state_id = 'Louisiana';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Louisiana') * 1000 + 2, 'MLA', 'Middle District of Louisiana', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Louisiana'), (SELECT states.region_id FROM states WHERE name = 'Louisiana'), 'Louisiana')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Louisiana') * 1000 + 2, name = 'Middle District of Louisiana', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Louisiana'), region_id = (SELECT states.region_id FROM states WHERE name = 'Louisiana'), state_id = 'Louisiana';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Louisiana') * 1000 + 3, 'WLA', 'Western District of Louisiana', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Louisiana'), (SELECT states.region_id FROM states WHERE name = 'Louisiana'), 'Louisiana')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Louisiana') * 1000 + 3, name = 'Western District of Louisiana', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Louisiana'), region_id = (SELECT states.region_id FROM states WHERE name = 'Louisiana'), state_id = 'Louisiana';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Maine') * 1000 + 1, 'ME', 'District of Maine', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Maine'), (SELECT states.region_id FROM states WHERE name = 'Maine'), 'Maine')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Maine') * 1000 + 1, name = 'District of Maine', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Maine'), region_id = (SELECT states.region_id FROM states WHERE name = 'Maine'), state_id = 'Maine';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Maryland') * 1000 + 1, 'MD', 'District of Maryland', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Maryland'), (SELECT states.region_id FROM states WHERE name = 'Maryland'), 'Maryland')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Maryland') * 1000 + 1, name = 'District of Maryland', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Maryland'), region_id = (SELECT states.region_id FROM states WHERE name = 'Maryland'), state_id = 'Maryland';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Massachusetts') * 1000 + 1, 'MA', 'District of Massachusetts', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Massachusetts'), (SELECT states.region_id FROM states WHERE name = 'Massachusetts'), 'Massachusetts')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Massachusetts') * 1000 + 1, name = 'District of Massachusetts', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Massachusetts'), region_id = (SELECT states.region_id FROM states WHERE name = 'Massachusetts'), state_id = 'Massachusetts';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Michigan') * 1000 + 1, 'EMI', 'Eastern District of Michigan', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Michigan'), (SELECT states.region_id FROM states WHERE name = 'Michigan'), 'Michigan')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Michigan') * 1000 + 1, name = 'Eastern District of Michigan', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Michigan'), region_id = (SELECT states.region_id FROM states WHERE name = 'Michigan'), state_id = 'Michigan';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Michigan') * 1000 + 2, 'WMI', 'Western District of Michigan', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Michigan'), (SELECT states.region_id FROM states WHERE name = 'Michigan'), 'Michigan')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Michigan') * 1000 + 2, name = 'Western District of Michigan', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Michigan'), region_id = (SELECT states.region_id FROM states WHERE name = 'Michigan'), state_id = 'Michigan';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Minnesota') * 1000 + 1, 'MN', 'District of Minnesota', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Minnesota'), (SELECT states.region_id FROM states WHERE name = 'Minnesota'), 'Minnesota')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Minnesota') * 1000 + 1,name = 'District of Minnesota', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Minnesota'), region_id = (SELECT states.region_id FROM states WHERE name = 'Minnesota'), state_id = 'Minnesota';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Mississippi') * 1000 + 1, 'NMS', 'Northern District of Mississippi', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Mississippi'), (SELECT states.region_id FROM states WHERE name = 'Mississippi'), 'Mississippi')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Mississippi') * 1000 + 1, name = 'Northern District of Mississippi', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Mississippi'), region_id = (SELECT states.region_id FROM states WHERE name = 'Mississippi'), state_id = 'Mississippi';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Mississippi') * 1000 + 2, 'SMS', 'Southern District of Mississippi', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Mississippi'), (SELECT states.region_id FROM states WHERE name = 'Mississippi'), 'Mississippi')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Mississippi') * 1000 + 2, name = 'Southern District of Mississippi', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Mississippi'), region_id = (SELECT states.region_id FROM states WHERE name = 'Mississippi'), state_id = 'Mississippi';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Missouri') * 1000 + 1, 'EMO', 'Eastern District of Missouri', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Missouri'), (SELECT states.region_id FROM states WHERE name = 'Missouri'), 'Missouri')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Missouri') * 1000 + 1, name = 'Eastern District of Missouri', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Missouri'), region_id = (SELECT states.region_id FROM states WHERE name = 'Missouri'), state_id = 'Missouri';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Missouri') * 1000 + 2, 'WMO', 'Western District of Missouri', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Missouri'), (SELECT states.region_id FROM states WHERE name = 'Missouri'), 'Missouri')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Missouri') * 1000 + 2, name = 'Western District of Missouri', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Missouri'), region_id = (SELECT states.region_id FROM states WHERE name = 'Missouri'), state_id = 'Missouri';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Nebraska') * 1000 + 1, 'NE', 'District of Nebraska', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Nebraska'), (SELECT states.region_id FROM states WHERE name = 'Nebraska'), 'Nebraska')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Nebraska') * 1000 + 1, name = 'District of Nebraska', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Nebraska'), region_id = (SELECT states.region_id FROM states WHERE name = 'Nebraska'), state_id = 'Nebraska';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Nevada') * 1000 + 1, 'NV', 'District of Nevada', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Nevada'), (SELECT states.region_id FROM states WHERE name = 'Nevada'), 'Nevada')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Nevada') * 1000 + 1, name = 'District of Nevada', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Nevada'), region_id = (SELECT states.region_id FROM states WHERE name = 'Nevada'), state_id = 'Nevada';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New Hampshire') * 1000 + 1, 'NH', 'District of New Hampshire', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New Hampshire'), (SELECT states.region_id FROM states WHERE name = 'New Hampshire'), 'New Hampshire')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New Hampshire') * 1000 + 1, name = 'District of New Hampshire', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New Hampshire'), region_id = (SELECT states.region_id FROM states WHERE name = 'New Hampshire'), state_id = 'New Hampshire';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New Jersey') * 1000 + 1, 'NJ', 'District of New Jersey', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New Jersey'), (SELECT states.region_id FROM states WHERE name = 'New Jersey'), 'New Jersey')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New Jersey') * 1000 + 1, name = 'District of New Jersey', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New Jersey'), region_id = (SELECT states.region_id FROM states WHERE name = 'New Jersey'), state_id = 'New Jersey';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New Mexico') * 1000 + 1,'NM', 'District of New Mexico', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New Mexico'), (SELECT states.region_id FROM states WHERE name = 'New Mexico'), 'New Mexico')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New Mexico') * 1000 + 1, name = 'District of New Mexico', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New Mexico'), region_id = (SELECT states.region_id FROM states WHERE name = 'New Mexico'), state_id = 'New Mexico';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 1, 'ENY', 'Eastern District of New York', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New York'), (SELECT states.region_id FROM states WHERE name = 'New York'), 'New York')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 1, name = 'Eastern District of New York', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New York'), region_id = (SELECT states.region_id FROM states WHERE name = 'New York'), state_id = 'New York';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 2, 'NNY', 'Northern District of New York', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New York'), (SELECT states.region_id FROM states WHERE name = 'New York'), 'New York')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 2, name = 'Northern District of New York', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New York'), region_id = (SELECT states.region_id FROM states WHERE name = 'New York'), state_id = 'New York';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 3, 'SNY', 'Southern District of New York', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New York'), (SELECT states.region_id FROM states WHERE name = 'New York'), 'New York')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 3, name = 'Southern District of New York', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New York'), region_id = (SELECT states.region_id FROM states WHERE name = 'New York'), state_id = 'New York';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 4, 'WNY', 'Western District of New York', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'New York'), (SELECT states.region_id FROM states WHERE name = 'New York'), 'New York')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='New York') * 1000 + 4, name = 'Western District of New York', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'New York'), region_id = (SELECT states.region_id FROM states WHERE name = 'New York'), state_id = 'New York';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='North Carolina') * 1000 + 1, 'ENC', 'Eastern District of North Carolina', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'North Carolina'), (SELECT states.region_id FROM states WHERE name = 'North Carolina'), 'North Carolina')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='North Carolina') * 1000 + 1, name = 'Eastern District of North Carolina', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'North Carolina'), region_id = (SELECT states.region_id FROM states WHERE name = 'North Carolina'), state_id = 'North Carolina';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='North Carolina') * 1000 + 2, 'MNC', 'Middle District of North Carolina', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'North Carolina'), (SELECT states.region_id FROM states WHERE name = 'North Carolina'), 'North Carolina')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='North Carolina') * 1000 + 2, name = 'Middle District of North Carolina', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'North Carolina'), region_id = (SELECT states.region_id FROM states WHERE name = 'North Carolina'), state_id = 'North Carolina';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='North Carolina') * 1000 + 3, 'WNC', 'Western District of North Carolina', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'North Carolina'), (SELECT states.region_id FROM states WHERE name = 'North Carolina'), 'North Carolina')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='North Carolina') * 1000 + 3, name = 'Western District of North Carolina', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'North Carolina'), region_id = (SELECT states.region_id FROM states WHERE name = 'North Carolina'), state_id = 'North Carolina';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='North Dakota') * 1000 + 1, 'ND', 'District of North Dakota', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'North Dakota'), (SELECT states.region_id FROM states WHERE name = 'North Dakota'), 'North Dakota')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='North Dakota') * 1000 + 1, name = 'District of North Dakota', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'North Dakota'), region_id = (SELECT states.region_id FROM states WHERE name = 'North Dakota'), state_id = 'North Dakota';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Ohio') * 1000 + 1, 'NOH', 'Northern District of Ohio', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Ohio'), (SELECT states.region_id FROM states WHERE name = 'Ohio'), 'Ohio')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Ohio') * 1000 + 1, name = 'Northern District of Ohio', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Ohio'), region_id = (SELECT states.region_id FROM states WHERE name = 'Ohio'), state_id = 'Ohio';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Ohio') * 1000 + 2, 'SOH', 'Southern District of Ohio', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Ohio'), (SELECT states.region_id FROM states WHERE name = 'Ohio'), 'Ohio')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Ohio') * 1000 + 2, name = 'Southern District of Ohio', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Ohio'), region_id = (SELECT states.region_id FROM states WHERE name = 'Ohio'), state_id = 'Ohio';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Oklahoma') * 1000 + 1, 'EOK', 'Eastern District of Oklahoma', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Oklahoma'), (SELECT states.region_id FROM states WHERE name = 'Oklahoma'), 'Oklahoma')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Oklahoma') * 1000 + 1, name = 'Eastern District of Oklahoma', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Oklahoma'), region_id = (SELECT states.region_id FROM states WHERE name = 'Oklahoma'), state_id = 'Oklahoma';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Oklahoma') * 1000 + 2, 'NOK', 'Northern District of Oklahoma', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Oklahoma'), (SELECT states.region_id FROM states WHERE name = 'Oklahoma'), 'Oklahoma')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Oklahoma') * 1000 + 2, name = 'Northern District of Oklahoma', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Oklahoma'), region_id = (SELECT states.region_id FROM states WHERE name = 'Oklahoma'), state_id = 'Oklahoma';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Oklahoma') * 1000 + 3, 'WOK', 'Western District of Oklahoma', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Oklahoma'), (SELECT states.region_id FROM states WHERE name = 'Oklahoma'), 'Oklahoma')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Oklahoma') * 1000 + 3, name = 'Western District of Oklahoma', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Oklahoma'), region_id = (SELECT states.region_id FROM states WHERE name = 'Oklahoma'), state_id = 'Oklahoma';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Oregon') * 1000 + 1, 'OR', 'District of Oregon', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Oregon'), (SELECT states.region_id FROM states WHERE name = 'Oregon'), 'Oregon')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Oregon') * 1000 + 1, name = 'District of Oregon', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Oregon'), region_id = (SELECT states.region_id FROM states WHERE name = 'Oregon'), state_id = 'Oregon';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Pennsylvania') * 1000 + 1, 'EPA', 'Eastern District of Pennsylvania', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Pennsylvania'), (SELECT states.region_id FROM states WHERE name = 'Pennsylvania'), 'Pennsylvania')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Pennsylvania') * 1000 + 1, name = 'Eastern District of Pennsylvania', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Pennsylvania'), region_id = (SELECT states.region_id FROM states WHERE name = 'Pennsylvania'), state_id = 'Pennsylvania';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Pennsylvania') * 1000 + 2, 'MPA', 'Middle District of Pennsylvania', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Pennsylvania'), (SELECT states.region_id FROM states WHERE name = 'Pennsylvania'), 'Pennsylvania')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Pennsylvania') * 1000 + 2, name = 'Middle District of Pennsylvania', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Pennsylvania'), region_id = (SELECT states.region_id FROM states WHERE name = 'Pennsylvania'), state_id = 'Pennsylvania';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Pennsylvania') * 1000 + 3, 'WPA', 'Western District of Pennsylvania', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Pennsylvania'), (SELECT states.region_id FROM states WHERE name = 'Pennsylvania'), 'Pennsylvania')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Pennsylvania') * 1000 + 3, name = 'Western District of Pennsylvania', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Pennsylvania'), region_id = (SELECT states.region_id FROM states WHERE name = 'Pennsylvania'), state_id = 'Pennsylvania';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Puerto Rico') * 1000 + 1, 'PR', 'District of Puerto Rico', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Puerto Rico'), (SELECT states.region_id FROM states WHERE name = 'Puerto Rico'), 'Puerto Rico')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Puerto Rico') * 1000 + 1, name = 'District of Puerto Rico', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Puerto Rico'), region_id = (SELECT states.region_id FROM states WHERE name = 'Puerto Rico'), state_id = 'Puerto Rico';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Rhode Island') * 1000 + 1, 'RI', 'District of Rhode Island', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Rhode Island'), (SELECT states.region_id FROM states WHERE name = 'Rhode Island'), 'Rhode Island')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Rhode Island') * 1000 + 1, name = 'District of Rhode Island', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Rhode Island'), region_id = (SELECT states.region_id FROM states WHERE name = 'Rhode Island'), state_id = 'Rhode Island';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='South Carolina') * 1000 + 1, 'SC', 'District of South Carolina', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'South Carolina'), (SELECT states.region_id FROM states WHERE name = 'South Carolina'), 'South Carolina')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='South Carolina') * 1000 + 1, name = 'District of South Carolina', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'South Carolina'), region_id = (SELECT states.region_id FROM states WHERE name = 'South Carolina'), state_id = 'South Carolina';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='South Dakota') * 1000 + 1, 'SD', 'District of South Dakota', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'South Dakota'), (SELECT states.region_id FROM states WHERE name = 'South Dakota'), 'South Dakota')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='South Dakota') * 1000 + 1, name = 'District of South Dakota', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'South Dakota'), region_id = (SELECT states.region_id FROM states WHERE name = 'South Dakota'), state_id = 'South Dakota';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Tennessee') * 1000 + 1, 'ETN', 'Eastern District of Tennessee', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Tennessee'), (SELECT states.region_id FROM states WHERE name = 'Tennessee'), 'Tennessee')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Tennessee') * 1000 + 1, name = 'Eastern District of Tennessee', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Tennessee'), region_id = (SELECT states.region_id FROM states WHERE name = 'Tennessee'), state_id = 'Tennessee';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Tennessee') * 1000 + 2, 'MTN', 'Middle District of Tennessee', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Tennessee'), (SELECT states.region_id FROM states WHERE name = 'Tennessee'), 'Tennessee')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Tennessee') * 1000 + 2, name = 'Middle District of Tennessee', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Tennessee'), region_id = (SELECT states.region_id FROM states WHERE name = 'Tennessee'), state_id = 'Tennessee';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Tennessee') * 1000 + 3, 'WTN', 'Western District of Tennessee', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Tennessee'), (SELECT states.region_id FROM states WHERE name = 'Tennessee'), 'Tennessee')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Tennessee') * 1000 + 3, name = 'Western District of Tennessee', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Tennessee'), region_id = (SELECT states.region_id FROM states WHERE name = 'Tennessee'), state_id = 'Tennessee';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 1, 'ETX', 'Eastern District of Texas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Texas'), (SELECT states.region_id FROM states WHERE name = 'Texas'), 'Texas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 1, name = 'Eastern District of Texas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Texas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Texas'), state_id = 'Texas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 2, 'NTX', 'Northern District of Texas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Texas'), (SELECT states.region_id FROM states WHERE name = 'Texas'), 'Texas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 2, name = 'Northern District of Texas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Texas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Texas'), state_id = 'Texas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 3, 'STX', 'Southern District of Texas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Texas'), (SELECT states.region_id FROM states WHERE name = 'Texas'), 'Texas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 3, name = 'Southern District of Texas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Texas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Texas'), state_id = 'Texas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 4, 'WTX', 'Western District of Texas', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Texas'), (SELECT states.region_id FROM states WHERE name = 'Texas'), 'Texas')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Texas') * 1000 + 4, name = 'Western District of Texas', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Texas'), region_id = (SELECT states.region_id FROM states WHERE name = 'Texas'), state_id = 'Texas';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Utah') * 1000 + 1, 'UT', 'District of Utah', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Utah'), (SELECT states.region_id FROM states WHERE name = 'Utah'), 'Utah')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Utah') * 1000 + 1, name = 'District of Utah', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Utah'), region_id = (SELECT states.region_id FROM states WHERE name = 'Utah'), state_id = 'Utah';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Vermont') * 1000 + 1, 'VT', 'District of Vermont', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Vermont'), (SELECT states.region_id FROM states WHERE name = 'Vermont'), 'Vermont')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Vermont') * 1000 + 1, name = 'District of Vermont', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Vermont'), region_id = (SELECT states.region_id FROM states WHERE name = 'Vermont'), state_id = 'Vermont';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Virginia') * 1000 + 1, 'EVA', 'Eastern District of Virginia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Virginia'), (SELECT states.region_id FROM states WHERE name = 'Virginia'), 'Virginia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Virginia') * 1000 + 1, name = 'Eastern District of Virginia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Virginia'), region_id = (SELECT states.region_id FROM states WHERE name = 'Virginia'), state_id = 'Virginia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Virginia') * 1000 + 2, 'WVA', 'Western District of Virginia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Virginia'), (SELECT states.region_id FROM states WHERE name = 'Virginia'), 'Virginia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Virginia') * 1000 + 2, name = 'Western District of Virginia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Virginia'), region_id = (SELECT states.region_id FROM states WHERE name = 'Virginia'), state_id = 'Virginia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Washington') * 1000 + 1, 'EWA', 'Eastern District of Washington', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Washington'), (SELECT states.region_id FROM states WHERE name = 'Washington'), 'Washington')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Washington') * 1000 + 1, name = 'Eastern District of Washington', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Washington'), region_id = (SELECT states.region_id FROM states WHERE name = 'Washington'), state_id = 'Washington';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Washington') * 1000 + 2, 'WWA', 'Western District of Washington', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Washington'), (SELECT states.region_id FROM states WHERE name = 'Washington'), 'Washington')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Washington') * 1000 + 2, name = 'Western District of Washington', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Washington'), region_id = (SELECT states.region_id FROM states WHERE name = 'Washington'), state_id = 'Washington';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='West Virginia') * 1000 + 1, 'NWV', 'Northern District of West Virginia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'West Virginia'), (SELECT states.region_id FROM states WHERE name = 'West Virginia'), 'West Virginia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='West Virginia') * 1000 + 1, name = 'Northern District of West Virginia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'West Virginia'), region_id = (SELECT states.region_id FROM states WHERE name = 'West Virginia'), state_id = 'West Virginia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='West Virginia') * 1000 + 2, 'SWV', 'Southern District of West Virginia', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'West Virginia'), (SELECT states.region_id FROM states WHERE name = 'West Virginia'), 'West Virginia')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='West Virginia') * 1000 + 2, name = 'Southern District of West Virginia', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'West Virginia'), region_id = (SELECT states.region_id FROM states WHERE name = 'West Virginia'), state_id = 'West Virginia';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Wisconsin') * 1000 + 1, 'EWI', 'Eastern District of Wisconsin', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Wisconsin'), (SELECT states.region_id FROM states WHERE name = 'Wisconsin'), 'Wisconsin')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Wisconsin') * 1000 + 1, name = 'Eastern District of Wisconsin', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Wisconsin'), region_id = (SELECT states.region_id FROM states WHERE name = 'Wisconsin'), state_id = 'Wisconsin';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Wisconsin') * 1000 + 2, 'WWI', 'Western District of Wisconsin', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Wisconsin'), (SELECT states.region_id FROM states WHERE name = 'Wisconsin'), 'Wisconsin')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Wisconsin') * 1000 + 2, name = 'Western District of Wisconsin', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Wisconsin'), region_id = (SELECT states.region_id FROM states WHERE name = 'Wisconsin'), state_id = 'Wisconsin';

INSERT INTO districts (districtId, districtCode, name, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, region_id, state_id)
VALUES ((SELECT rmp.states.stateId FROM rmp.states WHERE name='Wyoming') * 1000 + 1, 'WY', 'District of Wyoming', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT states.aor_id FROM states WHERE name = 'Wyoming'), (SELECT states.region_id FROM states WHERE name = 'Wyoming'), 'Wyoming')
ON DUPLICATE KEY UPDATE districtId = (SELECT rmp.states.stateId FROM rmp.states WHERE name='Wyoming') * 1000 + 1, name = 'District of Wyoming', centroidX = 0.0, centroidY = 0.0, bboxXY1 = 0.0, bboxXY2 = 0.0, bboxXY3 = 0.0, bboxXY4 = 0.0, aor_id = (SELECT states.aor_id FROM states WHERE name = 'Wyoming'), region_id = (SELECT states.region_id FROM states WHERE name = 'Wyoming'), state_id = 'Wyoming';

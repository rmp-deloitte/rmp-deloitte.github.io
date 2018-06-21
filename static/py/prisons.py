import csv

with open('./devenv/static/csv/prisons.csv') as c:
    csvfile = csv.reader(c, delimiter='\t')

    queryBuffer = []
    i = 0
    for row in csvfile:
        if i:
            queryBuffer.append(
                "INSERT INTO prisons (prisonId, name, type, capacity, population, status, securityLevel, address, telephone, zipcode, latitude, longitude, aor_id, region_id, state_id)\n" +
                "VALUES (" + row[1] + ", '" + ''.join(row[2].split("'")) + "', '" + row[10] + "', " + row[24] + ", " + row[12] + ", '" + row[11] + "', '" + row[23] + "', '" + row[4] + "', '" + row[9] + "', '" + row[7] + "', 0.0, 0.0, (SELECT aor_id FROM states WHERE abbv = '" + row[6]  + "' LIMIT 1), (SELECT region_id FROM states WHERE abbv = '" + row[6] + "' LIMIT 1), (SELECT name FROM states WHERE states.abbv = '" + row[6] + "' LIMIT 1))\n" +
                "ON DUPLICATE KEY UPDATE name = '" + ''.join(row[2].split("'")) + "', type = '" + row[10] + "', capacity = " + row[24] + ", population = " + row[12] + ", status = '" + row[11] + "', securityLevel = '" + row[23] +  "', address = '" + row[4] + "', telephone = '" + row[9] + "', zipcode = '" + row[7] + "', latitude = 0.0, longitude = 0.0;\n\n"
            )
        else:
            i = 1

with open('./scripts/prisons.sql', 'w') as f:
    for elem in queryBuffer:
        f.write(elem)

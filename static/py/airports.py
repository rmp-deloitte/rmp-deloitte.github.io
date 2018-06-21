import csv

with open('./devenv/static/csv/airports.csv', encoding='utf-8') as c:
    csvfile = csv.reader(c, delimiter=',')

    buffer = [row for row in csvfile if row[8] == "US"]
    queryBuffer = []
    for elem in buffer:
        code = elem[0]
        stabbv =  elem[9].split("-")[-1]
        municipality = ''.join(elem[10].split("'"))
        latitude = elem[4]
        longitude = elem[5]
        name = ''.join(elem[3].split("'"))
        queryBuffer.append(
            """
            INSERT INTO airports (code, name, stabbv, latitude, longitude, aor_id, region_id, state_id)
            VALUES (%s, '%s', '%s', %s, %s, (SELECT aor_id FROM states WHERE abbv = '%s' LIMIT 1),  (SELECT region_id FROM states WHERE abbv = '%s' LIMIT 1), (SELECT name FROM states WHERE states.abbv = '%s' LIMIT 1))
            ON DUPLICATE KEY UPDATE name = '%s', stabbv = '%s', latitude = %s, longitude = %s, aor_id = (SELECT aor_id FROM states WHERE abbv = '%s' LIMIT 1), region_id = (SELECT region_id FROM states WHERE abbv = '%s' LIMIT 1), state_id = (SELECT name FROM states WHERE states.abbv = '%s' LIMIT 1);
            """ % (code, name, stabbv, latitude, longitude, stabbv, stabbv, stabbv, name, stabbv, latitude, longitude, stabbv, stabbv, stabbv)
        )
with open('./scripts/airports.sql', 'w') as f:
    for elem in queryBuffer:
        f.write(elem)

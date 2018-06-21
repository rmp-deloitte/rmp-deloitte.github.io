import csv, random

with open('./meeseeks/static/csv/us_postal_codes.csv', encoding='UTF-8') as csvfile:
    c = csv.reader(csvfile)

    queryBuffer = []

    i = 0
    for row in c:
        if i:
            name = row[1]
            if len(row[0]) == 3:
                zipcode = "00%s" % row[0]
            elif len(row[0]) == 4:
                zipcode = "0%s" % row[0]
            else:
                zipcode = row[0]
            latitude = row[5]
            longitude = row[6]
            stabbv = row[3]
            state = row[2]
            county = row[4]

            queryBuffer.append(
                """
                INSERT INTO cities (cityId, name, zipcode, latitude, longitude, aor_id, county_id, district_id, region_id, state_id)
                VALUES ('%s', '%s', '%s', %s, %s, (SELECT rmp.counties.aor_id FROM rmp.counties WHERE rmp.counties.name = '%s' LIMIT 1), (SELECT rmp.counties.countyId FROM rmp.counties WHERE rmp.counties.name = '%s' LIMIT 1), (SELECT rmp.counties.district_id FROM rmp.counties WHERE rmp.counties.name = '%s' and rmp.counties.state_id = '%s' LIMIT 1), (SELECT rmp.counties.region_id FROM rmp.counties WHERE rmp.counties.name = '%s' LIMIT 1), '%s')
                ON DUPLICATE KEY UPDATE name = '%s', zipcode = '%s', latitude = %s, latitude = %s, aor_id = (SELECT rmp.counties.aor_id FROM rmp.counties WHERE rmp.counties.name = '%s' LIMIT 1), county_id = (SELECT rmp.counties.countyId FROM rmp.counties WHERE rmp.counties.name = '%s' LIMIT 1), district_id = (SELECT rmp.counties.district_id FROM rmp.counties WHERE rmp.counties.name = '%s' and rmp.counties.state_id = '%s' LIMIT 1), region_id = (SELECT rmp.counties.region_id FROM rmp.counties WHERE rmp.counties.name = '%s' LIMIT 1), state_id = '%s';
                """ % (zipcode, name, zipcode, latitude, longitude, county, county, county, state, county, state, name, zipcode, latitude, longitude, county, county, county, state, county, state)
            )
        else:
            i = 1

with open('./scripts/cities.sql', 'w') as f:
    for elem in queryBuffer:
        f.write(elem)

with open('./meeseeks/static/csv/national_county.csv', encoding='UTF-8') as csvfile:
    c = csv.reader(csvfile)
    queryBuffer = []
    i = 0
    for row in c:
        if row[0] not in set(['VI', 'MP', 'AS', 'UM', 'GU']) and i:
            if 'County' in row[3]:
                countyname = ''.join(row[3].split(" County")[:-1])
                countytype = row[3].split(" ")[-1]
            elif 'Census Area' in row[3]:
                countyname = ''.join(row[3].split(" Census Area")[:-1])
                countytype = ' '.join(row[3].split(" ")[-2:])
            elif 'Municipality' in row[3]:
                countyname = ''.join(row[3].split(" Municipality")[:-1])
                countytype = row[3].split(" ")[-1]
            elif 'Borough' in row[3]:
                countyname = ''.join(row[3].split(" Borough")[:-1])
                countytype = row[3].split(" ")[-1]
            elif 'Parish' in row[3]:
                countyname = ''.join(row[3].split(" Parish")[:-1])
                countytype = row[3].split(" ")[-1]
            elif 'District' in row[3]:
                if countyname == 'District of Columbia':
                    countyname = row[3]
                    countytype = 'District'
                else:
                    countyname = ''.join(row[3].split(" District")[:-1])
                    countytype = row[3].split(" ")[-1]

            # print(countytype)
            stabbv = row[0]
            stfips = row[1]
            countyfips = int(stfips) * 1000 + int(row[2])
            districtcode = "''"

            MAL_DISTRICT = set(['Autauga', 'Barbour', 'Bullock', 'Butler', 'Chambers', 'Chilton', 'Coffee', 'Coosa', 'Covington', 'Crenshaw', 'Dale', 'Elmore', 'Geneva', 'Henry', 'Houston', 'Lee', 'Lowndes', 'Macon', 'Montgomery', 'Pike', 'Randolph', 'Russell', 'Tallapoosa',])
            NAL_DISTRICT = set(['Blount', 'Calhoun', 'Cherokee', 'Clay', 'Cleburne', 'Colbert', 'Cullman', 'Dekalb', 'Etowah', 'Fayette', 'Franklin', 'Greene', 'Jackson', 'Jefferson', 'Lamar', 'Lauderdale', 'Lawrence', 'Limestone', 'Madison', 'Marion', 'Marshall', 'Morgan', 'Pickens', 'Shelby', 'St. Clair', 'Sumter', 'Talladega', 'Tuscaloosa', 'Walker', 'Winston'])
            SAL_DISTRICT = set(['Baldwin', 'Choctaw', 'Clarke', 'Conecuh', 'Dallas', 'Escambia', 'Hale', 'Marengo', 'Mobile', 'Monroe', 'Perry', 'Washington', 'Wilcox'])
            AK_DISTRICT = set(['Aleutians East', 'Aleutians West', 'Anchorage', 'Bethel', 'Bristol Bay', 'Denali', 'Dillingham', 'Fairbanks North Star', 'Haines', 'Hoonah-Angoon', 'Juneau', 'Kenai Peninsula', 'Ketchikan Gateway', 'Kodiak Islan', 'Lake and Peninsula', 'Matanuska-Susitna', 'Nome', 'North Slope', 'Northwest Artic', 'Petersburg', 'Prince of Wales-Hyder', 'Sitka', 'Skagway', 'Southeast Fairbanks', 'Valdez-Cordova', 'Wade Hampton', 'Wrangell', 'Yakutat', 'Yukon-Koyukuk'])
            AZ_DISTRICT = set(['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa', 'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma'])
            EAR_DISTRICT = set(['Arkansas', 'Chicot', 'Clay', 'Cleburne', 'Cleveland', 'Conway', 'Craighead', 'Crittenden', 'Cross', 'Dallas', 'Desha', 'Drew', 'Faulkner', 'Fulton', 'Grant', 'Greene', 'Independence', 'Izard', 'Jackson', 'Jefferson', 'Lawrence', 'Lee', 'Lincoln', 'Lonoke', 'Mississippi', 'Monroe', 'Perry', 'Phillips', 'POinsett', 'Pope', 'Prairie', 'Pulaski', 'Randolph', 'Saline', 'Sharp', 'St. Francis', 'Stone', 'Van Buren', 'White', 'Woodruff', 'Yell'])
            WAR_DISTRICT = set(['Ashley', 'Baxter', 'Benton', 'Boone', 'Bradley', 'Calhoun', 'Carroll', 'Clark', 'Columbia', 'Crawford', 'Franklin', 'Garland', 'Hempstead', 'Hot Spring', 'Howard', 'Johnson', 'LaFayette', 'Little River', 'Logan', 'Madison', 'Marion', 'Miller', 'Montgomery', 'Nevada', 'Newton', 'Ouachita', 'Pike', 'Polk', 'Scott', 'Searcy', 'Sebastian', 'Sevier', 'Union', 'Washington'])
            CCA_DISTRICT = set(['Los Angeles', 'Orange', 'Riverside', 'San Bernadino', 'San Luis Obispo', 'Santa Barbara', 'Ventrua'])
            ECA_DISTRICT = set(['Alpine', 'Amador', 'Butte', 'Calaveras', 'Colusa', 'El Dorado', 'Fresno', 'Glenn', 'Inyo', 'Kern', 'Kings', 'Lassen', 'Madera', 'Mariposa', 'Merced', 'Modoc', 'Mono', 'Nevada', 'Placer', 'Plumas', 'Sacramento', 'San Joaquin', 'Shasta', 'Sierra', 'Siskiyou', 'Solano', 'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Tulare', 'Toulumne', 'Yolo', 'Yuba',])
            NCA_DISTRICT = set(['Alameda', 'Contra Costa', 'Del Norte', 'Humboldt', 'Lake', 'Marin', 'Mendocino', 'Monterey', 'Napa', 'San Benito', 'San Francisco', 'San Mateo', 'Santa Clara', 'Santa Cruz', 'Sonoma',])
            SCA_DISTRICT = set(['Imperial', 'San Diego'])
            CO_DISTRICT = set(['Adams', 'Alamosa', 'Arapahoe', 'Archuleta', 'Baca', 'Bent', 'Boulder', 'Broomfield', 'Chaffee', 'Cheyenne', 'Clear Creek', 'Conejos', 'Costilla', 'Crowley', 'Custer', 'Delta', 'Denver', 'Dolores', 'Douglas', 'Eagle', 'El Paso', 'Elbert', 'Fremont', 'Garfield', 'Gilpin', 'Grand', 'Gunnison', 'Hinsdale', 'Huerfano', 'Jackson', 'Jefferson', 'Kiowa', 'Kit Carson', 'La Plata', 'Lake', 'Larimer', 'Las Animas', 'Lincoln', 'Logan', 'Mesa', 'Mineral', 'Moffat', 'Montezuma', 'Montrose', 'Morgan', 'Otero', 'Ouray', 'Park', 'Phillips', 'Pitkin', 'Prowers', 'Pueblo', 'Rio Blanco', 'Rio Grande', 'Routt', 'Saguache', 'San Juan', 'San Miguel', 'Sedgwick', 'Summit', 'Teller', 'Washington', 'Weld', 'Yuma'])
            CT_DISTRICT = set(['Fairfield', 'Hartford', 'Litchfield', 'Middlesex', 'New Haven', 'New Longdon', 'Tolland', 'Windham'])
            DE_DISTRICT = set(['Kent', 'New Castle', 'Sussex'])
            DC_DISTRICT = set(['District of Columbia'])
            MFL_DISTRICT = set(['Baker', 'Bradford', 'Brevard', 'Charlotte', 'Citrus', 'Clay', 'Collier', 'Columbia', 'Desoto', 'Duval', 'Flagler', 'Galdes', 'Hamilton', 'Hardee', 'Hendry', 'Hernando', 'Hillsborough', 'Lake', 'Lee', 'Manatee', 'Marion', 'Nassau', 'Orange', 'Osceloa', 'Pasco', 'Pinellas', 'Polk', 'Putnam', 'Sarasoa', 'Seminole', 'St. Johns', 'Sumter', 'Suwanne', 'Union', 'Volusia',])
            NFL_DISTRICT = set(['Alachua', 'Bay', 'Calhoun', 'Dixie', 'Escambia', 'Franklin', 'Gadsden', 'Gilchrist', 'Gulf', 'Holmes', 'Jackson', 'Jefferson', 'LaFayette','Lon', 'Levy', 'Liberty', 'Madison', 'Okaloosa', 'Santa Rosa', 'Taylor', 'Wakulla', 'Walton', 'Washington', ])
            SFL_DISTRICT = set(['Broward', 'Highlands', 'Indian River', 'Martin', 'Miami-Dade', 'Monroe', 'Okeechobee', 'Palm Beach', 'St. Lucie',])
            MGA_DISTRICT = set(['Baker', 'Baldwin', 'Ben Hill', 'Berrien', 'Bibb', 'Blecklety', 'Brooks', 'Butts', 'Calhoun', 'Chattahoochee', 'Clarke', 'Clay', 'Clinch', 'Colquitt', 'Cook', 'Crawford', 'Crisp', 'Decatur', 'Dooly', 'Dougherty', 'Early', 'Echols', 'Elbert', 'Franklin', 'Grady', 'Greene', 'Hancock', 'Harris', 'Hart', 'Houston', 'Irwin', 'Jasper', 'Jones', 'Lamar', 'Lanier', 'Lee', 'Lowndes', 'Macon', 'Madison', 'Marion', 'Miller', 'Mitchell', 'Monroe', 'Morgan', 'Muscogee', 'Oconee', 'Oglethorpe', 'Peach', 'Pulaski', 'Putnam', 'Quitman', 'Randolph', 'Schley', 'Seminole', 'Stewart', 'Sumter', 'Talbot', 'Taylor', 'Terrell', 'Thomas', 'Tift', 'Turner', 'Twiggs', 'Upson', 'Walton', 'Washington', 'Webster', 'Wilcox', 'Wilkinson', 'Worth',])
            NGA_DISTRICT = set(['Banks', 'Barrow', 'Bartow', 'Carroll', 'Catoosa', 'Chattooga', 'Cherokee', 'Clayton', 'Cobb', 'Coweta', 'Dade', 'Dawson', 'Dekalb', 'Douglas', 'Fannin', 'Fayeet', 'Floyd', 'Forsyth', 'Fulton', 'Gilmer', 'Gordon', 'Gwinnett', 'Habersham', 'Hall', 'Haralson', 'Heard', 'Henry', 'Jackson', 'Lumpkin', 'Meriwether', 'Murray', 'Newton', 'Paulding', 'Pickens', 'Pike', 'Polk', 'Rabun', 'Rockdale', 'Spalding', 'Stephens', 'Towns', 'Troup', 'Union', 'Walker', 'White', 'Whitefield'])
            SGA_DISTRICT = set(['Appling', 'Atkinson', 'Bacon', 'Brantley', 'Bryan', 'Bulloch', 'Burke', 'Camden', 'Candler', 'Charlton', 'Chatham', 'Coffee', 'Columbia', 'Dodge', 'Effingham', 'Emanuel', 'Evans', 'Glascock', 'Glynn', 'Jeff Davis', 'Jefferson', 'Jenkins', 'Johnson', 'Laurens', 'Liberty', 'Lincoln', 'Long', 'McDuffie', 'McIntosh', 'Montgomery', 'Pierce', 'Richmond', 'Screven', 'Taliaferro', 'Tattnall', 'Telfair', 'Toombs', 'Treutlen', 'Ware', 'Warren', 'Wayne', 'Wheeler', 'Wilkes'])
            HI_DISTRICT = set(['Hawaii', 'Honolulu', 'Kalawao', 'Kauai', 'Maui',])
            ID_DISTRICT = set(['Ada', 'Adams', 'Bannock', 'Bear Lake', 'Benewah', 'Bingham', 'Blaine', 'Boise', 'Bonner', 'Bonneville', 'Boundary', 'Butte', 'Camas', 'Canyon', 'Caribou', 'Cassia', 'Clark', 'Clearwater', 'Custer', 'Elmore', 'Franklin', 'Fremont', 'Gem', 'Gooding', 'Idaho', 'Jefferson', 'Jerome', 'Kootenai', 'Latai', 'Lemhi', 'Lewis', 'Lincoln', 'Madison', 'Minidoka', 'Nez Perce', 'Oneida', 'Owyhee', 'Payette', 'Power', 'Shoshone', 'Teton', 'Twin Falls', 'Valley', 'Washington',])
            CIL_DISTRICT = set(['Adams', 'Brown', 'Bureau', 'Cass', 'Champaign', 'Christian', 'Coles', 'De Witt', 'Douglas', 'Edgar', 'Ford', 'Fulton', 'Greene', 'Hancock', 'Henderson', 'Henry', 'Iroquois', 'Kankakee', 'Knowx', 'Livingston', 'Logan', 'Macon', 'Macoupin', 'Marshall', 'Mason', 'McDonough', 'McLean', 'Menard', 'Mercer', 'Montgomery', 'Morgan', 'Moultrie', 'Peoria', 'Piatt', 'Pike', 'Putnam', 'Rock Island', 'Sangamon', 'Schuyler', 'Scott', 'Shelby', 'Stark', 'Tazewell', 'Vermilion', 'Warren', 'Woodford',])
            NIL_DISTRICT = set(['Boone', 'Carroll', 'Cook', 'Dekalb', 'Dupage', 'Grundy', 'Jo Daviess', 'Kane', 'Kendall', 'La Salle', 'Lake', 'Lee', 'McHenry', 'Ogle', 'Stephenson', 'Whiteside', 'Will', 'Winnebago',])
            SIL_DISTRICT = set(['Alexander', 'Bond', 'Calhoun', 'Clark', 'Clay', 'Clinton', 'Crawford', 'Cumberland', 'Edwards', 'Effingham', 'Fayette', 'Franklin', 'Gallatin', 'Hamilton', 'Hardin', 'Jackson', 'Jasper', 'Jefferson', 'Jersey', 'Johnson', 'Lawrence', 'Madison', 'Marion', 'Massac', 'Monroe', 'Perry', 'Pope', 'Pulaski', 'Randolph', 'Richland', 'Saline', 'St. Clair', 'Union', 'Wabash', 'Washington', 'Wayne', 'White', 'Williamson',])
            NIN_DISTRICT = set(['Adams', 'Allen', 'Benton', 'Blackford', 'Carroll', 'Cass', 'Dekalb', 'Elkhart', 'Fulton', 'Grant', 'Huntington', 'Jasper', 'Jay', 'Kosciusko', 'LaGrange', 'Lake', 'LaPorte', 'Marshall', 'Miami', 'Newton', 'Noble', 'Porter', 'Pulaski', 'St. Joseph', 'Starke', 'Steuben', 'Tippecanoe', 'Wabash', 'Warren', 'Wells', 'White', 'Whitley'])
            SIN_DISTRICT = set(['Bartholomew', 'Boone', 'Brown', 'Clark', 'Clay', 'Clinton', 'Crawford', 'Daviess', 'Dearborn', 'Decatur', 'Delaware', 'DuBois', 'Fayette', 'Floyd', 'Fountain', 'Franklin', 'Gibson', 'Greene', 'Hamilton', 'Hancock', 'Harrison', 'Hendricks', 'Henry', 'Howard', 'Jackson', 'Jefferson', 'Jennings', 'Johnson', 'Knox', 'Lawrence', 'Madison', 'Marion', 'Martin', 'Monroe', 'Montgomery', 'Morgan', 'Ohio', 'Orange', 'Owen', 'Parke', 'Perry', 'Pike', 'Posey', 'Putnam', 'Randolph', 'Ripley', 'Rush', 'Scott', 'Shelby', 'Spencer', 'Sullivan', 'Switzerland', 'Tipton', 'Union', 'Vanderburgh', 'Vermillion', 'Vigo', 'Warrick', 'Washington', 'Wayne',])
            NIA_DISTRICT = set(['Allamakee', 'Benton', 'Black Hawk', 'Bremer', 'Buchanan', 'Buena Vista', 'Butler', 'Calhoun', 'Carroll', 'Cedar', 'Cerro Gordo', 'Cherokee', 'Chickasaw', 'Clay', 'Clayton', 'Crawford', 'Delaware', 'Dickinson', 'Dubuque', 'Emmet', 'Fayette', 'Floyd', 'Franklin', 'Grundy', 'Hamilton', 'Hancock', 'Hardin', 'Howard', 'Humboldt', 'Ida', 'Iowa', 'Jackson', 'Jones', 'Kossuth', 'Linn', 'Lyon', 'Mitchell', 'Monona', 'O\'Brien', 'Oscel=ola', 'Palo Alto', 'Plymouth', 'Pocahontas', 'Sac', 'Sioux', 'Tama', 'Webster', 'Winnebago', 'Winneshiek', 'Woodbury', 'Worth', 'Wright',])
            SIA_DISTRICT = set(['Adair', 'Adams', 'Appanoose', 'Audubon', 'Boone', 'Cass', 'Clarke', 'Clinton', 'Dallas', 'Davis', 'Decatur', 'Des Moines', 'Fremont', 'Greene', 'Guthrie', 'Harrison', 'Henry', 'Jasper', 'Jefferson', 'Johnson', 'Keokuk', 'Lee', 'Louisa', 'Lucas', 'Madison', 'Mahaska', 'Marion', 'Marshall', 'Mills', 'Monroe', 'Montgomery', 'Muscatine', 'Page', 'Polk', 'Pottawattamie', 'Poweshiek', 'Ringgold', 'Scott', 'Shelby', 'Story', 'Taylor', 'Union', 'Van Buren', 'Wapello', 'Warren', 'Washington', 'Wayne',])
            KS_DISTRICT = set(['Allen', 'Anderson', 'Atchinson', 'Barber', 'Bourbon', 'Brown', 'Butler', 'Chase', 'Chautauqua', 'Cherokee', 'Cheyenne', 'Clark', 'Clay', 'Cloud', 'Coffey', 'Comanche', 'Cowley', 'Crawford', 'Decatur', 'Dickinson', 'Doniphan', 'Douglas', 'Edwards', 'Elk', 'Ellis', 'Ellsworth', 'Finney', 'Ford', 'Franklin', 'Geary', 'Gove', 'Graham', 'Grant', 'Grant', 'Gray', 'Greeley', 'Greenwood', 'Hamilton', 'Harper', 'Harvey', 'Haskell', 'Hodgeman', 'Jackson', 'Jefferson', 'Jewell', 'Johnson', 'Kearny', 'Kingman', 'Kiowa', 'Labette', 'Lane', 'Leavenworth', 'Lincoln', 'Linn', 'Logan', 'Lyon', 'Marion', 'Marshall', 'McPherson', 'Meade', 'Miami', 'Mitchell', 'Montgomery', 'Morris', 'Morton', 'Nemaha', 'Neosho', 'Ness', 'Norton', 'Osage', 'Osborne', 'Ottawa', 'Pawnee', 'Phillips', 'Pottawatomie', 'Pratt', 'Rawlins', 'Reno', 'Republic', 'Reno', 'Riley', 'Rooks', 'Rush', 'Russell', 'Saline', 'Scott', 'Sedgwick', 'Seward', 'Shawnee', 'Sheridan', 'Sherman', 'Smith', 'Stafford', 'Stanton', 'Stevens', 'Sumner', 'Thomas', 'Trego', 'Wabaunsee', 'Wallace', 'Washington', 'Wichita', 'Wilson', 'Woodson', 'Wyandotte',])
            EKY_DISTRICT = set(['Anderson', 'Bath', 'Bell', 'Boone', 'Bourne', 'Boyd', 'Bracken', 'Breathitt', 'Campbell', 'Carroll', 'Carter', 'Clark', 'Clay', 'Elliott', 'Estill', 'Fayette', 'Fleming', 'Floyd', 'Franklin', 'Gallatin', 'Garrard', 'Grant', 'Greenup', 'Harlan', 'Harrison', 'Henry', 'Jackson', 'Jessamine', 'Johnson', 'Kenton', 'Knott', 'Knox', 'Laurel', 'Lawrence', 'Lee', 'Leslie', 'Letcher', 'Lewis', 'Lincoln', 'Madison', 'Magoffin', 'Martin', 'Mason', 'McCreary', 'Menifee', 'Mercer', 'Montgomery', 'Morgan', 'Nicholas', 'Owen', 'Owsley', 'Pendleton', 'Perry', 'Pike', 'Powell', 'Pulaski', 'Robertson', 'Rockcastle', 'Rowan', 'Scott', 'Shelby', 'Trimble', 'Wayne', 'Whitley', 'Wolfe', 'Woodford',])
            WKY_DISTRICT = set(['Adair', 'Allen', 'Ballard', 'Barren', 'Breckinridge', 'Bullitt', 'Butler', 'Caldwell', 'Calloway', 'Carlisle', 'Casey', 'Christian', 'Clinton', 'Crittenden', 'Cumberland', 'Daviess', 'Edmonson', 'Fulton', 'Graves', 'Green', 'Hancock', 'Hardin', 'Hart', 'Henderson', 'Hickman', 'Hopkins', 'Jefferson', 'Larue', 'Livingston', 'Logan', 'Lyon', 'Marion','Marshall','McCracken', 'McLean', 'Meade', 'Metcalfe', 'Monroe', 'Muhlenberg', 'Nelson', 'Ohio', 'Oldham', 'Russell', 'Simpson', 'Spencer', 'Taylor', 'Todd', 'Trigg', 'Union', 'Warren', 'Washington', 'Webster', ])
            ELA_DISTRICT = set(['Assumption', 'Jefferson', 'LaFourche', 'Orleans', 'Plaquemines', 'St. John The Baptist', 'St. Bernard', 'St. Charles', 'St. James', 'St. Tammany', 'Tangipahoa', 'Terrebonne', 'Washington',])
            MLA_DISTRICT = set(['Ascension', 'East Baton Rouge', 'East Feliciana', 'Iberville', 'Livingston', 'Pointe Coupee', 'St. Helena', 'West Baton Rouge', 'West Feliciana',])
            WLA_DISTRICT = set(['Acadia', 'Allen', 'Avoyelles', 'Beauregard', 'Bienville', 'Boosier', 'Caddo', 'Calcasieu', 'Caldwell', 'Cameron', 'Catahoula', 'Claiborne', 'Concordia', 'De Soto', 'East Carroll', 'Evangeline', 'Franklin', 'Grant', 'Iberia', 'Jackson', 'Jefferson Davis', 'La Salle', 'LaFayette', 'Lincoln', 'Madison', 'Morehouse', 'Natchitoches', 'Ouachita', 'Rapides', 'Red River', 'Richland', 'Sabine', 'St. Landry', 'St. Martin', 'St. Mary', 'Tensas', 'Union', 'Vermilion', 'Vernon', 'Vernon', 'Webster', 'West Carroll', 'Winn',])
            ME_DISTRICT = set(['Androscoggin', 'Aroostook', 'Cumberland', 'Franklin', 'Hancock', 'Kennebec', 'Knox', 'Lincoln', 'Oxford', 'Penobscot', 'Piscataquis', 'Sagadahoc', 'Waldo', 'Washington', 'York',])
            MD_DISTRICT = set(['Allegany', 'Anne Arundel', 'Baltimore City', 'Baltimore County', 'Baltimore', 'Calvert', 'Caroline', 'Carroll', 'Cecil', 'Charles', 'Dorchestor', 'Frederick', 'Garrett', 'Harford', 'Howard', 'Kent', 'Montgomery', 'Prince George\'s', 'Queen Anne\'s', 'Somerset', 'St. Mary\'s', 'Talbot', 'Washington','Wicomico', 'Worcester',])
            MA_DISTRICT = set(['Barnstable', 'Berkshire', 'Bristol', 'Dukes', 'Essex', 'Franklin', 'Hampden', 'Hampshire', 'Middlesex', 'Nantucket', 'Norfolk', 'Plymouth', 'Suffolk', 'Worcester',])
            EMI_DISTRICT = set(['Alcona', 'Alpena', 'Arenac', 'Bay', 'Cheboygan', 'Clare', 'Crawford', 'Genesee', 'Gladwin', 'Gratiot', 'Huron', 'Iosco', 'Isabella', 'Jackson', 'Lapeer', 'Lenawee', 'Livingston', 'Macomb', 'Midland', 'Monroe', 'Montgomery', 'Oakland', 'Ogemaw', 'Oscoda', 'Ostego', 'Presque Isle', 'Roscommon', 'Saginaw', 'Sanilac', 'Shiawassee', 'St. Clair', 'Tuscola', 'Washtenaw', 'Wayne', ])
            WMI_DISTRICT = set(['Alger', 'Allegan', 'Antrim', 'Baraga', 'Barry', 'Benzie', 'Berrien', 'Branch', 'Calhoun', 'Cass', 'Charlevoix', 'Chippewa', 'Clinton', 'Delta', 'Dickinson', 'Eaton', 'Emmet', 'Gogebic', 'Grand Traverse', 'Hillsdale', 'Houghton', 'Ingham', 'Ionia', 'Kalamazoo', 'Kalkaska', 'Kent', 'Keweenaw', 'Lake', 'Leelanau', 'Luce', 'Mackinac', 'Manistee', 'Marquette', 'Mason', 'Mecosta', 'Menominee', 'Missaukee', 'Montcalm', 'Muskegon', 'Newaygo', 'Oceana', 'Ontonagon', 'Osceola', 'Ottawa', 'Schoolcraft', 'Van Buren', 'Wexford',])
            MN_DISTRICT = set(['Atkin', 'Anoka', 'Becker', 'Beltrami', 'Benton', 'Big Stone', 'Blue Earth', 'Brown', 'Carlton', 'Carver', 'Cass', 'Chippewa', 'Chisago', 'Clay', 'Clearwater', 'Cook', 'Cottonwood', 'Crow Wing', 'Dakota', 'Dodge', 'Douglas', 'Faribault', 'Fillmore', 'Freeborn', 'Goodhue', 'Grant', 'Hennepin', 'Houston', 'Hubbard', 'Isanti', 'Itaska', 'Jackson', 'Kanabec', 'Kandiyohi', 'Kittson', 'Koochiching', 'Lac Qui Parle', 'Lake', 'Lake of the Woods', 'Le Sueur', 'Lincoln', 'Lyon', 'Mahnomen', 'Marshall', 'Martin', 'McLeod', 'Meeker', 'Mille Lacs', 'Morrison', 'Mower', 'Murray', 'Nicollet', 'Nobles', 'Norman', 'Olmsted', 'Otter Tail', 'Pennington', 'Pine', 'Pipestone', 'Polk', 'Pope', 'Ramsey', 'Red Lake', 'Redwood', 'Renville', 'Rice', 'Rock', 'Roseau', 'Scott', 'Sherburne', 'Sibley', 'St. Louis', 'Stearns', 'Steele', 'Stevens', 'Swift', 'Todd', 'Traverse', 'Wabasha', 'Wadena', 'Waseca', 'Washington', 'Watonwan', 'Wilkin', 'Wilkin', 'Winona', 'Wright', 'Yellow Medicine',])
            NMS_DISTRICT = set(['Alcorn', 'Attala', 'Benton', 'Bolivar', 'Cahoun', 'Carroll', 'Chickasaw', 'Choctaw', 'Clay', 'Coahoma', 'DeSoto', 'Grenada', 'Humphreys', 'Itawamba', 'LaFayette', 'Lee', 'LeFlore', 'Lowndes', 'Marshall', 'Monroe', 'Montgomery', 'Oktibbeha', 'Panola', 'Pontotoc', 'Prentiss', 'Quitman', 'Sunflower', 'Tallahatchie', 'Tate', 'Tippah', 'Tishomingo', 'Tunica', 'Union', 'Washington', 'Webster', 'Winston', 'Yalobusha',])
            SMS_DISTRICT = set(['Adams', 'Amite', 'Claiborne', 'Clarke', 'Copiah', 'Covington', 'Forrest', 'Franklin', 'George', 'Greene', 'Hancock', 'Harrison', 'Hinds', 'Holmes', 'Issaquena', 'Jackson', 'Jasper', 'Jefferson', 'Jefferson Davis', 'Jones', 'Kemper', 'Lamar', 'Lauderdale', 'Lawrence', 'Leake', 'Lincoln', 'Madison', 'Marioin', 'Neshoba', 'Newton', 'Noxubee', 'Pearl River', 'Perry', 'Pike', 'Rankin', 'Scott', 'Sharkey', 'Simpson', 'Smith', 'Stone', 'Walthall', 'Warren', 'Wayne', 'Wilkinson', 'Yazoo'])
            EMO_DISTRICT = set(['Adair', 'Audrain', 'Bollinger', 'Butler', 'Cape Girardeau', 'Carter', 'Chariton', 'Clark', 'Crawford', 'Cent', 'Dunklin', 'Franklin', 'Gasconade', 'Iron', 'Jefferson', 'Knox', 'Lewis', 'Lincoln', 'Linn', 'Macon', 'Madison', 'Maries', 'Marion', 'Mississippi', 'Monroe', 'Montgomery', 'New Madrid', 'Pemiscot', 'Perry', 'Phelps', 'Pike', 'Ralls', 'Randolph', 'Reynolds', 'Ripley', 'Schuyler', 'Scotland', 'Scott', 'Shannon', 'Shelby', 'St. Charles', 'St. Francois', 'St. Louis', 'St. Louis City', 'Ste. Genevieve', 'Stoddard', 'Warren', 'Washington', 'Wayne',])
            WMO_DISTRICT = set(['Andrew', 'Atchison', 'Barry', 'Barton', 'Bates', 'Benton', 'Boone', 'Buchanan', 'Caldwell', 'Callaway','Camden', 'Carroll', 'Cass', 'Cedar', 'Christian', 'Clay', 'Clinton', 'Cole', 'Cooper', 'Dade', 'Dallas', 'Daviess', 'Dekalb', 'Douglas', 'Genry', 'Greene', 'Grundy', 'Harrison', 'Henry', 'Hickory', 'Holt', 'Howard', 'Howell', 'Jackson', 'Jasper', 'Johnson', 'LaClede', 'LaFayette', 'Lawrence', 'Livingston', 'McDonald', 'Mercer', 'Miller', 'Moniteau', 'Morgan', 'Newton', 'Nodaway', 'Oregon', 'Osage', 'Ozark', 'Pettis', 'Platte', 'Polk', 'Pulaski', 'Putnam', 'Ray', 'Saline', 'St. Clair', 'Stone', 'Sullivan', 'Taney', 'Texas', 'Vernon', 'Webster', 'Worth', 'Wright',])
            MT_DISTRICT = set(['Beaverhead', 'Big Horn', 'Blaine', 'Broadwater', 'Carbon', 'Carter', 'Cascade', 'Chouteau', 'Custer', 'Daniels', 'Dawson', 'Deer Lodge', 'Fallon', 'Fergus', 'Flathead', 'Gallatin', 'Garfield', 'Glacier', 'Golden Valley', 'Granite', 'Hill', 'Jefferson', 'Judith Basin', 'Lake', 'Lewis and Clark', 'Libery', 'Lincoln', 'Madison', 'McCone', 'Meacher', 'Mineral', 'Missoula', 'Musselshell', 'Park', 'Petroleum', 'Phillips', 'Pondera', 'Powder River', 'Powell', 'Prairie', 'Ravalli', 'Richland', 'Roosevelt', 'Rosebud', 'Sanders', 'Sheridan', 'Silver Bow', 'Stillwater', 'Sweet Grass', 'Teton', 'Toole', 'Treasure', 'Valley', 'Wheatland', 'Wibaux', 'Yellowstone',])
            NE_DISTRICT = set(['Adams', 'Antelope', 'Arthur', 'Banner', 'Blaine', 'Boone', 'Box Butte', 'Boyd', 'Brown', 'Buffalo', 'Burt', 'Butler', 'Cass', 'Cedar', 'Chase', 'Cherry', 'Cheyenne', 'Clay', 'Colfax', 'Cuming', 'Custer', 'Dakota', 'Dawes', 'Dawson', 'Deuel', 'Dixon', 'Dodge', 'Douglas', 'Dundy', 'Fillmore', 'Franklin', 'Frontier', 'Furnas', 'Gage', 'Garden', 'Garfield', 'Gosper', 'Grant', 'Greeley', 'Hall', 'Hamilton', 'Harlan', 'Hayes', 'Hitchcock', 'Holt', 'Hooker', 'Howard', 'Jefferson', 'Johnson', 'Kearney', 'Keith', 'Keya Paha', 'Kimball', 'Knox', 'Lancaster', 'Lincoln', 'Logan', 'Loup', 'Madison', 'McPherson', 'Merrick', 'Morrill', 'Nance', 'Nemaha', 'Nuckolls', 'Otoe', 'Pawnee', 'Perkins', 'Phelps', 'Pierce', 'Platte', 'Polk', 'Red Willow', 'Richardson', 'Rock', 'Saline', 'Sarpy', 'Saunders', 'Scotts Bluff', 'Seward', 'Sheridan', 'Sherman', 'Sioux', 'Stanton', 'Thayer', 'Thomas', 'Thomas', 'Thurston', 'Valley', 'Washington', 'Wayne', 'Webster', 'Wheeler', 'York',])
            NV_DISTRICT = set(['Carson City', 'Churchill', 'Clark', 'Dougals', 'Elko', 'Esmeralda', 'Eureka', 'Humboldt', 'Lander', 'Lincoln', 'Lyon', 'Mineral', 'Nye', 'Pershing', 'Storey', 'Washoe', 'White Pine',])
            NH_DISTRICT = set(['Belknap', 'Carroll', 'Cheshire', 'Coos', 'Grafton', 'Hillsborough', 'Merrimack', 'Rockingham', 'Merrimack', 'Rockingham', 'Stafford', 'Sullivan',])
            NJ_DISTRICT = set(['Atlantic', 'Bergen', 'Burlington', 'Camden', 'Cape May', 'Cumberland', 'Essex', 'Gloucester', 'Hudson', 'Hunterdon', 'Mercer', 'Middlesex', 'Monmouth', 'Morris', 'Ocean', 'Passaic', 'Salem', 'Somerset', 'Sussex', 'Union', 'Warren',])
            NM_DISTRICT = set(['Bernalillo', 'Catron', 'Chaves', 'Cibola', 'Colfax', 'Curry', 'De Baca', 'Dona Ana', 'Eddy', 'Grant', 'Guadalupe', 'Harding', 'Hidalgo', 'Lea', 'Lincoln', 'Los Alamos', 'Luna', 'McKinley', 'Mora', 'Otero', 'Quay', 'Rio Arriba', 'Roosevelt', 'San Juan', 'San Miguel', 'Sandoval', 'Santa Fe', 'Sierra', 'Socorro', 'Taos', 'Torrance', 'Union', 'Valencia',])
            ENY_DISTRICT = set(['Kings', 'Nassau', 'Queens', 'Richmond', 'Suffolk',])
            NNY_DISTRICT = set(['Albany', 'Broome', 'Cayuga', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware', 'Essex', 'Franklin', 'Fulton', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Madison', 'Montgomery', 'Oneida', 'Onondaga', 'Owego', 'Otsego', 'Rensselaer', 'Saratoga', 'Schenectagy', 'Schoharie', 'St. Lawrence', 'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington',])
            SNY_DISTRICT = set(['Bronx', 'Dutchess', 'New York', 'Orange', 'Putnam', 'Rockland', 'Sullivan', 'Westchester',])
            WNY_DISTRICT = set(['Allegany', 'Cattaraugus', 'Chautauqua', 'Chemung', 'Erie', 'Genesee', 'Livingston', 'Monroe', 'Niagara', 'Ontario', 'Orleans', 'Schuyler', 'Seneca', 'Steuben', 'Wayne', 'Wyoming', 'Yates',])
            ENC_DISTRICT = set(['Beaufort', 'Bertie', 'Bladen', 'Brunswick', 'Camden', 'Carteret', 'Chowan', 'Columbus', 'Craven', 'Cumberland', 'Currituck', 'Dare', 'Duplin', 'Edgecombe', 'Franklin', 'Gates', 'Granville', 'Greene', 'Halifax', 'Harnett', 'Hertford', 'Hyde', 'Johnston', 'Jones', 'Lenoir', 'Martin', 'Nash', 'New Hanover', 'Northampton', 'Onslow', 'Pamlico', 'Pasquotank', 'Pender', 'Perquimans', 'Pitt', 'Robeson', 'Sampson', 'Tyrrell', 'Vance', 'Wake', 'Warren', 'Washington', 'Wayne', 'Wilson',])
            MNC_DISTRICT = set(['Alamance', 'Cabarrus', 'Caswell', 'Chatham', 'Davidson', 'Davie', 'Durham', 'Forsyth', 'Guilford', 'Hoke', 'Lee', 'Montgomery', 'Moore', 'Orange', 'Person', 'Randolph', 'Richmond', 'Rockingham', 'Rowan', 'Scotland', 'Stanly', 'Stokes', 'Surry', 'Watauga', 'Yadkin',])
            WNC_DISTRICT = set(['Alexander', 'Alleghany', 'Anson', 'Ashe', 'Avery', 'Buncombe', 'Burke', 'Caldwell', 'Catawba', 'Cherokee', 'Clay', 'Cleveland', 'Gaston', 'Graham', 'Haywood', 'Henderson', 'Iredell', 'Jackson', 'Lincoln', 'Macon', 'Madison', 'McDowell', 'Mecklenburg', 'Mitchell', 'Polk', 'Rutherford', 'Swain', 'Transylvania', 'Union', 'Wilkes', 'Yancey',])
            ND_DISTRICT = set(['Adams', 'Barnes', 'Benson', 'Billings', 'Bottineau', 'Bowman', 'Burke', 'Burleigh', 'Cass', 'Cavalier', 'Dickey', 'Divide', 'Dunn', 'Dunn', 'Eddy', 'Emmons', 'Foster', 'Golden Valley', 'Grand Forks', 'Grant', 'Griggs', 'Hettinger', 'Kidder', 'Lamoure', 'Logan', 'McHenry', 'McIntosh', 'McKenzie', 'McLean', 'Mercer', 'Morton', 'Mountrail', 'Nelson', 'Oliver', 'Pembina', 'Pierce', 'Ramsey', 'Ransom', 'Renville', 'Richland', 'Rolette', 'Sargent', 'Sheridan', 'Sioux', 'Slope', 'Stark', 'Steele', 'Stutsman', 'Towner', 'Traill', 'Walsh', 'Ward', 'Wells', 'Williams',])
            NOH_DISTRICT = set(['Allen', 'Ashland', 'Ashtabula', 'Auglaize', 'Carroll', 'Columbiana', 'Crawford', 'Cuyahoga', 'Defiance', 'Erie', 'Fulton', 'Geauga', 'Hancock', 'Hardin', 'Henry', 'Holmes', 'Huron', 'Lake', 'Lorain', 'Lucas', 'Mahoning', 'Marion', 'Medina', 'Mercer', 'Ottawa', 'Paulding', 'Portage', 'Putnam', 'Richland', 'Sandusky', 'Seneca', 'Stark', 'Summit', 'Trumbull', 'Tuscarawas', 'Van Wert', 'Wayne', 'Williams', 'Wood', 'Wyandot',])
            SOH_DISTRICT = set(['Adams', 'Athens', 'Belmont', 'Brown', 'Butler', 'Champaign', 'Clark', 'Clermont', 'Clinton', 'Coshocton', 'Darke', 'Delaware', 'Fairfield', 'Fayette', 'Franklin', 'GAllia', 'Greene', 'Guernsey', 'Hamilton', 'Harrison', 'Highland', 'Hocking', 'Jackson', 'Jefferson', 'Knox', 'Lawrence', 'Licking', 'Logan', 'Madison', 'Meigs', 'Miami', 'Monroe', 'Montgomery', 'Morgan', 'Morrow', 'Muskingum', 'Noble', 'Perry', 'Pickaway', 'Pike', 'Preble', 'Ross', 'Scioto', 'Shelby', 'Union', 'Vinton', 'Warren', 'Washington',])
            EOK_DISTRICT = set(['Adair', 'Atoka', 'Bryan', 'Carter', 'Cherokee', 'Choctaw', 'Coal', 'Haskell', 'Hughes', 'Johnston', 'Latimer', 'Le Flore', 'Love', 'Marshall', 'McCurtain', 'McIntosh', 'Murray', 'Muskogee', 'Okfuskee', 'Okmulgee', 'Pittsburg', 'Pontotoc', 'Pushmataha', 'Seminole', 'Sequoyah', 'Wagoner',])
            NOK_DISTRICT = set(['Craig', 'Creek', 'Delaware', 'Mayes', 'Nowata', 'Osage', 'Ottawa', 'Pawnee', 'Rogers', 'Tulsa', 'Washington',])
            WOK_DISTRICT = set(['Alfalfa', 'Beaver', 'Beckham', 'Blaine', 'Caddo', 'Canadian', 'Cimarron', 'Cleveland', 'Comanche', 'Cotton', 'Custer', 'Dewey', 'Ellis', 'Garfield', 'Garvin', 'Grady', 'Grant', 'Greer', 'Harmon', 'Harper', 'Jackson', 'Jefferson', 'Kay', 'Kingfisher', 'Kiowa', 'Lincoln', 'Logan', 'Major', 'McClain', 'Noble', 'Oklahoma', 'Payne', 'Pottawatomie', 'Roger Mills', 'Stephens', 'Texas', 'Washita', 'Woods', 'Woodward',])
            OR_DISTRICT = set(['Baker','Benton', 'Clackamas', 'Clatsop', 'Columbia', 'Coos', 'Crook', 'Curry', 'Deschutes', 'Douglas', 'Gilliams', 'Grant', 'Harney', 'Hood River', 'Jackson', 'Jefferson', 'Josephine', 'Klamath', 'Lake', 'Lane', 'Lincoln', 'Linn', 'Malheur', 'Marion', 'Morrow', 'Multnomah', 'Polk', 'Sherman', 'Tillamook', 'Umatilla', 'Union', 'Wallowa', 'Wasco', 'Washington', 'Wheeler', 'Yamhill',])
            EPA_DISTRICT = set(['Berks', 'Bucks', 'Chester', 'Delaware', 'Lancaster', 'Lehigh', 'Montgomery', 'Northmapton', 'Philadelphia',])
            MPA_DISTRICT = set(['Adams', 'Bradford', 'Cameron', 'Carbon', 'Centre', 'Clinton', 'Columbia', 'Cumberland', 'Dauphin', 'Franklin', 'Fulton', 'Huntingdon', 'Juniata', 'Lackawanna', 'Lebanon', 'Luzerne', 'Lycoming', 'Mifflin', 'Monroe', 'Montour', 'Northumberland', 'Perry', 'Pike', 'Potter', 'Schuylkill', 'Snyder', 'Sullivan', 'Susquehanna', 'Tioga', 'Union', 'Wayne', 'Wyoming', 'York',])
            WPA_DISTRICT = set(['Allegheny', 'Armstrong', 'Beaver', 'Bedford', 'Blair', 'Butler', 'Cambria', 'Clarion', 'Clearfield', 'Crawford', 'Elk', 'Erie', 'Fayette', 'Forest', 'Greene', 'Indiana', 'Jefferson', 'Lawrence', 'McKean', 'Mercer', 'Somerset', 'Venango', 'Warren', 'Washington', 'Westmoreland', ])
            PR_DISTRICT = set(['Adjuntas', 'Aguada', 'Aguadilla', 'Aguas Buenas', 'Aibonito', 'Anasco', 'Arecibo', 'Arroyo', 'Barceloneta', 'Barranquitas', 'Bayamon', 'Cabo Rojo', 'Caguas', 'Camuy', 'Canovanas', 'Carolina', 'Catano', 'Cayey', 'Ceiba', 'Ciales', 'Cidra', 'Coamo', 'Comerio', 'Corozal', 'Culebra', 'Dorado', 'FAjardo', 'Florida', 'Guanica', 'Guayama', 'Guayanilla', 'Guaynabo', 'Gurabo', 'Hatillo', 'Hormigueros', 'Humacao', 'Isabela', 'Jayuya', 'Juana Diaz', 'Juncos', 'Lajas', 'Lares', 'Las Marias', 'Las Piedras', 'Loiza', 'Luquillo', 'Manati', 'Maricao', 'Maunabo', 'Mayaguez', 'Moca', 'Morvois', 'Naguabo', 'Naranjito', 'Orocovis', 'Patillas', 'Penuelas', 'Ponce', 'Quebradillas', 'Rincon', 'Rio Grande', 'Sabana Grande', 'Salinas', 'San German', 'San Juan', 'San Lorenzo', 'San Sebastian', 'Santa Isabel', 'Toa Alta', 'Toa Baja', 'Trujillo Alto', 'Utuado', 'Vega Alta', 'Vega Baja', 'Vieques', 'Villalba', 'Yabucoa', 'Yauco',])
            RI_DISTRICT = set(['Bristol', 'Kent', 'Newport', 'Providence', 'Washington',])
            SC_DISTRICT = set(['Abbeville', 'Aiken', 'Allendale', 'Anderson', 'Bamberg', 'Barnwell', 'Beaufort', 'Berkeley', 'Calhoun', 'Charleston', 'Cherokee', 'Chester', 'Chesterfield', 'Clarendon', 'Colleton', 'Darlington', 'Dillon', 'Dorchester', 'Edgefield', 'Fairfield', 'Florence', 'Georgetown', 'Greenville', 'Greenwood', 'Hampton', 'Horry', 'Jasper', 'Kershaw', 'Lancaster', 'Laurens', 'Lee', 'Lexington', 'Marion', 'Marlboro', 'McCormick', 'Newberry', 'Oconee', 'Orangeburg', 'Pickens', 'Richland', 'Saluda', 'Spartanburg', 'Sumter', 'Union', 'WIlliamsburg', 'York',])
            SD_DISTRICT = set(['Aurora', 'Beadle', 'Bennett', 'Bon Homme', 'Brookings', 'Brown', 'Brule', 'Buffalo', 'Butte', 'Campbell', 'Charles Mix', 'Clark', 'Clay', 'Codington', 'Corson', 'Custer', 'Davison', 'Day', 'Deuel', 'Dewey', 'Douglas', 'Edmunds', 'Fall River', 'Faulk', 'Grant', 'Gregory', 'Haakon', 'Hamlin', 'Hand', 'Hanson', 'Harding', 'Hughes', 'Hutchinson', 'Hyde', 'Jackson', 'Jerauld', 'Jones', 'Kingsbury', 'Lake', 'Lawrence', 'Lincoln', 'Lyman', 'Marshall', 'McCook', 'McPherson', 'Meade', 'Mellette', 'Miner', 'Minnehaha', 'Moody', 'Pennington', 'Perkins', 'Potter', 'Roberts', 'Sanborn', 'Shannon', 'Spink', 'Stanley', 'Sully', 'Todd', 'Tripp', 'Turner', 'Union', 'Walworth', 'Yankton', 'Ziebach',])
            ETN_DISTRICT = set(['Anderson', 'Bedford', 'Bledsoe', 'Blount', 'Bradley', 'Campbell', 'Barter', 'Claiborne', 'Cocke', 'Coffee', 'Franklin', 'Grainger', 'Greene', 'Grundy', 'Hamblen', 'Hamilton', 'Hancock', 'Hawkins', 'Jefferson', 'Johnson', 'Knox', 'Lincoln', 'Loudon', 'Marion', 'McMinn', 'Meigs', 'Monroe', 'Moore', 'Morgan', 'Polk', 'Rhea', 'Roane', 'Scott', 'Sequatchie', 'Sevier', 'Sullivan', 'Unicoi', 'Union', 'Van Buren', 'Warren', 'Washington', ])
            MTN_DISTRICT = set(['Cannon', 'Cheatham', 'Clay', 'Cumberland', 'Davidson', 'Dekalb', 'Dickson', 'Fentress', 'Giles', 'Hickman', 'Houston', 'Humphreys', 'Jackson', 'Lawrence', 'Lewis', 'Macon', 'Marshall', 'Maury', 'Montgomery', 'Overton', 'Pickett', 'Putnam', 'Robertson', 'Rutherford', 'Smith', 'Stewart', 'Sumner', 'Trousdale', 'Wayne', 'White', 'Williamson', 'Wilson',])
            WTN_DISTRICT = set(['Benton', 'Carroll', 'Chester', 'Crockett', 'Decatur', 'Dyer', 'Fayette', 'Gibson', 'Hardeman', 'Hardin', 'Haywood', 'Henderson', 'Henry', 'Lake', 'Lauderdale', 'Madison', 'McNairy', 'Obion', 'Perry', 'Shelby', 'Tipton', 'Weakley',])
            ETX_DISTRICT = set(['Anderson', 'Angelina', 'Bowie', 'Camp', 'Cass', 'Cherokee', 'Collin', 'Cooke', 'Delta', 'Denton', 'Fannin', 'Franklin', 'Grayson', 'Gregg', 'Hardin', 'Harrison', 'Henderson', 'Hopkins', 'Houston', 'Jasper', 'Jefferson', 'Lamar', 'Liberty', 'Marion', 'Morris', 'Nacogdoches', 'Newton', 'Orange', 'Panola', 'Polk', 'Rains', 'Red River', 'Rusk', 'Sabine', 'San Augustine', 'Shelby', 'Smith', 'Titus', 'Trinity', 'Tyler', 'Upshur', 'Van Zandt', 'Wood',])
            NTX_DISTRICT = set(['Archer', 'Armstrong', 'Bailey', 'Baylor', 'Bordern', 'Briscoe', 'Brown', 'Callahan', 'Carson', 'Castro', 'Childress', 'Clay', 'Cochran', 'Coke', 'Coleman', 'Collingsworth', 'Comanche', 'Concho', 'Cottle', 'Crockett', 'Crosby', 'Dallam', 'Dallas', 'Dawson', 'Deaf Smith', 'Dickens', 'Donley', 'Eastland', 'Ellis', 'Erath', 'Fisher', 'Floyd', 'Foard', 'Gaines', 'Garza', 'Glasscock', 'Gray', 'Hale', 'Hall', 'Hansford', 'Hardeman', 'Hartley', 'Haskell', 'Hemphill', 'Hockley', 'Hood', 'Howard', 'Hunt', 'Hutchinson', 'Irion', 'Jack', 'Johnson', 'Jones', 'Kaufman', 'Kent', 'King', 'Knox', 'Lamb', 'Lipscomb', 'Lubbock', 'Lynn', 'Menard', 'Mills', 'Mitchell', 'Montague', 'Moore', 'Motley', 'Navarro', 'Nolan', 'Ochiltree', 'Oldham', 'Palo Pinto', 'Parker', 'Parmer', 'Potter', 'Randall', 'Reagan', 'Roberts', 'Rockwall', 'Runnels', 'Schleicher', 'Scurry', 'Shackelford', 'Sherman', 'Stephens', 'Sterling', 'Stonewall', 'Sutton', 'Swisher', 'Tarrant', 'Taylor', 'Terry', 'Throckmorton', 'Tom Green', 'Wheeler', 'Wichita', 'Wilbarger', 'Wise', 'Yoakum', 'Young',])
            STX_DISTRICT = set(['Aransas', 'Austin', 'Bee', 'Brazoria', 'Brazos', 'Brooks', 'Calhoun', 'Cameron', 'Chambers', 'Colorado', 'Dewitt', 'Duval', 'Fayette', 'Fort Bend', 'Galveston', 'Goliad', 'Grimes', 'Harris', 'Hidalgo', 'Jackson', 'Jim Hogg', 'Jim Wells', 'Kenedy', 'Kleberg', 'La Salle', 'Lavaca', 'Live Oak', 'Madison', 'Matagorda', 'McMullen', 'Montgomery', 'Nueces', 'Refugio', 'San Jacinto', 'San Patricio', 'Starr', 'Victoria', 'Walker', 'Waller', 'Webb', 'Wharton', 'Willacy', 'Zapata',])
            WTX_DISTRICT = set(['Andrews', 'Atascosa', 'Bandera', 'Bastrop', 'Bell', 'Bexar', 'Blanco', 'Bosque', 'Brewster', 'Burleson', 'Burnet', 'Caldwell', 'Comal', 'Coryell', 'Crane', 'Culberson', 'Dimmit', 'Ector', 'Edwards', 'El Paso', 'Falls', 'Freestone', 'Frio', 'Gillespie', 'Gonzales', 'Guadalupe', 'Hamilton', 'Hays', 'Hill', 'Hudspeth', 'Jeff Davis', 'Karnes', 'Kendall', 'Kerr', 'Kimble', 'Kinney', 'Lampasas', 'Lee', 'Leon', 'Limestone', 'Llano', 'Loving', 'Martin', 'Mason', 'Maverick', 'McCulloch', 'McLennan', 'Medina', 'Midland', 'Milam', 'Pecos', 'Presidio', 'Real', 'Reeves', 'Robertson', 'San Saba', 'Somervell', 'Terrell', 'Travis', 'Upton', 'Uvalde', 'Val Verde', 'Ward', 'Washington', 'Williamson', 'Wilson', 'Winkler', 'Zavala',])
            UT_DISTRICT = set(['Beaver', 'Box Elder', 'Cache', 'Carbon', 'Daggett', 'Davis', 'Duchesne', 'Emery', 'Garfield', 'Grand', 'Iron', 'Juab', 'Kane', 'Millard', 'Morgan', 'Piute', 'Rich', 'Salt Lake', 'San Juan', 'Sanpete', 'Seview', 'Summit', 'Tooele', 'Uintah', 'Utah', 'Wasatch', 'Washington', 'Wayne', 'Weber',])
            VT_DISTRICT = set(['Addison', 'Bennington', 'Caledonia', 'Chittenden', 'Essex', 'Franklin', 'Grand Isle', 'Lamoille', 'Orange', 'Orleans', 'Rutland', 'Washington', 'Windham', 'Windsor',])
            EVA_DISTRICT = set(['Accomack', 'Alexandria', 'Amelia', 'Arlington', 'Brunswick', 'Caroline', 'Charles City', 'Chesapeake', 'Chesterfield', 'Colonial Heights', 'Dinwiddie', 'Emporia', 'Essex', 'Fairfax', 'Fairfax City', 'Falls Church', 'Fauquier', 'Fredericksburg', 'Gloucester', 'Goochland', 'Greensville', 'Hampton', 'Hanover', 'Henrico', 'Hopewell', 'Isle of Wight', 'James City', 'King and Queen', 'King George', 'King William', 'Lancaster', 'Loudoun', 'Lunenburg', 'Manassas', 'Manassas Park', 'Mathews', 'Mecklenburg', 'Middlesex', 'New Kent', 'Newport News', 'Norfolk', 'Northampton', 'Northumberland', 'Nottoway', 'Petersburg', 'Poquoson', 'Portsmouth', 'Powhatan', 'Prince Edward', 'Prince George', 'Prince William', 'Richmond', 'Richmond City', 'Southampton', 'Spotsylvania', 'Stafford', 'Suffolk', 'Surry', 'Sussex', 'Virginia Beach', 'Westmoreland', 'Williamsburg', 'York',])
            WVA_DISTRICT = set(['Albemarle', 'Alleghany', 'Amherst', 'Appomattox', 'Augusta', 'Bath', 'Bedford', 'Bedford City', 'Bland', 'Botetourt', 'Bristol', 'Buchanan', 'Buckingham', 'Buena Vista', 'Campbell', 'Carroll', 'Charlotte', 'Charlottesville', 'Clarke', 'Covington', 'Craig', 'Culpeper', 'Cumberland', 'Danville', 'Dickenson', 'Floyd', 'Fluvanna', 'Franklin', 'Franklin City', 'Frederick', 'Galax', 'Giles', 'Grayson', 'Greene', 'Halifax', 'Harrisonburg', 'Henry', 'Highland', 'Lee', 'Lexington', 'Louisa', 'Lynchburg', 'Madison', 'Martinsville', 'Montgomery', 'Nelson', 'Norton', 'Orange', 'Page', 'Patrick', 'Pittsylvania', 'Pulaski', 'Radford', 'Rappahannock', 'Roanoke', 'Roanoke City', 'Rockbridge', 'Rockingham', 'Russell', 'Salem', 'Scott', 'Shenandoah', 'Smyth', 'Staunton', 'Tazewell', 'Warren', 'Washington', 'Waynesboro', 'Winchester', 'Wise', 'Wythe',])
            EWA_DISTRICT = set(['Adams', 'Asotin', 'Benton', 'Chelan', 'Columbia', 'Douglas', 'Ferry', 'Franklin', 'Garfield', 'Grant', 'Kittitas', 'Klickitat', 'Lincoln', 'Okanogan', 'Pend Oreille', 'Spokane', 'Stevens', 'Walla Walla', 'Whitman', 'Yakima',])
            WWA_DISTRICT = set(['Clallam', 'Clark', 'Cowlitz', 'Grays Harbor', 'Island', 'Jefferson', 'King', 'Kitsap', 'Lewis', 'Mason', 'Pacific', 'Pierce', 'San Juan', 'Skagit', 'Skamania', 'Snohomish', 'Thurston', 'Wahkiakum', 'Whatcom',])
            NWV_DISTRICT = set(['Barbour', 'Berkeley', 'Braxton', 'Brooke', 'Calhoun', 'Doddridge', 'Gilmer', 'Grant', 'Hampshire', 'Hancock', 'Hardy', 'Harrison', 'Jefferson', 'Lewis', 'Marion', 'Marshall', 'Mineral', 'Monongalia', 'Morgan', 'Ohio', 'Pendleton', 'Pleasants', 'Pocahontas', 'Preston', 'Randolph', 'Ritchie', 'Taylor', 'Tucker', 'Tyler', 'Upshur', 'Webster', 'Wetzel',])
            SWV_DISTRICT = set(['Boone', 'Cabell', 'Clay', 'Fayette', 'Greenbrier', 'Jackson', 'Kanawha', 'Lincoln', 'Logan', 'Mason', 'McDowell', 'Mercer', 'Mingo', 'Monroe', 'Nicholas', 'Putnam', 'Raleigh', 'Roane', 'Summers', 'Wayne', 'Wirt', 'Wood', 'Wyoming',])
            EWI_DISTRICT = set(['Brown', 'Calumet', 'Dodge', 'Door', 'Florence', 'Fond Du Lac', 'Forest', 'Green Lake', 'Kenosha', 'Kewaunee', 'Langlade', 'Manitowoc', 'Marinette', 'Marquette', 'Menominee', 'Milwaukee', 'Oconto', 'Outagamie', 'Ozaukee', 'Racine', 'Shawano', 'Sheboygan', 'Walworth', 'Washington', 'Waukesha', 'Waupaca', 'Waushara', 'Winnebago'])
            WWI_DISTRICT = set(['Adams', 'Ashland', 'Barron', 'Bayfield', 'Buffalo', 'Burnett', 'Chippewa', 'Clark', 'Columbia', 'Crawford', 'Dane', 'Douglas', 'Dunn', 'Eau Claire', 'Grant', 'Green', 'Iowa', 'Iron', 'Jackson', 'Jefferson', 'Juneau', 'La Crosse', 'LaFayette', 'Lincoln', 'Marathon', 'Monroe', 'Oneida', 'Pepin', 'Pierce', 'Polk', 'Portage', 'Price', 'Richland', 'Rock', 'Rusk', 'Sauk', 'Sawyer', 'St. Croix', 'Taylor', 'Trempealeau', 'Vernon', 'Vilas', 'Washburn', 'Wood',])
            WY_DISTRICT = set(['Albany', 'Big Horn', 'Campbell', 'Carbon', 'Converse', 'Crook', 'Fremont', 'Goshen', 'Hot Springs', 'Johnson', 'Laramie', 'Lincoln', 'Natrona', 'Niobrara', 'Park', 'Platte', 'Sheridan', 'Sublette', 'Sweetwater', 'Teton', 'Uinta', 'Washakie', 'Weston'])

            if stabbv == 'AL':
                if countyname in MAL_DISTRICT:
                    districtcode = "'%s'" % 'MAL'
                elif countyname in NAL_DISTRICT:
                    districtcode = "'%s'" % 'NAL'
                elif countyname in SAL_DISTRICT:
                    districtcode = "'%s'" % 'SAL'
                else:
                    districtcode = "'%s'" % random.choice(['NAL', 'MAL', 'SAL'])
            elif stabbv == 'AK':
                districtcode = "'%s'" % 'AK'
            elif stabbv == 'AZ':
                districtcode = "'%s'" % 'AZ'
            elif stabbv == 'AR':
                if countyname in EAR_DISTRICT:
                    districtcode = "'%s'" % 'EAR'
                elif countyname in WAR_DISTRICT:
                    districtcode = "'%s'" % 'WAR'
                else:
                    districtcode = "'%s'" % random.choice(['EAR', 'WAR'])
            elif stabbv == 'CA':
                if countyname in CCA_DISTRICT:
                    districtcode = "'%s'" % 'CCA'
                elif countyname in ECA_DISTRICT:
                    districtcode = "'%s'" % 'ECA'
                elif countyname in NCA_DISTRICT:
                    districtcode = "'%s'" % 'NCA'
                elif countyname in SCA_DISTRICT:
                    districtcode = "'%s'" % 'SCA'
                else:
                    districtcode = "'%s'" % random.choice(['CCA', 'ECA', 'NCA', 'SCA'])
            elif stabbv == 'CO':
                districtcode = "'%s'" % 'CO'
            elif stabbv == 'CT':
                districtcode = "'%s'" % 'CT'
            elif stabbv == 'DE':
                districtcode = "'%s'" % 'DE'
            elif stabbv == 'DC':
                districtcode = "'%s'" % 'DC'
            elif stabbv == 'FL':
                if countyname in MFL_DISTRICT:
                    districtcode = "'%s'" % 'MFL'
                elif countyname in NFL_DISTRICT:
                    districtcode = "'%s'" % 'NFL'
                elif countyname in SFL_DISTRICT:
                    districtcode = "'%s'" % 'SFL'
                else:
                    districtcode = "'%s'" % random.choice(['NFL', 'MFL', 'SFL'])
            elif stabbv == 'GA':
                if countyname in MGA_DISTRICT:
                    districtcode = "'%s'" % 'MGA'
                elif countyname in NGA_DISTRICT:
                    districtcode = "'%s'" % 'NGA'
                elif countyname in SGA_DISTRICT:
                    districtcode = "'%s'" % 'SGA'
                else:
                    districtcode = "'%s'" % random.choice(['NGA', 'MGA', 'SGA'])
            elif stabbv == 'HI':
                districtcode = "'%s'" % 'HI'
            elif stabbv == 'ID':
                districtcode = "'%s'" % 'ID'
            elif stabbv == 'IL':
                if countyname in CIL_DISTRICT:
                    districtcode = "'%s'" % 'CIL'
                elif countyname in SIL_DISTRICT:
                    districtcode = "'%s'" % 'SIL'
                elif countyname in NIL_DISTRICT:
                    districtcode = "'%s'" % 'NIL'
                else:
                    districtcode = "'%s'" % random.choice(['CIL', 'NIL', 'SIL'])
            elif stabbv == 'IN':
                if countyname in NIN_DISTRICT:
                    districtcode = "'%s'" % 'NIN'
                elif countyname in SIN_DISTRICT:
                    districtcode = "'%s'" % 'SIN'
                else:
                    districtcode = "'%s'" % random.choice(['SIN', 'NIN'])
            elif stabbv == 'IA':
                if countyname in NIA_DISTRICT:
                    districtcode = "'%s'" % 'NIA'
                elif countyname in SIA_DISTRICT:
                    districtcode = "'%s'" % 'SIA'
                else:
                    districtcode = "'%s'" % random.choice(['SIA', 'NIA'])
            elif stabbv == 'KS':
                districtcode = "'%s'" % 'KS'
            elif stabbv == 'KY':
                if countyname in WKY_DISTRICT:
                    districtcode = "'%s'" % 'WKY'
                elif countyname in EKY_DISTRICT:
                    districtcode = "'%s'" % 'EKY'
                else:
                    districtcode = "'%s'" % random.choice(['WKY', 'EKY'])
            elif stabbv == 'LA':
                if countyname in ELA_DISTRICT:
                    districtcode = "'%s'" % 'ELA'
                elif countyname in MLA_DISTRICT:
                    districtcode = "'%s'" % 'MLA'
                elif countyname in WLA_DISTRICT:
                    districtcode = "'%s'" % 'WLA'
                else:
                    districtcode = "'%s'" % random.choice(['ELA', 'MLA', 'WLA'])
            elif stabbv == 'ME':
                districtcode = "'%s'" % 'ME'
            elif stabbv == 'MD':
                districtcode = "'%s'" % 'MD'
            elif stabbv == 'MA':
                districtcode = "'%s'" % 'MA'
            elif stabbv == 'MI':
                if countyname in EMI_DISTRICT:
                    districtcode = "'%s'" % 'EMI'
                elif countyname in WMI_DISTRICT:
                    districtcode = "'%s'" % 'WMI'
                else:
                    districtcode = "'%s'" % random.choice(['EMI', 'WMI'])
            elif stabbv == 'MN':
                districtcode = "'%s'" % 'MN'
            elif stabbv == 'MS':
                if countyname in NMS_DISTRICT:
                    districtcode = "'%s'" % 'NMS'
                elif countyname in SMS_DISTRICT:
                    districtcode = "'%s'" % 'SMS'
                else:
                    districtcode = "'%s'" % random.choice(['SMS', 'NMS'])
            elif stabbv == 'MO':
                if countyname in EMO_DISTRICT:
                    districtcode = "'%s'" % 'EMO'
                elif countyname in WMO_DISTRICT:
                    districtcode = "'%s'" % 'WMO'
                else:
                    districtcode = "'%s'" % random.choice(['EMO', 'WMO'])
            elif stabbv == 'MT':
                districtcode = "'%s'" % 'MT'
            elif stabbv == 'NE':
                districtcode = "'%s'" % 'NE'
            elif stabbv == 'NV':
                districtcode = "'%s'" % 'NV'
            elif stabbv == 'NH':
                districtcode = "'%s'" % 'NH'
            elif stabbv == 'NJ':
                districtcode = "'%s'" % 'NJ'
            elif stabbv == 'NM':
                districtcode = "'%s'" % 'NM'
            elif stabbv == 'NY':
                if countyname in NNY_DISTRICT:
                    districtcode = "'%s'" % 'NNY'
                elif countyname in ENY_DISTRICT:
                    districtcode = "'%s'" % 'ENY'
                elif countyname in SNY_DISTRICT:
                    districtcode = "'%s'" % 'SNY'
                elif countyname in WNY_DISTRICT:
                    districtcode = "'%s'" % 'WNY'
                else:
                    districtcode = "'%s'" % random.choice(['NNY', 'ENY', 'SNY', 'WNY'])
            elif stabbv == 'NC':
                if countyname in ENC_DISTRICT:
                    districtcode = "'%s'" % 'ENC'
                elif countyname in MNC_DISTRICT:
                    districtcode = "'%s'" % 'MNC'
                elif countyname in WNC_DISTRICT:
                    districtcode = "'%s'" % 'WNC'
                else:
                    districtcode = "'%s'" % random.choice(['MNC', 'ENC', 'WNC'])
            elif stabbv == 'ND':
                districtcode = "'%s'" % 'ND'
            elif stabbv == 'OH':
                if countyname in NOH_DISTRICT:
                    districtcode = "'%s'" % 'NOH'
                elif countyname in SOH_DISTRICT:
                    districtcode = "'%s'" % 'SOH'
                else:
                    districtcode = "'%s'" % random.choice(['NOH', 'SOH'])
            elif stabbv == 'OK':
                if countyname in EOK_DISTRICT:
                    districtcode = "'%s'" % 'EOK'
                elif countyname in NOK_DISTRICT:
                    districtcode = "'%s'" % 'NOK'
                elif countyname in WOK_DISTRICT:
                    districtcode = "'%s'" % 'WOK'
                else:
                    districtcode = "'%s'" % random.choice(['NOK', 'EOK', 'WOK'])
            elif stabbv == 'OR':
                districtcode = "'%s'" % 'OR'
            elif stabbv == 'PA':
                if countyname in EPA_DISTRICT:
                    districtcode = "'%s'" % 'EPA'
                elif countyname in MPA_DISTRICT:
                    districtcode = "'%s'" % 'MPA'
                elif countyname in WPA_DISTRICT:
                    districtcode = "'%s'" % 'WPA'
                else:
                    districtcode = "'%s'" % random.choice(['EPA', 'WPA', 'MPA'])
            elif stabbv == 'PR':
                districtcode = "'%s'" % 'PR'
            elif stabbv == 'RI':
                districtcode = "'%s'" % 'RI'
            elif stabbv == 'SC':
                districtcode = "'%s'" % 'SC'
            elif stabbv == 'SD':
                districtcode = "'%s'" % 'SD'
            elif stabbv == 'TN':
                if countyname in ETN_DISTRICT:
                    districtcode = "'%s'" % 'ETN'
                elif countyname in MTN_DISTRICT:
                    districtcode = "'%s'" % 'MTN'
                elif countyname in WTN_DISTRICT:
                    districtcode = "'%s'" % 'WTN'
                else:
                    districtcode = "'%s'" % random.choice(['ETN', 'WTN', 'MTN'])
            elif stabbv == 'TX':
                if countyname in ETX_DISTRICT:
                    districtcode = "'%s'" % 'ETX'
                elif countyname in WTX_DISTRICT:
                    districtcode = "'%s'" % 'WTX'
                elif countyname in NTX_DISTRICT:
                    districtcode = "'%s'" % 'NTX'
                elif countyname in STX_DISTRICT:
                    districtcode = "'%s'" % 'STX'
                else:
                    districtcode = "'%s'" % random.choice(['ETX', 'WTX', 'NTX', 'STX'])
            elif stabbv == 'UT':
                districtcode = "'%s'" % 'UT'
            elif stabbv == 'VT':
                districtcode = "'%s'" % 'VT'
            elif stabbv == 'VA':
                if countyname in EVA_DISTRICT:
                    districtcode = "'%s'" % 'EVA'
                elif countyname in WVA_DISTRICT:
                    districtcode = "'%s'" % 'WVA'
                else:
                    districtcode = "'%s'" % random.choice(['EVA', 'WVA'])
            elif stabbv == 'WA':
                if countyname in EWA_DISTRICT:
                    districtcode = "'%s'" % 'EWA'
                elif countyname in WWA_DISTRICT:
                    districtcode = "'%s'" % 'WWA'
                else:
                    districtcode = "'%s'" % random.choice(['EWA', 'WWA'])
            elif stabbv == 'WV':
                if countyname in NWV_DISTRICT:
                    districtcode = "'%s'" % 'NWV'
                elif countyname in SWV_DISTRICT:
                    districtcode = "'%s'" % 'SWV'
                else:
                    districtcode = "'%s'" % random.choice(['NWV', 'SWV'])
            elif stabbv == 'WI':
                if countyname in EWI_DISTRICT:
                    districtcode = "'%s'" % 'EWI'
                elif countyname in WWI_DISTRICT:
                    districtcode = "'%s'" % 'WWI'
                else:
                    districtcode = "'%s'" % random.choice(['EWI', 'WWI'])
            elif stabbv == 'WY':
                districtcode = "'%s'" % 'WY'

            countyname = ''.join(countyname.split("'"))

            queryBuffer.append(
                """
                INSERT INTO counties (countyId, name, type, centroidX, centroidY, bboxXY1, bboxXY2, bboxXY3, bboxXY4, aor_id, district_id, region_id, state_id)
                VALUES (%d, '%s', '%s', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (SELECT rmp.states.aor_id FROM rmp.states WHERE rmp.states.abbv = '%s' LIMIT 1), %s, (SELECT rmp.states.region_id FROM rmp.states WHERE rmp.states.abbv = '%s' LIMIT 1), (SELECT rmp.states.name FROM rmp.states WHERE rmp.states.abbv = '%s' LIMIT 1))
                ON DUPLICATE KEY UPDATE name = '%s', type = '%s', aor_id = (SELECT rmp.states.aor_id FROM rmp.states WHERE rmp.states.abbv = '%s' LIMIT 1), district_id = '%s', region_id = (SELECT rmp.states.region_id FROM rmp.states WHERE rmp.states.abbv = '%s' LIMIT 1), state_id = (SELECT rmp.states.name FROM rmp.states WHERE rmp.states.abbv = '%s' LIMIT 1);
                """ % (countyfips, countyname, countytype, stabbv, districtcode, stabbv, stabbv, countyname, countytype, stabbv, districtcode, stabbv, stabbv)
            )
        else:
            i = 1

with open('./scripts/counties.sql', 'w') as f:
    for elem in queryBuffer:
        f.write(elem)

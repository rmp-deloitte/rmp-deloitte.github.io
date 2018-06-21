import sqlite3
import csv

sqlStatements = set()

with open(r'C:\Users\phdouglas\Desktop\Development\nappyblerd.github.io\projects\venv\rmp\Data\csv\us_postal_codes.csv') as c:
    AT_REGION = set(['Delaware','District of Columbia','Maryland','North Carolina','Pennsylvania','South Carolina','Virginia', 'New Jersey',])
    CT_REGION = set(['Illinois', 'Indiana', 'Kentucky', 'Michigan', 'Ohio', 'Tennessee', 'West Virginia',])
    CP_REGION = set(['District of Columbia'])
    MW_REGION = set(['Iowa', 'Wisconsin', 'Kansas', 'Iowa', 'Minnesota', 'Missouri', 'Nebraska',])
    MT_REGION = set(['Arizona','Colorado','Idaho','Montana','Nevada','North Dakota','South Dakota','Utah','Wyoming','New Mexico',])
    NE_REGION = set(['Connecticut', 'Maine', 'New Hampshire', 'Massachusetts', 'New York', 'Rhode Island', 'Vermont'])
    PA_REGION = set(['Alaska', 'California','Hawaii','Nevada','Oregon','Washington',])
    SE_REGION = set(['Alabama','Florida','Georgia','Louisiana','Mississippi','Puerto Rico',])
    SW_REGION = set(['Arkansas', 'Oklahoma', 'Texas'])

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

    records = csv.reader(c, delimiter=',')
    i = 0
    counties = set()
    for record in records:
        if i >= 1:
            sqlString = r'INSERT INTO counties (name, countyName, stateName_id, districtCode_id, regionName_id, aorName_id, centroid, bbox) VALUES ('
            if record[4] in counties:
                pass
            else:
                sqlString += "%d, '%s', '%s', " % (i, record[4], record[2])

                if record[2] == 'Alabama':
                    if record[4] in MAL_DISTRICT:
                        sqlString += "'%s', " % 'MAL'
                    elif record[4] in NAL_DISTRICT:
                        sqlString += "'%s', " % 'NAL'
                    elif record[4] in SAL_DISTRICT:
                        sqlString += "'%s', " % 'SAL'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Alaska':
                    if record[4] in AK_DISTRICT:
                        sqlString += "'%s', " % 'AK'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Arizona':
                    if record[4] in AZ_DISTRICT:
                        sqlString += "'%s', " % 'AZ'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Arkansas':
                    if record[4] in EAR_DISTRICT:
                        sqlString += "'%s', " % 'EAR'
                    elif record[4] in WAR_DISTRICT:
                        sqlString += "'%s', " % 'WAR'
                    else:
                        sqlString += "'', "
                elif record[2] == 'California':
                    if record[4] in CCA_DISTRICT:
                        sqlString += "'%s', " % 'CCA'
                    elif record[4] in ECA_DISTRICT:
                        sqlString += "'%s', " % 'ECA'
                    elif record[4] in NCA_DISTRICT:
                        sqlString += "'%s', " % 'NCA'
                    elif record[4] in SCA_DISTRICT:
                        sqlString += "'%s', " % 'SCA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Colorado':
                    if record[4] in CO_DISTRICT:
                        sqlString += "'%s', " % 'CO'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Connecticut':
                    if record[4] in CT_DISTRICT:
                        sqlString += "'%s', " % 'CT'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Delaware':
                    if record[4] in DE_DISTRICT:
                        sqlString += "'%s', " % 'DE'
                    else:
                        sqlString += "'', "
                elif record[2] == 'District of Columbia':
                    if record[4] in DC_DISTRICT:
                        sqlString += "'%s', " % 'DC'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Florida':
                    if record[4] in MFL_DISTRICT:
                        sqlString += "'%s', " % 'MFL'
                    elif record[4] in NFL_DISTRICT:
                        sqlString += "'%s', " % 'NFL'
                    elif record[4] in SFL_DISTRICT:
                        sqlString += "'%s', " % 'SFL'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Georgia':
                    if record[4] in MGA_DISTRICT:
                        sqlString += "'%s', " % 'MGA'
                    elif record[4] in NGA_DISTRICT:
                        sqlString += "'%s', " % 'NGA'
                    elif record[4] in SGA_DISTRICT:
                        sqlString += "'%s', " % 'SGA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Hawaii':
                    if record[4] in HI_DISTRICT:
                        sqlString += "'%s', " % 'HI'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Idaho':
                    if record[4] in ID_DISTRICT:
                        sqlString += "'%s', " % 'ID'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Illinois':
                    if record[4] in CIL_DISTRICT:
                        sqlString += "'%s', " % 'CIL'
                    elif record[4] in SIL_DISTRICT:
                        sqlString += "'%s', " % 'SIL'
                    elif record[4] in NIL_DISTRICT:
                        sqlString += "'%s', " % 'NIL'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Indiana':
                    if record[4] in NIN_DISTRICT:
                        sqlString += "'%s', " % 'NIN'
                    elif record[4] in SIN_DISTRICT:
                        sqlString += "'%s', " % 'SIN'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Iowa':
                    if record[4] in NIA_DISTRICT:
                        sqlString += "'%s', " % 'NIA'
                    elif record[4] in SIA_DISTRICT:
                        sqlString += "'%s', " % 'SIA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Kansas':
                    if record[4] in KS_DISTRICT:
                        sqlString += "'%s', " % 'KS'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Kentucky':
                    if record[4] in WKY_DISTRICT:
                        sqlString += "'%s', " % 'WKY'
                    elif record[4] in EKY_DISTRICT:
                        sqlString += "'%s', " % 'EKY'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Louisiana':
                    if record[4] in ELA_DISTRICT:
                        sqlString += "'%s', " % 'ELA'
                    elif record[4] in MLA_DISTRICT:
                        sqlString += "'%s', " % 'MLA'
                    elif record[4] in WLA_DISTRICT:
                        sqlString += "'%s', " % 'WLA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Maine':
                    if record[4] in ME_DISTRICT:
                        sqlString += "'%s', " % 'ME'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Maryland':
                    if record[4] in MD_DISTRICT:
                        sqlString += "'%s', " % 'MD'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Massachusetts':
                    if record[4] in MA_DISTRICT:
                        sqlString += "'%s', " % 'MA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Michigan':
                    if record[4] in EMI_DISTRICT:
                        sqlString += "'%s', " % 'EMI'
                    elif record[4] in WMI_DISTRICT:
                        sqlString += "'%s', " % 'WMI'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Minnesota':
                    if record[4] in MN_DISTRICT:
                        sqlString += "'%s', " % 'MN'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Mississippi':
                    if record[4] in NMS_DISTRICT:
                        sqlString += "'%s', " % 'NMS'
                    elif record[4] in SMS_DISTRICT:
                        sqlString += "'%s', " % 'SMS'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Missouri':
                    if record[4] in EMO_DISTRICT:
                        sqlString += "'%s', " % 'EMO'
                    elif record[4] in WMO_DISTRICT:
                        sqlString += "'%s', " % 'WMO'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Montana':
                    if record[4] in MT_DISTRICT:
                        sqlString += "'%s', " % 'MT'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Nebraska':
                    if record[4] in NE_DISTRICT:
                        sqlString += "'%s', " % 'NE'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Nevada':
                    if record[4] in NV_DISTRICT:
                        sqlString += "'%s', " % 'NV'
                    else:
                        sqlString += "'', "
                elif record[2] == 'New Hampshire':
                    if record[4] in NH_DISTRICT:
                        sqlString += "'%s', " % 'NH'
                    else:
                        sqlString += "'', "
                elif record[2] == 'New Jersey':
                    if record[4] in NJ_DISTRICT:
                        sqlString += "'%s', " % 'NJ'
                    else:
                        sqlString += "'', "
                elif record[2] == 'New Mexico':
                    if record[4] in NM_DISTRICT:
                        sqlString += "'%s', " % 'NM'
                    else:
                        sqlString += "'', "
                elif record[2] == 'New York':
                    if record[4] in NNY_DISTRICT:
                        sqlString += "'%s', " % 'NNY'
                    elif record[4] in ENY_DISTRICT:
                        sqlString += "'%s', " % 'ENY'
                    elif record[4] in SNY_DISTRICT:
                        sqlString += "'%s', " % 'SNY'
                    elif record[4] in WNY_DISTRICT:
                        sqlString += "'%s', " % 'WNY'
                    else:
                        sqlString += "'', "
                elif record[2] == 'North Carolina':
                    if record[4] in ENC_DISTRICT:
                        sqlString += "'%s', " % 'ENC'
                    elif record[4] in MNC_DISTRICT:
                        sqlString += "'%s', " % 'MNC'
                    elif record[4] in WNC_DISTRICT:
                        sqlString += "'%s', " % 'WNC'
                    else:
                        sqlString += "'', "
                elif record[2] == 'North Dakota':
                    if record[4] in ND_DISTRICT:
                        sqlString += "'%s', " % 'ND'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Ohio':
                    if record[4] in NOH_DISTRICT:
                        sqlString += "'%s', " % 'NOH'
                    elif record[4] in SOH_DISTRICT:
                        sqlString += "'%s', " % 'SOH'
                    else:
                        sqlString += "'', "
                elif record[2] == 'OKlahoma':
                    if record[4] in EOK_DISTRICT:
                        sqlString += "'%s', " % 'EOK'
                    elif record[4] in NOK_DISTRICT:
                        sqlString += "'%s', " % 'NOK'
                    elif record[4] in WOK_DISTRICT:
                        sqlString += "'%s', " % 'WOK'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Oregon':
                    if record[4] in OR_DISTRICT:
                        sqlString += "'%s', " % 'OR'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Pennsylvania':
                    if record[4] in EPA_DISTRICT:
                        sqlString += "'%s', " % 'EPA'
                    elif record[4] in MPA_DISTRICT:
                        sqlString += "'%s', " % 'MPA'
                    elif record[4] in WPA_DISTRICT:
                        sqlString += "'%s', " % 'WPA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Puerto Rico':
                    if record[4] in PR_DISTRICT:
                        sqlString += "'%s', " % 'PR'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Rhode Island':
                    if record[4] in RI_DISTRICT:
                        sqlString += "'%s', " % 'RI'
                    else:
                        sqlString += "'', "
                elif record[2] == 'South Carolina':
                    if record[4] in SC_DISTRICT:
                        sqlString += "'%s', " % 'SC'
                    else:
                        sqlString += "'', "
                elif record[2] == 'South Dakota':
                    if record[4] in SD_DISTRICT:
                        sqlString += "'%s', " % 'SD'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Tennessee':
                    if record[4] in ETN_DISTRICT:
                        sqlString += "'%s', " % 'ETN'
                    elif record[4] in MTN_DISTRICT:
                        sqlString += "'%s', " % 'MTN'
                    elif record[4] in WTN_DISTRICT:
                        sqlString += "'%s', " % 'WTN'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Texas':
                    if record[4] in ETX_DISTRICT:
                        sqlString += "'%s', " % 'ETX'
                    elif record[4] in WTX_DISTRICT:
                        sqlString += "'%s', " % 'WTX'
                    elif record[4] in NTX_DISTRICT:
                        sqlString += "'%s', " % 'NTX'
                    elif record[4] in STX_DISTRICT:
                        sqlString += "'%s', " % 'STX'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Utah':
                    if record[4] in UT_DISTRICT:
                        sqlString += "'%s', " % 'UT'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Vermont':
                    if record[4] in VT_DISTRICT:
                        sqlString += "'%s', " % 'VT'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Virginia':
                    if record[4] in EVA_DISTRICT:
                        sqlString += "'%s', " % 'EVA'
                    elif record[4] in WVA_DISTRICT:
                        sqlString += "'%s', " % 'WVA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Washington':
                    if record[4] in EWA_DISTRICT:
                        sqlString += "'%s', " % 'EWA'
                    elif record[4] in WWA_DISTRICT:
                        sqlString += "'%s', " % 'WWA'
                    else:
                        sqlString += "'', "
                elif record[2] == 'West Virginia':
                    if record[4] in NWV_DISTRICT:
                        sqlString += "'%s', " % 'NWV'
                    elif record[4] in SWV_DISTRICT:
                        sqlString += "'%s', " % 'SWV'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Wisconsin':
                    if record[4] in EWI_DISTRICT:
                        sqlString += "'%s', " % 'EWI'
                    elif record[4] in WWI_DISTRICT:
                        sqlString += "'%s', " % 'WWI'
                    else:
                        sqlString += "'', "
                elif record[2] == 'Wyoming':
                    if record[4] in WY_DISTRICT:
                        sqlString += "'%s', " % 'WY'
                    else:
                        sqlString += "'', "
                else:
                    sqlString += "'', "

                if record[2] in AT_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Atlantic', 'East')
                elif record[2] in CT_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Central', 'East')
                elif record[2] in CP_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Capital', 'East')
                elif record[2] in MW_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Midwest', 'West')
                elif record[2] in MT_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Mountain', 'West')
                elif record[2] in NE_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Northeast', 'East')
                elif record[2] in PA_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Pacific', 'West')
                elif record[2] in SE_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Southeast', 'East')
                elif record[2] in SW_REGION:
                    sqlString += "'%s', '%s', '', '');" % ('Southwest', 'West')

                counties.add(record[4])
                sqlStatements.add(sqlString)
                i+=1
        else:
            i = 1

cursor = sqlite3.connect('db.sqlite3')
with open(r'../Lib/custom_scripts/counties.sql', 'w') as f:
    for sql in sqlStatements:
        f.write(sql + '\n')

import json

# parse the nobel-laureates JSON and convert it into a Python Dictionary
with open('/home/cs143/data/nobel-laureates.json') as fileName:
  info = json.load(fileName)

LaureateInfo = info['laureates']

# Laureate(ID, NAME, FAMILYNAME, GENDER, DATE, CITY)
LAUREATE = dict()
# create the file 'Laureate.del' to store this information
file1 = open('Laureate.del', 'w')

for item in LaureateInfo:
  # initialize variables, set defaults
  ID = r'\N'
  NAME = r'\N'
  FAMILYNAME = r'\N'
  GENDER = r'\N'
  DATE = r'\N'
  CITY = r'\N'

  # ID
  ID = item['id']

  # NAME
  # options between givenName (for a person) or orgName (for an organization)
  opt = ['givenName', 'orgName']
  # select the correct option based on whether 'givenName' or 'orgName' was found in the JSON item
  for o in opt:
    if o in item:
      NAME = '"' + item[o]['en'] + '"'

  # FAMILYNAME           
  if 'familyName' in item:
    FAMILYNAME = '"' + item['familyName']['en'] + '"'

  # GENDER
  if 'gender' in item:
    GENDER = '"' + item['gender'] + '"'

  # DATE, CITY
  # options between birth (for a person) or founded (for an organization)
  opt = ['birth', 'founded']
  for o in opt:
    if o in item:
      # birthdate / founding date
      if 'date' in item[o]:
        DATE = item[o]['date'].replace('-','')
      # birthplace / founding place
      if 'place' in item[o]:
        place = item[o]['place']
        if 'city' in place:
          CITY = '"' + place['city']['en'] + '"'

  row = [ID, NAME, FAMILYNAME, GENDER, DATE, CITY]

  # couldn't find the ID in the the LAUREATE dictionary, need to write it into 'Laureate.del'
  if ID not in LAUREATE:
    s = ','.join(row) + '\n'
    file1.write(s)
    LAUREATE[ID] = True
file1.close()




# Place(CITY, COUNTRY)
PLACE = dict()
# create the file 'Place.del' to store this information
file2 = open('Place.del', 'w')

# birthplace or founded place
for item in LaureateInfo:
  # initialize variables, set defaults
  CITY = r'\N'
  COUNTRY = r'\N'
  # options between birth (for a person) or founded (for an organization)
  opt = ['birth', 'founded']
  for o in opt:
    if o in item:
      place = item[o]['place']
      # city 
      if 'city' in place:
        CITY = '"' + place['city']['en'] + '"'

      # country
      if 'country' in place:
        COUNTRY = '"' + place['country']['en'] + '"'
  
  row = [CITY, COUNTRY]
  # if (city not already in the PLACE dictionary) and (city was found) and (country was found), write it into 'Place.del'
  if (CITY not in PLACE) and (CITY != r'\N') and (COUNTRY != r'\N'):
    s = ','.join(row) + '\n'
    file2.write(s)
    PLACE[CITY] = True


  # places for nobelPrize (affiliations)
  nobelPrizes = item['nobelPrizes']
  for NP in nobelPrizes:
    # initialize variables, set defaults
    CITY = r'\N'
    COUNTRY = r'\N'
    # affiliations ("name", "city", "country")
    if 'affiliations' in NP:
      affiliations = NP['affiliations']
      for a in affiliations:
        # city
        if 'city' in a:
          CITY = '"' + a['city']['en'] + '"'

        # country
        if 'country' in a:
          COUNTRY = '"' + a['country']['en'] + '"'

        row = [CITY, COUNTRY]
        # if (city not already in the PLACE dictionary) and (city was found) and (country was found), write it into 'Place.del'
        if (CITY not in PLACE) and (CITY != r'\N') and (COUNTRY != r'\N'):
          s = ','.join(row) + '\n'
          file2.write(s)
          PLACE[CITY] = True
file2.close()




# NobelPrize(id, awardYear, category, sortOrder, portion, prizeStatus, dateAwarded, motivation, priceAmount)
# create the file 'NobelPrize.del' to store this information
file3 = open('NobelPrize.del', 'w')

# Affiliation(name, city, id)
# create the file 'Affiliation.del' to store this information
file4 = open('Affiliation.del', 'w')

count = 1
for item in LaureateInfo:
  LaureateID = item['id']
  Prizes = item['nobelPrizes']

  for p in Prizes:
    AWARDYEAR = p['awardYear']
    CATEGORY = '"' + p['category']['en'] + '"'
    SORTORDER = p['sortOrder']
    PORTION = p['portion']
    PRIZESTATUS = '"' + p['prizeStatus'] + '"'
    MOTIVATION = '"' + p['motivation']['en'] + '"'
    PRIZEAMOUNT = str(p['prizeAmount'])
    if 'dateAwarded' in p:
      DATEAWARDED = p['dateAwarded'].replace('-','')
    else:
      DATEAWARDED = r'\N'

    row = [str(count), LaureateID, AWARDYEAR, CATEGORY, SORTORDER, PORTION, DATEAWARDED, PRIZESTATUS, MOTIVATION, PRIZEAMOUNT]
    s = ','.join(row) + '\n'
    # write in all this information to 'NobelPrize.del'
    file3.write(s)


    # Nobel Prize affiliations
    if 'affiliations' in p:
      # affiliations ("name", "city", "country")
      affiliations = p['affiliations']

      for a in affiliations:
        # name of the affiliation (i.e. Stanford University)
        
        if 'name' in a:
          NAME = '"' + a['name']['en'] + '"'
        # name not found
        else:
          NAME = r'\N'

        # city
        if 'city' in a:
          CITY = '"' + a['city']['en'] + '"'
        # city not found
        else:
          CITY = r'\N'

        row = [NAME, CITY, str(count)]
        s = ','.join(row) + '\n'
        # write in all this information to 'Affiliation.del'
        file4.write(s)
    count += 1

file3.close()
file4.close()
print("Converted successfully.")

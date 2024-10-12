import requests

def highestInternationalStudents(firstCity, secondCity):

    highestInternationalStudentsUniversity = ''

    if firstCity == None and secondCity == None:
        return highestInternationalStudentsUniversity
  
    # Url with hackerrank mock
    url = "https://jsonmock.hackerrank.com/api/universities"
    
    highestInternationalStudentsCity = {
        'firstCity': {
            'university': '',
            'numberOfInternationalStudents': 0
        },
        'secondCity': {
            'university': '',
            'numberOfInternationalStudents': 0
        }
    }
    
    # Initial request in order to get the JSON
    response = requests.get(url)
    if response.status_code == 500:
        return highestInternationalStudentsUniversity
    
    if response.status_code == 200:
        page_data = response.json()
        total_pages = page_data['total_pages']  # Get total pages

        # Go through each page
        for page in range(1, total_pages + 1):
            page_response = requests.get(f"{url}?page={page}")
            page_data = page_response.json()
            
            # Go through each university in 'data'. The algorithm applied was greedy algorithm, basically computing 
            # the maximum international students for each iteration and both cities (due firstCity can be placed on 
            # last item in the last pagination).
            for item in page_data['data']:   
                internationalStudents = item['international_students'].replace(',', '') 
                internationalStudents = int(internationalStudents)             
                if item['location']['city'] == firstCity and \
                    internationalStudents > highestInternationalStudentsCity['firstCity']['numberOfInternationalStudents']:
                        highestInternationalStudentsCity['firstCity'] = {
                            'university': item['university'],
                            'numberOfInternationalStudents': internationalStudents
                        }
                    
                if item['location']['city'] == secondCity and \
                    internationalStudents > highestInternationalStudentsCity['secondCity']['numberOfInternationalStudents']:
                        highestInternationalStudentsCity['secondCity'] = {
                            'university': item['university'],
                            'numberOfInternationalStudents': internationalStudents
                        }

    if highestInternationalStudentsCity['firstCity']['university'] and \
        highestInternationalStudentsCity['firstCity']['numberOfInternationalStudents'] > 0:
        highestInternationalStudentsUniversity = highestInternationalStudentsCity['firstCity']['university']  
    elif highestInternationalStudentsCity['secondCity']['university'] and \
        highestInternationalStudentsCity['secondCity']['numberOfInternationalStudents'] > 0:     
        highestInternationalStudentsUniversity = highestInternationalStudentsCity['secondCity']['university']           

    return highestInternationalStudentsUniversity         

if __name__ == "__main__":                 
    print(highestInternationalStudents('Pune', 'New Delhi')) 
    print(highestInternationalStudents('Cambridge', 'Santiago')) 
    print(highestInternationalStudents('', 'Zürich'))
    print(highestInternationalStudents(None, '')) 
    print(highestInternationalStudents('', None)) 
    print(highestInternationalStudents(None, None)) 
    print(highestInternationalStudents('', ''))   
    print(highestInternationalStudents('MockCity1', 'MockCity2')) 
    print(highestInternationalStudents('London', '')) 

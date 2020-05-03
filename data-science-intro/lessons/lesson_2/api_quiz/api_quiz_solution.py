import json
import requests


def api_get_request(url,position):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    #url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=c91c8acfd443cef1f5880abe911f72d0&format=json'

    data = requests.get(url).text
    data = json.loads(data)

    #print data ['topartists']['artist'][0]['name']

    return data ['topartists']['artist'][position]['name'] # return the top artist in Spain for the desired position


if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain

        url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=c91c8acfd443cef1f5880abe911f72d0&format=json' 
        print api_get_request(url,0)

'''

data = requests.get('http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=c91c8acfd443cef1f5880abe911f72d0&format=json').text
data = json.loads(data)
print type(data)
print data ['topartists']['artist'][0]['name']

data = requests.get(url).text
data = json.loads(data)
print type(data)
print data
data['artist']


API Key: c91c8acfd443cef1f5880abe911f72d0
Secret: is 4736a83a5d2993108fb832c885a09b0b

http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=c91c8acfd443cef1f5880abe911f72d0&format=json

'''


import requests
import datetime

TOKEN = 'xxx'
today = datetime.datetime.today().strftime('%Y-%m-%d')
URL='https://hulu.rideamigos.com/api/v1/users/5b279ed4d1bd140613716c29/triplogs'
payload = '{"miles":5,"times":["8:45 AM","6:00 PM"],"locations":[{"type":"Feature","geometry":{"type":"Point","coordinates":[-118.42095999999998,34.01986000000005]},"properties":{"label":"Palms, Los Angeles, California"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-118.47411594717414,34.03075545471689]},"properties":{"label":"2450 Broadway, Santa Monica, California, 90404"}}],"selectedTrip":{"id":"other","text":"Other","trip":{"origin":{"type":"Feature","geometry":{"type":"Point","coordinates":[-118.42095999999998,34.01986000000005]},"properties":{"label":"Palms, Los Angeles, California"}},"destination":{"type":"Feature","geometry":{"type":"Point","coordinates":[-118.47411594717414,34.03075545471689]},"properties":{"label":"2450 Broadway, Santa Monica, California, 90404"}}}},"distance":5,"mode":"transit","timeZoneOffset":420,"dates":["%s"],"timezoneOffset":"-07:00"}' %(today)
#print(payload)
r = requests.post(URL, data = payload, headers={'authorization': 'Bearer {}'.format(TOKEN), 'content-type': 'application/json'})
if r.status_code == 201:
    print('Success')
else:
    print(r.text)

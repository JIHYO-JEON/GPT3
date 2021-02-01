import requests

# http://www.khoa.go.kr/oceangrid/khoa/takepart/openapi/openApiObsAtempBuRealDataInfo.do
service_key = ""
location = 'TW_0062' #해운대해수욕장
date = '20141101'
endpoint = 'http://www.khoa.go.kr/oceangrid/grid/api/obsWaveHight/search.do?ServiceKey={}&ObsCode={}&Date={}&ResultType=json'.format(service_key, location, date)

resp = requests.get(endpoint)
print(resp.status_code)
print(resp.text)

data = resp.json()
print(data)
wave = data['result']['data'][-1]['wave_height']
print(wave)
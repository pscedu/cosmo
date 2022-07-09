# run uvicorn main:app --reload first
import requests
import json
response = requests.get('http://127.0.0.1:8000/pig/{id}/lengthbytype/n={num}'.format(id=251, num=5))
print(response.url) # http://127.0.0.1:8000/pig/251/lengthbytype/n=10
print(response.json()) # {'length_by_type': '[[446499, 507723, 0, 0, 561897, 7], [700225, 0, 0, 0, 1, 0], [239021, 247773, 0, 0, 173607, 8], [125966, 152736, 0, 0, 206388, 2], [172170, 171025, 0, 0, 83207, 11]]'}
print(response.status_code) # 200
# Use the json module to load response into a dictionary.
response_dict = json.loads(response.text)
for i in response_dict:
    print("key: ", i, " val: ", response_dict[i])
# key:  length_by_type  val:  [[446499, 507723, 0, 0, 561897, 7], [700225, 0, 0, 0, 1, 0], [239021, 247773, 0, 0, 173607, 8], [125966, 152736, 0, 0, 206388, 2], [172170, 171025, 0, 0, 83207, 11]]
payload = {'groupid_list': [2]}
response = requests.get('http://127.0.0.1:8000/pig/{id}/{ptype}/{feature}/'.format(id=251, ptype="star", feature="Generation"), params=payload)
print(response.json())
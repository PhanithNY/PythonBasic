import json
from urllib.request import  urlopen

json_string = '''
{
  "data": {
    "successBtn": [
      "detail",
      "expense",
      "share"
    ],
    "successDetailBtn": [
      "screenshot",
      "share",
      "expense"
    ],
    "successContent": [
      {
        "value": "15-03-2025 | 02:10:18 PM",
        "label_kh": "កាលបរិច្ឆេទ:",
        "label_ch": "日期和时间：",
        "is_shareable": false,
        "index": 1,
        "total": false,
        "label_parameter": "transactionDate",
        "label_en": "Date and Time:"
      },
      {
        "value": "100004749",
        "label_kh": "ពីគណនី:",
        "label_ch": "从账户:",
        "is_shareable": true,
        "index": 2,
        "total": false,
        "label_parameter": "fromAccount",
        "label_en": "From Account:"
      }
    ]
  },
  "code": "200"
}
'''

data = json.loads(json_string)
print(data)

# Access field "code" inside json string, easy like that.
status_code = data["code"]
print(status_code)

# ensure_ascii = false allow all unicodes to render properly
# sort_keys = true will sort all json properties by name from A-Z
new_json = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
print(new_json)

# Open sample.json file from current directory in read mode
# Using `with`, the memory will release automatically if no longer access.
with open("sample.json", "r") as file:
    file_data = json.load(file)
    print(file_data)

# Create new file call sample_write.json in the same directory and write json data to it.
with open("sample_write.json", "w") as file:
    new_json_file = file_data
    new_json_file["code"] = 300
    json.dump(new_json_file, file, ensure_ascii=False, indent=2, sort_keys=True)
    print(new_json_file)

print("Content from data.successContents")
successContents = file_data["data"]["successContent"]
for content in successContents:
    print(content["label_en"], content["value"])

# Create new file call sample_without_success_content.json, remove object "successContent" in data and write to it.
with open("sample_without_success_content.json", "w") as file:
    del file_data["data"]["successContent"]
    json.dump(file_data, file, ensure_ascii=False, indent=2, sort_keys=True)


sample_api_url = "https://api.restful-api.dev/objects"
with urlopen(sample_api_url) as response:
    source = response.read()

url_data = json.loads(source)
print(json.dumps(url_data, indent=2))

for item in url_data:
    print("id:", item["id"], "name:", item["name"], "data:", item["data"], sep="|")

filtered_items = list(filter(lambda item: item["data"] == None, url_data))
print(filtered_items)
print(url_data)
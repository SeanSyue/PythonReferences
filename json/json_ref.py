# https://www.youtube.com/watch?v=9N6a-VLBa2I&t=8s
import json

people_string = """
{
  "people": [
    {
      "name": "John Smith", 
      "phone": "615-665-4324", 
      "emails": ["johnsmith@gogusemail.com", "john.smith@work-place.com"], 
      "has_licence": false
    }, 
    {
      "name": "Jane Doe", 
      "phone": "553-432-4242", 
      "emails": null, 
      "has_license": true
    }
  ]
}
"""

data = json.loads(people_string)
print(data)

for person in data['people']:
    print(person['name'])
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)
print(new_str)

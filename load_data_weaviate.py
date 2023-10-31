import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080",
)

f =  open("./cleaned_data.json")
data = json.load(f)

client.batch.configure(batch_size=len(data)) 
with client.batch as batch:
    for obj in data:
        batch.add_data_object(data_object=obj, class_name="Resource")
        
f.close()
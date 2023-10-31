class_obj = {
    "class": "Resource",
    "vectorizer": "text2vec-contextionary",
    "moduleConfig": {
        "text2vec-contextionary": {
          "vectorizeClassName": False
        }
      },
      "properties": [
        {
          "name": "title",
          "dataType": [
            "text"
          ],
          "description": "Title of resource",
          "moduleConfig": {
            "text2vec-contextionary": {
              "skip": True,
              "vectorizePropertyName": False
            }
          }
        },
        {
          "name": "url",
          "dataType": [
            "text"
          ],
          "description": "URL of resource",
          "moduleConfig": {
            "text2vec-contextionary": {
              "skip": True,
              "vectorizePropertyName": False
            }
          }
        },
        {
          "name": "content",
          "dataType": [
            "text"
          ],
          "description": "Content of resource",
          "moduleConfig": {
            "text2vec-contextionary": {
              "skip": False,
              "vectorizePropertyName": True
            }
          }
        }
      ]
}


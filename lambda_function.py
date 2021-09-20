import json

def lambda_handler(event, context):
    text = json.loads(event["body"])["text"].lower()

    if text:
        result = {
            "textLength": {
                "withSpaces": len(text),
                "withoutSpaces": len(text.replace(" ", ""))
            },
            "wordCount": len(text.split()),
        }
        charDict = {}
        for c in [x for x in text if x.isalpha()]:
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1
        
        characterCount = []
        keys = list(charDict.keys())
        keys.sort()
        for c in keys:
            characterCount.append({c: charDict[c]})
        
        result["characterCount"] = characterCount

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    else:
        #couldn't find a way of reliably detecting if the text parameter is present
        # because if the text is empty the parameter is not passed!!
        return {
            'statusCode': 200,
            'body': json.dumps({
                "textLength": {
                    "withSpaces": 0,
                    "withoutSpaces": 0
                },
                "wordCount": 0,
                "characterCount": []
            })
        }

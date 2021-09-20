

def analyzeText(text):
    text = str(text)
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
    return result
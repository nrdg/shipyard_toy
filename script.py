with open("text.txt","r") as f:
    data = f.read()
    result = len(data)
    
with open("result.txt","w") as out:
    out.write(result)
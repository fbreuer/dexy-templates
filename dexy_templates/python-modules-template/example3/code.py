### @export "fix-python-path"
import sys
sys.path.append("..")

### @export "read"
import json
f = open("data1.json")
print json.load(f)["hello"]
f.close()

### @export "write"
f = open("output.json","w")
json.dump([1,2,3],f)
f.close()

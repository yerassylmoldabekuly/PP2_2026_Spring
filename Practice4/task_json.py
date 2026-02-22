#JSON is a syntax for storing and exchanging data.

import json

with open("sample-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 95)
print(f'{"DN":55} {"Description":15} {"Speed":8} {"MTU":5}')
print("-" * 95)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs["dn"]
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:55} {descr:15} {speed:8} {mtu:5}")
import requests
import OMMCOLLECTION

xOMM = requests.get("http://208.87.130.67:3000/spacedata/latest/omm/0x9858effd232b4033e47d90003d41ec34ecaeda94?format=fbs")

yOMMCOLLECTION = OMMCOLLECTION.OMMCOLLECTION.GetRootAsOMMCOLLECTION(xOMM.content)

for yOMM in range(yOMMCOLLECTION.RECORDSLength()):
    yOMMRECORD = yOMMCOLLECTION.RECORDS(yOMM)
    print(yOMMRECORD.NORAD_CAT_ID())
import OMMCOLLECTION
import OMM
import flatbuffers

provider_eth_address = "0x9858EfFD232B4033E47d90003D41EC34EcaEda94"
fb_cid = "QmepW1hutjHdrPMhWBJCyinz8bfjtJ3WKsspb5vvcD6DTz"
pdFP = f"{provider_eth_address}/{fb_cid}.OMM.fbs"

# Load OMMCOLLECTION from file
with open("data/"+pdFP, "rb") as f:
    xOMM = f.read()

# Load the signature from a text file
with open("data/"+pdFP+".sig", "r") as f:
    signature = f.read()

# check if the signature starts with "0x" and remove it if so
if signature.startswith("0x"):
    signature = signature[2:]

yOMMCOLLECTION = OMMCOLLECTION.OMMCOLLECTION.GetRootAsOMMCOLLECTION(xOMM)

for yOMM in range(yOMMCOLLECTION.RECORDSLength()):
    yOMMRECORD = yOMMCOLLECTION.RECORDS(yOMM)
    print(yOMMRECORD.NORAD_CAT_ID())

# create OMM object
ommt = OMM.OMMT()

# set OMM object properties
ommt.NORAD_CAT_ID = 25544
ommt.OBJECT_NAME = "ISS (ZARYA)"
ommt.OBJECT_ID = "1998-067A"
ommt.EPOCH = "2023-01-03T12:36:01.932768"
ommt.MEAN_MOTION = 15.49892242
ommt.ECCENTRICITY = 0.0005004
ommt.INCLINATION = 51.6453
ommt.RA_OF_ASC_NODE = 64.1711
ommt.ARG_OF_PERICENTER = 218.5032
ommt.MEAN_ANOMALY = 238.7671
ommt.EPHEMERIS_TYPE = 0
ommt.CLASSIFICATION_TYPE = "U"
ommt.ELEMENT_SET_NO = 999
ommt.REV_AT_EPOCH = 37625
ommt.BSTAR = 0.00030219
ommt.MEAN_MOTION_DOT = 0.00016767
ommt.MEAN_MOTION_DDOT = 0

# create builder and pack OMM properties
builder = flatbuffers.Builder(1024)
ISS_BUILT = ommt.Pack(builder)
builder.Finish(ISS_BUILT)
buf = builder.Output()

OMMCOLLECTION.StartRECORDSVector(builder, 1)
builder.PrependUOffsetTRelative(ISS_BUILT)
SATS = builder.EndVector()
OMMCOLLECTION.Start(builder)
OMMCOLLECTION.AddRECORDS(builder, SATS)
OMMC_BUILT = OMMCOLLECTION.End(builder)
builder.Finish(OMMC_BUILT)
ommc_buf = builder.Output()

ISS = OMM.OMM.GetRootAs(buf, 0)
print("CREATED OMM FOR ISS", ISS.NORAD_CAT_ID())

OMMC = OMMCOLLECTION.OMMCOLLECTION.GetRootAs(ommc_buf, 0)
print("CREATED OMMCOLLECTION, ADDED ISS", OMMC.RECORDS(0).NORAD_CAT_ID())

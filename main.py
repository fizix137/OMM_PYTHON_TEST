import requests
import OMMCOLLECTION
import OMM
import flatbuffers

with open("data/0x9858EfFD232B4033E47d90003D41EC34EcaEda94/QmepW1hutjHdrPMhWBJCyinz8bfjtJ3WKsspb5vvcD6DTz.OMM.fbs", "rb") as f:
    xOMM = f.read()

yOMMCOLLECTION = OMMCOLLECTION.OMMCOLLECTION.GetRootAsOMMCOLLECTION(
    xOMM)

for yOMM in range(yOMMCOLLECTION.RECORDSLength()):
    yOMMRECORD = yOMMCOLLECTION.RECORDS(yOMM)
    print(yOMMRECORD.NORAD_CAT_ID())

builder = flatbuffers.Builder(1024)
ISS_OBJECT_NAME = builder.CreateString("ISS (ZARYA)")
ISS_OBJECT_ID = builder.CreateString("1998-067A")
ISS_OBJECT_EPOCH = builder.CreateString("2023-01-03T12:36:01.932768")
ISS_OBJECT_CLASSIFICATION_TYPE = builder.CreateString("U")

OMM.Start(builder)
OMM.AddNORAD_CAT_ID(builder, 25544)
OMM.AddOBJECT_NAME(builder, ISS_OBJECT_NAME)
OMM.AddOBJECT_ID(builder, ISS_OBJECT_ID)
OMM.AddEPOCH(builder, ISS_OBJECT_EPOCH)
OMM.AddMEAN_MOTION(builder, 15.49892242)
OMM.AddECCENTRICITY(builder, 0.0005004)
OMM.AddINCLINATION(builder, 51.6453)
OMM.AddRA_OF_ASC_NODE(builder, 64.1711)
OMM.AddARG_OF_PERICENTER(builder, 218.5032)
OMM.AddMEAN_ANOMALY(builder, 238.7671)
OMM.AddEPHEMERIS_TYPE(builder, 0)
OMM.AddCLASSIFICATION_TYPE(builder, ISS_OBJECT_CLASSIFICATION_TYPE)
OMM.AddNORAD_CAT_ID(builder, 25544)
OMM.AddELEMENT_SET_NO(builder, 999)
OMM.AddREV_AT_EPOCH(builder, 37625)
OMM.AddBSTAR(builder, 0.00030219)
OMM.AddMEAN_MOTION_DOT(builder, 0.00016767)
OMM.AddMEAN_MOTION_DDOT(builder, 0)
ISS_BUILT = OMM.End(builder)
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

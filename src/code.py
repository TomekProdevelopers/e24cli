import hashlib
import base64
m = hashlib.sha256('/0BOSvMRmcEyf3UQ6F920Qvt2nTU64CMBMel4Xvl'.encode('utf-8')).hexdigest()
print(base64.b64encode(m))




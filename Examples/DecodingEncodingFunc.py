#DecodingEncodingFunc

import base64

#Encoding
Str="Hello World"
Str=base64.b64encode(Str.encode('utf-8'))
print("Encode String: ", Str)

#Decoding
Str=base64.b64decode(Str.decode('utf-8'))
print("Encode String: ", Str)


###The Encoding is always the same thing... ???
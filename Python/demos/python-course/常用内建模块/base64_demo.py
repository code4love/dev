# -*- coding: utf-8 -*-

import base64
print(base64.b64encode(b'binary\x00string'))
#Out: b'YmluYXJ5AHN0cmluZw=='
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#Out: b'binary\x00string'
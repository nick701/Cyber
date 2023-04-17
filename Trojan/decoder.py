# Does not work

import base64

encoded_data = input("Enter the encoded data: ")

# Add padding to the encoded data if necessary
padding = len(encoded_data) % 4
if padding != 0:
    encoded_data += "=" * (4 - padding)

decoded_data = base64.b64decode(encoded_data)
print(decoded_data.decode("utf-8"))

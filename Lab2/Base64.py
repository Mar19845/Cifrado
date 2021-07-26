import base64
  

def stringToBase64(text):
    sample_string_bytes = text.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def Base64ToString(text):
    base64_bytes = text.encode("ascii")
    
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return sample_string






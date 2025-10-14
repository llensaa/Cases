import re

#1

#2

#3
def find_system_info(text) -> dict[str, list[str]]:
    '''
    Finds system information
    Return: {'ips': [], 'files': [], 'emails': []}
    '''
    result = {
        'ips': [],
        'files': [],
        'emails': []
    }
    
    email_pattern = r'\b[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?@[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+\b'
    
    for match in re.finditer(email_pattern, text):
        email = match.group()
        if email not in result['emails']:
            result['emails'].append(email)
    
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
  
    for match in re.finditer(ip_pattern, text):
        ip = match.group()
        octets = ip.split('.')
        valid = all(0 <= int(octet) <= 255 for octet in octets)
        if valid and ip not in result['ips']:
            result['ips'].append(ip)

    file_pattern = r'\b\w+\.(txt|pdf|doc|docx|xls|xlsx|ppt|pptx|jpg|jpeg|png|gif|zip|rar|exe|dll|sys|log|config|ini|xml|json|csv|py|js|html|css)\b'
    file_matches = re.finditer(file_pattern, text, re.IGNORECASE)
    
    for match in file_matches:
        filename = match.group()
        if filename not in result['files']:
            result['files'].append(filename)
    
    return result

#4
def decode_messages(text) -> dict[str, list[str]]:
    """
    Finds and decodes messages
    Return: {'base64': [], 'hex': [], 'rot13': []}
    """
    result = {
        'base64': [],
        'hex': [],
        'rot13': []
    }
    
    base64_pattern = r'[A-Za-z0-9+/]{4,}={0,2}'
    
    for match in re.finditer(base64_pattern, text):
        base64_string = match.group()
        try:
            decoded_bytes = base64.b64decode(base64_string)
            decoded_text = decoded_bytes.decode('utf-8')
            if len(decoded_text) > 1:
                result['base64'].append(f"{base64_string} -> {decoded_text}")
        except (base64.binascii.Error, UnicodeDecodeError, ValueError):
            pass


    hex_escape_pattern = r'(?:\\x[0-9A-Fa-f]{2})+'
    
    for match in re.finditer(hex_escape_pattern, text):
        hex_escape_string = match.group()
        try:
            hex_only = hex_escape_string.replace(r'\x', '')
            if len(hex_only) % 2 != 0:
                continue
            
            decoded_bytes = bytes.fromhex(hex_only)
            decoded_text = decoded_bytes.decode('utf-8')
            if len(decoded_text) > 1:
                result['hex'].append(f"{hex_escape_string} -> {decoded_text}")
        except (ValueError, UnicodeDecodeError):
            pass

    hex_direct_pattern = r'\b(?:0x)?[0-9A-Fa-f]{6,}\b'

    for match in re.finditer(hex_direct_pattern, text):
        hex_string = match.group()
        hex_clean = hex_string[2:] if hex_string.startswith('0x') else hex_string
    
        if len(hex_clean) % 2 != 0:
            continue
        
        try:
            decoded_bytes = bytes.fromhex(hex_clean)
            decoded_text = decoded_bytes.decode('utf-8')
            if len(decoded_text) > 1:
                result['hex'].append(f"{hex_string} -> {decoded_text}")
        except (ValueError, UnicodeDecodeError):
            pass



    def rot13_decode(text) -> str:
        result_rot = []
        for char in text:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                result_rot.append(chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset))
            else:
                result_rot.append(char)
        return ''.join(result_rot)
    
    rot13_pattern = r'\b(?:[a-zA-Z]{1,}(?:\s+[a-zA-Z]{1,})*)\b'
    
    for match in re.finditer(rot13_pattern, text):
        rot13_string = match.group()
        decoded_text = rot13_decode(rot13_string)
        if (decoded_text != rot13_string and 
            len(decoded_text) > 1):
            result['rot13'].append(f"{rot13_string} -> {decoded_text}")
    
    return result
#5

#6


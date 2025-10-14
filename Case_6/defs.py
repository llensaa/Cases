import re

#1

#2

#3
def find_system_info(text):
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
    
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
  
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

#5

#6


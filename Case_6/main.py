import re
import base64
import codecs

def find_and_validate_credit_cards(main_text):
    pass

def find_secrets(main_text):
    pass


def find_system_info(main_text) -> dict[str, list[str]]:
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

    for match in re.finditer(email_pattern, main_text):
        email = match.group()
        if email not in result['emails']:
            result['emails'].append(email)

    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

    for match in re.finditer(ip_pattern, main_text):
        ip = match.group()
        octets = ip.split('.')
        valid = all(0 <= int(octet) <= 255 for octet in octets)
        if valid and ip not in result['ips']:
            result['ips'].append(ip)

    file_pattern = r'\b\w+\.(txt|pdf|doc|docx|xls|xlsx|ppt|pptx|jpg|jpeg|png|gif|zip|rar|exe|dll|sys|log|config|ini|xml|json|csv|py|js|html|css)\b'
    file_matches = re.finditer(file_pattern, main_text, re.IGNORECASE)

    for match in file_matches:
        filename = match.group()
        if filename not in result['files']:
            result['files'].append(filename)

    return result

def decode_messages(main_text):
    pass

def analyze_logs(log_text) -> dict:
    sql_injection_patterns = [
        r'(\%27)|(\')|(\-\-)|(\%23)|(#)',  # ' or -- or #
        r'((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))',  # =’ or =--
        r'\b(OR|AND)\b.+\b(=|LIKE)\b',  # OR 1=1
        r'UNION\s+SELECT',  # UNION SELECT
        r'INSERT\s+INTO', r'UPDATE\s+\w+', r'DELETE\s+FROM'
    ]

    xss_patterns = [
        r'<script.*?>.*?</script.*?>',  # <script>...</script>
        r"on\w+\s*=\s*['\"]?.*?['\"]?",  # onerror=, onclick=, etc.
        r'<.*?javascript:.*?>',         # <a href="javascript:...">
        r'document\.cookie',
        r'<iframe.*?>',
        r'<img\s+.*?onerror\s*=.*?>'
    ]

    suspicious_user_agents_keywords = [
        'sqlmap', 'nmap', 'nikto', 'curl', 'wget', 'hydra', 'fuzzer', 'python-requests', 'nobody'
    ]

    failed_login_patterns = [
        r'login\s+failed', r'authentication\s+failure', r'invalid\s+password', r'401\s+Unauthorized'
    ]

    results = {
        'sql_injections': [],
        'xss_attempts': [],
        'suspicious_user_agents': [],
        'failed_logins': []
    }

    lines = log_text.splitlines()

    for line in lines:
        lower_line = line.lower()

        for pattern in sql_injection_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                results['sql_injections'].append(line)
                break

        for pattern in xss_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                results['xss_attempts'].append(line)
                break

        if "user-agent" in lower_line:
            for keyword in suspicious_user_agents_keywords:
                if keyword in lower_line:
                    results['suspicious_user_agents'].append(line)
                    break

        for pattern in failed_login_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                results['failed_logins'].append(line)
                break

    return results


def normalize_and_validate(messy_data):
    pass


def generate_comprehensive_report(main_text, log_text, messy_data) -> dict:
    report = {
        'financial_data': find_and_validate_credit_cards(main_text),
        'secrets': find_secrets(main_text),
        'system_info': find_system_info(main_text),
        'encoded_messages': decode_messages(main_text),
        'security_threats': analyze_logs(log_text),
        'normalized_data': normalize_and_validate(messy_data)
    }
    return report


def print_report(report):
    print('=' * 50)
    print('ОТЧЕТ ОПЕРАЦИИ \'DATA SHIELD\'')
    print('=' * 50)

    sections = [
        ('ФИНАНСОВЫЕ ДАННЫЕ', report['financial_data']),
        ('СЕКРЕТНЫЕ КЛЮЧИ', report['secrets']),
        ('СИСТЕМНАЯ ИНФОРМАЦИЯ', report['system_info']),
        ('РАСШИФРОВАННЫЕ СООБЩЕНИЯ', report['encoded_messages']),
        ('УГРОЗЫ БЕЗОПАСНОСТИ', report['security_threats']),
        ('НОРМАЛИЗОВАННЫЕ ДАННЫЕ', report['normalized_data'])
    ]

    for title, data in sections:
        print(f'\n{title}:')
        print('-' * 30)


if __name__ == '__main__':
    with open('data_leak_sample.txt', 'r', encoding='utf-8') as f:
        main_text = f.read()

    with open('web_server_logs.txt', 'r', encoding='utf-8') as f:
        log_text = f.read()

    with open('messy_data.txt', 'r', encoding='utf-8') as f:
        messy_data = f.read()

    report = generate_comprehensive_report(main_text, log_text, messy_data)
    print_report(report)

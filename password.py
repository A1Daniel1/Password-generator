from hashlib import sha256

def create_password(service, master_key):
    password = sha256(master_key.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()[:10]
    return password


def get_password(master_key, service):
    return create_password(service, master_key)

def add_password(service, master_key):
    return create_password(service, master_key)


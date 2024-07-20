import sys

def update_config(user_id):
    with open('config.py', 'r') as f:
        config = f.read()

    config = config.replace('ALLOWED_USERS = [', f'ALLOWED_USERS = [{user_id}, ')

    with open('config.py', 'w') as f:
        f.write(config)

if __name__ == "__main__":
    user_id = sys.argv[1]
    update_config(user_id)
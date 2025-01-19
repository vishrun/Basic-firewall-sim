import random

def generate_ip():
    return f'192.168.1.{random.randint(1,20)}'

def check_action(ip, rules):
    for rule_ip, actions in rules.items():
        if rule_ip == ip:
            return actions
    return "Allow"

def main():
    print('hi')
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }
       
    for _ in range(0,12):
        ip_addr= generate_ip()
        action = check_action(ip_addr,firewall_rules)
        print(f'IP address {ip_addr} , Actions- {action} , Random- {random.randint(0,9999)}')

if __name__ == "__main__":
    main()
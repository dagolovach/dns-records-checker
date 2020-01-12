#!/usr/bin/env python3

"""Module docstring. bbest"""

# Imports
import dns.resolver
import dns.reversename


# Module Functions and Classes
class DnsRecordChecker:

    def __init__(self, name_check, req_type, name_servers):
        self.name_check = name_check
        self.req_type = req_type
        self.name_servers = name_servers.split(" ")

    def check_a_record(self):
        my_resolver = dns.resolver.Resolver()
        my_resolver.timeout = 1.0
        domain = self.name_check
        for each in self.name_servers:
            server_result = []
            my_resolver.nameservers = [each]
            try:
                answers = my_resolver.query(domain, self.req_type)
                for server in answers:
                    server_result.append(str(server))
            except dns.exception.Timeout:
                print(f'Timeout for {each}')

            print(f"===> On {each} ===> {domain} is {server_result}")

    def check_ptr_record(self):
        my_resolver = dns.resolver.Resolver()
        addr = dns.reversename.from_address(self.name_check)
        for each in self.name_servers:
            server_result = []
            my_resolver.nameservers = [each]
            try:
                answers = my_resolver.query(addr, self.req_type)
                for server in answers:
                    server_result.append(str(server))
            except dns.exception.Timeout:
                print(f'Timeout for {each}')

            print(f"===> On {each} ===> {self.name_check} is {server_result}")


def main(name_check, req_type, name_servers):
    """Main script function."""

    a = DnsRecordChecker(name_check, req_type, name_servers)
    if req_type == 'A':
        a.check_a_record()
    elif req_type == "PTR":
        a.check_ptr_record()
    else:
        print("Not Supported")

    return


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main("yahoo.com", "A", "3.45.48.15 8.8.8.8")
'''
    if len(sys.argv) < 4:
        raise SyntaxError("Insufficient arguments.")
    #if len(sys.argv) != 3:
    #    # If there are keyword arguments
    #    main(sys.argv[1], sys.argv[2], *sys.argv[3:])
    else:
        # If there are no keyword arguments
        main(sys.argv[1], sys.argv[2], ' '.join(sys.argv[3:]))
'''
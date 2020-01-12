#!/usr/bin/env python3

"""Module docstring. Test"""

# Imports
import dns.resolver
import dns.reversename


# Module Functions and Classes
class DnsRecordChecker:
    """Creating the class with:

    name_check = IP address or FQDN
    name_servers = IP addresses of DNS servers records need to be check at
    req_type = A/PTR type
    """

    def __init__(self, name_check, req_type, name_servers):
        self.name_check = name_check
        self.req_type = req_type
        self.name_servers = name_servers.split(" ")

    def check_a_record(self):
        """Function to check the A record"""

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
        """Function to check the PTR record"""

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
    """Main script function"""

    name_to_check = DnsRecordChecker(name_check, req_type, name_servers)
    if req_type == 'A':
        name_to_check.check_a_record()
    elif req_type == "PTR":
        name_to_check.check_ptr_record()
    else:
        print("Not Supported")

    return


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main("yahoo.com", "A", "8.8.8.8 8.8.4.4")
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
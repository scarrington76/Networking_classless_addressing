import re

class Problem ():

    def __init__(self, slash):
        self.slash = slash
        self.n = 0
        self.ipsplit = []
        self.ipstring = ''

    def solve(self): ## Main function to solve the problem
        self.get_n()
        self.ip_to_bin()
        self.ipstring = ''.join(self.ipsplit)
        self.get_prefix_and_suffix()

    def get_n(self): ## Gets the n value for the problem by splitting it off the address
        split = self.slash.split('/')
        self.n = int(split[1])
        print ('N value is: ' + str(self.n))

    def ip_to_bin(self): ## Converts ip address to list of binary numbers
        self.ipsplit = re.split('[./]', self.slash)
        for i in range(0, len(self.ipsplit)):
            self.ipsplit[i] = int(self.ipsplit[i])
            self.ipsplit[i] = '{0:08b}'.format(self.ipsplit[i])
        self.ipsplit.pop(-1)

    def get_prefix_and_suffix(self): ## Splits prefix and suffixes based on n and acquires first/last addresses
        prefix = list(self.ipstring)
        suffix = list(self.ipstring)
        for i in range(self.n, len(prefix)):
            prefix[i] = 0
            suffix[i] = 1
        print ('First address is: ' + str(self.list_to_ip(prefix)))
        print ('Last address is: ' + str(self.list_to_ip(suffix)))

    def bin_to_int(self, b): ## Function to convert number from binary base 2 into int
        return (int(b, 2))

    def list_to_ip(self, s): ##Converts list of binary numbers back into IP address
        result = ''
        r = ''
        count = 0
        for ele in s:
            r = r + str(ele)
            count += 1
            if count in (8, 16, 24, 32):
                x = self.bin_to_int(r)
                result = result + str(x) + '.'
                r = ''  
        return result[:-1]   

slash = input('Enter the slash notation (xx.xx.xx.xx/xx) address: ')
print ('The address you input is: ' + slash)
p = Problem(slash)
p.solve()



from Tool_functions import dec2bin, and_function, bin2dec


class IPv4:
    def __init__(self, ip_addr):
        self.ipv4_addr = ip_addr
        self.decimal_int_list = self.ipv4_addr.split('.')
        self.binary_int_list = []
        self.cal_bin_list()

    def cal_bin_list(self):
        for dec_num in self.decimal_int_list:
            dec_num = int(dec_num)
            self.binary_int_list.append(dec2bin(dec_num))

    def if_the_same_ip(self, ipv4):
        return self.ipv4_addr == ipv4.ipv4_addr

    def cal_and(self, ipv4):
        binary_list = []
        for bin_1, bin_2 in zip(self.binary_int_list, ipv4.binary_int_list):
            binary_list.append(and_function(bin_1, bin_2))
        ipv4_addr = ''
        for bin_num in binary_list:
            ipv4_addr += bin2dec(bin_num)
            ipv4_addr += '.'
        ipv4_addr = ipv4_addr[:-1]
        new_ipv4 = IPv4(ipv4_addr)
        return new_ipv4
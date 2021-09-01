import pandas as pd
from IPv4 import IPv4


class RouterList:
    def __init__(self, path):
        self.router_list = pd.read_csv(path)
        self.destination_network_list = self.create_ip_list('目的网络')
        self.subnet_mask_list = self.create_ip_list('子网掩码')
        self.next_list = self.router_list['下一跳'].tolist()
        self.length = len(self.next_list)

    def create_ip_list(self, label):
        ip_list = self.router_list[label].tolist()
        output_list = []
        for ip_addr in ip_list:
            if ip_addr == 'None':
                output_list.append('None')
                continue
            ipv4 = IPv4(ip_addr)
            output_list.append(ipv4)
        return output_list

    def match_network(self, ipv4):
        my_next_step = ''
        for des_net, sub_net, next_step in zip(self.destination_network_list,
                                               self.subnet_mask_list, self.next_list):
            if des_net == "None" and sub_net == "None":
                my_next_step = next_step
                break
            new_ipv4 = sub_net.cal_and(ipv4)
            if des_net.if_the_same_ip(new_ipv4):
                my_next_step = next_step
                break
        return my_next_step


if __name__ == '__main__':
    path = 'Router list.csv'
    router_list = RouterList(path)
    destination_addr_list = [
        '128.96.39.10',
        '128.96.40.12',
        '128.96.40.151',
        '192.4.153.17',
        '192.4.153.90'
    ]
    IPv4 = [IPv4(i) for i in destination_addr_list]
    my_next_step_list = [router_list.match_network(ipv4) for ipv4 in IPv4]
    print(my_next_step_list)
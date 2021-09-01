def dec2bin(dec):
    """
    input: decimal string
    return: 8 bits binary string
    """
    bin_list = []

    while dec != 0:
        residue = dec % 2
        dec = int(dec / 2)
        bin_list.append(residue)

    bin = ''
    for i in bin_list[::-1]:
        bin += str(i)

    less_bits = 8 - len(bin)
    zero_string = ''
    for i in range(0, less_bits):
        zero_string += '0'
    bin = zero_string + bin
    return bin


def bin2dec(bin):
    """
    input: binary string
    return: decimal string
    """
    dec = 0
    for i, num in enumerate(bin[::-1]):
        dec += int(num) * pow(2, i)
    return str(dec)


def and_function(bin_1, bin_2):
    """
    input: 2 binary strings
    return: one binary string
    """
    and_str = ''
    length = len(bin_1)
    for i in range(0, length):
        result = int(bin_1[i]) and int(bin_2[i])
        and_str += str(result)

    return and_str


# Write a Python program to remove leading zeros from an IP address.

def remove_leading_zeros(ip_address):
    try:
        new_ip = ''
        if ip_address.find('.') :
            new_ip = '.'.join(str(int(i)) for i in ip_address.split('.'))
        else:
            new_ip = '.'.join(str(int(i)) for i in ip_address.split(':'))
    except:
        print('Error')
    return new_ip

ip_address = input('Enter IP address: ')
modified_ip = remove_leading_zeros(ip_address)
print('Correct IP : ', modified_ip)
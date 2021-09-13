def ip_to_ten(ips):
    s = ips.split('.')
    nums = [int(i) for i in s]
    total = 0
    length = len(nums)-1
    for i in nums:
        total += i * 256**length
        length -= 1
    return total


ipaddress = ['192.168.1.2']
ipaddress.sort(key=ip_to_ten)
for i in ipaddress:
    print(i)

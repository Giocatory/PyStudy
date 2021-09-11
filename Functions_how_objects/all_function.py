def correct_IP(text):
    try:
        ip = [int(i) for i in text.split('.')]
        if all(0<=i<=255 for i in ip):
            return True
        else:
            return False
    except:
        return False


# print(all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, input().split('.'))))
def calcMask(user_input):
    subnet_bits = user_input-24
    subnets = 2**(subnet_bits)
    host_bits = (32-user_input)
    dist = 2**(host_bits)
    subnet_address = list()
    broadcast_address = list()

    i=0
    while (i<256):
        subnet_address.append(i)
        broadcast_address.append(i+dist-1)
        i += dist
    print(f"subnets: {subnets}")
    print(f"hosts/subnet: {2**host_bits-2}")
    print("subnet address (last byte): " + " ".join(map(str, subnet_address)))
    print("broadcast_address (last byte): " + " ".join(map(str, broadcast_address)))
    return


def isMask(user_input):

    if (len(user_input) == 2 and int(user_input) <= 30 and int(user_input) >= 25):
        return calcMask(int(user_input))

    try:
        lastByte = int(user_input.split(".")[-1])
        if (lastByte >=0 and lastByte <= 255):
            for i in user_input.split(".", 2):
                if (i == '255'):
                    continue
    except:
        print("Not a valid argument")
        return False

    zeros = 0
    j=0
    lastByte = int(user_input.split(".")[-1])
    try:
        for i in range(7, 0, -1):
            j += 2**i
            if lastByte == j:
                zeros = i
        if zeros != 0:
            return calcMask(32-zeros)
    except:
        print("Not a valid argument")
        return False


def main():
    user_input = input("Type your C class subnet mask:")
    isMask(user_input)


if __name__ == "__main__" :
    main()
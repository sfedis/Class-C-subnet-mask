def single_mask(user_input):

    dist = 2**(32-user_input)
    print(f"subnets: {2**(user_input-24)}")
    print(f"hosts/subnet: {dist-2}")
    print("subnet address (last byte):", end=" ")
    i=0
    while (i<255):
        print(f"{i}", end=" ")
        i += dist
    print("")
    
    print("broadcast address (last byte):", end=" ")
    j=0
    while (j<256):
        print(f"{j+dist-1}", end=" ")
        j += dist
    print("")
    
def whole_mask(user_input):
    zeros = 0
    j=0
    lastByte = int(user_input.split(".")[-1])
    for i in range(7, 0, -1):
        j += 2**i
        if lastByte == j:
            zeros = i
    if zeros != 0:
        single_mask(32-zeros) 
    else:
        print("Not a valid argument")
    return

def isMask(user_input):
    try:
        lastByte = int(user_input.split(".")[-1])
        if (lastByte >=0 and lastByte <= 255):
            for i in user_input.split(".", 2):
                if (i == '255'):
                    continue
            return True
    except:
        return False

def main():
    user_input = input("Type your C class subnet mask:")

    if (len(str(user_input)) == 2 and int(user_input) <= 30 and int(user_input) >= 25):
        single_mask(int(user_input))
        return
    
    #check if input is valid mask
    if (isMask(user_input)):
        whole_mask(user_input)
        return
    else:
        print("Not a valid argument")


if __name__ == "__main__" :
    main()
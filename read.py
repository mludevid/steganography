import sys
import wave

def decode_message(input_bytes):
    input_array = list(input_bytes)
    message = []
    
    count = 0
    char = 0
    for i in input_array:
        char += 1 & i
        if count == 7:
            if char == 0:
                break
            message.append(char)
            char = 0
            count = 0
        else:
            char <<= 1
            count += 1

    return bytes(message).decode()



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You need to provide an arguments: filename (in parenthesis if more than one word).")
        exit()

    origin = wave.open(sys.argv[1], 'rb')

    print(decode_message(origin.readframes(origin.getnframes())))
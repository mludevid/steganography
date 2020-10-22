import sys
import wave

def encode_message(input_bytes, message):
    input_array = list(input_bytes)
    message_array = list(message.encode())
    if len(input_array) < 8 * len(message_array):
        raise OverflowError("Message too large for the input file.")

    count = 0
    for m in message_array:
        for i in range(8):
            input_array[count] |= (128 & m) >> 7
            m <<= 1
            count += 1

    return bytes(input_array)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("You need to provide 2 arguments: filename and message (in parenthesis if more than one word).")
        exit()
    origin = wave.open(sys.argv[1], 'rb')
    output = wave.open(sys.argv[1].replace('.wav', '_message.wav'), 'wb')

    output.setparams((origin.getnchannels(), origin.getsampwidth(), origin.getframerate(), origin.getnframes(), 'NONE', origin.getcompname()))

    output.writeframesraw(encode_message(origin.readframes(origin.getnframes()), sys.argv[2]))

    origin.close()
    output.close()
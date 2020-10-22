# Steganography

Stores a string in a .wav audio file. Since it only uses the least significant bit the modification can not be perceived. Easily expandable to other file formats since it works with bytes.

## Example usage:
```
python write.py "audios/mySong.wav" "Hello World!"
```
This encodes the message "Hello World!" into the file mySong.wav and produces a file called mySong_message.wav.

```
python read.py "audios/mySong_message.wav"
# Hello World!
```
This decodes the message from the file.

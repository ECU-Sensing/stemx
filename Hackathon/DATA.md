![CIEI](../images/ciei.jpg)
# Data Format for Hack-A-Thon 2023

For the Hack-A-Thon, the data you collect and send via the LoRaWAN network must adhere to the following format:

```python
[featherid, piece_count, piece_category]
```

- `featherid`: This should be a unique identifier for each Feather device used by your team. This will help identify which device the data is coming from.
- `piece_count`: This field should contain the count of the chess piece category detected by your ML code.
- `piece_category`: This field should indicate the category of the chess piece you are counting. For instance, this could be 'pawn', 'queen', 'bishop', etc., depending on the pieces you are identifying with your image capturing ML code. ***Check the datasources on [Roboflow](https://universe.roboflow.com/joseph-nelson/chess-pieces-new) to see the categories available in the dataset.***



The data in this format should be prepackaged as a bytearray in the `get_data()` function in your `data.py` script.

## Bytearray and Bit Shifting

The bytearray is used because it is a mutable sequence of integers in the range 0 <= x < 256. It's efficient and saves memory for large amounts of data.

You may notice this operation in the `get_data()` function:

```python
(temp_val >> 8) & 0xff
```

This is a bit shift operation followed by a bitwise AND operation. 

- The `>>` operator shifts the bits of `temp_val` to the right by 8 bits. This essentially divides `temp_val` by 2^8, giving the most significant byte (MSB) of the value.

- The `&` operator performs a bitwise AND operation. `0xff` is a hexadecimal value equivalent to 255 in decimal. The operation `& 0xff` effectively keeps only the least significant byte (LSB) of the value.

These operations are used to split a 16-bit integer value into two bytes, which can then be stored efficiently in the bytearray. They are necessary for numbers, which can be larger than what a single byte can hold. Each byte can represent a number in the range 0-255. If a number is larger than 255, it cannot be represented by a single byte and needs to be split into multiple bytes.

## Strings and Bytearrays

Strings are different from numbers. Each character in a string is already represented by a certain number of bytes (usually 1 byte for ASCII characters, and 2-4 bytes for Unicode characters). Therefore, there is no need to perform bit shifting on strings.

To convert a string to a bytearray in Python, you can use the `bytearray()` function and provide the string and its encoding as arguments. Here is an example:

```python
# Convert a string to a bytearray
string = "Hello, World!"
byte_array = bytearray(string, 'utf-8')
```

In this code, `'utf-8'` is the character encoding used to convert the string to bytes. UTF-8 is a widely used character encoding that can represent any character in the Unicode standard, yet is backward-compatible with ASCII. It is the default encoding used by Python.

<div style="display: flex; justify-content: space-between;">
  <img src="../images/stemx.png" width="30%" height="10%" />
  <img src="../images/PoweredByPITON.png" width="30%" height="10%"/> 
</div>


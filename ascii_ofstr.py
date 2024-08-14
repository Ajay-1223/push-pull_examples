def string_to_ascii_array(string):
    ascii_codes = []
    for char in s:
       ascii_codes.append(ord(char))

    return ascii_codes
s='hello,ajay'
ascii_code=string_to_ascii_array(s)
print(ascii_code)

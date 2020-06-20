import codecs


def encode(text, user_key):
    return codecs.encode(encode_or_decode(text, user_key), "unicode_escape")


def decode(cipher, user_key):
    return encode_or_decode(codecs.decode(cipher, "unicode_escape"), user_key)


def encode_or_decode(text, user_key):
    result = ""
    index = 0
    for c in text:
        xored = ord(c) ^ get_key_ord(user_key, index)
        result += chr(xored)
        index += 1
    return result


def get_key_ord(user_key, index):
    return ord(user_key[index % len(user_key)])


if __name__ == '__main__':
    user_key = "test"
    cipher = encode("encode this", user_key)
    print(cipher)
    text = decode(cipher, user_key)
    print(text)
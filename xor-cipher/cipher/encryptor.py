import itertools

class XorEncryptor:

    def __init__(self):
        self.valid_decrypted_range = range(32, 127)
        self.valid_ascii_key_range = range(97, 123)

    def xor_encrypt(self, plain_text, key):
        cipher_nums = []
        for i in range(len(plain_text)):
            ascii_cipher = ord(plain_text[i]) ^ ord(key[i % len(key)])
            cipher_nums.append(ascii_cipher)
        return cipher_nums

    def xor_decrypt(self, encrypted_text, key):
        decrypted = ''
        for i in range(len(encrypted_text)):
            ascii_decrypted = int(encrypted_text[i]) ^ ord(key[i % len(key)])
            decrypted += chr(ascii_decrypted)
        return decrypted

    def guess_key(self, encrypted_text, key_size):
        for possible_key in self.key_generator(key_size):
            possible_key = self.convert_from_ascii(possible_key)
            if possible_key == 'yz':
                print('')
            if self.validate_decrypted(self.xor_decrypt(encrypted_text, possible_key)):
                yield possible_key

    def key_generator(self, key_size):
        for combo in itertools.combinations(self.valid_ascii_key_range, key_size):
            for perm in itertools.permutations(combo):
                yield perm

    def validate_decrypted(self, decrypted):
        for ascii_char in decrypted:
            if ord(ascii_char) not in self.valid_decrypted_range:
                return False
        return True

    def convert_from_ascii(self, ascii_arr):
        plain_text = ''
        for val in ascii_arr:
            plain_text += chr(val)
        return plain_text

    def convert_to_ascii(self, plain_text):
        ascii_arr = []
        for char in plain_text:
            ascii_arr.append(ord(char))
        return ascii_arr

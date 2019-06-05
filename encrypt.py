def encrypt_this(text):
    return " ".join(filter(None, [''.join([str(ord(word[0])) if len(word) else '', word[-1] if len(word) > 1 else '',
                    ''.join([word[2:-1], word[1]]) if len(word) > 2 else ''])
                    for word in text.split(" ")])) \
            if text else ''

print(encrypt_this("  T a "))

from base64 import b64encode


def embed_image(image_path):
    file = open(image_path, 'rb')
    image = file.read()

    image_encoded = b64encode(image).decode('ascii')
    out = 'data:image/png;base64, {0}'.format(image_encoded)

    file.close()

    return out
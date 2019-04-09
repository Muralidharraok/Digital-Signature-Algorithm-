from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA1

def generate():
    # Create a new DSA key
    key = DSA.generate(1024)
    f = open("public_key.pem", "wb")
    f.write(key.publickey().export_key())
    f.close()
    return key

def sign(msg, key):
    # Sign a message
    message = msg.encode()
    hash_obj = SHA1.new(message)
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

def authenticate(msg, signature):
    # Load the public key
    message = msg.encode()
    f = open("public_key.pem", "r")
    hash_obj = SHA1.new(message)
    pub_key = DSA.import_key(f.read())
    verifier = DSS.new(pub_key, 'fips-186-3')

    # Verify the authenticity of the message
    try:
        verifier.verify(hash_obj, signature)
        print ("The message is authentic.")
    except ValueError:
        print("The message is not authentic.")

#demo purpose

#sender
k = generate()
print(k.domain())
m = "123456123456123456123456123456123456123456123456123456123456123456123456"
s = sign(m,k)
#receiver
mm = "hi my name  murali"
authenticate(mm, s)

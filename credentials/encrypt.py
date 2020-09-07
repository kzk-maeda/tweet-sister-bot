import boto3
from boto3.session import Session
import yaml

# Encrypt a data key

KEY_ALIAS="twitter-key"
KEYID=f"arn:aws:kms:ap-northeast-1:728291782722:alias/{KEY_ALIAS}"


def encrypt(kms, text):
    response = kms.encrypt(
        KeyId=KEYID,
        Plaintext=text
    )
    ciphertext = response['CiphertextBlob'] 
    return ciphertext


def decrypt(kms, encrypted_text):
    response = kms.decrypt(
        KeyId=KEYID,
        CiphertextBlob=encrypted_text
    )
    plaintext = response['Plaintext']
    return plaintext


if __name__ == "__main__":
    # load raw credentials
    with open('./raw_credentials.yml', 'r') as yml:
        credentials = yaml.load(yml, Loader=yaml.FullLoader)

    # get kms session
    session = Session(
        profile_name='kzk-serverless'
    )
    kms_client = session.client('kms')

    # encrypt credentials
    ## customer_key
    encrypted_ck = encrypt(kms_client, credentials.get('customer_key'))
    print(f'customer_key : {encrypted_ck}')
    ## customer_secret_key
    encrypted_csk = encrypt(kms_client, credentials.get('customer_secret_key'))
    print(f'customer_secret_key : {encrypted_csk}')
    ## access_token
    encrypted_at = encrypt(kms_client, credentials.get('access_token'))
    print(f'access_token : {encrypted_at}')
    ## access_token_secret
    encrypted_ats = encrypt(kms_client, credentials.get('access_token_secret'))
    print(f'access_token_secret : {encrypted_ats}')

    # output credentials
    encrypted_credentials = {
        'encrypted_customer_key': encrypted_ck,
        'encrypted_customer_secret_key': encrypted_csk,
        'encrypted_access_token': encrypted_at,
        'encrypted_access_token_secret': encrypted_ats
    }

    with open('../src/encrypted_credentials.yml', 'w') as yml:
        yaml.dump(encrypted_credentials, yml, encoding='utf-8')


    # debug
    # plain_ck = decrypt(kms_client, encrypted_ck)
    # print(plain_ck)
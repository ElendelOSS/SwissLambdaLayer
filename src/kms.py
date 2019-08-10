import boto3


class kms:
    def __init__(self, session):
        self.kmsClient = boto3.client(
            'kms',
            aws_access_key_id=session["Credentials"]["AccessKeyId"],
            aws_secret_access_key=session["Credentials"]["SecretAccessKey"],
            aws_session_token=session["Credentials"]["SessionToken"]
        )

    def list_keys(self):
        keys = []
        response = self.kmsClient.list_keys()
        keys.extend(response["Keys"])
        while "NextToken" in response:
            response = self.kmsClient.list_keys()
            keys.extend(response["Keys"])

        return keys

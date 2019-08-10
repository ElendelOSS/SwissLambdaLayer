import json
import boto3


class acm:
    def __init__(self, region):
        self.acmClient = boto3.client('acm', region_name=region)
        self.acmWaiter = self.acmClient.get_waiter('certificate_validated')

    def add_tags_to_certificate(self, CertificateArn, Tags):
        self.acmClient.add_tags_to_certificate(
            CertificateArn=CertificateArn,
            Tags=Tags
        )

    def delete_certificate(self, CertificateArn):
        self.acmClient.delete_certificate(
            CertificateArn=CertificateArn
        )

    def describe_certificate(self, CertificateArn):
        response = self.acmClient.describe_certificate(
            CertificateArn=CertificateArn
        )

        return response

    def export_certificate(self, CertificateArn, Passphrase):
        response = self.acmClient.export_certificate(
            CertificateArn=CertificateArn,
            Passphrase=Passphrase
        )

        return response

    def get_certificate(self, CertificateArn):
        response = self.acmClient.get_certificate(
            CertificateArn=CertificateArn
        )

        return response

    def import_certificate(self, CertificateArn, Certificate, PrivateKey, CertificateChain):
        response = self.acmClient.import_certificate(
            CertificateArn=CertificateArn,
            Certificate=Certificate,
            PrivateKey=PrivateKey,
            CertificateChain=CertificateChain
        )

        return response

    def list_certificates(self):
        certs = []
        response = self.acmClient.list_certificates()
        certs.extend(response["CertificateSummaryList"])
        while "NextToken" in response:
            response = self.acmClient.list_certificates(
                NextToken=response["NextToken"]
            )
            certs.extend(response["CertificateSummaryList"])

        return certs

    def list_tags_for_certificate(self, CertificateArn):
        response = self.acmClient.list_tags_for_certificate(
            CertificateArn=CertificateArn
        )

        return response

    def remove_tags_from_certificate(self, CertificateArn, Tags):
        self.acmClient.remove_tags_from_certificate(
            CertificateArn=CertificateArn,
            Tags=Tags
        )

    def request_certificate(self, DomainName, IdempotencyToken, Options={'CertificateTransparencyLoggingPreference': 'ENABLED'}, ValidationMethod="DNS"):
        response = self.acmClient.request_certificate(
            DomainName=DomainName,
            ValidationMethod=ValidationMethod,
            IdempotencyToken=IdempotencyToken,
            Options=Options
        )

        return response

    def resend_validation_email(self, CertificateArn, Domain, ValidationDomain):
        self.acmClient.resend_validation_email(
            CertificateArn=CertificateArn,
            Domain=Domain,
            ValidationDomain=ValidationDomain
        )

    def update_certificate_options(self, CertificateArn, Options):
        self.acmClient.update_certificate_options(
            CertificateArn=CertificateArn,
            Options=Options
        )

    def wait(self, CertificateArn):
        self.acmWaiter.wait(
            CertificateArn=CertificateArn,
            WaiterConfig={
                "Delay": 10,
                "MaxAttempts": 60
            }
        )

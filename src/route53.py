import json
import boto3


class route53:
    def __init__(self, session):
        self.r53Client = session.client('route53')

    def change_resource_record_sets(self, HostedZoneId, ChangeBatch):
        response = self.r53Client.change_resource_record_sets(
            HostedZoneId=HostedZoneId,
            ChangeBatch=ChangeBatch
        )

        return response

    def create_reusable_delegation_set(self, CallerReference):
        response = self.r53Client.create_reusable_delegation_set(
            CallerReference=CallerReference
        )

        return response

    def create_hosted_zone(self, Name, CallerReference, HostedZoneConfig, DelegationSetId):
        response = self.r53Client.create_hosted_zone(
            Name=Name,
            CallerReference=CallerReference,
            HostedZoneConfig=HostedZoneConfig,
            DelegationSetId=DelegationSetId
        )

        return response

    def get_hosted_zone(self, Id):
        response = self.r53Client.get_hosted_zone(
            Id=Id
        )

        return response

    def list_hosted_zones(self):
        zones = []
        response = self.r53Client.list_hosted_zones()
        zones.extend(response["HostedZones"])
        while response["IsTruncated"]:
            response = self.r53Client.list_hosted_zones(
                Marker=response["NextMarker"]
            )
            zones.extend(response["HostedZones"])

        return zones

    def list_hosted_zones_by_name(self, DNSName):
        zones = []
        response = self.r53Client.list_hosted_zones_by_name(
            DNSName=DNSName
        )
        zones.extend(response["HostedZones"])
        while response["IsTruncated"]:
            response = self.r53Client.list_hosted_zones_by_name(
                DNSName=DNSName,
                Marker=response["NextMarker"]
            )
            zones.extend(response["HostedZones"])

        return zones

    def list_resource_record_sets(self, HostedZoneId):
        records = []
        response = self.r53Client.list_resource_record_sets(
            HostedZoneId=HostedZoneId
        )
        records.extend(response["ResourceRecordSets"])
        while response["IsTruncated"]:
            response = self.r53Client.list_resource_record_sets(
                HostedZoneId=HostedZoneId,
                StartRecordIdentifier=response["NextRecordIdentifier"],
                StartRecordName=response["NextRecordName"],
                StartRecordType=response["NextRecordType"]
            )
            records.extend(response["ResourceRecordSets"])

        return records

    def list_reusable_delegation_sets(self):
        delegation_sets = []
        response = self.r53Client.list_reusable_delegation_sets()
        delegation_sets.extend(response["DelegationSets"])
        while response["IsTruncated"]:
            response = self.r53Client.list_reusable_delegation_sets(
                Marker=response["NextMarker"]
            )
            delegation_sets.extend(response["DelegationSets"])

        return delegation_sets

    def delete_reusable_delegation_set(self, Id):
        self.r53Client.delete_reusable_delegation_set(
            Id=Id
        )

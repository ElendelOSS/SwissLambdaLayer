import boto3
import botocore


class organizations:

    def __init__(self, session):
        self.orgClient = boto3.client(
            'organizations',
            aws_access_key_id=session["Credentials"]["AccessKeyId"],
            aws_secret_access_key=session["Credentials"]["SecretAccessKey"],
            aws_session_token=session["Credentials"]["SessionToken"]
        )

    def accept_handshake(self, HandshakeId):
        response = self.orgClient.accept_handshake(
            HandshakeId=HandshakeId
        )

        return response["Handshake"]

    def attach_policy(self, PolicyId, TargetId):
        self.orgClient.attach_policy(
            PolicyId=PolicyId,
            TargetId=TargetId
        )

    def cancel_handshake(self, HandshakeId):
        response = self.orgClient.cancel_handshake(
            HandshakeId=HandshakeId
        )

        return response["Handshake"]

    def create_account(self, Email, AccountName, RoleName, IamUserAccessToBilling="ALLOW"):
        response = self.orgClient.create_account(
            Email=Email,
            AccountName=AccountName,
            RoleName=RoleName,
            IamUserAccessToBilling=IamUserAccessToBilling
        )

        return response["CreateAccountStatus"]

    def create_organization(self, FeatureSet):
        response = self.orgClient.create_organization(
            FeatureSet=FeatureSet
        )

        return response["Organization"]

    def create_organizational_unit(self, ParentId, Name):
        response = self.orgClient.create_organizational_unit(
            ParentId=ParentId,
            Name=Name
        )

        return response["OrganizationalUnit"]

    def create_policy(self, Content, Description, Name, Type):
        response = self.orgClient.create_policy(
            Content=Content,
            Description=Description,
            Name=Name,
            Type=Type
        )

        return response["Policy"]

    def decline_handshake(self, HandshakeId):
        response = self.orgClient.decline_handshake(
            HandshakeId=HandshakeId
        )

        return response["Handshake"]

    def delete_organization(self):
        self.orgClient.delete_organization()

    def delete_organizational_unit(self, OrganizationalUnitId):
        self.orgClient.delete_organizational_unit(
            OrganizationalUnitId=OrganizationalUnitId
        )

    def delete_policy(self, PolicyId):
        self.orgClient.delete_policy(
            PolicyId=PolicyId
        )

    def describe_account(self, AccountId):
        response = self.orgClient.describe_account(
            AccountId=AccountId
        )

        return response["Account"]

    def describe_create_account_status(self, CreateAccountRequestId):
        response = self.orgClient.describe_create_account_status(
            CreateAccountRequestId=CreateAccountRequestId
        )

        return response["CreateAccountStatus"]

    def describe_handshake(self, HandshakeId):
        response = self.orgClient.describe_handshake(
            HandshakeId=HandshakeId
        )

        return response["Handshake"]

    def describe_organization(self):
        response = self.orgClient.describe_organization()

        return response["Organization"]

    def describe_organizational_unit(self, OrganizationalUnitId):
        response = self.orgClient.describe_organizational_unit(
            OrganizationalUnitId=OrganizationalUnitId
        )

        return response["OrganizationalUnit"]

    def describe_policy(self, PolicyId):
        response = self.orgClient.describe_policy(
            PolicyId=PolicyId
        )

        return response["Policy"]

    def detach_policy(self, PolicyId, TargetId):
        self.orgClient.detach_policy(
            PolicyId=PolicyId,
            TargetId=TargetId
        )

    def disable_aws_service_access(self, ServicePrincipal):
        self.orgClient.disable_aws_service_access(
            ServicePrincipal=ServicePrincipal
        )

    def disable_policy_type(self, RootId, PolicyType):
        response = self.orgClient.disable_policy_type(
            RootId=RootId,
            PolicyType=PolicyType
        )

        return response["Root"]

    def enable_all_features(self):
        response = self.orgClient.enable_all_features()

        return response["Handshake"]

    def enable_aws_service_access(self, ServicePrincipal):
        self.orgClient.enable_aws_service_access(
            ServicePrincipal=ServicePrincipal
        )

    def enable_policy_type(self, RootId, PolicyType):
        response = self.orgClient.enable_policy_type(
            RootId=RootId,
            PolicyType=PolicyType
        )

        return response["Root"]

    def invite_account_to_organization(self, Id, Type, Notes=None):
        response = self.orgClient.invite_account_to_organization(
            Target={
                'Id': Id,
                'Type': Type
            },
            Notes=Notes
        )

        return response["Handshake"]

    def leave_organization(self):
        self.orgClient.leave_organization()

    def list_accounts(self):
        accounts = []
        response = self.orgClient.list_accounts()
        accounts.extend(response["Accounts"])
        while "NextToken" in response:
            response = self.orgClient.list_accounts(
                NextToken=response["NextToken"]
            )
            accounts.extend(response["Accounts"])

        return accounts

    def list_accounts_for_parent(self, ParentId):
        accounts = []
        response = self.orgClient.list_accounts_for_parent(
            ParentId=ParentId
        )
        accounts.extend(response["Accounts"])
        while "NextToken" in response:
            response = self.orgClient.list_accounts_for_parent(
                ParentId=ParentId
            )
            accounts.extend(response["Accounts"])

        return accounts

    def list_aws_service_access_for_organization(self):
        principals = []
        response = self.orgClient.list_aws_service_access_for_organization()
        principals.extend(response["EnabledServicePrincipals"])
        while "NextToken" in response:
            response = self.orgClient.list_aws_service_access_for_organization(
                NextToken=response["NextToken"]
            )
            principals.extend(response["EnabledServicePrincipals"])

        return principals

    def list_children(self, ParentId, ChildType):
        children = []
        response = self.orgClient.list_children(
            ParentId=ParentId,
            ChildType=ChildType
        )
        children.extend(response["Children"])
        while "NextToken" in response:
            response = self.orgClient.list_children(
                ParentId=ParentId,
                ChildType=ChildType,
                NextToken=response["NextToken"]
            )
            children.extend(response["Children"])

        return children

    def list_create_account_status(self, States=['IN_PROGRESS', 'SUCCEEDED', 'FAILED']):
        accounts = []
        response = self.orgClient.list_create_account_status(
            States=States
        )
        accounts.extend(response["CreateAccountStatuses"])
        while "NextToken" in response:
            response = self.orgClient.list_create_account_status(
                States=States,
                NextToken=response["NextToken"]
            )
            accounts.extend(response["CreateAccountStatuses"])

        return accounts

    def list_handshakes_for_account(self, Filter=None):
        handshakes = []
        response = self.orgClient.list_handshakes_for_account(
            Filter=Filter
        )
        handshakes.extend(response["Handshakes"])
        while "NextToken" in response:
            response = self.orgClient.list_handshakes_for_account(
                Filter=Filter,
                NextToken=response["NextToken"]
            )
            handshakes.extend(response["Handshakes"])

        return handshakes

    def list_handshakes_for_organization(self, Filter={}):
        handshakes = []
        response = self.orgClient.list_handshakes_for_organization(
            Filter=Filter
        )
        handshakes.extend(response["Handshakes"])
        while "NextToken" in response:
            response = self.orgClient.list_handshakes_for_organization(
                Filter=Filter
            )
            handshakes.extend(response["Handshakes"])

        return handshakes

    def list_organizational_units_for_parent(self, ParentId):
        org_units = []
        response = self.orgClient.list_organizational_units_for_parent(
            ParentId=ParentId
        )
        org_units.extend(response["OrganizationalUnits"])
        while "NextToken" in response:
            response = self.orgClient.list_organizational_units_for_parent(
                ParentId=ParentId,
                NextToken=response["NextToken"]
            )
            org_units.extend(response["OrganizationalUnits"])

        return org_units

    def list_parents(self, ChildId):
        parents = []
        response = self.orgClient.list_parents(
            ChildId=ChildId
        )
        parents.extend(response["Parents"])
        while "NextToken" in response:
            response = self.orgClient.list_parents(
                ChildId=ChildId,
                NextToken=response["NextToken"]
            )
            parents.extend(response["Parents"])

        return parents

    def list_policies(self):
        policies = []
        response = self.orgClient.list_policies()
        policies.extend(response["Policies"])
        while "NextToken" in response:
            response = self.orgClient.list_policies(
                NextToken=response["NextToken"]
            )
            policies.extend(response["Policies"])

        return policies

    def list_policies_for_target(self, TargetId):
        policies = []
        response = self.orgClient.list_policies_for_target(
            TargetId=TargetId
        )
        policies.extend(response["Policies"])
        while "NextToken" in response:
            response = self.orgClient.list_policies_for_target(
                TargetId=TargetId,
                NextToken=response["NextToken"]
            )
            policies.extend(response["Policies"])

        return policies

    def list_roots(self):
        roots = []
        response = self.orgClient.list_roots()
        roots.extend(response["Roots"])
        while "NextToken" in response:
            response = self.orgClient.list_roots(
                NextToken=response["NextToken"]
            )
            roots.extend(response["Roots"])

        return roots

    def list_targets_for_policy(self, PolicyId):
        targets = []
        response = self.orgClient.list_targets_for_policy(
            PolicyId=PolicyId
        )
        targets.extend(response["Targets"])
        while "NextToken" in response:
            response = self.orgClient.list_targets_for_policy(
                PolicyId=PolicyId,
                NextToken=response["NextToken"]
            )
            targets.extend(response["Targets"])

        return targets

    def move_account(self, AccountId, SourceParentId, DestinationParentId):
        self.orgClient.move_account(
            AccountId=AccountId,
            SourceParentId=SourceParentId,
            DestinationParentId=DestinationParentId
        )

    def remove_account_from_organization(self, AccountId):
        self.orgClient.remove_account_from_organization(
            AccountId=AccountId
        )

    def update_organizational_unit(self, OrganizationalUnit, Name):
        response = self.orgClient.update_organizational_unit(
            OrganizationalUnit=OrganizationalUnit,
            Name=Name
        )

        return response

    def update_policy(self, OrganizationalUnitId, Name):
        response = self.orgClient.OrganizationalUnitId(
            OrganizationalUnitId=OrganizationalUnitId,
            Name=Name
        )

        return response

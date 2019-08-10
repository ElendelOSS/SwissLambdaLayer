import json
import boto3


class glue:
    def __init__(self, region):
        self.glue_client = boto3.client('glue', region_name=region)

    def batch_create_partition(self, DatabaseName, TableName, PartitionInputList, CatalogId=None):
        response = self.glue_client.batch_create_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionInputList=PartitionInputList
        )

        return response.get("Errors", None)

    def batch_delete_connection(self, ConnectionNameList, CatalogId=None):
        response = self.glue_client.batch_delete_connection(
            CatalogId=CatalogId,
            ConnectionNameList=ConnectionNameList
        )

        return response.get("Succeeded", None), response.get("Errors", None)

    def batch_delete_partition(self, DatabaseName, TableName, PartitionsToDelete, CatalogId=None):
        response = self.glue_client.batch_delete_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionsToDelete=PartitionsToDelete
        )

        return response.get("Errors", None)

    def batch_delete_table(self, DatabaseName, TablesToDelete, CatalogId=None):
        response = self.glue_client.batch_delete_table(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TablesToDelete=TablesToDelete
        )

        return response.get("Errors", None)

    def batch_delete_table_version(self, DatabaseName, TableName, VersionIds, CatalogId=None):
        response = self.glue_client.batch_delete_table_version(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            VersionIds=VersionIds
        )

        return response.get("Errors", None)

    def batch_get_crawlers(self, CrawlerNames):
        response = self.glue_client.batch_get_crawlers(
            CrawlerNames=CrawlerNames
        )

        return response.get("Crawlers", []), response.get("CrawlersNotFound", [])

    def batch_get_dev_endpoints(self, DevEndpointNames):
        response = self.glue_client.batch_get_dev_endpoints(
            DevEndpointNames=DevEndpointNames
        )

        return response.get("DevEndpoints", []), response.get("DevEndpointsNotFound", [])

    def batch_get_jobs(self, JobNames):
        response = self.glue_client.batch_get_jobs(
            JobNames=JobNames
        )

        return response.get("Jobs", []), response.get("JobsNotFound", [])

    def batch_get_partition(self, DatabaseName, TableName, PartitionsToGet, CatalogId=None):
        response = self.glue_client.batch_get_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionsToGet=PartitionsToGet
        )

        return response.get("Partitions", []), response.get("UnprocessedKeys", [])

    def batch_get_triggers(self, TriggerNames):
        response = self.glue_client.batch_get_triggers(
            TriggerNames=TriggerNames
        )

        return response.get("Triggers", []), response.get("TriggersNotFound", [])

    def batch_stop_job_run(self, JobName, JobRunIds):
        response = self.glue_client.batch_stop_job_run(
            JobName=JobName,
            JobRunIds=JobRunIds
        )

        return response.get("SuccessfulSubmissions", []), response.get("Errors", [])

    def create_classifier(self, GrokClassifier, XMLClassifier, JsonClassifier, CsvClassifier):
        self.glue_client.create_classifier(
            GrokClassifier=GrokClassifier,
            XMLClassifier=XMLClassifier,
            JsonClassifier=JsonClassifier,
            CsvClassifier=CsvClassifier
        )

    def create_connection(self, ConnectionInput, CatalogId=None):
        self.glue_client.create_connection(
            CatalogId=CatalogId,
            ConnectionInput=ConnectionInput
        )

    def create_crawler(self, Name, Role, DatabaseName, Targets, Description=None, Schedule=None, Classifiers=[], TablePrefix=None, SchemaChangePolicy={}, Configuration=None, CrawlerSecurityConfiguration=None, Tags={}):
        self.glue_client.create_crawler(
            Name=Name,
            Role=Role,
            DatabaseName=DatabaseName,
            Description=Description,
            Targets=Targets,
            Schedule=Schedule,
            Classifiers=Classifiers,
            TablePrefix=TablePrefix,
            SchemaChangePolicy=SchemaChangePolicy,
            Configuration=Configuration,
            CrawlerSecurityConfiguration=CrawlerSecurityConfiguration,
            Tags=Tags
        )

    def create_database(self, DatabaseInput, CatalogId=None):
        self.glue_client.create_database(
            CatalogId=CatalogId,
            DatabaseInput=DatabaseInput
        )

    def create_dev_endpoint(self, EndpointName, RoleArn, SecurityGroupIds, SubnetId, PublicKeys, NumberOfNodes, ExtraPythonLibsS3Path=None, ExtraJarsS3Path=None, SecurityConfiguration=None, Tags=None, Arguments=None):
        response = self.glue_client.create_dev_endpoint(
            EndpointName=EndpointName,
            RoleArn=RoleArn,
            SecurityGroupIds=SecurityGroupIds,
            SubnetId=SubnetId,
            PublicKeys=PublicKeys,
            NumberOfNodes=NumberOfNodes,
            ExtraPythonLibsS3Path=ExtraPythonLibsS3Path,
            ExtraJarsS3Path=ExtraJarsS3Path,
            SecurityConfiguration=SecurityConfiguration,
            Tags=Tags,
            Arguments=Arguments
        )

        return response

    def create_job(self, Name, Description, LogUri, Role, ExecutionProperty, Command, DefaultArguments, Connections, MaxRetries, AllocatedCapacity, Timeout, MaxCapacity, NotificationProperty, SecurityConfiguration, Tags):
        response = self.glue_client.create_job(
            Name=Name,
            Description=Description,
            LogUri=LogUri,
            Role=Role,
            ExecutionProperty=ExecutionProperty,
            Command=Command,
            DefaultArguments=DefaultArguments,
            Connections=Connections,
            MaxRetries=MaxRetries,
            AllocatedCapacity=AllocatedCapacity,
            Timeout=Timeout,
            MaxCapacity=MaxCapacity,
            NotificationProperty=NotificationProperty,
            SecurityConfiguration=SecurityConfiguration,
            Tags=Tags
        )

        return response

    def create_partition(self, DatabaseName, TableName, PartitionInput, CatalogId=None):
        self.glue_client.create_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionInput=PartitionInput
        )

    def create_script(self, DagNodes, DagEdges, Language):
        response = self.glue_client.create_script(
            DagNodes=DagNodes,
            DagEdges=DagEdges,
            Language=Language
        )

        return response

    def create_security_configuration(self, Name, EncryptionConfiguration):
        response = self.glue_client.create_security_configuration(
            Name=Name,
            EncryptionConfiguration=EncryptionConfiguration
        )

        return response

    def create_table(self, DatabaseName, TableInput, CatalogId=None):
        self.glue_client.create_table(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableInput=TableInput
        )

    def create_trigger(self, Name, Type, Schedule, Predicate, Actions, Description, Tags, StartOnCreation=False):
        response = self.glue_client.create_trigger(
            Name=Name,
            Type=Type,
            Schedule=Schedule,
            Predicate=Predicate,
            Actions=Actions,
            Description=Description,
            StartOnCreation=StartOnCreation,
            Tags=Tags
        )

        return response

    def create_user_defined_function(self, DatabaseName, FunctionInput, CatalogId=None):
        self.glue_client.create_user_defined_function(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            FunctionInput=FunctionInput
        )

    def delete_classifier(self, Name):
        self.glue_client.delete_classifier(
            Name=Name
        )

    def delete_connection(self, ConnectionName, CatalogId=None):
        self.glue_client.delete_connection(
            CatalogId=CatalogId,
            ConnectionName=ConnectionName
        )

    def delete_crawler(self, Name):
        self.glue_client.delete_crawler(
            Name=Name
        )

    def delete_database(self, Name, CatalogId=None):
        self.glue_client.delete_database(
            CatalogId=CatalogId,
            Name=Name
        )

    def delete_dev_endpoint(self, EndpointName):
        self.glue_client.delete_dev_endpoint(
            EndpointName=EndpointName
        )

    def delete_job(self, JobName):
        response = self.glue_client.delete_job(
            JobName=JobName
        )

        return response

    def delete_partition(self, DatabaseName, TableName, PartitionValues, CatalogId=None):
        self.glue_client.delete_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionValues=PartitionValues
        )

    def delete_resource_policy(self, PolicyHashCondition):
        self.glue_client.delete_resource_policy(
            PolicyHashCondition=PolicyHashCondition
        )

    def delete_security_configuration(self, Name):
        self.glue_client.delete_security_configuration(
            Name=Name
        )

    def delete_table(self, DatabaseName, Name, CatalogId=None):
        self.glue_client.delete_table(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            Name=Name
        )

    def delete_table_version(self, DatabaseName, TableName, VersionId, CatalogId=None):
        self.glue_client.delete_table_version(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            VersionId=VersionId
        )

    def delete_trigger(self, Name):
        self.glue_client.delete_trigger(
            Name=Name
        )

    def delete_user_defined_function(self, DatabaseName, FunctionName, CatalogId=None):
        self.glue_client.delete_user_defined_function(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            FunctionName=FunctionName
        )

    def get_catalog_import_status(self, CatalogId):
        response = self.glue_client.get_catalog_import_status(
            CatalogId=CatalogId
        )

        return response

    def get_classifier(self, Name):
        response = self.glue_client.get_classifier(
            Name=Name
        )

        return response

    def get_classifiers(self):
        classifiers = []

        response = self.glue_client.get_classifiers()
        classifiers.append(response["Classifiers"])

        while "NextToken" in response:
            response = self.glue_client.get_classifiers(
                NextToken=response["NextToken"]
            )
            classifiers.append(response["Classifiers"])

        return classifiers

    def get_connection(self, Name, HidePassword, CatalogId=None):
        response = self.glue_client.get_connection(
            CatalogId=CatalogId,
            Name=Name,
            HidePassword=HidePassword
        )

        return response

    def get_connections(self, CatalogId=None, HidePassword=True):
        connections = []

        response = self.glue_client.get_connections(
            CatalogId=CatalogId,
            HidePassword=HidePassword
        )
        connections.append(response["ConnectionList"])

        while "NextToken" in response:
            response = self.glue_client.get_connections(
                CatalogId=CatalogId,
                HidePassword=HidePassword,
                NextToken=response["NextToken"]
            )
            connections.append(response["ConnectionList"])

        return connections

    def get_crawler(self, Name):
        response = self.glue_client.get_crawler(
            Name=Name
        )

        return response

    def get_crawler_metrics(self, CrawlerNameList):
        metrics = []

        response = self.glue_client.get_crawler_metrics(
            CrawlerNameList=CrawlerNameList
        )
        metrics.append(response["CrawlerMetricsList"])
        while "NextToken" in response:
            response = self.glue_client.get_crawler_metrics(
                CrawlerNameList=CrawlerNameList,
                NextToken=response["NextToken"]
            )
            metrics.append(response["CrawlerMetricsList"])

        return metrics

    def get_crawlers(self):
        crawlers = []

        response = self.glue_client.get_crawlers()
        crawlers.append(response["Crawlers"])
        while "NextToken" in response:
            response = self.glue_client.get_crawlers(
                NextToken=response["NextToken"]
            )
            crawlers.append(response["Crawlers"])

        return crawlers

    def get_data_catalog_encryption_settings(self, CatalogId=None):
        response = self.glue_client.get_data_catalog_encryption_settings(
            CatalogId=CatalogId
        )

        return response

    def get_database(self, Name, CatalogId=None):
        response = self.glue_client.get_database(
            CatalogId=CatalogId,
            Name=CatalogId
        )

        return response

    def get_databases(self, CatalogId=None):
        databases = []

        response = self.glue_client.get_databases(
            CatalogId=CatalogId
        )
        databases.append(response["DatabaseList"])
        while "NextToken" in response:
            response = self.glue_client.get_databases(
                CatalogId=CatalogId,
                NextToken=response["NextToken"]
            )
            databases.append(response["DatabaseList"])

        return databases

    def get_dataflow_graph(self, PythonScript):
        response = self.glue_client.get_dataflow_graph(
            PythonScript=PythonScript
        )

        return response

    def get_dev_endpoint(self, EndpointName):
        response = self.glue_client.get_dev_endpoint(
            EndpointName=EndpointName
        )

        return response

    def get_dev_endpoints(self):
        endpoints = []

        response = self.glue_client.get_dev_endpoints()
        endpoints.append(response["DevEndpoints"])
        while "NextToken" in response:
            response = self.glue_client.get_dev_endpoints(
                NextToken=response["NextToken"]
            )
            endpoints.append(response["DevEndpoints"])

        return endpoints

    def get_job(self, JobName):
        response = self.glue_client.get_job(
            JobName=JobName
        )

        return response

    def get_job_run(self, JobName, RunId, PredecessorsIncluded):
        response = self.glue_client.get_job_run(
            JobName=JobName,
            RunId=RunId,
            PredecessorsIncluded=PredecessorsIncluded
        )

        return response

    def get_job_runs(self, JobName):
        job_runs = []

        response = self.glue_client.get_job_runs(
            JobName=JobName
        )
        job_runs.append(response["JobRuns"])
        while "NextToken" in response:
            response = self.glue_client.get_job_runs(
                JobName=JobName,
                NextToken=response["NextToken"]
            )
            job_runs.append(response["JobRuns"])

        return job_runs

    def get_jobs(self):
        jobs = []

        response = self.glue_client.get_jobs()
        jobs.append(response["Jobs"])
        while "NextToken" in response:
            response = self.glue_client.get_jobs(
                NextToken=response["NextToken"]
            )
            jobs.append(response["Jobs"])

        return jobs

    def get_mapping(self, Source, Sinks, Location):
        response = self.glue_client.get_mapping(
            Source=Source,
            Sinks=Sinks,
            Location=Location
        )

        return response

    def get_partition(self, DatabaseName, TableName, PartitionValues, CatalogId=None):
        response = self.glue_client.get_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionValues=PartitionValues
        )

        return response

    def get_partitions(self, DatabaseName, TableName, Expression, Segment, CatalogId=None):
        parititions = []

        response = self.glue_client.get_partitions(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            Expression=Expression,
            Segment=Segment
        )
        parititions.append(response["Partitions"])
        while "NextToken" in response:
            response = self.glue_client.get_partitions(
                CatalogId=CatalogId,
                DatabaseName=DatabaseName,
                TableName=TableName,
                Expression=Expression,
                Segment=Segment,
                NextToken=response["NextToken"]
            )
            parititions.append(response["Partitions"])

        return parititions

    def get_plan(self, Mapping, Source, Sinks, Location, Language):
        response = self.glue_client.get_plan(
            Mapping=Mapping,
            Source=Source,
            Sinks=Sinks,
            Location=Location,
            Language=Language
        )

        return response

    def get_resource_policy(self):
        response = self.glue_client.get_resource_policy()

        return response

    def get_security_configuration(self, Name):
        response = self.glue_client.get_security_configuration(
            Name=Name
        )

        return response

    def get_security_configurations(self):
        security_configurations = []

        response = self.glue_client.get_security_configurations()
        security_configurations.append(response["SecurityConfigurations"])
        while "NextToken" in response:
            response = self.glue_client.get_security_configurations(
                NextToken=response["NextToken"]
            )
            security_configurations.append(response["SecurityConfigurations"])

        return security_configurations

    def get_table(self, Name, DatabaseName, CatalogId=None):
        response = self.glue_client.get_table(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            Name=Name
        )

        return response

    def get_table_version(self, DatabaseName, TableName, VersionId, CatalogId=None):
        response = self.glue_client.table_version(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            VersionId=VersionId
        )

        return response

    def get_table_versions(self, DatabaseName, TableName, CatalogId=None):
        versions = []

        response = self.glue_client.get_table_versions(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName
        )
        versions.append(response["TableVersions"])
        while "NextToken" in response:
            response = self.glue_client.get_table_versions(
                CatalogId=CatalogId,
                DatabaseName=DatabaseName,
                TableName=TableName,
                NextToken=response["NextToken"]
            )
            versions.append(response["TableVersions"])

        return versions

    def get_tables(self, DatabaseName, Expression, CatalogId=None):
        tables = []

        response = self.glue_client.get_tables(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            Expression=Expression,
        )
        tables.append(response["TableList"])
        while "NextToken" in response:
            response = self.glue_client.get_tables(
                CatalogId=CatalogId,
                DatabaseName=DatabaseName,
                Expression=Expression,
                NextToken=response["NextToken"]
            )
            tables.append(response["TableList"])

        return tables

    def get_tags(self, ResourceArn):
        response = self.glue_client.get_tags(
            ResourceArn=ResourceArn
        )
        return response

    def get_trigger(self, Name):
        response = self.glue_client.get_trigger(
            Name=Name
        )

        return response

    def get_triggers(self):
        triggers = []

        response = self.glue_client.get_triggers()
        triggers.append(response["Triggers"])
        while "NextToken" in response:
            response = self.glue_client.get_triggers(
                NextToken=response["NextToken"]
            )
            triggers.append(response["Triggers"])

        return triggers

    def get_user_defined_function(self, DatabaseName, FunctionName, CatalogId=None):
        response = self.glue_client.get_user_defined_function(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            FunctionName=FunctionName
        )

        return response

    def get_user_defined_functions(self, DatabaseName, Pattern, CatalogId=None):
        user_functions = []

        response = self.glue_client.get_user_defined_functions(
            CatalogId='string',
            DatabaseName='string',
            Pattern='string',
        )
        user_functions.append(response["UserDefinedFunctions"])
        while "NextToken" in response:
            response = self.glue_client.get_user_defined_functions(
                CatalogId='string',
                DatabaseName='string',
                Pattern='string',
                NextToken=response["NextToken"]
            )
            user_functions.append(response["UserDefinedFunctions"])

        return user_functions

    def import_catalog_to_glue(self, CatalogId):
        self.glue_client.import_catalog_to_glue(
            CatalogId=CatalogId
        )

    def list_crawlers(self):
        crawlers = []

        response = self.glue_client.list_crawlers()
        crawlers.append(response["CrawlerNames"])
        while "NextToken" in response:
            response = self.glue_client.list_crawlers(
                NextToken=response["NextToken"]
            )
            crawlers.append(response["CrawlerNames"])

        return crawlers

    def list_dev_endpoints(self):
        endpoints = []

        response = self.glue_client.list_dev_endpoints()
        endpoints.append(response["DevEndpointNames"])
        while "NextToken" in response:
            response = self.glue_client.list_dev_endpoints(
                NextToken=response["NextToken"]
            )
            endpoints.append(response["DevEndpointNames"])

        return endpoints

    def list_jobs(self):
        jobs = []

        response = self.glue_client.list_jobs()
        jobs.append(response["JobNames"])
        while "NextToken" in response:
            response = self.glue_client.list_jobs(
                NextToken=response["NextToken"]
            )
            jobs.append(response["JobNames"])

        return jobs

    def list_triggers(self):
        triggers = []

        response = self.glue_client.list_triggers()
        triggers.append(response["TriggerNames"])
        while "NextToken" in response:
            response = self.glue_client.list_triggers(
                NextToken=response["NextToken"]
            )
            triggers.append(response["TriggerNames"])

        return triggers

    def put_data_catalog_encryption_settings(self, CatalogId, DataCatalogEncryptionSettings):
        response = self.glue_client.put_data_catalog_encryption_settings(
            CatalogId=CatalogId,
            DataCatalogEncryptionSettings=DataCatalogEncryptionSettings
        )

        return response

    def put_resource_policy(self, PolicyInJson, PolicyHashCondition, PolicyExistsCondition):
        response = self.glue_client.put_resource_policy(
            PolicyInJson=PolicyInJson,
            PolicyHashCondition=PolicyHashCondition,
            PolicyExistsCondition=PolicyExistsCondition
        )

        return response

    def reset_job_bookmark(self, JobName):
        response = self.glue_client.reset_job_bookmark(
            JobName=JobName
        )

        return response

    def start_crawler(self, Name):
        self.glue_client.start_crawler(
            Name=Name
        )

    def start_crawler_schedule(self, CrawlerName):
        self.glue_client.start_crawler_schedule(
            CrawlerName=CrawlerName
        )

    def start_job_run(self, JobName, JobRunId, Arguments, AllocatedCapacity, Timeout, MaxCapacity, NotificationProperty, SecurityConfiguration):
        response = self.glue_client.start_job_run(
            JobName=JobName,
            JobRunId=JobRunId,
            Arguments=Arguments,
            AllocatedCapacity=AllocatedCapacity,
            Timeout=Timeout,
            MaxCapacity=MaxCapacity,
            NotificationProperty=NotificationProperty,
            SecurityConfiguration=SecurityConfiguration
        )

        return response

    def start_trigger(self, Name):
        response = self.glue_client.start_trigger(
            Name='string'
        )

        return response

    def stop_crawler(self, Name):
        self.glue_client.stop_crawler(
            Name='string'
        )

    def stop_crawler_schedule(self, CrawlerName):
        self.glue_client.stop_crawler_schedule(
            CrawlerName=CrawlerName
        )

    def stop_trigger(self, Name):
        response = self.glue_client.stop_trigger(
            Name=Name
        )

        return response

    def tag_resource(self, ResourceArn, TagsToAdd):
        self.glue_client.tag_resource(
            ResourceArn=ResourceArn,
            TagsToAdd=TagsToAdd
        )

    def untag_resource(self, ResourceArn, TagsToRemove):
        self.glue_client.untag_resource(
            ResourceArn=ResourceArn,
            TagsToRemove=TagsToRemove
        )

    def update_classifier(self, GrokClassifier, XMLClassifier, JsonClassifier, CsvClassifier):
        self.glue_client.update_classifier(
            GrokClassifier=GrokClassifier,
            XMLClassifier=XMLClassifier,
            JsonClassifier=JsonClassifier,
            CsvClassifier=CsvClassifier
        )

    def update_connection(self, Name, ConnectionInput, CatalogId=None):
        self.glue_client.update_connection(
            CatalogId=CatalogId,
            Name=Name,
            ConnectionInput=ConnectionInput
        )

    def update_crawler(self, Name, Role, DatabaseName, Description, Targets, Schedule, Classifiers, TablePrefix, SchemaChangePolicy, Configuration, CrawlerSecurityConfiguration):
        self.glue_client.update_crawler(
            Name=Name,
            Role=Role,
            DatabaseName=DatabaseName,
            Description=Description,
            Targets=Targets,
            Schedule=Schedule,
            Classifiers=Classifiers,
            TablePrefix=TablePrefix,
            SchemaChangePolicy=SchemaChangePolicy,
            Configuration=Configuration,
            CrawlerSecurityConfiguration=CrawlerSecurityConfiguration
        )

    def update_crawler_schedule(self, CrawlerName, Schedule):
        self.glue_client.update_crawler_schedule(
            CrawlerName=CrawlerName,
            Schedule=Schedule
        )

    def update_database(self, Name, DatabaseInput, CatalogId=None):
        self.glue_client.update_database(
            CatalogId=CatalogId,
            Name=Name,
            DatabaseInput=DatabaseInput
        )

    def update_dev_endpoint(self, EndpointName, PublicKey, AddPublicKeys, DeletePublicKeys, CustomLibraries, UpdateEtlLibraries, DeleteArguments, AddArguments):
        self.glue_client.update_dev_endpoint(
            EndpointName=EndpointName,
            PublicKey=PublicKey,
            AddPublicKeys=AddPublicKeys,
            DeletePublicKeys=DeletePublicKeys,
            CustomLibraries=CustomLibraries,
            UpdateEtlLibraries=UpdateEtlLibraries,
            DeleteArguments=DeleteArguments,
            AddArguments=AddArguments
        )

    def update_job(self, JobName, JobUpdate):
        response = self.glue_client.update_job(
            JobName=JobName,
            JobUpdate=JobUpdate
        )

        return response

    def update_partition(self, DatabaseName, TableName, PartitionValueList, PartitionInput, CatalogId=None):
        self.glue_client.update_partition(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            PartitionValueList=PartitionValueList,
            PartitionInput=PartitionInput
        )

    def update_table(self, DatabaseName, TableInput, SkipArchive, CatalogId=None):
        self.glue_client.update_table(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableInput=TableInput,
            SkipArchive=SkipArchive
        )

    def update_trigger(self, Name, TriggerUpdate):
        response = self.glue_client.update_trigger(
            Name=Name,
            TriggerUpdate=TriggerUpdate
        )

        return response

    def update_user_defined_function(self, DatabaseName, FunctionName, FunctionInput, CatalogId=None):
        self.glue_client.update_user_defined_function(
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            FunctionName=FunctionName,
            FunctionInput=FunctionInput
        )

import json
import boto3


class appmesh:
    def __init__(self, session):
        self.meshClient = session.client('appmesh')

    def create_mesh(self, token, meshName, spec, tags):
        response = self.meshClient.create_mesh(
            token=token,
            meshName=meshName,
            spec=spec,
            tags=tags
        )

        return response

    def create_route(self, token, meshName, routeName, spec, tags, virtualRouterName):
        response = self.meshClient.create_route(
            token=token,
            meshName=meshName,
            routeName=routeName,
            spec=spec,
            tags=tags,
            virtualRouterName=virtualRouterName
        )

        return response

    def create_virtual_node(self, token, meshName, spec, tags, virtualNodeName):
        response = self.meshClient.create_virtual_node(
            token=token,
            meshName=meshName,
            spec=spec,
            tags=tags,
            virtualNodeName=virtualNodeName
        )

        return response

    def create_virtual_router(self, token, meshName, spec, tags, virtualRouterName):
        response = self.meshClient.create_virtual_router(
            token=token,
            meshName=meshName,
            spec=spec,
            tags=tags,
            virtualRouterName=virtualRouterName
        )

        return response

    def create_virtual_service(self, token, meshName, spec, tags, virtualServiceName):
        response = self.meshClient.create_virtual_service(
            token=token,
            meshName=meshName,
            spec=spec,
            tags=tags,
            virtualServiceName=virtualServiceName
        )

        return response

    def delete_mesh(self, meshName):
        response = self.meshClient.delete_mesh(
            meshName=meshName
        )

        return response

    def delete_route(self, meshName, meshRouter, virtualRouterName):
        response = self.meshClient.delete_route(
            meshName=meshName,
            meshRouter=meshRouter,
            virtualRouterName=virtualRouterName
        )

        return response

    def delete_virtual_node(self, meshName, virtualNodeName):
        response = self.meshClient.delete_virtual_node(
            meshName=meshName,
            virtualNodeName=virtualNodeName
        )

        return response

    def delete_virtual_router(self, meshName, virtualRouterName):
        response = self.meshClient.delete_virtual_router(
            meshName=meshName,
            virtualRouterName=virtualRouterName
        )

        return response

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from airbyte import utils
from airbyte.models import operations, shared
from typing import Optional

class DestinationDefinition:
    r"""DestinationDefinition related resources."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_custom_destination_definition(self, request: shared.CustomDestinationDefinitionCreate) -> operations.CreateCustomDestinationDefinitionResponse:
        r"""Creates a custom destinationDefinition for the given workspace"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/create_custom'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateCustomDestinationDefinitionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionRead])
                res.destination_definition_read = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def delete_destination_definition(self, request: shared.DestinationDefinitionIDRequestBody) -> operations.DeleteDestinationDefinitionResponse:
        r"""Delete a destination definition"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/delete'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteDestinationDefinitionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def get_destination_definition(self, request: shared.DestinationDefinitionIDRequestBody) -> operations.GetDestinationDefinitionResponse:
        r"""Get destinationDefinition"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/get'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDestinationDefinitionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionRead])
                res.destination_definition_read = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def get_destination_definition_for_workspace(self, request: shared.DestinationDefinitionIDWithWorkspaceID) -> operations.GetDestinationDefinitionForWorkspaceResponse:
        r"""Get a destinationDefinition that is configured for the given workspace"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/get_for_workspace'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDestinationDefinitionForWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionRead])
                res.destination_definition_read = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def grant_destination_definition_to_workspace(self, request: shared.DestinationDefinitionIDWithWorkspaceID) -> operations.GrantDestinationDefinitionToWorkspaceResponse:
        r"""grant a private, non-custom destinationDefinition to a given workspace"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/grant_definition'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GrantDestinationDefinitionToWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PrivateDestinationDefinitionRead])
                res.private_destination_definition_read = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def list_destination_definitions(self) -> operations.ListDestinationDefinitionsResponse:
        r"""List all the destinationDefinitions the current Airbyte deployment is configured to use"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/list'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListDestinationDefinitionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionReadList])
                res.destination_definition_read_list = out

        return res

    
    def list_destination_definitions_for_workspace(self, request: shared.WorkspaceIDRequestBody) -> operations.ListDestinationDefinitionsForWorkspaceResponse:
        r"""List all the destinationDefinitions the given workspace is configured to use"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/list_for_workspace'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListDestinationDefinitionsForWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionReadList])
                res.destination_definition_read_list = out

        return res

    
    def list_latest_destination_definitions(self) -> operations.ListLatestDestinationDefinitionsResponse:
        r"""List the latest destinationDefinitions Airbyte supports
        Guaranteed to retrieve the latest information on supported destinations.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/list_latest'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListLatestDestinationDefinitionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionReadList])
                res.destination_definition_read_list = out

        return res

    
    def list_private_destination_definitions(self, request: shared.WorkspaceIDRequestBody) -> operations.ListPrivateDestinationDefinitionsResponse:
        r"""List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/list_private'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListPrivateDestinationDefinitionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PrivateDestinationDefinitionReadList])
                res.private_destination_definition_read_list = out

        return res

    
    def revoke_destination_definition_from_workspace(self, request: shared.DestinationDefinitionIDWithWorkspaceID) -> operations.RevokeDestinationDefinitionFromWorkspaceResponse:
        r"""revoke a grant to a private, non-custom destinationDefinition from a given workspace"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/revoke_definition'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RevokeDestinationDefinitionFromWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def update_destination_definition(self, request: shared.DestinationDefinitionUpdate) -> operations.UpdateDestinationDefinitionResponse:
        r"""Update destinationDefinition"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/destination_definitions/update'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateDestinationDefinitionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DestinationDefinitionRead])
                res.destination_definition_read = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
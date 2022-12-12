import boto3
import json

client = boto3.client('workspaces')

def lambda_handler(event, context):

    statusCode = 200
    print("Alarm activated")
    DirectoryId = "d-966714f11"
    UnhealthyWorkspace = []
    
    if(DirectoryId == 'd-966714f114'):
        response = client.describe_workspaces(
            WorkspaceIds = (should be in an array)
        )

    us = response["Contents"]

    for i in us:
        if(State == 'Stopped'):
            print(i)
            UnhealthyWorkspace.append(i)
    

    response1 = client.reboot_workspaces(
        StartWorkspaceRequests=[
            {
                'WorkspaceId' : UnhealthyWorkspace
            }
        ]
    )

print(Workspaces succesully started)






from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def list_compute_engine_instances(project_id):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    
    print(f"\nCompute Engine Instances in Project {project_id}:")
    total_vms = 0  # Counter for VM instances
    request = service.instances().aggregatedList(project=project_id)
    while request is not None:
        response = request.execute()
        for zone, instances_scoped_list in response['items'].items():
            if 'instances' in instances_scoped_list:
                for instance in instances_scoped_list['instances']:
                    total_vms += 1
                    print(f"- Instance: {instance['name']}, Zone: {zone}, Type: {instance['machineType']}")
        request = service.instances().aggregatedList_next(previous_request=request, previous_response=response)
    print(f"Total Compute Engine VM Instances: {total_vms}")

def list_cloud_sql_instances(project_id):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('sqladmin', 'v1', credentials=credentials)

    total_sql_instances = 0  # Counter for SQL instances
    print(f"\nCloud SQL Instances in Project {project_id}:")
    request = service.instances().list(project=project_id)
    response = request.execute()

    if 'items' in response:
        for instance in response['items']:
            total_sql_instances += 1
            print(f"- Database Instance: {instance['name']}, Type: {instance['databaseVersion']}, Region: {instance['region']}")
    else:
        print("No Cloud SQL instances found.")
    print(f"Total Cloud SQL Instances: {total_sql_instances}")

def list_resources_for_projects(project_ids):
    for project_id in project_ids:
        list_compute_engine_instances(project_id)
        list_cloud_sql_instances(project_id)

# List of GCP project IDs you want to check
project_ids = ['project-id-1', 'project-id-2', 'project-id-3']

# List resources in the specified projects
list_resources_for_projects(project_ids)

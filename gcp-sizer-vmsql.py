from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# Global counters for totals across all projects
total_vms_global = 0
total_sql_instances_global = 0

def list_compute_engine_instances(project_id):
    global total_vms_global  # Use the global counter
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    
    print(f"\nCompute Engine Instances in Project {project_id}:")
    total_vms = 0  # Counter for VM instances within the current project
    request = service.instances().aggregatedList(project=project_id)
    while request is not None:
        response = request.execute()
        for zone, instances_scoped_list in response['items'].items():
            if 'instances' in instances_scoped_list:
                for instance in instances_scoped_list['instances']:
                    total_vms += 1
                    # Simplify the output by extracting the machine type name
                    machine_type = instance['machineType'].split('/')[-1]
                    print(f"- Instance: {instance['name']}, Zone: {zone.split('/')[-1]}, Type: {machine_type}")
        request = service.instances().aggregatedList_next(previous_request=request, previous_response=response)
    print(f"Total Compute Engine VM Instances: {total_vms}")
    total_vms_global += total_vms  # Update the global counter

def list_cloud_sql_instances(project_id):
    global total_sql_instances_global  # Use the global counter
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('sqladmin', 'v1', credentials=credentials)

    total_sql_instances = 0  # Counter for SQL instances within the current project
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
    total_sql_instances_global += total_sql_instances  # Update the global counter

def list_resources_for_projects(project_ids):
    for project_id in project_ids:
        list_compute_engine_instances(project_id)
        list_cloud_sql_instances(project_id)
    # After listing all resources, print the total counts across all projects
    print(f"\nTotal VMs across all projects: {total_vms_global}")
    print(f"Total Cloud SQL instances across all projects: {total_sql_instances_global}")

# List of GCP project IDs you want to check
project_ids = ['insert project id', 'insert project id', 'insert project id']

# List resources in the specified projects
list_resources_for_projects(project_ids)

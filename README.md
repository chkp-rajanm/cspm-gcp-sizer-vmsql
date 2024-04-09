Before you run this script, ensure you have the following:

A GCP account and access to a GCP project.
The necessary permissions to list Compute Engine and Cloud SQL instances in your GCP project.
Python 3.6 or later installed on your machine.
Google Cloud SDK installed and initialized for your project (optional for authentication purposes).
Setup Instructions
Enable APIs: Make sure the Compute Engine API and Cloud SQL Admin API are enabled in your GCP project. You can enable these APIs through the GCP Console under APIs & Services.

Authentication: The script uses Google Cloud's default credentials for authentication. You can authenticate using one of the following methods:

If you have the Google Cloud SDK installed, authenticate your session with gcloud auth application-default login.
Alternatively, you can set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the file path of the JSON key file for a service account with the necessary permissions.
Install Required Python Libraries: Install the google-api-python-client and oauth2client libraries using pip:

css
Copy code
pip install --upgrade google-api-python-client oauth2client
Running the Script
Update the project_id variable in the script with your GCP project ID.

Run the script using Python:

Copy code
python list_gcp_assets.py
The script will list all VM instances and Cloud SQL instances in the specified project. After listing these assets, it will output the total count for each type.

Output
The script outputs the following information for each asset:

For Compute Engine VM instances: Instance name, zone, and machine type.
For Cloud SQL instances: Database instance name, database version, and region.
At the end of the script's execution, it summarizes the total number of Compute Engine VM instances and Cloud SQL instances found.

Example Output
yaml
Copy code
Compute Engine Instances (Assets):
- Instance: example-instance-1, Zone: us-central1-a, Type: e2-medium
- Instance: example-instance-2, Zone: europe-west1-b, Type: n1-standard-1
Total Compute Engine VM Instances: 2

Cloud SQL Instances (Assets):
- Database Instance: example-sql-1, Type: POSTGRES_12, Region: us-central1
Total Cloud SQL Instances: 1
Troubleshooting
APIs Not Enabled: If you encounter errors related to disabled APIs, ensure the Compute Engine API and Cloud SQL Admin API are enabled for your project.
Authentication Issues: Verify that your Google Cloud SDK is properly authenticated or your GOOGLE_APPLICATION_CREDENTIALS environment variable points to a valid service account JSON key file.
Permission Errors: Ensure your user or service account has the necessary roles/permissions to list VM instances and Cloud SQL instances.
For further assistance, refer to the Google Cloud Documentation.


from googleapiclient.discovery import build

def gcs_to_bigquery_trigger_job(cloud_event,environment):

    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"
    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

# Data flow template
    template_body = {
        "jobName": "gcs_to_bigquery_load",
        "parameters": {
            "inputFilePattern": "gs://gcs-to-bigquery-project/weather_report.csv",
            "JSONPath": "gs://gcs-to-bigquery-project/dataSchema.json",
            "outputTable": "vertical-idea-423218-n4:weather_data.weather_report",
            "bigQueryLoadingTemporaryDirectory": "gs://gcs-to-bigquery-project",
            "javascriptTextTransformGcsPath": "gs://gcs-to-bigquery-project/udfunction.js",
            "javascriptTextTransformFunctionName": "schema_function"
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()

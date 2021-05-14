from streamsets.sdk import ControlHub, DataCollector
import json
import pdb

# Replace the argument values according to your setup
control_hub = ControlHub(server_url='https://cloud.streamsets.com',
                         username='admin@redshelf.com',
                         password='[secret]')

DataCollector.VERIFY_SSL_CERTIFICATES = False
data_collector = DataCollector('https://localhost:18630', control_hub=control_hub)
print(data_collector.id)

def create_pipeline():
    with open('./CDCEnrichment801f42bb-983e-42b2-b912-01ee9762978c:redshelf.com.json', 'r') as input_file:
        pipeline_json = json.load(input_file)

    pipeline_builder = control_hub.get_pipeline_builder(control_hub.data_collectors.get(id=data_collector.id))
    pipeline_builder.import_pipeline(pipeline=pipeline_json)
    pipeline = pipeline_builder.build(title='Modified using Pipeline Builder')
    control_hub.publish_pipeline(pipeline)

def create_job():
   pipeline = control_hub.pipelines.get(name='Modified using Pipeline Builder')
   job_builder = control_hub.get_job_builder()
   job = job_builder.build(job_name='Modified using Pipeline Builder', pipeline=pipeline)
   control_hub.add_job(job)

def start_job():
   job = control_hub.jobs.get(job_name='Modified using Pipeline Builder')
   control_hub.start_job(job)

start_job()

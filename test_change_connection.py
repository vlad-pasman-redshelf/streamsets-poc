from streamsets.sdk.sch import ControlHub
import json
import pdb

# Replace the argument values according to your setup
control_hub = ControlHub(server_url='https://cloud.streamsets.com',
                         username='admin@redshelf.com',
                         password='[secret]')

# DataCollector.VERIFY_SSL_CERTIFICATES = False
# data_collector = DataCollector('https://localhost:18630', control_hub=control_hub)
# print(data_collector.id)
mod_pp = control_hub.pipelines.get(name='Modified using Pipeline Builder')
src_stg = mod_pp.stages.get(instance_name='JDBCMultitableConsumer_01')

src_stg.connection
src_stg.connection = control_hub.connections.get(name='pg-stream1').id
control_hub.publish_pipeline(mod_pp)
src_stg.connection

job=control_hub.jobs.get(job_name='Modified using Pipeline Builder')
control_hub.upgrade_job(job)

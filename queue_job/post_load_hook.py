from odoo.addons.queue_job.jobrunner.runner import QueueJobRunner


def post_load_hook():
    QueueJobRunner.requeue_jobs()

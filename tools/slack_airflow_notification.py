from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

SLACK_CONN_ID = 'slack_d0a100'


def task_fail_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    link = '<{log_url}|{dag}/{task}>'.format(
        log_url=context.get('task_instance').log_url,
        task=context.get('task_instance').task_id,
        dag=context.get('task_instance').dag_id,
    )
    failed_alert = SlackWebhookOperator(
        task_id='slack_failed',
        http_conn_id=SLACK_CONN_ID,
        webhook_token=slack_webhook_token,
        message=f':red_circle: Task: {link} Failed.',
        username="airflow",
    )
    return failed_alert.execute(context=context)


def task_success_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    link = '<{log_url}|{dag}/{task}>'.format(
        log_url=context.get('task_instance').log_url,
        task=context.get('task_instance').task_id,
        dag=context.get('task_instance').dag_id,
    )
    success_alert = SlackWebhookOperator(
        task_id='slack_failed',
        http_conn_id=SLACK_CONN_ID,
        webhook_token=slack_webhook_token,
        message=f':green_circle: Task: {link} Succeded.',
        username="airflow",
    )
    return success_alert.execute(context=context)

import os
from kombu import Queue
from kombu import Exchange
from kombu import serialization
from TopSpeedData_Worker.log import get_logger

DEBUG = True  # True是本机运行

# 注册
INSTALLED_TASKS = [
    'automation.target_automodel',
    'call_task.call_pro',
    'call_task.port_data_update',
    'data_extract.t_bsc_investment_advice',
    'data_extract.t_bsc_pensionproduct',
    'data_extract.t_bsc_pool',
    'data_extract.t_bsc_wmp',
    'data_extract.t_bus_pledgedrepo_pool',
    'data_extract.t_data_md5',
    'data_extract.t_globle_data',
    'data_extract.t_instruction',
    'data_extract.t_ods_securitycomp',
    'data_extract.t_redis_md5'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# Redis 连接信息
REDIS_HOST = '10.88.158.99'
REDIS_POST = 6379
REDIS_DB = 9
REDIS_DB_PARALLEL = 14  # 平台并行库
REDIS_PASSWORD = '123456'

# Redis集群信息
REDIS_NODES_GROUP = [{'host': '10.88.147.57', 'port': 6379},
                     {'host': '10.88.147.58', 'port': 6379},
                     {'host': '10.88.147.61', 'port': 6379},
                     ]


# Rabbitmq 集群地址
RABBITMQ_IP_GROUP_1 = '10.88.147.57'
RABBITMQ_IP_GROUP_2 = '10.88.147.58'
RABBITMQ_IP_GROUP_3 = '10.88.147.61'
RABBITMQ_PORT_GROUP = '5672'
RABBITMQ_USER_GROUP = 'guest'
RABBITMQ_PASS_GROUP = "guest"

RABBITMQ_SINGLE = True  # mq单点模式/集群模式
REDIS_SINGLE = True  # redis单点模式/集群模式

# celery
serialization.registry._decoders.pop("application/x-python-serialize")
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False
CELERYD_CONCURRENCY = 10
# CELERYD_MAX_TASKS_PER_CHILD = 3  #  每个worker最多执行1个任务就会被销毁，可防止内存泄露
CELERY_QUEUES = (
    Queue('TSD_Default', exchange=Exchange('default'), routing_key='default'),
    Queue('TSD_Tasks_Main', exchange=Exchange('Tasks_Main'), routing_key='Tasks_Main'),
    Queue('TSD_MessInform', exchange=Exchange('TSD_MessInform'), routing_key='MessInform'),
)
CELERY_ROUTES = {
    'tsd.tasks.main': {'queue': 'TSD_Tasks_Main', 'routing_key': 'Tasks_Main'},
    'tsd.messinform': {'queue': 'TSD_MessInform', 'routing_key': 'MessInform'}
}
CELERY_DEFAULT_QUEUE = 'TSD_Default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'
CELERY_IMPORTS = ('TopSpeedData_Worker.tasks',)

# log
LOG_FILE_DIR = os.path.join(BASE_DIR, "log/")
LOG_FILE_NAME = LOG_FILE_DIR + 'tsd_worker.log'
logger = get_logger(LOG_FILE_NAME)

# 读取基础数据 到75
READ_SERVER_ADDRESS = '10.88.17.75'
READ_SERVICE_NAME = 'mastdb'
READ_SERVER_USER = 'md_developer'
READ_SERVER_PASS = 'md_developer'


# 读取基础数据 从pas  #如果这里的tns连接不可用，运行程序会把ora无监听程序的错误
READ_SERVER_ADDRESS1 = '10.88.147.60'
READ_SERVICE_NAME1 = 'imsuat'
READ_SERVER_USER1 = 'md'
READ_SERVER_PASS1 = 'md'

# Mysql数据连接
MYSQL_SERVER_ADDRESS = '10.88.147.59'
MYSQL_DATABASE_NAME = 'test'
MYSQL_SERVER_USER = 'root'
MYSQL_SERVER_PASS = 'mysql'

# Rabbitmq 地址
RABBITMQ_IP = '10.88.147.59'
RABBITMQ_PORT = '5672'
RABBITMQ_USER = 'admin'
RABBITMQ_PASS = "admin"

#MD数据库连接  用于数据抽取连接目标表
MD_SERVER_ADDRESS = '10.88.147.60'
MD_SERVICE_NAME = 'imsuat'
MD_SERVER_USER = 'md'
MD_SERVER_PASS = 'md'

# # MD数据库连接  用于数据抽取连接目标表
# MD_SERVER_ADDRESS = '10.88.158.97'
# MD_SERVICE_NAME = 'hxtkdb'
# MD_SERVER_USER = 'md'
# MD_SERVER_PASS = 'md'

#HR数据库连接  用于数据抽取连接目标表
HR_SERVER_ADDRESS = '10.88.53.17'
HR_SERVICE_NAME = 'oawh'
HR_SERVER_USER = 'cifdm_ai'
HR_SERVER_PASS = 'Tkamcoracle00'


from celery.schedules import crontab
# 配置结果后端
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_SERIALIZER = 'json'
# 配置时区
enable_utc = False
timezone = 'Asia/Shanghai'
# 限制时间
CELERY_TASK_SOFT_TIME_LIMIT = CELERY_TASK_TIME_LIMIT = 10 * 60

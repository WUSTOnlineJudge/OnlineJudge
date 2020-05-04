from __future__ import absolute_import
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineJudge.settings')
app = Celery()
app.config_from_object('judger.config')

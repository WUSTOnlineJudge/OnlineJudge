import time
from django.db import models
from utils.models import RichTextField
from account.models import User


class Problem(models.Model):
    display_id = models.CharField(default='1000', max_length=9, verbose_name='题目ID')
    # contest = models.ForeignKey()
    is_public = models.BooleanField(default=True, verbose_name='公开')
    title = models.TextField(verbose_name='题目')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 题目内容
    description = RichTextField(verbose_name='描述')
    description_input = RichTextField(verbose_name='输入描述')
    description_output = RichTextField(verbose_name='输出描述')
    hint = RichTextField(null=True, verbose_name='提示')
    source = RichTextField(null=True, verbose_name='来源')

    # 题目具体内容
    # [{input: "test", output: "123"}, {input: "test123", output: "456"}]
    samples = models.TextField(verbose_name='样例')
    # [{input: "test", output: "123", "score": 0}]
    test_case = models.TextField(verbose_name='测试例')

    # 默认数据
    create_time = models.IntegerField(default=time.time, blank=True, verbose_name='创建时间')
    last_update_time = models.IntegerField(default=time.time, verbose_name="最后修改事件")

    # 题目限制
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()

    # 其他功能
    submission_number = models.BigIntegerField(default=0, verbose_name="提交次数")
    ac_number = models.BigIntegerField(default=0, verbose_name="Accept次数")
    wa_number = models.BigIntegerField(default=0, verbose_name="WA次数")
    tle_number = models.BigIntegerField(default=0, verbose_name="TLE次数")
    mle_number = models.BigIntegerField(default=0, verbose_name="MLE次数")
    re_number = models.BigIntegerField(default=0, verbose_name="RE次数")
    ce_number = models.BigIntegerField(default=0, verbose_name="CE次数")

    class Meta:
        unique_together = ("display_id",)
        ordering = ("create_time",)

    def __str__(self):
        return f"id:{self.display_id} 标题: {self.title}"

    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save(update_fields=["submission_number"])

    def add_ac_number(self):
        self.ac_number = models.F("ac_number") + 1
        self.save(update_fields=["ac_number"])

    def add_wa_number(self):
        self.submission_number = models.F("wa_number") + 1
        self.save(update_fields=["wa_number"])

    def add_tle_number(self):
        self.submission_number = models.F("tle_number") + 1
        self.save(update_fields=["tle_number"])

    def add_mle_number(self):
        self.submission_number = models.F("mle_number") + 1
        self.save(update_fields=["mle_number"])

    def add_re_number(self):
        self.submission_number = models.F("re_number") + 1
        self.save(update_fields=["re_number"])

    def add_ce_number(self):
        self.submission_number = models.F("ce_number") + 1
        self.save(update_fields=["ce_number"])


class AcmProblemStatus(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='提交用户')
    problem_id = models.ForeignKey(Problem, models.CASCADE, verbose_name='提交题目')
    status = models.IntegerField(default=0, verbose_name='状态')
    submit_time = models.IntegerField(default=time.time, verbose_name='提交时间')

    class Meta:
        verbose_name = 'acm提交数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'用户名{self.user} 题目{self.problem_id} 状态{self.status}'

import time
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from account import Perms


class User(AbstractBaseUser):
    class UserType:
        SUPER_ADMIN = 0,
        ADMIN = 1,
        REGULAR = 2
    user_type_choice = (
        (UserType.SUPER_ADMIN, 'Super Admin'),
        (UserType.ADMIN, 'Admin'),
        (UserType.REGULAR, 'Regular')
    )
    # 用户基础数据
    username = models.CharField(unique=True, blank=False, max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=100, blank=False, verbose_name='密码')
    email = models.EmailField(blank=False, null=False, verbose_name='邮箱')
    create_time = models.IntegerField(default=time.time, blank=True, verbose_name='创建时间')
    user_type = models.IntegerField(default=0, choices=user_type_choice, verbose_name='用户类型')
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'account'

    def __str__(self):
        return f'用户名{self.username} 用户类型{self.user_type_choice[self.user_type][1]}'

    def has_perm(self, perm, obj=None):
        return self.user_type != User.UserType.REGULAR

    def is_admin_or_has_perm(self, perm: str):
        if self.user_type != User.UserType.REGULAR:
            return True
        return len(UserPerm.objects.filter(user=self, perm=perm)) > 0

    def is_admin_or_has_perms(self, perms: list):
        if self.user_type != User.UserType.REGULAR:
            return True
        return len(UserPerm.objects.filter(user=self, perm__in=perms)) >= len(perms)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(default='', max_length=16, verbose_name='昵称')
    real_name = models.CharField(default='', max_length=16, verbose_name='真实姓名')
    blog = models.URLField(default='', verbose_name='博客')
    github = models.URLField(default='', verbose_name='Github')
    sign = models.TextField(default='', verbose_name='个性签名')
    school = models.TextField(default='', verbose_name='学校')

    submission_num = models.IntegerField(default=0, verbose_name='提交次数')
    accept_num = models.IntegerField(default=0, verbose_name='通过次数')

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'用户名{self.user} 昵称{self.nickname}'


class UserPerm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perm = models.CharField(max_length=6, choices=Perms.PERM_CHOICES, null=False, blank=False)

    class Meta:
        unique_together = (
            ('user', 'perm')
        )

    def __str__(self):
        return f'{self.id}-{self.user.username}-{self.perm}'
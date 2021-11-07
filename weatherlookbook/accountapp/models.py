from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
                                        
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password, **extra_fields) :
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.model(email=email, **extra_fields)

        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uid = models.AutoField(primary_key=True)

    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=30,unique=True)
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )
    
    profile_image = models.ImageField(upload_to='Image/', null=True, blank=True)

    #like_boards = models.ManyToManyField('Board', blank=True, related_name='like_users')


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        #ordering = ('-date_joined',)

    def __str__(self):
        return self.username

    def get_full_name(self):        
        return self.username

    def get_short_name(self):
        return self.username
   
    @property
    def is_staff(self):
        return self.is_superuser




"""
# Create your models here.
class User(AbstractUser):
    uid = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(null=True)
"""
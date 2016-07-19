# -*- coding: utf-8 -*-
# Apr.26.2016
from django.db import models


class Message(models.Model):
    """ 消息
    status:消息状态（0：正常，1：删除），默认为0；
    title:消息标题；
    content：消息内容；
    categoriy：消息类型（0：系统消息，1：用户消息），demo考虑0即可
    """
    status = models.SmallIntegerField(verbose_name=u'状态', default=0)
    title = models.CharField(verbose_name=u'消息标题', max_length=64)
    content = models.TextField(verbose_name=u'消息内容', null=True, blank=True)
    category = models.PositiveSmallIntegerField(verbose_name=u'消息类型',
                                                default=0)

    def __unicode__(self):
        return u'%s' % self.title

    def _bind_UserMessage(self,send_user ,recv_user):
        user_message = UserMessage.objects.create(
            send_user = send_user,
            recv_user = recv_user,
            message = self
        )
        return user_message


class UserMessage(models.Model):
    """ 用户消息
    recv_user:接收者（用户ID）；
    send_user:发送者（用户ID），系统消息时用户ID为1；
    readed：消息是否已读；
    status：消息状态（0：正常，1：删除）；
    create_time：消息发送时间；
    message：消息外键
    """
    recv_user = models.IntegerField(verbose_name=u'接收者', null=True, blank=True)
    send_user = models.IntegerField(verbose_name=u'发送者', null=True, blank=True)
    readed = models.BooleanField(verbose_name=u'已读', default=False)
    status = models.IntegerField(verbose_name=u'记录状态', default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    message = models.ForeignKey(Message, null=True, blank=True)

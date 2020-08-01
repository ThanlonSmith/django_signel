from django.db.models import signals


def before_save(*args, **kwargs):
    """
    增加之前
    :param args:
    :param kwargs:
    :return:
    """
    print(args)  # ()
    print(kwargs)


"""
{
    'signal': <django.db.models.signals.ModelSignal object at 0x7fb2c41964c0>,
    'sender': <class 'app.models.User'>,
    'instance': <User: User object (None)>,
    'raw': False,
    'using': 'default',
    'update_fields': None
}
"""


def after_save(*args, **kwargs):
    """
    增加之后
    :param args:
    :param kwargs:
    :return:
    """
    print(args)  # ()
    print(kwargs)
    """
    {
    'signal': <django.db.models.signals.ModelSignal object at 0x7f3196b96400>, 
    'sender': <class 'app.models.User'>, 
    'instance': <User: User object (10)>, 
    'created': True, 
    'update_fields': None, 
    'raw': False, 
    'using': 'default'
    }
    """


signals.pre_save.connect(before_save)
signals.post_save.connect(after_save)
"""
Model signals
    pre_init                    # django的modal执行其构造方法前，自动触发
    post_init                   # django的modal执行其构造方法后，自动触发
    pre_save                    # django的modal对象保存前，自动触发
    post_save                   # django的modal对象保存后，自动触发
    pre_delete                  # django的modal对象删除前，自动触发
    post_delete                 # django的modal对象删除后，自动触发
    m2m_changed                 # django的modal中使用m2m字段操作第三张表（add,remove,clear）前后，自动触发
    class_prepared              # 程序启动时，检测已注册的app中modal类，对于每一个类，自动触发
Management signals
    pre_migrate                 # 执行migrate命令前，自动触发
    post_migrate                # 执行migrate命令后，自动触发
Request/response signals
    request_started             # 请求到来前，自动触发
    request_finished            # 请求结束后，自动触发
    got_request_exception       # 请求异常后，自动触发
Test signals
    setting_changed             # 使用test测试修改配置文件时，自动触发
    template_rendered           # 使用test测试渲染模板时，自动触发
Database Wrappers
    connection_created          # 创建数据库连接时，自动触发
"""

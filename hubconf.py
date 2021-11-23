dependencies = ["torch", "pytorch-lightning"]

from whos_there.callback import NotificationCallback as _NotificationCallback


def notification_callback():
    """This docstring shows up in hub.help()"""
    return _NotificationCallback

from freenasUI.freeadmin.tree import TreeNode
from django.utils.translation import ugettext_lazy as _

BLACKLIST = ['Email', 'Advanced', 'Settings', 'SSL', 'Registration']
NAME = _('System')
ICON = u'SystemIcon'


class Reporting(TreeNode):

    gname = 'Reporting'
    name = _(u'Reporting')
    view = 'system_reporting'
    icon = u"ReportingIcon"


class Info(TreeNode):

    gname = 'SysInfo'
    name = _(u'System Information')
    view = 'system_info'
    icon = u"InfoIcon"


class Settings(TreeNode):

    gname = 'Settings'
    name = _(u'Settings')
    view = 'system_settings'
    icon = u"SettingsIcon"

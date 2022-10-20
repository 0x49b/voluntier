from django.db import models


# DROP TABLE IF EXISTS `Groups`;
# CREATE TABLE `Groups` (
#   `Name` varchar(35) NOT NULL,
#   `UID` int(11) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
class Group(models.Model):
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    name = models.CharField(max_length=35)
    uid = models.IntegerField()


# Create your models here.
# DROP TABLE IF EXISTS `GroupPrivileges`;
# CREATE TABLE `GroupPrivileges` (
#   `id` int(11) NOT NULL,
#   `group_id` int(11) NOT NULL,
#   `privilege_id` int(11) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# class GroupPrivileges(models.Model):
#     class Meta:
#         verbose_name = 'Group Privilege'
#         verbose_name_plural = 'Group Privileges'

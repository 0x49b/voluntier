import uuid

from django.db import models


class EventConfig(models.Model):
    class Meta:
        verbose_name = "Event Config"
        verbose_name_plural = "Event Configs"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=255)
    buildup_start_date = models.DateField(blank=True)
    event_start_date = models.DateField(blank=True)
    event_end_date = models.DateField(blank=True)
    teardown_end_date = models.DateField(blank=True)
    event_welcome_message = models.CharField(max_length=255, blank=True, null=True)


class Room(models.Model):
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)
    man = models.TextField(blank=True, null=True)
    from_pentabarf = models.BooleanField(default=False)
    show = models.BooleanField(default=True)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

'''
DROP TABLE IF EXISTS `ShiftEntry`;
CREATE TABLE `ShiftEntry` (
  `id` int(11) NOT NULL,
  `SID` int(11) NOT NULL DEFAULT '0',
  `TID` int(11) NOT NULL DEFAULT '0',
  `UID` int(11) NOT NULL DEFAULT '0',
  `Comment` text,
  `freeload_comment` text,
  `freeloaded` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

''' 
DROP TABLE IF EXISTS `Shifts`;
CREATE TABLE `Shifts` (
  `SID` int(11) NOT NULL,
  `title` text,
  `shifttype_id` int(11) NOT NULL,
  `start` int(11) NOT NULL,
  `end` int(11) NOT NULL,
  `RID` int(11) NOT NULL DEFAULT '0',
  `URL` text,
  `PSID` int(11) DEFAULT NULL,
  `created_by_user_id` int(11) DEFAULT NULL,
  `created_at_timestamp` int(11) NOT NULL,
  `edited_by_user_id` int(11) DEFAULT NULL,
  `edited_at_timestamp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
from asgiref.sync import sync_to_async
from django.db import models


class AsyncManager(models.Manager):
    aget_func = sync_to_async(models.Manager.get)
    aget_or_create_func = sync_to_async(models.Manager.get_or_create)
    acount_func = sync_to_async(models.Manager.count)
    acreate_func = sync_to_async(models.Manager.create)
    alast_func = sync_to_async(models.Manager.last)
    alatest_func = sync_to_async(models.Manager.latest)

    async def aget(self, *args, **kwargs):
        return await self.aget_func(*args, **kwargs)

    async def aget_or_create(self, *args, **kwargs):
        return await self.aget_or_create_func(*args, **kwargs)

    async def acount(self, *args, **kwargs):
        return await self.acount_func(*args, **kwargs)

    async def acreate(self, *args, **kwargs):
        return await self.acreate_func(*args, **kwargs)

    # Example decorator
    @sync_to_async
    def afirst_func(self, *args, **kwargs):
        return self.filter(*args, **kwargs).first()

    async def afirst(self, *args, **kwargs):
        return await self.afirst_func(*args, **kwargs)

    async def alast(self, *args, **kwargs):
        return await self.alast_func(*args, **kwargs)

    async def alatest(self, *args, **kwargs):
        return await self.alatest_func(*args, **kwargs)

    async def afilter(self, *args, **kwargs):
        return await sync_to_async(list)(self.filter(*args, **kwargs))

    async def aall(self, *args, **kwargs):
        return await sync_to_async(list)(self.all())

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


# Create your views here.


# noinspection PyUnusedLocal
def index(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the contacts index.")

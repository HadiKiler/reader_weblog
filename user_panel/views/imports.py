from django.shortcuts import render
from rest_framework.response import *
from react_panel.models import *
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import make_password
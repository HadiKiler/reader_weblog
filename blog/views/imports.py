from django.shortcuts import *
from django.urls import reverse
from react_panel.models  import *
from django.db import transaction
from django.contrib.auth.decorators import login_required
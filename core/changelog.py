import asyncio
import re
from subprocess import PIPE
from typing import List

from discord import Embed

from core.models import getLogger
from core.utils import truncate

logger = getLogger(__name__)

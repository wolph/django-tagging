from django.db.models import get_model
from coffin.template import Library
from django.utils.translation import ugettext as _

from tagging.models import Tag, TaggedItem
from tagging.utils import LINEAR, LOGARITHMIC

register = Library()

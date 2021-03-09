"""Get Method for HTML Dictionary Value Retrieval"""
from django import template
register = template.Library()


@register.filter(name='get')
def get(mapping, key):
    """Retrive values based on keys"""
    return mapping.get(key, 'N/A')

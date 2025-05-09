from django import template
import re
import textwrap
from django.utils.html import strip_tags
from html import unescape

register = template.Library()

@register.filter
def trim_title(value, args="30,3"):
    """Обрезает title по количеству строк и добавляет троеточие"""
    try:
        line_length, max_lines = map(int, args.split(','))
    except ValueError:
        line_length, max_lines = 30, 3  # дефолт

    wrapped = textwrap.wrap(value, width=line_length)
    if len(wrapped) > max_lines:
        trimmed = wrapped[:max_lines]
        trimmed[-1] = trimmed[-1].rsplit(' ', 1)[0] + '...'
        return '\n'.join(trimmed)
    return value


@register.filter
def first_paragraph(value):
    match = re.search(r'<p>(.*?)</p>', value, re.DOTALL)
    return match.group(0) if match else ''


@register.filter
def prepare_meta(text):
    """
    Подготавливает текст для использования в meta-тегах:
    1. Удаляет все HTML-теги
    2. Преобразует HTML-сущности в нормальные символы
    3. Удаляет специальные символы
    4. Убирает лишние пробелы
    5. Обрезает до разумной длины
    """
    if not text:
        return ""
    
    # 1. Удаляем HTML-теги
    text = strip_tags(str(text))
    
    # 2. Преобразуем HTML-сущности
    text = unescape(text)
    
    # 3. Удаляем специальные символы
    text = re.sub(r'[\'"<>]', '', text)
    
    # 4. Заменяем множественные пробелы и переносы строк
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 5. Обрезаем до 160 символов (стандарт для meta description)
    return text[:160]
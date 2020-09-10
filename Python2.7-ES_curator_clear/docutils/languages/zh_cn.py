# -*- coding: utf-8 -*-
# $Id: zh_cn.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: Pan Junyong <panjy@zopechina.com>
# Copyright: This module has been placed in the public domain.

# New language mappings are welcome.  Before doing a new translation, please
# read <http://docutils.sf.net/docs/howto/i18n.html>.  Two files must be
# translated for each language: one in docutils/languages, the other in
# docutils/parsers/rst/languages.

"""
Simplified Chinese language mappings for language-dependent features
of Docutils.
"""

__docformat__ = 'reStructuredText'

labels = {
      # fixed: language-dependent
      'author': u'作者',
      'authors': u'作者群',
      'organization': u'組織',
      'address': u'網址',
      'contact': u'聯系',
      'version': u'版本',
      'revision': u'修訂',
      'status': u'狀态',
      'date': u'日期',
      'copyright': u'版權',
      'dedication': u'獻辭',
      'abstract': u'摘要',
      'attention': u'注意',
      'caution': u'小心',
      'danger': u'危險',
      'error': u'錯誤',
      'hint': u'提示',
      'important': u'重要',
      'note': u'注解',
      'tip': u'技巧',
      'warning': u'警告',
      'contents': u'目錄',
} 
"""Mapping of node class name to label text."""

bibliographic_fields = {
      # language-dependent: fixed
      u'作者': 'author',
      u'作者群': 'authors',
      u'組織': 'organization',
      u'網址': 'address',
      u'聯系': 'contact',
      u'版本': 'version',
      u'修訂': 'revision',
      u'狀态': 'status',
      u'時間': 'date',
      u'版權': 'copyright',
      u'獻辭': 'dedication',
      u'摘要': 'abstract'}
"""Simplified Chinese to canonical name mapping for bibliographic fields."""

author_separators = [';', ',',
                     u'\uff1b', # '；'
                     u'\uff0c', # '，'
                     u'\u3001', # '、'
                    ]
"""List of separator strings for the 'Authors' bibliographic field. Tried in
order."""
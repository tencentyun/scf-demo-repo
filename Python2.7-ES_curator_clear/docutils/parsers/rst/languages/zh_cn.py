# -*- coding: utf-8 -*-
# $Id: zh_cn.py 7119 2011-09-02 13:00:23Z milde $
# Author: Panjunyong <panjy@zopechina.com>
# Copyright: This module has been placed in the public domain.

# New language mappings are welcome.  Before doing a new translation, please
# read <http://docutils.sf.net/docs/howto/i18n.html>.  Two files must be
# translated for each language: one in docutils/languages, the other in
# docutils/parsers/rst/languages.

"""
Simplified Chinese language mappings for language-dependent features of
reStructuredText.
"""

__docformat__ = 'reStructuredText'


directives = {
      # language-dependent: fixed
      u'注意': 'attention',
      u'小心': 'caution',
      u'code (translation required)': 'code',
      u'危險': 'danger',
      u'錯誤': 'error',
      u'提示': 'hint',
      u'重要': 'important',
      u'注解': 'note',
      u'技巧': 'tip',
      u'警告': 'warning',
      u'忠告': 'admonition',
      u'側框': 'sidebar',
      u'主題': 'topic',
      u'line-block (translation required)': 'line-block',
      u'parsed-literal (translation required)': 'parsed-literal',
      u'醒目': 'rubric',
      u'銘文': 'epigraph',
      u'要點': 'highlights',
      u'pull-quote (translation required)': 'pull-quote',
      u'複合': 'compound',
      u'容器': 'container',
      #u'questions (translation required)': 'questions',
      u'表格': 'table',
      u'csv表格': 'csv-table',
      u'清單表格': 'list-table',
      #u'qa (translation required)': 'questions',
      #u'faq (translation required)': 'questions',
      u'中繼資料': 'meta',
      u'math (translation required)': 'math',
      #u'imagemap (translation required)': 'imagemap',
      u'圖片': 'image',
      u'圖例': 'figure',
      u'包含': 'include',
      u'原文': 'raw',
      u'代替': 'replace',
      u'統一碼': 'unicode',
      u'日期': 'date',
      u'類型': 'class',
      u'角色': 'role',
      u'預設角色': 'default-role',
      u'標題': 'title',
      u'目錄': 'contents',
      u'章節序號': 'sectnum',
      u'題頭': 'header',
      u'頁腳': 'footer',
      #u'footnotes (translation required)': 'footnotes',
      #u'citations (translation required)': 'citations',
      u'target-notes (translation required)': 'target-notes',
      u'restructuredtext-test-directive': 'restructuredtext-test-directive'}
"""Simplified Chinese name to registered (in directives/__init__.py)
directive name mapping."""

roles = {
    # language-dependent: fixed
    u'縮寫': 'abbreviation',
    u'簡稱': 'acronym',
    u'code (translation required)': 'code',
    u'index (translation required)': 'index',
    u'i (translation required)': 'index',
    u'下標': 'subscript',
    u'上標': 'superscript',
    u'title-reference (translation required)': 'title-reference',
    u'title (translation required)': 'title-reference',
    u't (translation required)': 'title-reference',
    u'pep-reference (translation required)': 'pep-reference',
    u'pep (translation required)': 'pep-reference',
    u'rfc-reference (translation required)': 'rfc-reference',
    u'rfc (translation required)': 'rfc-reference',
    u'強調': 'emphasis',
    u'加粗': 'strong',
    u'字面': 'literal',
    u'math (translation required)': 'math',
    u'named-reference (translation required)': 'named-reference',
    u'anonymous-reference (translation required)': 'anonymous-reference',
    u'footnote-reference (translation required)': 'footnote-reference',
    u'citation-reference (translation required)': 'citation-reference',
    u'substitution-reference (translation required)': 'substitution-reference',
    u'target (translation required)': 'target',
    u'uri-reference (translation required)': 'uri-reference',
    u'uri (translation required)': 'uri-reference',
    u'url (translation required)': 'uri-reference',
    u'raw (translation required)': 'raw',}
"""Mapping of Simplified Chinese role names to canonical role names
for interpreted text."""
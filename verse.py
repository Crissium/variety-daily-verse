import json
import requests
from html import unescape
from variety.plugins.IQuoteSource import IQuoteSource


class DailyVerse(IQuoteSource):
	def __init__(self):
		super(IQuoteSource, self).__init__()

	@classmethod
	def get_info(cls):
		return {
			"name": "Bible Gateway's Verse of the Day",
			"description": "A daily word of exultation",
			"author": "Xing Yi",
			"version": "1.0.1",
		}

	def supports_search(self):
		return False

	def get_random(self):
		version = 'ESV'
		response = json.loads(requests.get('https://www.biblegateway.com/votd/get/?format=json&version=' + version).content)
		return [{'quote': unescape(response['votd']['text']), 'author': response['votd']['display_ref'], 'sourceName': None, 'link': None}]

	def get_for_author(self, author):
		return []

	def get_for_keyword(self, keyword):
		return []

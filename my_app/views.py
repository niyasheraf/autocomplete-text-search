# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
import pandas as pd
import numpy as np
# Create your views here.


def search(request):
	if request.method == "GET":
		try:
			query = request.GET.get("word")
			if query:
				df = pd.read_csv('word_search.tsv',sep='\t', header=None, names=["word","frequency"])
				res = df[df['word'].str.contains(query)==True]
				for i, row in res.iterrows():
					pos = row.word.find(query)
					res.at[i,'pos'] = pos
					dif = len(row.word) - len(query)
					res.at[i,'diff'] = dif
				sorted_res = res.sort_values(['pos', 'diff', 'frequency'], ascending=[True,True, False])['word'].to_list()[:25]
				res = HttpResponse()
				res.content = json.dumps(sorted_res)
				res.content_type = "application/json"
				res['Access-Control-Allow-Origin'] = '*'
				return res
			else:
				res = HttpResponse()
				res.content = json.dumps([])
				res.content_type = "application/json"
				res['Access-Control-Allow-Origin'] = '*'
				return res
		except Exception as e:
			return HttpResponse(json.dumps({"error":"Unknown Error!"}))


def search_page(request):
	return render(request, 'search.html')

# python
# -*- coding:utf-8 -*-
# author liao_wk time
from scopus import AuthorSearch
from scopus import AbstractRetrieval
from scopus import ScopusSearch
from scopus import Search

s = AuthorSearch('AUTHLAST(Guiying) and AUTHFIRST(Xu)', refresh=True )
# print(s)
ab = ScopusSearch("Fabrication")
# print(ab)


* 关键词检索默认每页50个，按相似度排
得到URL：（POST）
http://apps.webofknowledge.com/UA_GeneralSearch.do
得到参数：
{
fieldCount	1
action	search
product	UA
search_mode	GeneralSearch
SID	5CTA979bx1s8hZwSbiF
max_field_count	25
max_field_notice	注意:+无法添加另一字段。
input_invalid_notice	检索错误:+请输入检索词。
exp_notice	检索错误:+专利检索词可以在多个家族中找到+(
input_invalid_notice_limits	+<br/>注意:+滚动框中显示的字段必须至少与一个其他检索字段相组配。
sa_params	UA||5CTA979bx1s8hZwSbiF|http://apps.webofknowledge.com|'
formUpdated	true
value(input1)	Neuromorphic+Chips
value(select1)	TS
value(hidInput1)	
limitStatus	collapsed
ss_lemmatization	On
ss_spellchecking	Suggest
SinceLastVisit_UTC	
SinceLastVisit_DATE	
range	CUSTOM
period	Year+Range
startYear	1990
endYear	2018
editions	[…]
0	WOS.ESCI
1	WOS.SSCI
2	WOS.SCI
3	WOS.IC
4	WOS.AHCI
5	WOS.ISTP
6	WOS.CCR
7	BCI.BCI
8	KJD.KJD
9	MEDLINE.MEDLINE
10	RSCI.RSCI
11	SCIELO.SCIELO
collections	[…]
0	WOS
1	BCI
2	KJD
3	MEDLINE
4	RSCI
5	SCIELO
update_back2search_link_param	yes
ssStatus	display:none
ss_showsuggestions	ON
ss_query_language	auto
ss_numDefaultGeneralSearchFields	1
rs_sort_by	RS.D;PY.D;AU.A;SO.A;VL.D;PG.A
}

* 选中50篇论文，添加到结果列表
得到URL（POST）
http://apps.webofknowledge.com/MarkRecords.do?product=UA&
mark_id=UDB&SID=5CTA979bx1s8hZwSbiF&qid=3&search_mode=GeneralSearch
得到参数
{
product	UA
mark_id	UDB
SID	5CTA979bx1s8hZwSbiF
qid	3
search_mode	GeneralSearch
selectedIds	1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50

colName	
mark_from	
mark_to	
viewType	summary
}


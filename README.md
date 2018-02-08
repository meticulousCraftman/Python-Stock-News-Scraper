
# Python-News-Scraper
A program that scrapes for announcements from [moneycontrol.com](www.moneycontrol.com) so that traders can take informed decision.
Here is how to get started,
 

    import moneycontrol as mc
    
    # First parameter is the ticker symbol
    stock = mc.MoneyControl("ONGC")

The "stock" object has 3 main methods at present that can be used to extract announcements from Money Control.

### fetch_a(page_no=1)
This method is used to fetch announcements from the given page number. By default, page_no is 1. It returns a list of dictionary with all the values in it.

	# Fetching the announcements on page number 3 ofthe website
    stock.fetch_a(3)
    
	# Here is the output after running this method. 
	[
	   {
	      'content':'Oil & Natural Gas Corporation Limited has informed the Exchange regarding Change in Director(s) of the company.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=10266461',
	      'date':'4th-Jan-2018 14:11',
	      'title':' Oil & Natural Gas Corporation Limited ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oil-natural-gas-corporation-limited-10266461.html'
	   },
	   {
	      'content':'Pursuant to Regulation 30 of Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015, we hereby inform that Shri T K Sengupta, Director (Offshore), has ceased to be Director of the Company upon his attaining superannuation on 31.12.2017.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=10266101',
	      'date':'4th-Jan-2018 13:21',
	      'title':'Oil and Natural Gas Corporation - Change in Directorate ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-changedirectorate-10266101.html'
	   },
	   {
	      'content':'The Exchange had sought clarification from the Company with respect to news item captioned "Venezuela\'\'s PDVSA misses debt payments, used Russian bank to pay ONGC". The response from the Company is enclosed.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9926541',
	      'date':'15th-Nov-2017 16:56',
	      'title':' Oil & Natural Gas Corporation Limited ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oil-natural-gas-corporation-limited-9926541.html'
	   },
	   {
	      'content':'Reply to Clarification on media report.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9925541',
	      'date':'15th-Nov-2017 16:24',
	      'title':'Oil and Natural Gas Corporation - Updates ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-updates-9925541.html'
	   },
	   {
	      'content':'The Exchange has sought clarification from Oil & Natural Gas Corporation Ltd with respect to news article appearing on moneycontrol.com on November 13, 2017 titled "Venezuela likely to go bankrupt in a day?."The reply is awaited.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9860941',
	      'date':'13th-Nov-2017 14:23',
	      'title':'Oil and Natural Gas Corporation - Clarification sought from Oil & Natural Gas Corporation Ltd ',
	      'pdf_link':None
	   },
	   {
	      'content':'Oil & Natural Gas Corporation Limited has informed the Exchange regarding Change in Director(s) of the company.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9719361',
	      'date':'2nd-Nov-2017 12:20',
	      'title':' Oil & Natural Gas Corporation Limited ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oil-natural-gas-corporation-limited-9719361.html'
	   },
	   {
	      'content':'Shri A K Srinivasan, Director Finance, has ceased to be Director of the Company upon his attaining superannuation on 31.10.2017',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9717921',
	      'date':'2nd-Nov-2017 11:15',
	      'title':'Oil and Natural Gas Corporation - Change in Directorate ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-changedirectorate-9717921.html'
	   },
	   {
	      'content':"Un-audited Financial Results for the second Quarter and Half Year ended 30th September, 2017- Auditors''Limited Review Report",
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9660001',
	      'date':'28th-Oct-2017 16:58',
	      'title':'Oil and Natural Gas Corporation - Updates ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-updates-9660001.html'
	   },
	   {
	      'content':"ONGC declares results for Q2 FY''18; records impressive production performance",
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9659761',
	      'date':'28th-Oct-2017 16:37',
	      'title':'Oil and Natural Gas Corporation - Press Release / Media Release ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-press-release-media-release-9659761.html'
	   },
	   {
	      'content':'Pursuant to Regulation 30 of Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015, it is hereby inform that Govt. of India has nominated Dr. Sambit Patra, as an Independent Director on the Board of the Company.The Board of Directors of the Company have also approved induction of Dr. Sambit Patra, as an Additional Director with effect from 28th October, 2017.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9658841',
	      'date':'28th-Oct-2017 15:56',
	      'title':'Oil and Natural Gas Corporation - Change in Directorate ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-changedirectorate-9658841.html'
	   }
	]

Each announcement is described using 5 keys, namely:

 - **content** - The small description of the announcement present on the website.
 - **link** - The exact link of the announcement page from where the data is scraped.
 - **date** - The date and time of the announcement
 - **title** - The title of the announcement
 - **pdf_link** - The PDF link of the announcement if present, otherwise, None


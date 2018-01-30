import requests
import bs4

SEARCH_URL = "http://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str="
PREFIX_URL = "http://www.moneycontrol.com"


class MoneyControl(object):

    def __init__(self, ticker):
        self.ticker = ticker
        self.fetch_ticker()

    def fetch_ticker(self):
        try:
            r = requests.get(SEARCH_URL+self.ticker)
            if r.status_code==200:
                print("Fetched page for ticker : "+self.ticker)
                # Creating a bs4 object to store the contents of the requested page
                self.soup = bs4.BeautifulSoup(r.content, 'html.parser')
                self.more_anno_link = PREFIX_URL + str(self.soup.find("div", attrs={"class":"PT5 gL_11", "align":"right"}).find("a")["href"] ) # class name extracted after looking at the document
                self.more_news_link = PREFIX_URL + str(self.soup.find("div", attrs={"class":"PT5 gL_11 FR"}).find("a")["href"])
            elif r.status_code==404:
                print("Page not found")
            else:
                print("A different status code received : "+str(r.status_code))

        except requests.ConnectionError as ce:
            print("There is a network problem (DNS Failure, refused connectionn etc.). Error : "+str(ce))
            raise Exception
        
        except requests.Timeout as te:
            print("Request timed out. Error : "+str(te))
            raise Exception
        
        except requests.TooManyRedirects as tmre:
            print("The request exceeded the maximum no. of redirections. Error : "+str(tmre))
            raise Exception
        
        except requests. requests.exceptions.RequestException as oe:
            print("Any type of request related error : "+str(oe))
            raise Exception

    def fetch_annoucement(self):
        r = requests.get(self.more_anno_link)
        annoucement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        raw_links = annoucement_soup.find_all("a", attrs={"class":"bl_15"})
        list_of_links = []
        for x in raw_links:
            list_of_links.append(PREFIX_URL + x['href'])
        return list_of_links

    def fetch_news(self):
        pass

a = MoneyControl("ril")
print(a.fetch_annoucement())
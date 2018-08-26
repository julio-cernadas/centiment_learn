import webhoseio

def get_webhose_news(ticker):
        webhoseio.config(token="517a4e21-e484-4eac-aa8c-f50916e8db85")
        query_params = {
        "q": """language:english thread.country:US published:>1483232461 (site_category:stocks) (WFC OR wells fargo)
                (site_type:blogs OR site_type:discussions) (thread.title:'WFC' OR thread.title:'wells fargo')""",
        "ts": "1533754757303",
        "sort": "published"
        }
        output = webhoseio.query("filterWebContent", query_params)
        lst = [x for x in output['posts'][20]['text'].split('. ')
                for var in names if var in x.lower()]
        

        if len(company_name) >= 2:
                var1 = company_name[0].lower()
                var2 = company_name[1].lower()
                tick = ticker.lower()
                names = [var1,var2,tick]
        else:
                var1 = company_name[0].lower()
                tick = ticker.lower()
                names = [var1,tick]
        barrons_news = [[date,text] for date,text in lst
                                        for var in names 
                                        if var in text]

# lst = [ x.lower() for x in output['posts'][20]['text'].split('. ') 
#         if 'wfc' or 'wells' in x.lower()]
# print(lst)

# print(output['posts'][0]['text']) # Print the text of the first post
# print(output['posts'][0]['published']) # Print the text of the first post publication date

    
# # Get the next batch of posts
# output = webhoseio.get_next()
# print(output)

    
# Print the site of the first post
# print(output['posts'][0]['thread']['site'])

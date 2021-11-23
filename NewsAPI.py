import importlib
NewsAPI = importlib.import_module("newsapi-python")

newsapi = NewsApiClient(api_key='0f6bb26533f74234ab55c3d6bcee6de2')
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
sources = newsapi.get_sources()
api.get_everything(q='bitcoin')

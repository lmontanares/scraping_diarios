# Scrapy settings for diarios_chile project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "diarios_chile"

SPIDER_MODULES = ["diarios_chile.spiders"]
NEWSPIDER_MODULE = "diarios_chile.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'diarios_chile (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'diarios_chile.middlewares.DiariosChileSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    # 'diarios_chile.middlewares.DiariosChileDownloaderMiddleware': 543,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    # "scrapy_proxies.RandomProxy": 100,
    # "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 110,
    "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
    "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
}

# PROXY_MODE = 0
# PROXY_LIST = "/home/somebody/development/scrapy_pruebas/proxies/proxy_list.txt"


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     "diarios_chile.pipelines.BioBioPipeline": 1,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


FEEDS = {
    "items.json": {
        "format": "jsonlines",
        "encoding": "utf-8",
        "fields": ["title", "url", "date", "category"],
        "indent": 4,
        "overwrite": True,
        "store_empty": False,
    }
}


FAKEUSERAGENT_PROVIDERS = [
    "scrapy_fake_useragent.providers.FakeUserAgentProvider",  # this is the first provider we'll try
    "scrapy_fake_useragent.providers.FakerProvider",  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    "scrapy_fake_useragent.providers.FixedUserAgentProvider",  # fall back to USER_AGENT value
]
# USER_AGENT = "<your user agent string which you will fall back to if all other providers fail>"
FAKEUSERAGENT_FALLBACK = "Mozilla/5.0 (Android; Mobile; rv:40.0)"
RANDOM_UA_PER_PROXY = True

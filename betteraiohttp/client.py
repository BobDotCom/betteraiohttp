import aiohttp
import re
import url_parser


async def check_link_base(url, block_list):
    """
    :meta: private
    """
    url = url_parser.get_url(url)._asdict()
    for blocked in block_list:
        parsed_blocked = url_parser.get_url(blocked.replace('*', '-'))._asdict()
        delete = True
        for k in ['sub_domain', 'domain', 'top_domain', 'path']:
            rep = parsed_blocked[k]
            if k == 'path':
                rep = rep[1:]
            if url[k] != rep and rep.replace('.','') != '-':
                delete = False
                break
        if delete:
            return True


async def check_links(urls, block_list):
    """
    :meta: private
    """
    for url in urls:
        if await check_link_base(url, block_list):
            return True


class ClientSession(aiohttp.ClientSession):
    """
    Base ClientSession class. A subclass of :class:`aiohttp.ClientSession`, this functions in almost the same way.

    Parameters
    ----------
    rickroll_queries: :class:`list`
        Rickroll quotes to search for. The defaults will work for most cases.
    block: :class:`list`
        List of links to block.
    """
    def __init__(self, *args, **kwargs):
        default = {
            'rickroll_queries': ["rickroll", "rick roll", "rick astley", "never gonna give you up"],
            'block': [],
            'timeout': aiohttp.ClientTimeout(total=300, sock_read=10)
            }
        default.update(kwargs)
        self.rickroll_regex = re.compile('|'.join(default['rickroll_queries']), re.IGNORECASE)
        self.block_list = default['block']
        del default['rickroll_queries']
        del default['block']
        super().__init__(*args, **default)

    async def _request(self, *args, **kwargs):
        req = await super()._request(*args, **kwargs)
        regex = self.rickroll_regex
        content = str(await req.content.read())
        req.rickroll = bool(regex.search(content))
        blocked_urls = self.block_list
        urls = [str(redirect.url_obj) for redirect in req.history]
        req.blocked = bool(await check_links(urls, blocked_urls))
        return req

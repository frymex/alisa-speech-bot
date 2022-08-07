import aiohttp


class Randomus:
    cookies = {
        'yandexuid': '5836250011634414048',
        'yuidss': '5836250011634414048',
        'ymex': '1949774050.yrts.1634414050',
        'gdpr': '0',
        'yandex_login': 'malinoshevskiy.dmitriy',
        'mda': '0',
        'my': 'YwA=',
        'L': 'RmN9e1h2WQ1hVH5TUnpuBldUBltZQXd+CRBVLV0/BhImFSoZKwhLISsqH0QdLA==.1649795946.14945.363453.f2be84fccfbee2e96bf209ca3a9762cc',
        'is_gdpr': '0',
        'is_gdpr_b': 'CKWUcRDlbigC',
        'i': 'vW7Vaw7qgisYSdBDThOIJBDCcd8o5bO6Bx3jiaWfwZBgguLdM6XTu6XtagiQtPkpaoaQwKgF7aTnkRS44TZ9d0yUE70=',
        '_ym_uid': '1653409573109401737',
        'yp': '1965155946.udn.cDptYWxpbm9zaGV2c2tpeS1kbWl0cml5#1952287638.multib.1#1665563520.szm.1_25:1536x864:1536x714#1660084441.ygu.1',
        'yandex_gid': '132',
        'bltsr': '1',
        '_ym_d': '1658779663',
        'Session_id': '3:1659812245.5.1.1634931289972:ECIAAOnKDQGKBxEMuAYCKg:4a.1.2:1|1291551515.2691000.2.1:272093698.2:2691000|194982144.14864657.2.2:14864657|3:10256375.215684.873Pd40mx2jtEmmUNq3a9Q5NuhE',
        'sessionid2': '3:1659812245.5.1.1634931289972:ECIAAOnKDQGKBxEMuAYCKg:4a.1.2:1.499:1|1291551515.2691000.2.1:272093698.2:2691000|194982144.14864657.2.2:14864657|3:10256375.132115.Ni01h1PEyJ2SULdC6rwwAFWjzLU',
        '_yasc': '+IIwoyt0FdSti2gnPURKUAEZny8+s7urrW7WuycNOToMA5Yd0tNRyj9QA/8=',
        'no-region-popup': 'true',
        'session-geo-data': 'eyJyZWdpb25OYW1lIjoiVGVsIEF2aXYiLCJjb3VudHJ5TmFtZSI6IklzcmFlbCIsInRpbWV6b25lIjoiQXNpYS9KZXJ1c2FsZW0iLCJsb2NhbGUiOnsiY29kZSI6ImVuIiwibmFtZSI6IkludGVybmF0aW9uYWwgKEVuZ2xpc2gpIiwibGFuZyI6ImVuIiwibGFuZ05hbWUiOiJFbmdsaXNoIiwicmVnaW9uIjoiaW50IiwicmVnaW9uTmFtZSI6IkludGVybmF0aW9uYWwiLCJjdXJyZW5jeSI6IlVTRCIsInRsZCI6ImNvbSIsIm9yZGVyIjoxMDAsImRlZmF1bHQiOnRydWV9fQ%3D%3D',
        'XSRF-TOKEN': '59b32985cdae6bc17ec94c8ef65515dff5c4c9c9%3A1659815810',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://cloud.yandex.ru',
        'Referer': 'https://cloud.yandex.ru/services/speechkit',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-csrf-token': 'bf57fb54dad97e3cfc137310862fcac535eb14d1:1659815774',
    }





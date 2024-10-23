# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 10:36
# @Author  : lx
# @desc  :  xhs

import requests,os
import execjs,base64
from lxpy import get_md5
from requests.utils import dict_from_cookiejar


# 更换canvas
def get_cookie():
    with open('./meihua.js', 'r', encoding='gbk')as f:
        js_script = f.read()
    d = execjs.compile(js_script)

    params = '{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","webdriver":false,"language":"zh-CN","colorDepth":24,"deviceMemory":8,"hardwareConcurrency":8,"screenResolution":"1920;1080","availableScreenResolution":"1920;1040","timezoneOffset":-480,"timezone":"Asia/Shanghai","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","plugins":["Chrome PDF Plugin::Portable Document Format::application/x-google-chrome-pdf~pdf","Chrome PDF Viewer::::application/pdf~pdf","KGChromePlugin_64.dll::::application/kg-plugin~","Native Client::::application/x-nacl~,application/x-pnacl~"],"canvas":"20cfbbb02b2606dbc2ccb15a3cd2b558","adBlock":false,"hasLiedLanguages":false,"hasLiedResolution":false,"hasLiedOs":false,"hasLiedBrowser":false,"touchSupport":"0;false;false","fonts":"4;7;8","audio":"124.04347527516074"}'
    sign = d.call('timeStamp2',params)

    id = get_md5(sign+"RRq9y03tuV")
    data = {'id': id,'sign': sign}

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.xiaohongshu.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    }
    cookie_url = "https://www.xiaohongshu.com/fe_api/burdock/v2/shield/registerCanvas?p=cc"
    req = requests.post(cookie_url, json=data,headers=headers)
    return dict_from_cookiejar(req.cookies)


def run(item_url):
    sess = requests.session()
    cookiedict = get_cookie()
    timestamp2 = cookiedict['timestamp2']
    timestamp2_sig = cookiedict['timestamp2.sig']
    Headers = {
        "origin": "https://www.xiaohongshu.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        'cookie': f"timestamp2={timestamp2};&timestamp2.sig={timestamp2_sig}",
    }
    Headers.update({'cookie':get_gid()+Headers['cookie']})
    print(Headers)
    return sess.get(item_url, headers=Headers).text


def get_gid():
    sig_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "cache-control": "no-cache",
        "content-length": "3032",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "referer": "https://www.xiaohongshu.com/discovery/item/613df18d0000000001024e4f",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "x-b3-traceid": "a4319ce6cab6bf5d",
        "x-s": "sBTGOjVk1lMiOiFp0Y5K02MlsidvsY5iOgqJOYTWOis3",
        "x-s-common": "2UQAPsHCPsIjqArjwjHjNsQhPsHCPsIj2erjwjHUN0Z1PjFUHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQfqfSS2frjNsQh+sHCH0r1weG1PsHVHdWMH0ijP/WlG/P9G/WIPAZ987HF2nREyn8Uyep94Bzjq9pD8o4lG0rEy7Hh+9uIPeZIPeHF+/GM+UHVHdW9H0il+0L7+/Z9+/cF+/WENsQh+UHCHd+spr4OyS83Pnl+yLRkzdZIn/pNPeQ+Jo+k8o8An/pk/94laDR8pb4OygPAHjIj2eWjwjHh4gz9agG78pSVLBSQ4f+TanVIq7Y1+nL9ze+APbm78SrI/LbHnD8aaL+HPsTn4BYQyrzY/fRTP9El4rMYLo4xa/+P8rTp+9LAcfTPJnQcasTPzLEYqg4+anT98pzj+g+ncDbS8S8FP/Yg4nTIqgzn8p8F+BMM4AzQcA8A2e48zLSbP9LINFTSy9G98/mgLbZh+FMfLrMDq7Yn4URQyb4waL+MOaHVHdWEH0iTPArhPeZ7PeW7Kc==",
        "x-sign": "X8efe40ac90c7df2a07c0c5a1ffa73c41",
        "x-t": "1657506544589"
    }
    sig_data = {"platform": "Windows", "sdkVersion": "2.0.2-2", "svn": "0",
                "profileData": "020bc4c6cd2e52b94cff7e394019c991266dbc1b63406df026698a45d612461bb11cbaba61194bc66881a1f35fb73bf6aba664e735c294a0f0852a0f48b25c1709ac61e4058ed90fd772745ed0adead9d6eedd3e6298f16c90d2d103ea1b431d29a77a8ac580d8262fe61699337e07ac10653aeebeb7982f1bb2d4a53ed988c394b5a741075a4af03d2055d101afa7188560cc6c70c13523327ff705e883fa185def7b11d14529e60bfc19b06f588facbb04e0978cecbb6464e022dd832bfab1536205ea7bbf5580c0f7bbde33ac8b7dd665cc9a97a2f85f24a9ce19c9f0a38b223415b5127b51f8a33f12bc43cade4c128e6e7adecc0356ee40499e856ab4e10598dff3c8c6f7aa128e6e7adecc03569ff3ff158db33a93ad152662932ec9cc8c4c161d04abcac58ec71b700e81616515b6a934f18cba7dc0f4f8db0603c459ebea3b41f7c8d02886f338e7a24e9c8a215e038e56f0e111b9c0811769afa6bb69361d7d357ada6fe471c05e121faea7deadb1b95d7229d8d5b58df589f44c9c19bc0bef2212fb35e4b6592f3b2df10a2e5187aab23910d4aabeee883328a796e289e8d8cd9d65606b45a05a807783425a53a7d1a666d6922876fcfe31cfded1aabeee883328a7961d0479d7e37c1b4b34ce4cdc6caf5b5ccf685d50e13bb3430dee54a1cf74a19108a865c57b02316346365fb2de774f24fbc9e2490678764b905196625770c97347c3df8e6952798c3a8605925a46b76a0083979fe6044559989e10449fae7a4ed99833ef60c34dc6f06b4c3227bf05365cbec82320bebf8532cada09ecf2cebf002f8fa54543d138c9940e121b113ab6972a4e10b2edc0f4fca382a23a035bb782d61ae8ec21ab0063663772564050fd15827a77940046048c98d67d35133c92c9cd78281673dc35993cdd83cc6bf665472a550b5705f33b5cbec82320bebf8532cada09ecf2cebf002f8fa54543d138c9940e121b113ab6972a4e10b2edc0f4fca382a23a035bb782d61ae8ec21ab0063663772564050fd15827a77940046048c98d67d35133c92c9cd78281673dc3535afbf36f81f955586af57b6db281e3a178aac60a8ebb9c45cbec82320bebf8532cada09ecf2cebf002f8fa54543d138c9940e121b113ab6972a4e10b2edc0f4fca382a23a035bb782d61ae8ec21ab0063663772564050fd15827a77940046048c98d67d35133c92c9cd78281673dc3585a8c7d22f83d53116be5924039b719fb49324584db8e5ef0dd640145a125731002f8fa54543d138c9940e121b113ab6972a4e10b2edc0f4fca382a23a035bb782d61ae8ec21ab0063663772564050fd15827a77940046048c98d67d35133c92c9cd78281673dc35bdb9e4ffae1f57223d2d35dcd3a236e08a16b2da86c1ff27c2a3aae3b733b55986d16b71d4ba56af2b0e3814ce38bc0988df66efde31b9a1831bc358a992e93dfd63e2328b965a0441558cd7380b5a81890c245bfdf932a041558cd7380b5a810cc1d0d16fa56be241558cd7380b5a81f2aa8a8bf787583741558cd7380b5a81a52040878e34caec41558cd7380b5a818c3e174b76c8ee87920185786ce4a679131977961bb39a4ea8cbc75eaa7414441d2f7cdf67301c7d17b4aafe3300a407213d357aa872d03566a6009b1591e0c6a05bf15363f745f0cc23900e08f72cc9f8d627e8aed97ce96c113d1a2fe9b520a6e283a06ee06690febbacaa861770c85271bc04a8ce01da171b902a4662db924ffdbfdee3e9b09928ff4f50e6956566a9cf10c52add99ea7c6d5ca09f64bc73df15a07cb2750d3141ba21b809ab8436704f2578d18cadfdce75b3cab13cb187781cb5ffd11b183a748697e92be9050f9b19e2cdfd3d9f03027f00cfbb4eb5a525fff9cf3b1bb76a77964d823952b04a435c83d7562737d91f6c14a802e7586fcd68a720f387fd382180a794b93b3c8ea11bfd35fe64403658f0853b6a568455a2ef8498c6f5da69ea335d3cbdc2166631356ee7ea1952b931356ee7ea1952b90ff7b31b24c01a4f0acc147db4daf87f985586f327847d6c31356ee7ea1952b9820e4ed607d3a4e9"}
    s = requests.post('https://www.xiaohongshu.com/fe_api/burdock/v2/shield/profile', headers=sig_headers,
                  json=sig_data).cookies
    gid = s.get('gid')
    gid_sig = s.get('gid.sig')
    return f'gid={gid};gid_sig={gid_sig};'


if __name__ == '__main__':
    # "https://www.xiaohongshu.com/user/profile/5b87a4713f383400019f2723"
    item_url = "https://www.xiaohongshu.com/user/profile/5b87a4713f383400019f2723"
    response_text = run(item_url)
    print(response_text)


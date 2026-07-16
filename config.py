# 配置文件，包含直播源URL、黑名单URL、公告信息、EPG URL、测速超时时间和线程池最大工作线程数

# 优先使用的IP版本，这里设置为ipv4
ip_version_priority = "ipv4"

# 直播源URL列表
source_urls = [

"https://github.boki.moe/https://raw.githubusercontent.com/frxz751113/IPTVzb1/refs/heads/main/js.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/alantang1977/iptv-auto/refs/heads/main/my.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/alantang1977/iptvm3u/refs/heads/main/py/live.txt",
"https://raw.githubusercontent.com/q1017673817/iptvz/refs/heads/main/zubo.txt",
"https://raw.githubusercontent.com/jn950/live/main/tv/pllive.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/develop202/migu_video/refs/heads/main/interface.txt",
"https://sub.ottiptv.cc/yylunbo.m3u",
"https://ghfast.top/raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt",
"https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.txt",
"https://raw.githubusercontent.com/yyyr-otz/iptv-api/refs/heads/master/output/user_result.txt",
"https://raw.githubusercontent.com/pdd520/iptv-api/master/output/result.txt",
"https://raw.githubusercontent.com/JE668/iptv-api/master/output/result.txt",
"https://raw.githubusercontent.com/qingtingjjjjjjj/config-tv/main/zubo_all.txt",
"https://live.zbds.top/tv/iptv4.txt",
"https://raw.githubusercontent.com/laodaoxiaoge/iptv-api/refs/heads/master/output/result.txt",
"https://2121.ccwu.cc/",
"http://202.140.142.145:40207/zhibo/iptv.txt",
"https://raw.githubusercontent.com/iptv-org/iptv/gh-pages/countries/cn.m3u",
"https://live.hacks.tools/tv/iptv4.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/fingersc/iptv-api/master/output/user_result.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/perrsonxxa/iptv-api/master/output/user_result.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/mike1996/iptv-api/refs/heads/master/output/result.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/gz8482552/itv/refs/heads/master/output/result.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/lemonTV/main/iptv-fe.m3u",
"https://raw.githubusercontent.com/jn950/live/refs/heads/main/tv/pllive.txt",
"https://raw.githubusercontent.com/jn950/live/main/tv/holive.m3u",
"https://raw.githubusercontent.com/cyh92/live/main/source/webtv.txt",
"https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
"https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/gat.txt",
"https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
"https://raw.githubusercontent.com/alantang1977/iptv-auto/refs/heads/main/my.txt",
"https://cnb.cool/fgvss/zbds/-/git/raw/main/zbtvupan.txt",
"https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
"https://raw.githubusercontent.com/zwc456baby/iptv_alive/refs/heads/master/live.m3u",
"https://raw.githubusercontent.com/pdd520/IPTV/refs/heads/master/config/rtp/tw.txt",
"https://raw.githubusercontent.com/Supprise0901/TVBox_live/refs/heads/main/live.txt",
"https://raw.githubusercontent.com/iptv-org/iptv/master/streams/cn.m3u",
"https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u",
"https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt",
"https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/others_output.txt",
"https://gitee.com/mytv-android/mytvJS/raw/main/js.gitee.m3u",
"http://38.75.136.137:88/api/tvlist.php",
"https://l.gmbbk.com/upload/18281828.txt",
"https://live.zbds.top/tv/iptv6.txt",   
]

# 直播源黑名单URL列表，去除了重复项
url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226419/index.m3u8",
    "http://[2409:8087:5e00:24::1e]:6060/000000001000/1000000006000233001/1.m3u8",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "stream1.freetv.fun",
    "chinamobile",
    "gaoma",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

# 公告信息
announcements = [
    {
        "channel": "更新日期",
        "entries": [
            {
                "name": None,
                "url": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Robot.mp4",
                "logo": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Chao.png"
            }
        ]
    }
]

# EPG（电子节目指南）URL列表
epg_urls = [
    "https://epg.v1.mk/fy.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
# 测速超时时间（秒）
TEST_TIMEOUT = 10

# 测速线程池最大工作线程数
MAX_WORKERS = 20

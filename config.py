# 配置文件，包含直播源URL、黑名单URL、公告信息、EPG URL、测速超时时间和线程池最大工作线程数

# 优先使用的IP版本，这里设置为ipv4
ip_version_priority = "ipv4"

# 直播源URL列表
source_urls = [
"https://raw.githubusercontent.com/q1017673817/iptvz/main/组播_湖北电信.txt",
"https://raw.githubusercontent.com/q1017673817/iptvz/refs/heads/main/zubo.txt",
"https://raw.githubusercontent.com/jn950/live/refs/heads/main/tv/pllive.txt",
"https://raw.githubusercontent.com/jn950/live/main/tv/holive.m3u",
"https://raw.githubusercontent.com/cyh92/live/main/source/webtv.txt",
"https://im5k.fun/vip.m3u",
"http://rihou.cc:555/gggg.nzk",
"https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
"https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/gat.txt",
"https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
"https://raw.githubusercontent.com/alantang1977/iptv-auto/refs/heads/main/my.txt",
"https://cloud.7so.top/f/xv80ux/天浪.txt",
"https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg1",

"https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.txt",
"https://raw.githubusercontent.com/YueChan/Live/main/APTV.m3u",
"https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
"https://raw.githubusercontent.com/zwc456baby/iptv_alive/refs/heads/master/live.m3u",
"https://raw.githubusercontent.com/pdd520/IPTV/refs/heads/master/config/rtp/tw.txt",
"https://raw.githubusercontent.com/Supprise0901/TVBox_live/refs/heads/main/live.txt",
"http://49.0.205.239:8866/Sub?type=txt",
"https://raw.githubusercontent.com/iptv-org/iptv/gh-pages/countries/cn.m3u",
"https://raw.githubusercontent.com/iptv-org/iptv/master/streams/cn.m3u",
"https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u",
"https://raw.githubusercontent.com/Guovin/iptv-database/master/result.txt",
"https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt",
"https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/others_output.txt",
"https://raw.githubusercontent.com/asdjkl6/tv/tv/.m3u/整套直播源/测试/整套直播源/l.txt",
"https://raw.githubusercontent.com/asdjkl6/tv/tv/.m3u/整套直播源/测试/整套直播源/kk.txt",
"https://raw.githubusercontent.com/yuanzl77/IPTV/master/live.txt",
"http://wx.thego.cn/df.txt",
"http://wx.thego.cn/backup.m3u",
"https://raw.githubusercontent.com/rad168/iptv/main/live.m3u",
"https://raw.githubusercontent.com/mytv-android/BRTV-Live-M3U8/refs/heads/main/BRTV.m3u",
"https://raw.githubusercontent.com/hujingguang/ChinaIPTV/refs/heads/main/cnTV_AutoUpdate.m3u8",
"https://raw.githubusercontent.com/250992941/iptv/refs/heads/main/st1.txt",
"https://live.zbds.top/tv/iptv4.txt",
"https://raw.githubusercontent.com/xiongjian83/TvBox/refs/heads/main/live.txt",
"https://www.cloudplains.cn/result.txt",
"https://raw.githubusercontent.com/xzw832/cmys/main/S_CCTV.txt",
"https://raw.githubusercontent.com/xzw832/cmys/main/S_weishi.txt",
"https://raw.githubusercontent.com/lalifeier/IPTV/main/m3u/IPTV.m3u",
"https://raw.githubusercontent.com/lalifeier/IPTV/main/txt/hotel/全国.txt",
"https://raw.githubusercontent.com/alienlu/iptv/refs/heads/master/iptv.m3u",
"https://gitee.com/liliang74120/cxkj6863/raw/master/mySD",
"http://8.138.7.223/v12.txt",
"https://live.zbds.top/tv/iptv6.txt",
"https://tv.iill.top/m3u/Gather",
"https://gitee.com/mytv-android/mytvJS/raw/main/js.gitee.m3u",
    
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

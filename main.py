from urllib import request
import subprocess
# 为请求添加请求头
opener = request.build_opener()
opener.addheaders = [
    ('Referer','https://www.bilibili.com/'),
    ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36')
]
request.install_opener(opener)

url_1 = 'https://cn-gdgz-fx-bcache-10.bilivideo.com/upgcxcode/37/65/22926537/22926537_da3-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1604761514&gen=playurl&os=bcache&oi=2026177750&trid=95c02f2b7d984144bd816c5d133138b6u&platform=pc&upsig=57d8b948d7fa01a1db9ad37bfe725310&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=3810&mid=59459051&orderid=0,3&agrr=0&logo=80000000'
url_2 = 'https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/37/65/22926537/22926537_da3-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1604761514&gen=playurl&os=hwbv&oi=2026177750&trid=95c02f2b7d984144bd816c5d133138b6u&platform=pc&upsig=a635c13f2662d8dffa863a67c5b4f7b5&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=59459051&orderid=0,3&agrr=0&logo=80000000'
print("爬取中……请耐心等候")
request.urlretrieve(url=url_1,filename='shunv.mp4')
request.urlretrieve(url=url_2,filename='shunv.mp3')
print("爬取完毕。")
print("合并音视频中……")
subprocess.call('ffmpeg -i shunv.mp4 -i shunv.mp3 -strict -2 -f mp4 shunv_final.mp4', shell=True)
print("合并完成，准备删除未合并的音视频")
print("删除中")
subprocess.call('del shunv.mp4', shell=True)
subprocess.call('del shunv.mp3', shell=True)
print("删除完成")
print("完毕。")
import rumps
import pyperclip
from pytube import YouTube
import time
import getpass

DOWNLOAD_DIR=r"/Users/"+getpass.getuser()+"/downloads/YoutubeDownloader"

class MenuBarUtils(object):
    def __init__(self):
        self.config={
            "app_name":"MenuBarUtils",
            "download_video":"Download video from clipboard"
        }

        self.app=rumps.App(self.config["app_name"])
        self.set_up_menu()  #method

        self.download_video_button=rumps.MenuItem(title=self.config["download_video"], callback=self.downloadVideo)#add an action with callback=method
        self.app.menu=[self.download_video_button]

    def set_up_menu(self):
        self.app.icon="icon.ico"

        if  self.app.icon==None:
            self.app.title="Downloader"



    def run(self):
        self.app.run()

    def downloadVideo(self,sender):
        #copy url from clipboard
        url=pyperclip.paste()

        print(url)#DEBUG

        try:
            video=YouTube(url)
            stream=video.streams.get_highest_resolution()

            #creating notificatin strings
            videoName="Downloading: "+video.title
            videoSize="The video size is: "+str(format((stream.filesize/1000000),".2f"))+"Mb."

            #displaying notifications
            rumps.notification("⏬The url is valid ⏬","The video is downloading.",videoSize,data=None,sound=True)
            stream.download(DOWNLOAD_DIR)

            rumps.notification("The video has been downloaded ✅","File is located in: ",DOWNLOAD_DIR,data=None,sound=True)
        except:
            rumps.notification("Alert ⚠️❗️","Your clipboard does not contain any youtube url.","If you copyed a url correctly try again.",data=None,sound=True)
            return
        return



    def downloadIT(self,url):
        video=YouTube(url)
        stream=video.streams.get_highest_resolution()




if __name__ == '__main__':
    app=MenuBarUtils()
    app.run()

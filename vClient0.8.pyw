import vClient.connectbuild.connectwin as connectbuild
import vClient.appbuild.appwin as appbuild


def main():

    connectwin = connectbuild.VisualClientConnectWin()
    connectwin.root.mainloop()

    while connectwin.root.state == 'normal':
        pass

    if connectwin.main_frame.client is not None:
        try:
            appwin = appbuild.VisualClientApp(connectwin.main_frame.client)
            appwin.root.mainloop()
        except:
            pass

if __name__ == '__main__':
    main()

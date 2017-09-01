from multiprocessing import Process
from multiprocessing import Pool
import os
import Ports
import sys
import devices
from appium import webdriver


# def run_proc(_port):
#    cmd = str('appium -p %s -bp %s') % (_port, _port+10)
#    os.system(cmd)


# if __name__ == '__main__':
#    port = 4723
#    p = Pool(2)
#    for i in range(2):
#        p.apply_async(run_proc, args=(port,))
#        port = port + 2
#    p.close()
#    p.join()

class AppiumServer:
    def __init__(self, runs):
        self._runs = runs

    def start_server(self):
        pool = Pool(processes=len(self._runs))
        # port = Ports.Ports().get_ports(self._runs * 2)
        for run in self._runs:
            pool.apply_async(self.run_server, args=(run,))
        pool.close()
        # pool.join()

    def run_server(self, run):
        port = run.get_port()
        cmd = str('appium -p %s -bp %s') % (port[0], port[1])
        os.system(cmd)

    def kill_server(self):
        os.system('taskkill /f /im  node.exe')

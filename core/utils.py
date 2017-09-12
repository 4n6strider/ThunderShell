"""
    @author: Mr.Un1k0d3r RingZer0 Team
    @package: core/utils.py
"""
import os
import string
import random
import urllib2
import datetime
from core.ui import UI

class Utils:
    VERSION = "1.1"
    
    @staticmethod
    def file_exists(path, die=False, show_error=True):
        if os.path.exists(path):
            return True
        
        if show_error:
            UI.error("%s not found" % path, die)
        return False
    
    @staticmethod
    def load_file(path, die=False):
        if Utils.file_exists(path, die):
            return open(path, "rb").read()
        return ""
    
    @staticmethod
    def load_file_unsafe(path):
        return open(path, "rb").read()
    
    @staticmethod
    def create_folder_tree(path):
        os.makedirs(path)
        
    @staticmethod
    def unix_to_date(timestamp):
        return datetime.datetime.fromtimestamp(float(timestamp)).strftime('%d/%m/%Y %H:%M:%S')
    
    @staticmethod
    def get_arg_at(cmd, index, max):
        cmd = cmd.split(" ", max)
        if len(cmd) - 1 >= index:
            return cmd[index]
        return ""
    
    @staticmethod
    def download_url(path):
        request = urllib2.Request(path)
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0")
        data = ""
        try:
            data = urllib2.urlopen(request).read()
        except:
            UI.error("Failed to fetch %s" % path)
        
        return data
    
    @staticmethod
    def load_powershell_script(path, length):
        data = Utils.load_file("powershell/%s" % path)
        return Utils.update_vars(data, length)
        
    @staticmethod
    def update_vars(data, length):
        for i in reversed(range(0, length + 1)):
            data = data.replace("var%d" % i, Utils.gen_str(random.randrange(4, 16)))
        return data   
    
    @staticmethod
    def update_key(data, key, value):
        return data.replace("[%s]" % key, value) 
        
    @staticmethod
    def gen_str(size):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(size)) 
        
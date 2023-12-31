# -*- coding: utf-8 -*-
# Copyright (c) 2023, Harry Huang
# @ MIT License
import os, json

class Config():
    '''
    Configuration class for CustomSplasher
    配置类
    '''

    __config_path = 'CustomSplasherConfig.json'
    __file_encoding = 'UTF-8'
    __default_config = {
        'target_program': "C:\Program Files (x86)\Seewo\EasiNote5\swenlauncher\swenlauncher.exe",
        'launch_interval': 1500,
        'exit_interval': 2000,
        'layout': {
            'height': 1080,
            'width': 1920,
            'offset_x': 0,
            'offset_y': 0,
            'force_topmost': True
        },
        'media': {
            'file': 'video.mp4',
            'speed': 2.5,
            'reverse_color': False,
            'addictive_color': [0, 0, 0]
        },
        'cmd_preprocess': ''
    }
    
    def __init__(self):
        '''
        ## Initialized the config system
        #### 初始化配置文件系统
        '''
        self.read_config()
        self.save_config()
    
    def get(self, key):
        '''
        ## Get the specified config field
        #### 获取指定的配置字段值
        :param key: The JSON key to the field;
        :returns:   (Any) None if the key doesn't exist;
        '''
        return self.config[key] if key in self.config.keys() else None
    
    def read_config(self):
        '''
        ## Read the config from file
        #### 读取（反序列化）配置文件
        Note: Default config will be used if the config file doesn't exist or an error occurs.
        :returns: (none);
        '''
        try:
            self.config = json.load(open(Config.__config_path, 'r', encoding=Config.__file_encoding)) if os.path.exists(Config.__config_path) else Config.__default_config
            # Success
        except Exception as arg:
            self.config = Config.__default_config
            print("Failed to read config, using default config...")
    
    def save_config(self):
        '''
        ## Save the config to file
        #### 保存（序列化）配置文件
        :returns: (none);
        '''
        try:
            json.dump(self.config, open(self.__config_path, 'w', encoding=Config.__file_encoding), indent=4, ensure_ascii=False)
            # Success
        except Exception as arg:
            print("Failed to save config...")

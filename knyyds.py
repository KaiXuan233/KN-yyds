# 梗来源：TsOg服成员KN1999WXC现已有6任
# 女朋友，并在幼儿园就学会了手冲（
# 作者(minecraft正版id)：Kai_Xuan
# 无聊搓的 没有版权 想改就改 爱咋用咋用
# TODO 更加花里胡哨的字体
# from utils.rtext import *

import json
import re

configPath = 'plugins/config/knyyds.json'
config = {}
defaultConfig = {
    'KN': 'KN1999WXC',
    'knyyds': [
        '§l§6KN，永远的神！！！'
    ],
    'yyds': [
        '§l§6{}, 永远滴神！！！'
    ],
    'onKnJoinServerSay': [
        '§lOHHHHHHHHHHHHHHHHH',
        '§lKN大佬上线了！KN，永远的神！！！'
    ],
    'onKnJoinTitle': '欢迎KN，永远的神进入服务器！',
    'onKnJoin@aSay': 'KN，永远的神',
    'onKnLeaveServerSay': [
        '§l恭送KN大佬'
    ]
}
KN = ''


def on_load(server, old):
    global configPath, config, defaultConfig, KN
    # 创建默认配置文件
    try:
        with open(configPath, 'r'):
            pass
    except FileNotFoundError:
        with open(configPath, 'w', encoding='utf8') as f:
            f.write(json.dumps(defaultConfig))
        server.logger.info('没有找到配置文件，创建中...')
    # 读取配置文件
    with open(configPath, 'r') as f:
        config = json.load(f)
        server.logger.info('\"KN，永远的神\"已加载配置')
    try:
        KN = config['KN']
    except KeyError:
        KN = 'KN1999WXC'
    # 添加help信息
    server.add_help_message('!!knyyds', 'KN, 永远的神！')
    server.add_help_message('!!yyds <玩家>', '<玩家>，永远的神！')
    # 提示插件加载
    server.logger.info('\"KN，永远的神\"插件已经加载')


def on_info(server, info):
    global config
    if info.content == '!!knyyds':
        for a in config['knyyds']:
            server.logger.info(a)
            server.say(a)
    elif info.content == '!!yydstest':
        server.logger.info('working')
    elif re.match(r'!!yyds.*', info.content) is not None:
        args = str(info.content).lstrip('!!yyds ').split(' ')
        for arg in args:
            for a in config['yyds']:
                server.logger.info(a.format(arg))
                server.say(a.format(arg))


def on_player_joined(server, player):
    global config, KN
    if player == KN:
        for a in config['onKnJoinServerSay']:
            server.say(a)
        server.execute('title' + ' ' + '@a' + ' ' + 'title' +
                       '{\"text\":\"' + config['onKnJoinTitle'] +
                       '\",\"color\":\"gold\",\"bold\":\"true\"}')
        server.execute('execute as @a run say ' + config['onKnJoin@aSay'])


def on_player_left(server, player):
    global config, KN
    if player == KN:
        for a in config['onKnLeaveServerSay']:
            server.say(a)

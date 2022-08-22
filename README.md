# wx-autoreminder
微信公众号测试接口发送提醒的python脚本
自动定时运行如下操作：
1. Linux环境下确保安装crontab，可以crontab -l查看是否已安装
2. crontab -e 进入vim编辑一个新的crontab任务
3. 可以用crontab.guru设置自动定时运行的时间和频率（crontab的syntax比较反人类）
4. 例如: “* * * * * /usr/bin/env python3 /root/autoreminder.py“ 这会让代码每分钟循环运行

python脚本内的一些token，id等需要自行设置。

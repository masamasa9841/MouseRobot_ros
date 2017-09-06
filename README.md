# mouserobot_ros
## rosでMouseRobotを操作しよう。
主にゲームコントローラーを使って操作します。
このパッケージは以下のコントローラーをサポートします。
* Logicool Wireless Gamepad F710

### 前提条件
1. PCにROSのインストールとセットアップ
* 参考: [http://wiki.ros.org/rosserial?distro=kinetic](http://wiki.ros.org/rosserial?distro=kinetic)

2. rosserialのインストール
* 参考: [http://wiki.ros.org/rosserial?distro=kinetic](http://wiki.ros.org/rosserial?distro=kinetic)

3. joy_nodeのインストール
```
sudo apt install ros-kinetic-joy
```

### インストール
初めに`catkin_ws/src`の中にこちらのリポジトリをダウンロードして、ビルドします。
```
cd ~/catkin_ws/src
git clone https://github.com/masamasa9841/mouserobot_ros
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```

### 使い方
1. Arduinoにパッケージをビルドします。ArduinoIDEで　`Arduino/Arduino.ino`をビルドします。

2. rosスクリプトを実行します。
```
roslaunch mouserobot_ros arduino_ros.launch
```

### コントローラーの使い方
そのうち書く
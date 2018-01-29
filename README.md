# mouserobot_ros

## MouseRobotについて

タミヤの壁伝いれずみに二つの光センサを取り付けて、光に反応するロボットです。

* 参考:[https://jsupratman13.github.io/MouseRobotProject/index.html](https://jsupratman13.github.io/MouseRobotProject/index.html)

## rosでMouseRobotを操作しよう。

このリポジトリはゲームコントラーまたは、キーボードを使ってMouseRobotを操作する紹介です。

このパッケージは以下のコントローラーをサポートします。

* Logicool Wireless Gamepad F710

### 環境

* Ubuntu 16.04 LTS
* ROS Kinetic
* Arduino nano

### 前提条件

1. PCにROSのインストールとセットアップ
    * 参考: [http://wiki.ros.org/kinetic/Installation](http://wiki.ros.org/kinetic/Installation)

1. Arduino IDEのセットアップ
    * 参考: [http://wiki.ros.org/ja/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup](http://wiki.ros.org/ja/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)

1. rosserialのインストール
    * 参考: [http://wiki.ros.org/rosserial?distro=kinetic](http://wiki.ros.org/rosserial?distro=kinetic)

1. joy_nodeのインストール(ゲームコントローラーを使う場合)

    ```shell
    sudo apt install ros-kinetic-joy
    ```

### インストール

初めに`catkin_ws/src`の中にこちらのリポジトリをダウンロードして、ビルドします。

```shell
cd ~/catkin_ws/src
git clone https://github.com/masamasa9841/mouserobot_ros
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```

### 使い方

1. Arduino nanoとPCを接続し、権限を変更します。

    ```shell
    sudo chmod 666 /dev/ttyUSB0
    ```

1. Arduinoにパッケージをビルドします。ArduinoIDEで`Arduino/logitech_teleop.ino`をビルドします。
1. 任意のrosスクリプトを実行します。

#### ゲームコントローラーで操作する場合

```shell
roslaunch mouserobot_ros teleope_twist_logicool.launch
```

#### キーボードで操作する場合

```shell
roslaunch mouserobot_ros teleope_twist_keyboard.launch
rosrun mouserobot_ros teleope_twist_keyboard.py
```
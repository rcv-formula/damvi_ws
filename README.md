# damvi_ws
ros workspace of damvi

download and install code : 
<br>
```
git clone https://github.com/rcv-formula/damvi_ws.git
cd damvi_ws
git checkout red_damvi
git submodule update --init --force --recursive
rosdep update
cd ../..
rosdep install --from-paths src -i -y
```

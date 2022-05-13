# Software Defined Video Streaming Homework for 2022-2 Network Lab

## What is This


## Demo
[youtube](https://www.youtube.com/watch?v=1w_JFab4DJw)

![](resources/demo.webp)

## How to Run
Download the code to your Jetson Nano
```
# on Jetson Nano
git clone https://github.com/dlccyes/netlab_sdvs.git
```

Install essential things
```
sudo apt install protobuf-compiler build-essential make
```

Run the server
```
# on Jetson Nano
python3 server.py --ip 0.0.0.0 --port 8080
```

Run the client (on another terminal session)
```
# on Jetson Nano
python3 client.py --ip localhost --port 8080 --mode 0
```

On your local computer, run this to have the video shown. 
```
# on local computer
ffplay -fflags nobuffer rtmp://<Jetson Nano IP>/rtmp/live
```


To change the real-time video processing algorithm, append `grey`, `hand`, `face` or `object` after
```
# on Jetson Nano
python3 client.py --ip localhost --port 8080 --mode
```

For example, to enable real-time face detection, do
```
# on Jetson Nano
python3 client.py --ip localhost --port 8080 --mode hand
```



## Troubleshooting
```
sudo systemctl restart nvargus-daemon
```
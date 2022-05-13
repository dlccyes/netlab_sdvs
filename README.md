# Software Defined Video Streaming Homework for 2022-2 Network Lab

```
sudo systemctl restart nvargus-daemon
```

```
python3 server.py --ip 0.0.0.0 --port 8080
```

start
```
python3 client.py --ip localhost --port 8080 --mode 0
```

change mode  
`hand`, `face`, `object`
```
python3 client.py --ip localhost --port 8080 --mode hand
```

```
ffplay -fflags nobuffer rtmp://<Jetson Nano IP>/rtmp/live
```
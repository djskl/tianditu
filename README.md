# tianditu  
其中的`deploy`为响应weehook(coding.net)的uwsgi服务，使用的时候要把它放到其他目录中去  

待解决问题：  

- [ ] 切片服务的日志输出到了部署服务日志 
- [ ] 切片服务无法在uwsgi进程一次启动(会卡死)，只能逐个启动

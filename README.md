# tianditu  
其中的`deploy`为响应weehook(coding.net)的uwsgi服务，使用的时候要把它放到其他目录中去  

待解决问题：  

* ~~切片服务的日志输出到了部署服务日志~~ 
* ~~切片服务无法在uwsgi进程一次启动(会卡死)，只能逐个启动~~  

把启动方式换成了`os.kill(pid, signal.SIGHUP)`以上两个问题烟消云散，很多疑难杂症很可能源自错误的方法。  
[The Art of Graceful Reloadin](http://uwsgi-docs.readthedocs.io/en/latest/articles/TheArtOfGracefulReloading.html)

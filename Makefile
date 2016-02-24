
rpm:
	wget https://repo.varnish-cache.org/source/varnish-3.0.3.tar.gz
	tar zxvf varnish-3.0.3.tar.gz
	spectool -g secdown.spec

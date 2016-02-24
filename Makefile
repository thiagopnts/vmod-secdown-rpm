
rpm:
	mkdir -p dist/{BUILD,RPMS,SPECS,SOURCES,SRPMS,install}
	wget https://repo.varnish-cache.org/source/varnish-3.0.3.tar.gz
	wget https://github.com/footplus/libvmod-secdown/archive/master.tar.gz -O libvmod-secdown.tar.gz
	mv varnish-3.0.3.tar.gz dist/BUILD
	mv libvmod-secdown.tar.gz dist/SOURCES
	tar -zxf dist/BUILD/varnish-3.0.3.tar.gz -C dist/BUILD
	tar -zxf dist/SOURCES/libvmod-secdown.tar.gz -C dist/BUILD
	rpmbuild -ba \
			--define "_topdir $(pwd)/dist" \
			--define "buildroot $(pwd)/dist/install" \
			--clean \
			nytd-libvmod-secdown-1.1.spec

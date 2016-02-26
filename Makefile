rpm:
	mkdir -p dist/{BUILD,RPMS,SPECS,SOURCES,SRPMS,install}
	cp nytd-libvmod-secdown-1.1.spec dist/SPECS
	wget https://github.com/footplus/libvmod-secdown/archive/master.tar.gz -O libvmod-secdown.tar.gz
	cp varnish-3.0.3.tar.gz dist/BUILD
	mv libvmod-secdown.tar.gz dist/SOURCES
	tar -zxf dist/BUILD/varnish-3.0.3.tar.gz -C dist/BUILD
	cd dist/SPECS
	rpmbuild -ba \
                    --define "_topdir $(PWD)/dist" \
                    --define "buildroot $(PWD)/dist/install" \
                    --clean \
                    nytd-libvmod-secdown-1.1.spec

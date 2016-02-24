Summary: Varnish Vmod for url hash signing
Name: secdown
Version: 1.1
Packager: NYTimes
Group: Development/Libraries
License: FreeBSD
URL: https://github.com/footplus/libvmod-secdown
Source0: https://github.com/footplus/libvmod-secdown/archive/master.tar.gz
Requires: varnish >= 3.0.0
BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pcre-devel
BuildRequires: python-docutils
BuildRequires: varnish >= 3.0.0
BuildRequires: varnish-libs-devel >= 3.0.0

%description
Varnish Vmod for url hash signing

%build
./autogen.sh
VMODDIR=/usr/lib64/varnish/vmods VARNISHSRC=/opt/varnish-3.0.5/ ./configure
make
make install

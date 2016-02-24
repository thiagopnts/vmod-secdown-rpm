Summary: Varnish Vmod for url hash signing
Name: secdown
Version: 1.1
Release: 1
Packager: NYTimes
Group: Development/Libraries
License: FreeBSD
URL: https://github.com/footplus/libvmod-secdown
Source0: libvmod-secdown.tar.gz
BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pcre-devel
BuildRequires: python-docutils

%description
Varnish Vmod for url hash signing

%build
./autogen.sh
VMODDIR=/usr/lib64/varnish/vmods VARNISHSRC=./varnish-3.0.3/ ./configure
make

%install
sudo make install

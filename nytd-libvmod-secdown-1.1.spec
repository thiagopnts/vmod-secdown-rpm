Summary: Varnish Vmod for url hash signing
Name: secdown
Version: 1.1
Release: 1
Packager: NYTimes
Group: Development/Libraries
License: FreeBSD
URL: https://github.com/footplus/libvmod-secdown
Source: libvmod-secdown.tar.gz
BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pcre-devel
BuildRequires: python-docutils

%description
Varnish Vmod for url hash signing

%prep
pwd
%setup -n libvmod-secdown-master

%build
./autogen.sh
VMODDIR=%{buildroot}/usr/lib64/varnish/vmods VARNISHSRC=../varnish-3.0.3/ ./configure --prefix %{buildroot}
make

%install
make install

%files
/usr/lib64/varnish/vmods/libvmod_secdown.a
/usr/lib64/varnish/vmods/libvmod_secdown.la
/usr/lib64/varnish/vmods/libvmod_secdown.so
/usr/lib64/varnish/vmods/libvmod_secdown.so.1
/usr/lib64/varnish/vmods/libvmod_secdown.so.1.0.0
/share/man/man3/vmod_secdown.3

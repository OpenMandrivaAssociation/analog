%define name	analog
%define version	6.0
%define release	%mkrel 2

Summary:	WWW server logfile analysis program
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://www.analog.cx/%{name}-%{version}.tar.bz2
Patch0:		%{name}-5.21-htmlform.patch
Patch1:		%{name}-5.23-perlform.patch
Patch2:		%{name}-5.31-config.patch
Patch3:		%{name}-5.22-defaults.patch
Patch4:		%{name}-5.22-png.patch
License:	Distributable
Group:		Monitoring
URL:		http://www.analog.cx/
BuildRequires:	XFree86-devel
BuildRequires:	freetype2-devel
BuildRequires:	gd-devel >= 2
BuildRequires:	jpeg-devel
BuildRequires:	pcre-devel
BuildRequires:	libpng-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
WWW server logfile analysis program with lots of features. Check
the home page at http://www.statslab.cam.ac.uk/~sret1/analog/ for
more information. You should edit the /etc/analog.cfg and
customizer it for your webserver with the HOSTNAME and HOSTURL
options. Perl is required for the html forms interface. Apache is
suggested as the default web server.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%make \
    CFLAGS="%{optflags}" \
    DEFS="-DHAVE_GD -DHAVE_ZLIB -DHAVE_PCRE -DLANGDIR=\\\"%{_datadir}/analog/\\\" -DCONFIGDIR=\\\"%{_sysconfdir}/\\\"" \
    LIBS="-lgd -lpcre -lpng -ljpeg -lz -lm" \

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}/var/www/html/images
install -d %{buildroot}/var/www/html/analog/images
install -d %{buildroot}/var/www/cgi-bin
install -d %{buildroot}%{_datadir}/analog
install -d %{buildroot}%{_mandir}/man1

install -m755 analog %{buildroot}%{_bindir}/
install -m644 analog.cfg %{buildroot}%{_sysconfdir}/
install -m555 anlgform.pl %{buildroot}/var/www/cgi-bin/
install -m644 anlgform.html %{buildroot}/var/www/html/
install -m644 analog.man %{buildroot}%{_mandir}/man1/analog.1

install -m644  images/*.png %{buildroot}/var/www/html/images/
install -m644  lang/* %{buildroot}%{_datadir}/analog/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Licence.txt README.txt docs/ examples/
%config(noreplace) %{_sysconfdir}/analog.cfg
%{_bindir}/analog
/var/www/cgi-bin/anlgform.pl
/var/www/html/anlgform.html
/var/www/html/images/*.png
%dir /var/www/html/analog
%dir /var/www/html/analog/images
%dir %{_datadir}/analog
%{_datadir}/analog/*
%{_mandir}/man1/*


Summary:	WWW server logfile analysis program
Name:		analog
Version:	6.0
Release:	9
License:	Distributable
Group:		Monitoring
URL:		http://www.analog.cx/
Source:		http://www.analog.cx/%{name}-%{version}.tar.bz2
Patch0:		analog-5.21-htmlform.patch
Patch1:		analog-5.23-perlform.patch
Patch2:		analog-5.31-config.patch
Patch3:		analog-5.22-defaults.patch
Patch4:		analog-5.22-png.patch
Patch5:		analog-6.0-link.patch
BuildRequires:	bzip2-devel
BuildRequires:	gd-devel >= 2
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
WWW server logfile analysis program with lots of features. Check the home page
at http://www.statslab.cam.ac.uk/~sret1/analog/ for more information. You
should edit the /etc/analog.cfg and customizer it for your webserver with the
HOSTNAME and HOSTURL options. Perl is required for the html forms interface.
Apache is suggested as the default web server.

%prep

%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p0 -b .link

%build

%make \
    CC="gcc %ldflags" \
    CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE" \
    DEFS="-DHAVE_GD -DHAVE_ZLIB -DHAVE_BZLIB -DHAVE_PCRE -DLANGDIR=\\\"%{_datadir}/analog/\\\" -DCONFIGDIR=\\\"%{_sysconfdir}/\\\"" \
    LIBS="-lgd -lpcre -lz -lbz2 -lm"

%install
rm -rf %{buildroot}

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

install -m644 images/*.png %{buildroot}/var/www/html/images/
install -m644 lang/* %{buildroot}%{_datadir}/analog/

%clean
rm -rf %{buildroot}

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


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0-8mdv2012.0
+ Revision: 772936
- relink against libpcre.so.1

* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 6.0-7mdv2011.0
+ Revision: 627845
- add debian patch for llinking

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 6.0-6mdv2011.0
+ Revision: 609975
- rebuild

* Mon Aug 17 2009 Oden Eriksson <oeriksson@mandriva.com> 6.0-5mdv2010.0
+ Revision: 417300
- rediffed one patch
- rebuilt against libjpeg v7

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 6.0-4mdv2009.0
+ Revision: 238931
- fix deps

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 6.0-3mdv2008.0
+ Revision: 83846
- rebuild


* Sat Dec 02 2006 Emmanuel Andry <eandry@mandriva.org> 6.0-2mdv2007.0
+ Revision: 90065
- bump release
  bunzipped patches
- Import analog

* Thu Nov 10 2005 Buchan Milne <bgmilne@mandriva.org> 6.0-1mdk
- 6.0
- drop p4 (merged upstream)
- drop redundant explicit requires

* Tue Jul 13 2004 Robert Vojta <robert.vojta@mandrake.org> 5.32-6mdk
- rpmlint warning fix (5.23-5mdk -> 5.32-5mdk), hope it's last typo :)

* Tue Jul 13 2004 Robert Vojta <robert.vojta@mandrake.org> 5.32-5mdk
- rpmlint warning fix (5.32.-4mdk -> 5.23-4mdk)

* Tue Jul 13 2004 Robert Vojta <robert.vojta@mandrake.org> 5.32-4mdk
- - #10238 - pass -D... to gcc, correct paths used

* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.32-3mdk
- Fix DIRM (distlint)


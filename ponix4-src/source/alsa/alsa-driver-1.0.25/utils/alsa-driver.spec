%define version  1.0.25
%define rel 1

Summary:   ALSA driver
Name:      alsa-driver
Version:   %{version}
Release:   %rel
Source:    ftp://ftp.alsa-project.org/pub/driver/%{name}-%{version}.tar.bz2
URL:       http://www.alsa-project.org
Copyright: GPL
Group:     Base/Kernel
Requires:  kernel >= 2.4
Requires:  initscripts

BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires:	kernel >= 2.4
BuildRequires:	kernel-source >= 2.4
BuildRequires:	initscripts

%changelog
* Mon Mar  3 2003 Ronny V. Vindenes <sublett@dc-s.com>
- change BuildRoot from /var/tmp to %%{_tmppath}
- use standard rpm macros for %%build section
- simplify %%install section
- updated dependencies

* Tue Nov 20 2001 Jaroslav Kysela <perex@perex.cz>

- changed BuildRoot to /var/tmp

* Sun Nov 11 2001 Miroslav Benes <mbenes@tenez.cz>

- dangerous command "rm -rf $RPM_BUILD_ROOT" checks $RPM_BUILD_ROOT variable
- deleting service alsasound migrates from %%postun into %%preun script -
  after uninstalling chkconfig utility cannot found alsasound script


%description
Advanced Linux Sound Architecture driver. Driver is fully compatible
with OSS/Lite, but contains many enhanced features.

%prep
%setup

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_includedir}/sound
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_sbindir}/rc.d/init.d

make DESTDIR=$RPM_BUILD_ROOT install

%post
if [ -x /sbin/chkconfig ]; then
  chkconfig --add alsasound
fi
depmod -a

%preun
if [ "$1" = 0 ] ; then
  if [ -x /sbin/chkconfig ]; then
    chkconfig --del alsasound
  fi
fi

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/rc.d/init.d/*
%{_includedir}/*
/lib/modules/*/kernel/*
%doc FAQ INSTALL README TODO snddevices doc/*

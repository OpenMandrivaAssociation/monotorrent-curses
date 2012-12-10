%define name monotorrent-curses
%define version 0.2
%define svn r128192
%define release %mkrel 0.%svn.3

Summary: Bittorrent client for Mono with a simple curses UI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{svn}.tar.bz2
#gw this is automatically generated at build time by attrib, but this does
# not work in iurt
Source1: constants.cs
Patch: monotorrent-curses-makefile.patch
License: MIT
Group: Networking/File transfer
Url: http://www.mono-project.com/MonoCurses
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: libncurses-devel
BuildRequires: monodoc

%description
This is a simple Bittorrent client with a curses UI based on Monotorrent.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package contains the API documentation for the %name in
Monodoc format.

%prep
%setup -q -n mono-curses
%patch
cp %SOURCE1 .

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 
%if %_lib != lib
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/{*.so,pkgconfig} %buildroot%_libdir

%endif

%post doc
%_bindir/monodoc --make-index > /dev/null
%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS
%_libdir/libmono-curses.so
%_libdir/pkgconfig/mono-curses.pc
%_prefix/lib/mono/gac/mono-curses
%_prefix/lib/mono/mono-curses



%files doc
%defattr(-,root,root)
%doc ChangeLog
%_prefix/lib/monodoc/sources/mono-curses.*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-0.r128192.3mdv2011.0
+ Revision: 620391
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-0.r128192.2mdv2010.0
+ Revision: 430089
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - new snapshot
    - fix build
    - update file list

* Tue Jun 24 2008 Götz Waschk <waschk@mandriva.org> 0.2-0.r102179.2mdv2009.0
+ Revision: 228504
- rebuild for new monotorrent

* Wed Apr 30 2008 Götz Waschk <waschk@mandriva.org> 0.2-0.r102179.1mdv2009.0
+ Revision: 199422
- work around build bot bug
- new version
- drop source 1
- fix make file
- bump deps
- add doc subpackage
- fix deps

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Götz Waschk <waschk@mandriva.org> 0.1-1mdv2008.0
+ Revision: 18485
- Import monotorrent-curses



* Thu Apr 26 2007 Götz Waschk <waschk@mandriva.org> 0.1-1mdv2008.0
- initial package

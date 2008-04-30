%define name monotorrent-curses
%define version 0.2
%define svn r102179
%define release %mkrel 0.%svn.1

Summary: Bittorrent client for Mono with a simple curses UI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{svn}.tar.bz2
Patch: monotorrent-curses-makefile.patch
License: MIT
Group: Networking/File transfer
Url: http://www.mono-project.com/MonoCurses
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: libncurses-devel
BuildRequires: monotorrent >= 0.30
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

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 
%if %_lib != lib
ln -sf  %_prefix/lib/monotorrent/MonoTorrent.dll %buildroot%_prefix/lib/monotorrent/
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/monotorrent %buildroot%_libdir
%else 
rm -f %buildroot%_prefix/lib/monotorrent/MonoTorrent.dll
%endif

perl -pi -e "s^%_prefix/lib^%_libdir/^" %buildroot%_bindir/monotorrent
#install -m 644 %SOURCE1 %buildroot%_libdir/monotorrent/

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
%_bindir/monotorrent
%_libdir/monotorrent/

%files doc
%defattr(-,root,root)
%doc ChangeLog
%_prefix/lib/monodoc/sources/mono-curses.*

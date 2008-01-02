%define name monotorrent-curses
%define version 0.1
%define release %mkrel 1

Summary: Bittorrent client for Mono with a simple curses UI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: mono-curses.dll.config
License: MIT
Group: Networking/File transfer
Url: http://www.monotorrent.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: libncurses-devel
BuildRequires: monotorrent
Requires: ncurses
%define _requires_exceptions ^lib.*

%description
This is a simple Bittorrent client with a curses UI based on Monotorrent.

%prep
%setup -q

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
ln -sf  %_prefix/lib/bitsharp/*.dll %buildroot%_prefix/lib/monotorrent/
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif
perl -pi -e "s^%_prefix/lib^%_libdir/^" %buildroot%_bindir/monotorrent
install -m 644 %SOURCE1 %buildroot%_libdir/monotorrent/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/monotorrent
%_libdir/monotorrent/

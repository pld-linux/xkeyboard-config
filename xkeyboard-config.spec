Summary:	X Keyboard Configuration Database
Name:		xkeyboard-config
Version:	0.9
Release:	0.3
License:	BSD
Group:		X11/Development/Libraries
Source0:	http://xlibs.freedesktop.org/xkbdesc/%{name}-%{version}.tar.bz2
# Source0-md5:	52afe60101ace8532881e70f6c2dc020
URL:		http://www.freedesktop.org/wiki/Software_2fXKeyboardConfig
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-xkbcomp
BuildArch:	noarch
Obsoletes:	xorg-data-xkbdata
Provides:	xorg-data-xkbdata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The non-arch keyboard configuration database for X Window. The goal is
to provide the consistent, well-structured, frequently released open
source of X keyboard configuration data for X Window System
implementations (free, open source and commercial). The project is
targetted to XKB-based systems.

%prep
%setup -q

%build
%configure  \
	--enable-xkbcomp-symlink \
	--enable-compat-rules \
	--with-xkb-rules-symlink=xorg \
	--with-xkb-base=%{_datadir}/X11/xkb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO docs/H* docs/R*
%{_datadir}/X11/xkb
%exclude %{_datadir}/X11/xkb/compiled

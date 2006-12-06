Summary:	X Keyboard Configuration Database
Summary(pl):	Baza danych konfiguracji klawiatury pod X
Name:		xkeyboard-config
Version:	0.9
Release:	0.3
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xlibs.freedesktop.org/xkbdesc/%{name}-%{version}.tar.bz2
# Source0-md5:	52afe60101ace8532881e70f6c2dc020
URL:		http://www.freedesktop.org/wiki/Software_2fXKeyboardConfig
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-xkbcomp
Provides:	xorg-data-xkbdata
Obsoletes:	xorg-data-xkbdata
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The non-arch keyboard configuration database for X Window System. The
goal is to provide the consistent, well-structured, frequently
released open source of X keyboard configuration data for X Window
System implementations (free, open source and commercial). The project
is targeted to XKB-based systems.

%description -l pl
Niezale¿na od architektury baza danych konfiguracji klawiatury dla
systemu X Window. Celem jest dostarczenie spójnych, dobrze
zbudowanych, czêsto wydawanych danych konfiguracji klawiatury pod X z
otwartymi ¼ród³ami dla implementacji X Window System (wolnodostêpnych,
maj±cych otwarte ¼ród³a i komercyjnych). Projekt jest przeznaczony dla
systemów opartych na XKB.

%prep
%setup -q

%build
%configure \
	--enable-xkbcomp-symlink \
	--enable-compat-rules \
	--with-xkb-rules-symlink=xorg \
	--with-xkb-base=%{_datadir}/X11/xkb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/X11/xkb/compiled
ln -s /var/lib/xkb $RPM_BUILD_ROOT%{_datadir}/X11/xkb/compiled

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README TODO docs/H* docs/R*
%{_datadir}/X11/xkb

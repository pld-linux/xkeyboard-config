Summary:	X Keyboard Configuration Database
Summary(pl.UTF-8):	Baza danych konfiguracji klawiatury pod X
Name:		xkeyboard-config
Version:	2.2.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/data/xkeyboard-config/%{name}-%{version}.tar.bz2
# Source0-md5:	1867472501d13594d5ca17e696cc09ca
URL:		http://www.freedesktop.org/wiki/Software/XKeyboardConfig
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel
# AM_GLIB_GNU_GETTEXT
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	intltool >= 0.30
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	xorg-app-xkbcomp
# for sinhala layouts
Requires:	xorg-lib-libX11 >= 1.4.3
Provides:	xorg-data-xkbdata
Obsoletes:	xorg-data-xkbdata < 0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The non-arch keyboard configuration database for X Window System. The
goal is to provide the consistent, well-structured, frequently
released open source of X keyboard configuration data for X Window
System implementations (free, open source and commercial). The project
is targeted to XKB-based systems.

%description -l pl.UTF-8
Niezależna od architektury baza danych konfiguracji klawiatury dla
systemu X Window. Celem jest dostarczenie spójnych, dobrze
zbudowanych, często wydawanych danych konfiguracji klawiatury pod X z
otwartymi źródłami dla implementacji X Window System (wolnodostępnych,
mających otwarte źródła i komercyjnych). Projekt jest przeznaczony dla
systemów opartych na XKB.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--disable-runtime-deps \
	--enable-compat-rules \
	--with-xkb-rules-symlink=xorg \
	--with-xkb-base=%{_datadir}/X11/xkb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s /var/lib/xkb $RPM_BUILD_ROOT%{_datadir}/X11/xkb/compiled

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
# it used to be directory in xkbdata
if [ -d %{_datadir}/X11/xkb/symbols/pc ]; then
	mv -b %{_datadir}/X11/xkb/symbols/pc{,.dir}
%banner -e %{name} <<EOF
Check out %{_datadir}/X11/xkb/symbols/pc.dir
for your own files and remove it when done.
EOF
fi
if [ -d %{_datadir}/X11/xkb/compiled ]; then
	rm -rf %{_datadir}/X11/xkb/compiled
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README TODO docs/H* docs/R*
%{_datadir}/X11/xkb
%{_npkgconfigdir}/xkeyboard-config.pc

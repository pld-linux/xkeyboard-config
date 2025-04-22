# TODO: BR python>=3.11 when available in PLD instead of separate StrEnum package
Summary:	X Keyboard Configuration Database
Summary(pl.UTF-8):	Baza danych konfiguracji klawiatury pod X
Name:		xkeyboard-config
Version:	2.44
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/data/xkeyboard-config/%{name}-%{version}.tar.xz
# Source0-md5:	623a88fe63c6aefe3621bdfd5ba72764
URL:		https://www.freedesktop.org/wiki/Software/XKeyboardConfig
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.9
BuildRequires:	python3-StrEnum
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRequires:	xz
# for sinhala layouts
Requires:	xorg-lib-libX11 >= 1.4.3
Provides:	xorg-data-xkbdata
Obsoletes:	xorg-data-xkbdata < 0.9
# due to large maximum keycode handling
Conflicts:	xorg-app-xkbcomp < 1.4.2
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%doc AUTHORS COPYING ChangeLog.md README.md docs/H* docs/R*
%{_datadir}/X11/xkb
%{_npkgconfigdir}/xkeyboard-config.pc
%{_mandir}/man7/xkeyboard-config.7*

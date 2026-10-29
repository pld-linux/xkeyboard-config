Summary:	X Keyboard Configuration Database
Summary(pl.UTF-8):	Baza danych konfiguracji klawiatury pod X
Name:		xkeyboard-config
Version:	2.48
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/data/xkeyboard-config/%{name}-%{version}.tar.xz
# Source0-md5:	575106aff79b589abe4aff6c4bff4782
URL:		https://www.freedesktop.org/wiki/Software/XKeyboardConfig
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.61.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.11
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
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

ln -s /var/lib/xkb $RPM_BUILD_ROOT%{_datadir}/xkeyboard-config-2/compiled

# xkeyboard-config and xkeyboard-config-2 domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans -p <lua>
-- %{_datadir}/X11/xkb used to be a directory, it's a symlink now
local function rmtree(path)
	local st = posix.stat(path)
	if st and st.type == "directory" then
		for _, name in ipairs(posix.dir(path)) do
			if name ~= "." and name ~= ".." then
				rmtree(path .. "/" .. name)
			end
		end
		posix.rmdir(path)
	elseif st then
		os.remove(path)
	end
end
local st = posix.stat("%{_datadir}/X11/xkb")
if st and st.type == "directory" then
	rmtree("%{_datadir}/X11/xkb")
end

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog.md README.md docs/HOWTO.testing docs/README.*
%{_datadir}/X11/xkb
%{_datadir}/xkeyboard-config-2
%{_npkgconfigdir}/xkeyboard-config.pc
%{_npkgconfigdir}/xkeyboard-config-2.pc
%{_mandir}/man7/xkeyboard-config.7*
%{_mandir}/man7/xkeyboard-config-2.7*

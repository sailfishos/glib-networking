Name:       glib-networking

%define keepstatic 1

Summary:    Network extensions for GLib
Version:    2.63.3
Release:    1
License:    LGPLv2+
URL:        https://git.merproject.org/mer-core/glib-networking
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(glib-2.0) >= 2.60.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gettext
BuildRequires:  ca-certificates
BuildRequires:  meson

%description
Networking extensions for GLib

%prep
%setup -q -n %{name}-%{version}/glib-networking

%build
%meson -Dopenssl=enabled -Dgnutls=disabled -Dlibproxy=disabled -Dgnome_proxy=disabled
%meson_build

%install
%meson_install

%find_lang glib-networking

%files -f glib-networking.lang
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/gio/modules/libgioopenssl.so

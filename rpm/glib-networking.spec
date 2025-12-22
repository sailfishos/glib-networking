Name:       glib-networking

%define keepstatic 1

Summary:    Network extensions for GLib
Version:    2.80.1
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/glib-networking
Source0:    %{name}-%{version}.tar.bz2
Patch1:     0001-openssl-properly-check-return-value-when-writing-to-.patch
Patch2:     0002-openssl-check-return-value-of-g_tls_bio_alloc.patch
Patch3:     0003-openssl-check-return-values-of-BIO_new.patch
BuildRequires:  pkgconfig(glib-2.0) >= 2.73.3
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
%license COPYING
%{_libdir}/gio/modules/libgioopenssl.so

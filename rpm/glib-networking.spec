Name:       glib-networking

%define keepstatic 1

Summary:    Network extensions for GLib
Version:    2.29.9
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        https://git.merproject.org/mer-core/glib-networking
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  intltool
BuildRequires:  ca-certificates

%description
Networking extensions for GLib

%prep
%setup -q -n %{name}-%{version}/glib-networking

%build
NOCONFIGURE=1 ./autogen.sh

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%find_lang glib-networking

%files -f glib-networking.lang
%defattr(-,root,root,-)
%{_libdir}/gio/modules/libgiognutls.so


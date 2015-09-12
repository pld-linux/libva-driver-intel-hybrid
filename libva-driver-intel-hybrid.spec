%define	libva_req	1.6.1
Summary:	Codecs for VA Intel Driver
Summary(pl.UTF-8):	Kodeki dla sterownika VA Intel
Name:		libva-driver-intel-hybrid
Version:	1.0.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/01org/intel-hybrid-driver/archive/%{version}.tar.gz
# Source0-md5:	5800e38acf4590543019f406bdfc46eb
URL:		https://github.com/01org/intel-hybrid-driver
# for wayland, not used in 1.0.1
#BuildRequires:	EGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libcmrt-devel >= 0.10.0
BuildRequires:	libdrm-devel >= 2.4.45
BuildRequires:	libtool
BuildRequires:	libva-devel >= %{libva_req}
BuildRequires:	libva-drm-devel >= %{libva_req}
# for wayland, not used in 1.0.1
#BuildRequires:	libva-wayland-devel >= %{libva_req}
BuildRequires:	libva-x11-devel >= %{libva_req}
BuildRequires:	pkgconfig
# API version, not just package version
BuildRequires:	pkgconfig(libva) >= 0.38
# wayland-client, not used in 1.0.1
#BuildRequires:	wayland-devel
Requires:	libdrm >= 2.4.45
Requires:	libva >= %{libva_req}
Requires:	libva-driver-intel >= 1.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Codecs for VA Intel Driver:
- Hybrid VP8 Encoder
- Hybrid VP9 Decoder

%description -l pl.UTF-8
Kodeki dla sterownika VA Intel:
- Hybrydowy koder VP8
- Hybrydowy dekoder VP9

%prep
%setup -q -n intel-hybrid-driver-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libva/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/libva/dri/hybrid_drv_video.so

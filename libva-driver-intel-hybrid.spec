#
# Conditional build:
%bcond_with	drm	# DRM backend, not used as of 1.0.2 (grep for HAVE_VA_DRM, USE_DRM)
%bcond_with	wayland	# Wayland backend, not used as of 1.0.2 (grep for HAVE_VA_WAYLAND, USE_WAYLAND)

%define	libva_ver	1.6.1
Summary:	Codecs for VA Intel Driver
Summary(pl.UTF-8):	Kodeki dla sterownika VA Intel
Name:		libva-driver-intel-hybrid
Version:	1.0.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/01org/intel-hybrid-driver/releases
Source0:	https://github.com/01org/intel-hybrid-driver/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	05e97e6948963f08eb14a4a8f68bcf69
URL:		https://github.com/01org/intel-hybrid-driver
%{?with_wayland:BuildRequires:	EGL-devel}
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
# pkgconfig(libcmrt) >= 0.10.0, but cmrt <= 1.0.5 provided cmrt.pc instead of libcmrt.pc
BuildRequires:	libcmrt-devel >= 1.0.6
%{?with_drm:BuildRequires:	libdrm-devel >= 2.4.45}
BuildRequires:	libtool
BuildRequires:	libva-devel >= %{libva_ver}
%{?with_drm:BuildRequires:	libva-drm-devel >= %{libva_ver}}
%{?with_wayland:BuildRequires:	libva-wayland-devel >= %{libva_ver}}
BuildRequires:	libva-x11-devel >= %{libva_ver}
BuildRequires:	pkgconfig
# API version, not just package version
BuildRequires:	pkgconfig(libva) >= 0.38
%{?with_wayland:BuildRequires:	wayland-devel}
%{?with_drm:Requires:	libdrm >= 2.4.45}
Requires:	libva >= %{libva_ver}
Requires:	libva-driver-intel >= 1.6.1
ExclusiveArch:	%{ix86} %{x8664} x32
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

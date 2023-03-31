%define	_disable_rebuild_configure 1
# Speed up it a bit (angry)
%global optflags %optflags -O3

%define         api             0.0
%define         major           0
%define         libname         %mklibname mypaint %{major}
%define         libname_gegl    %mklibname mypaint-gegl %{major}
%define         libdevelname    %mklibname -d mypaint
%define         girname         %mklibname mypaint-gir %{gmajor}
%define         girname_gegl    %mklibname mypaintgegl-gir %{gmajor}
%define         geglapi         0
%define         gmajor          1.6

Name:           libmypaint
Version:        1.6.1
Release:        4
Summary:        System libraries based on Mypaint
Group:          System/Libraries
License:        GPLv2+
URL:            http://mypaint.org
Source0:        https://github.com/mypaint/libmypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool
# Should be profived by clang itself (llvm-devel)
#BuildRequires:  gomp-devel
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.100
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  typelib(Gegl)

%description
%{summary}.


%package -n %{name}-i18n
Summary:        Internationalization and locale data for libmypaint
Group:          System/Libraries
BuildArch:      noarch

%description -n %{name}-i18n
%{summary}.


%package -n %{libname}
Summary:        System libraries based on Mypaint
Group:          System/Libraries

%description -n %{libname}
This is an independent release of libmypaint, the library associated
with Mypaint, as a separate module.

%package -n %{libname_gegl}
Summary:        System libraries based on Mypaint
Group:          System/Libraries

%description -n %{libname_gegl}
This is an independent release of libmypaint, the library associated
with Mypaint, as a separate module.

%package -n %{girname}
Summary:        GObject Introspection interface description for MyPaint
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for MyPaint.

%package -n %{girname_gegl}
Summary:        GObject Introspection interface description for MyPaintGegl
Group:          System/Libraries
Requires:       %{libname_gegl} = %{version}-%{release}

%description -n %{girname_gegl}
GObject Introspection interface description for MyPaintGegl.

%package -n %{libdevelname}
Summary:        Development files for libmypaint
Group:          Development/Other
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libname_gegl} = %{version}-%{release}
Requires:       %{girname} = %{version}-%{release}
Requires:       %{girname_gegl} = %{version}-%{release}
Requires:       pkgconfig

%description -n %{libdevelname}
%{summary}.

%prep
%autosetup -p1

%build
%configure --enable-gegl --enable-openmp --enable-introspection=yes
%make_build

%install
%make_install

%find_lang %{name} --all-name
find %{buildroot}%{_libdir} -name '*.la' -delete

%files -n %{name}-i18n -f %{name}.lang

%files -n %{libname}
%doc README.md
%{_libdir}/libmypaint.so.%{major}*

%files -n %{libname_gegl}
%doc README.md
%{_libdir}/libmypaint-gegl.so.%{geglapi}*

%files -n %{girname}
%{_libdir}/girepository-1.0/MyPaint-%{gmajor}.typelib

%files -n %{girname_gegl}
%{_libdir}/girepository-1.0/MyPaintGegl-%{gmajor}.typelib

%files -n %{libdevelname}
%{_includedir}/libmypaint-gegl/
%{_includedir}/libmypaint/
%{_libdir}/libmypaint.so
%{_libdir}/libmypaint-gegl.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/MyPaint-%{gmajor}.gir
%{_datadir}/gir-1.0/MyPaintGegl-%{gmajor}.gir

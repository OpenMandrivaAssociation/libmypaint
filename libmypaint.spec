%define	_disable_rebuild_configure 1

%define         api             1.5
%define         major           1
%define         libname         %mklibname mypaint %{api} %{major}
%define         libname_gegl    %mklibname mypaint-gegl %{major}
%define         libdevelname    %mklibname -d mypaint
%define         girname         %mklibname mypaint-gir %{gmajor}
%define         girname_gegl    %mklibname mypaintgegl-gir %{gmajor}
%define         geglapi         0
%define         gmajor          1.5

Name:           libmypaint
Version:        1.5.0
Release:        1
Summary:        System libraries based on Mypaint
Group:          System/Libraries
License:        GPLv2+
URL:            http://mypaint.org
Source0:        https://github.com/mypaint/libmypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool
BuildRequires:  libgomp-devel
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  pkgconfig(babl)
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
Conflicts:      mypaint <= 1.2.1

%description -n %{name}-i18n
%{summary}.


%package -n %{libname}
Summary:        System libraries based on Mypaint
Group:          System/Libraries
Obsoletes:      %{_lib}mypaint0 < 1.3.0-3

%description -n %{libname}
This is an independent release of libmypaint, the library associated
with Mypaint, as a separate module.

%package -n %{libname_gegl}
Summary:        System libraries based on Mypaint
Group:          System/Libraries
Conflicts:      %{_lib}mypaint0 < 1.3.0-2

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
#Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libname_gegl} = %{version}-%{release}
Requires:       %{girname} = %{version}-%{release}
Requires:       %{girname_gegl} = %{version}-%{release}

%description -n %{libdevelname}
%{summary}.

%prep
%setup -q

%build
sed -i 's!gegl-0.3!gegl-0.4!' configure.ac configure gegl/Makefile* gegl/libmypaint-gegl.pc*
sed -i 's!Gegl-0.3!Gegl-0.4!' gegl/Makefile*
%configure --enable-gegl --enable-openmp --enable-introspection=yes
%make_build

%install
%make_install

%find_lang %{name} --all-name
find %{buildroot}%{_libdir} -name '*.la' -delete

%files -n %{name}-i18n -f %{name}.lang

%files -n %{libname}
%doc README.md
%{_libdir}/libmypaint-%{api}.so.%{major}*

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

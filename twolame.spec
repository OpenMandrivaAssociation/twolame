%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Optimized MPEG Audio Layer 2 (MP2) encoder
Name:		twolame
Version:	0.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.twolame.org/
Source0:	http://downloads.sourceforge.net/project/%name/%name/%version/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	libtool
BuildRequires:	dos2unix

%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder based on tooLAME by
Mike Cheng, which in turn is based upon the ISO dist10 code and portions of
LAME.

Features added to TwoLAME:
 - Fully thread-safe
 - Static and shared library (libtwolame)
 - API very similar to LAME's (for easy porting)
 - C99 compliant
 - Frontend supports wider range of input files (using libsndfile)

%package -n	%{libname}
Summary:	TwoLAME MP2 encoding library
Group:		System/Libraries

%description -n	%{libname}
TwoLAME MP2 encoding library.

%package -n	%{develname}
Summary:	Header files for TwoLAME library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{develname}
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder based on tooLAME by
Mike Cheng, which in turn is based upon the ISO dist10 code and portions of
LAME.

Features added to TwoLAME:
 - Fully thread-safe
 - Static and shared library (libtwolame)
 - API very similar to LAME's (for easy porting)
 - C99 compliant
 - Frontend supports wider range of input files (using libsndfile)

This package contains the static development library and header files for the
TwoLAME library.

%prep

%setup -q
sed -i -e 's/-O3//' configure.ac

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_docdir}/twolame

%files
%doc AUTHORS ChangeLog README
%{_bindir}/twolame
%{_mandir}/man1/twolame.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


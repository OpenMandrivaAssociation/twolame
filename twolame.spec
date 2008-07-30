%define	major 0
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Optimized MPEG Audio Layer 2 (MP2) encoder
Name:		twolame
Version:	0.3.12
Release:	%mkrel 3
License:	LGPL
Group:		System/Libraries
URL:		http://www.twolame.org/
Source0:	http://dl.sourceforge.net/twolame/%{name}-%{version}.tar.gz
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	dos2unix
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}

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
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%build
libtoolize --copy --force; aclocal; autoconf; autoheader; automake

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

rm -rf %{buildroot}%{_docdir}/twolame

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/twolame
%{_mandir}/man1/twolame.1*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*



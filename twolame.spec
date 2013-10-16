%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

Summary:	Optimized MPEG Audio Layer 2 (MP2) encoder
Name:		twolame
Version:	0.3.13
Release:	7
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
%doc AUTHORS ChangeLog README TODO
%{_bindir}/twolame
%{_mandir}/man1/twolame.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.13-2mdv2011.0
+ Revision: 670736
- mass rebuild

* Tue Jan 25 2011 Götz Waschk <waschk@mandriva.org> 0.3.13-1
+ Revision: 632513
- new version
- fix source URL
- drop patch

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-6mdv2011.0
+ Revision: 608047
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.12-5mdv2010.1
+ Revision: 524285
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.12-4mdv2010.0
+ Revision: 427454
- rebuild
- make sure autoreconf updates libtool files to avoid libtool 1.5/2.2 mismatches

* Sun Jan 11 2009 Götz Waschk <waschk@mandriva.org> 0.3.12-3mdv2009.1
+ Revision: 328310
- rebuild

* Thu Dec 18 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.12-2mdv2009.1
+ Revision: 315793
- docs in main not lib package, don't package COPYING
- protect major in file list
- add subst_space.patch: fix issues in configure.ac that broke build
- clean some unnecessary whitespace
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Guillaume Bedot <littletux@mandriva.org> 0.3.12-1mdv2008.1
+ Revision: 179947
- update to new version 0.3.12

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import twolame


* Wed Aug 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.10-1mdv2008.0
+ Revision: 57652
- Import twolame



* Wed Aug 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.10-1mdv2008.0
- initial Mandriva package (PLD import)

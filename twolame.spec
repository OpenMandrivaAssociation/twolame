# sources from upstream git
#
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# cd xdg-utils
# git archive --format=tar --prefix=xdg-utils-20121008/ master | xz > ../xdg-utils-20121008.tar.xz
#

%define gitdate 20130218

Name:		xdg-utils
Version:	1.1.0
Release:	0.%{gitdate}.2
Summary:	A basic desktop integration tools for any Free Desktop
License:	MIT
Url:		http://portland.freedesktop.org/wiki/
Group:		System/Base
Source0:	xdg-utils-%{gitdate}.tar.xz
#Source0:	http://portland.freedesktop.org/download/xdg-utils-%{version}%{?beta:-%{beta}}.tar.gz
Patch0:		xdg-utils-1.0.2-email_loop.patch
Patch1:		xdg-utils-1.0.2-email_silent_errors.patch
Patch2:		xdg-utils-1.0.3-enable-xdg-terminal.patch
BuildRequires:	xsltproc
BuildRequires:	gawk
BuildRequires:	xmlto
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
Requires:	desktop-file-utils
Requires:	xprop
Requires:	xset
BuildArch:	noarch

%description
This version of xdg-utils contains the following commands:
xdg-desktop-menu:	command line tool for (un)installing 
			desktop menu items
xdg-desktop-icon:	command line tool for (un)installing 
			icons to the desktop
xdg-mime:	        command line tool for querying information 
			about file type handling and adding 
			descriptions for new file types
xdg-icon-resource:	command line tool for (un)installing icon resources
xdg-open:	        opens a file or URL in the user's preferred 
			application
xdg-email:	        command line tool for sending mail using the user's 
			preferred 
			e-mail composer
xdg-su:	                run a program as root after prompting for the root 
			password
xdg-screensaver:	command line tool for controlling the screensaver

Testsuite for xdg-utils is available from
http://portland.freedesktop.org/wiki/TestSuite

%prep
%setup -qn %{name}-%{gitdate}

%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%configure2_5x

%if %{gitdate}
%make scripts-clean -C scripts
%make man scripts -C scripts
%endif

%make
%make -C scripts

%install
%makeinstall_std
sed -i -e "s,_LIBDIR_,%{_libdir}/kde4/libexec,g" %{buildroot}/%{_bindir}/xdg-email

%files
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings
%{_bindir}/xdg-terminal
%{_mandir}/man1/xdg*.*


Name:		ccal
License:	GPLv2+
Group:		System/Base
Version:	2.5
Release:	%mkrel 1
URL:		http://ccal.chinesebay.com/ccal/ccal.htm
Summary:	A program to display a calendar together with Chinese calendar
Source:		http://ccal.chinesebay.com/ccal/%{name}-%{version}.tar.gz 
BuildRoot:	%{_tmppath}/%name-%version-%release-root
Patch0:		ccal-2.4-fix-prefix.patch
Requires:	ghostscript

%description
The ccal utility writes a Gregorian calendar together with Chinese
calendar to standard output.

%prep
%setup -q
%patch0 -p0

%build
export CXXFLAGS="%optflags"
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%makeinstall_std-man

%files
%defattr(-, root, root)
%doc ChangeLog README
%{_mandir}/man1/*
%attr(0755, root, root) %{_bindir}/ccal
%attr(0755, root, root) %{_bindir}/ccalpdf

%clean
rm -rf ${RPM_BUILD_ROOT}

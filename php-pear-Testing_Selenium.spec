%define		_class		Testing
%define		_subclass	Selenium
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.4.4
Release:	2
Summary:	PHP Client for Selenium RC
License:	Apache License
Group:		Development/PHP
URL:		https://pear.php.net/package/XML_Util/
Source0:	http://download.pear.php.net/package/Testing_Selenium-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Selenium Remote Control (SRC) is a test tool that allows you to write automated
web application UI tests in any programming language against any HTTP website
using any mainstream JavaScript-enabled browser. SRC provides a Selenium
Server, which can automatically start/stop/control any supported browser. It
works by using Selenium Core, a pure-HTML+JS library that performs automated
tasks in JavaScript; the Selenium Server communicates directly with the browser
using AJAX (XmlHttpRequest).

http://www.openqa.org/selenium-rc/

This module sends commands directly to the Server using simple HTTP GET/POST
requests. Using this module together with the Selenium Server, you can
automatically control any supported browser.

To use this module, you need to have already downloaded and started the
Selenium RC Server.  (The Selenium Server is a Java application.)

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/ChangeLog
%doc %{upstream_name}-%{version}/README
%doc %{upstream_name}-%{version}/TODO
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
%{_datadir}/pear/data/%{upstream_name}


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-10mdv2012.0
+ Revision: 742285
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-9
+ Revision: 679589
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-8mdv2011.0
+ Revision: 613781
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-7mdv2010.1
+ Revision: 466335
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-6mdv2010.0
+ Revision: 430698
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-4mdv2009.0
+ Revision: 237102
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-3mdv2008.1
+ Revision: 107007
- PHPUnit2/PHPUnit

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2008.0
+ Revision: 64198
- rebuild

* Wed Apr 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2008.0
+ Revision: 14682
- Import php-pear-Testing_Selenium



* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2008.0
- initial Mandriva package


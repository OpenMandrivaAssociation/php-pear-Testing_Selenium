%define _requires_exceptions pear(simpletest

%define		_class		Testing
%define		_subclass	Selenium
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.1
Release:	%mkrel 9
Summary:	PHP Client for Selenium RC
License:	Apache License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_Util/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/ChangeLog
%doc %{upstream_name}-%{version}/README
%doc %{upstream_name}-%{version}/TODO
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

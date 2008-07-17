%define _requires_exceptions pear(simpletest

%define		_class		Testing
%define		_subclass	Selenium
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PHP Client for Selenium RC
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	%mkrel 4
License:	Apache License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/XML_Util/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

perl -pi -e "s|PHPUnit2|PHPUnit|g" %{_pearname}-%{version}/examples/*

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%doc %{_pearname}-%{version}/tests
%doc %{_pearname}-%{version}/ChangeLog
%doc %{_pearname}-%{version}/README
%doc %{_pearname}-%{version}/TODO
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml

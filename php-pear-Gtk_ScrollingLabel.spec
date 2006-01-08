%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	ScrollingLabel
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - A scrolling label for PHP-Gtk
Summary(pl):	%{_pearname} - Przesuwaj±ca siê etykieta dla PHP-Gtk
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	408af13927cc3fad18505c75561dadc9
URL:		http://pear.php.net/package/Gtk_ScrollingLabel/
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
Requires:	php4-gtk
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a class to encapsulate the functionality needed for a
scrolling GTK+ label. This class provides a simple, easy to understand
API for setting up and controlling the label. It allows for the
ability to scroll in either direction, start and stop the scroll,
pause and unpause the scroll, get and set the text, and set display
properties of the text.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa zawiera funkcjonalno¶æ potrzebn± dla przewijaj±cej siê
etykiety w GTK+. Dostarcza proste, ³atwe do zrozumienia API do
ustawiania i kontrolowania etykiety. Daje mo¿liwo¶æ przewijania w
dowolnym kierunku, w³±czania, wy³±czania, zatrzymywania i wznawiania
przewijania, pobierania i ustawiania tekstu oraz ustawiania
w³a¶ciwo¶ci wy¶wietlania tekstu.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

sed -i -e 's,ScrollingLabel.php,%{_class}/ScrollingLabel.php,' ./%{php_pear_dir}/tests/%{_pearname}/*.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

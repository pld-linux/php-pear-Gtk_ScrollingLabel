%include	/usr/lib/rpm/macros.php
%define         _class          Gtk
%define         _subclass       ScrollingLabel
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - A scrolling label for PHP-Gtk
Summary(pl):	%{_pearname} - Przesuwaj±ca siê etykieta dla PHP-Gtk
Name:		php-pear-%{_pearname}
Version:	0.3.0
%define _suf	beta1
Release:	0.%{_suf}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_suf}.tgz
# Source0-md5:	e77d7734079fce530958a1f31d697f93
URL:		http://pear.php.net/package/Gtk_ScrollingLabel/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a class to encapsulate the functionality needed for a
scrolling gtk label. This class provides a simple, easy to understand
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}%{_suf}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_suf}/docs
%{php_pear_dir}/%{_class}/*.php

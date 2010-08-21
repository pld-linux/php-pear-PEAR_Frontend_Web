%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Frontend
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Web
Summary:	%{_pearname} - HTML (Web) PEAR package manager
Summary(pl.UTF-8):	%{_pearname} - HTML-owy zarządca pakietów PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.7.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ddf433c469571d5634b6c3d22f644fc9
URL:		http://pear.php.net/package/PEAR_Frontend_Web/
BuildRequires:	php-pear-PEAR >= 1:1.6.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_Template_IT
Requires:	php-pear-Net_UserAgent_Detect
Requires:	php-pear-PEAR >= 1:1.4.0-0.a1
Requires:	php-pear-PEAR-core >= 1:1.6.1
Provides:	pear(Frontend)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web interface to the PEAR package manager. Needed only when you want
to use PEAR from their CVS.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs HTML-owy (WWW) do zarządcy pakietów PEAR-a. Potrzebny tylko,
jeżeli chcesz używać PEAR-a z ich CVS-u.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/docs/*
%{php_pear_dir}/pearfrontendweb.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/Command/*
%{php_pear_dir}/%{_class}/%{_subclass}/*
%{php_pear_dir}/data/%{_pearname}

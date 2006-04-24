%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Frontend
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_Web

Summary:	%{_pearname} - HTML (Web) PEAR package manager
Summary(pl):	%{_pearname} - HTML-owy zarz±dca pakietów PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d469f82a95b644898ea4a9536ca97c45
URL:		http://pear.php.net/package/PEAR_Frontend_Web/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.0-0.a1
Requires:	php-pear-Net_UserAgent_Detect
Requires:	php-pear-HTML_Template_IT
Provides:	pear(Frontend)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web interface to the PEAR package manager. Needed only when you want
to use PEAR from their CVS.

In PEAR status of this package is: %{_status}.

%description -l pl
Interfejs HTML-owy (WWW) do zarz±dcy pakietów PEAR-a. Potrzebny tylko,
je¿eli chcesz u¿ywaæ PEAR-a z ich CVS-u.

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
%doc install.log
%doc docs/%{_pearname}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Web
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
# FIXME: to data/ directory?
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.png
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.gif
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.jpg
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.html
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.css
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.js

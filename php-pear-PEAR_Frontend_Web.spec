%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Frontend
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Web

Summary:	%{_pearname} - HTML (Web) PEAR package manager
Summary(pl):	%{_pearname} - HTML-owy zarz±dca pakietów PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7d90c55962a7760ef7b7834a6d4338aa
URL:		http://pear.php.net/package/PEAR_Frontend_Web/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Provides:	pear(Frontend)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web interface to the PEAR package manager. Needed only when you want
to use PEAR from their CVS.

In PEAR status of this package is: %{_status}.

%description -l pl
HTML-owy (webowy) interfejs do zarz±dcy pakietów PEAR-a. Potrzebny
tylko, je¿eli chcesz u¿ywaæ PEAR-a z ich CVS-u.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Web

install %{_pearname}-%{version}/WebInstaller.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/Web.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Web/*.png $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.gif $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.html $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.js $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Web

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Web
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.png
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.gif
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.html
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.css
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.js

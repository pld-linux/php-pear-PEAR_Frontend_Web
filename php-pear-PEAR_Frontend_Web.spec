%include	/usr/lib/rpm/macros.php
%define         _class          PEAR
%define         _subclass       Frontend
%define		_pearname	%{_class}_%{_subclass}_Web
Summary:	%{_pearname} - HTML (Web) PEAR Package Manager
Summary(pl):	%{_pearname} - HTML-owy menad¿er pakietów PEAR-a
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
#Provides:	pear(Frontend)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web Interface to the PEAR Package Manager.

%description -l pl
HTML-owy (webowy) interfejs do menad¿era pakietów PEAR-a.

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
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Web
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.png
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.gif
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.html
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.css
%{php_pear_dir}/%{_class}/%{_subclass}/Web/*.js

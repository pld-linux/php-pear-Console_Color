%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Color
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - easily use ANSI console colors in your application
Summary(pl.UTF-8):	%{_pearname} - łatwe użycie kolorów ANSI w aplikacjach
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	2
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8fe454cb9d04b2bbe40bf06626217839
URL:		http://pear.php.net/package/Console_Color/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can use Console_Color::convert to transform colorcodes like %r
into ANSI control codes. 'print Console_Color::convert("%rHello
World!%n");' would print "Hello World" in red, for example.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Console_Color::convert można używać do przekształcania kodów kolorów
typu %r na kody sterujące ANSI. Na przykład 'print
Console_Color::convert("%rHello World!%n");' wypisze "Hello World" na
czerwono.

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
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

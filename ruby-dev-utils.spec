Summary:	Tools to aid Ruby development
Summary(pl):	Narzêdzia pomagaj±ce przy programowaniu w jêzyku Ruby
Name:		ruby-dev-utils
Version:	1.0.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1678/dev-utils-%{version}.tgz
# Source0-md5:	4869bdb1d0f72ab015110797e691a530
URL:		http://dev-utils.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%ruby_mod_ver_requires_eq
Requires:	ruby-extensions
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dev-utils provides utilites to assist the process of developing Ruby
programs. At the moment, the target areas are debugging and unit
testing (planned).

%description -l pl
Pakiet dev-utils dostarcza narzêdzia pomagaj±ce przy procesie
tworzenia programów w jêzyku Ruby. Aktualnie docelowe obszary to
odpluskwianie i testy jednostkowe (planowane).

%prep
%setup -q -n dev-utils-%{version}

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README.txt README.txt lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/dev-utils
%{ruby_ridir}/DevUtils

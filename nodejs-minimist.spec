%{?scl:%scl_package nodejs-minimist}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

# sometimes you might need to disable tests to get it to build since tap
# depends on this
%global enable_tests 0

Name:           %{?scl_prefix}nodejs-minimist
Version:        0.0.8
Release:        2%{?dist}
Summary:        Parse argument options in Node.js

Group:          System Environment/Libraries
License:        MIT
URL:            http://github.com/substack/minimist
Source0:        http://registry.npmjs.org/minimist/-/minimist-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

#BuildRequires:  %{?scl_prefix}

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tap)
BuildRequires:  %{?scl_prefix}npm(tape)
%endif

%description
%{summary}.

This module is the guts of nodejs-optimist's argument parser without all the 
fanciful decoration.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/minimist
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/minimist

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
%tap test/*.js
%endif

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/minimist
%doc LICENSE readme.markdown example

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.8-2
- rebuilt

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-4
- New upstream release 0.0.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-2
- update to new nodejs standards

* Mon Aug 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-1
- initial package

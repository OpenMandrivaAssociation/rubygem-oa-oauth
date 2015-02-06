%define oname oa-oauth

Name:       rubygem-%{oname}
Version:    0.0.1
Release:    2
Summary:    OAuth strategies for OmniAuth
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/intridea/omniauth
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Suggests:   rubygem(rspec)
Suggests:   rubygem(webmock)
Suggests:   rubygem(rack-test)
Suggests:   rubygem(mg)
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{oname}) = %{version}

%description
OAuth strategies for OmniAuth.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/*.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.0.1-1mdv2011.0
+ Revision: 623522
- import rubygem-oa-oauth


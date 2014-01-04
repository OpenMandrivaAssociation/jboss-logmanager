%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logmanager
Version:          1.5.1
Release:          1.0%{?dist}
Summary:          JBoss Log Manager
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logmanager
Source0:          https://github.com/jboss-logging/jboss-logmanager/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    testng
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    qdox
BuildRequires:    jboss-modules
BuildRequires:    jboss-parent

%description
This package contains the JBoss Log Manager

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logmanager-%{namedversion}

# We won't run on JDK 6
%pom_remove_plugin "org.jboss.seven2six:seven2six"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING.txt

%changelog
* Tue Sep 10 2013 Marek Goldmann <mgoldman@redhat.com> - 1.5.1-1
- Upstream release 1.5.1.Final

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Marek Goldmann <mgoldman@redhat.com> - 1.4.1-1
- Upstream release 1.4.1.Final

* Mon Jun 03 2013 Marek Goldmann <mgoldman@redhat.com> - 1.3.0-1
- Upstream release 1.3.0.Final
- New guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.2-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.2.2-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Marek Goldmann <mgoldman@redhat.com> 1.2.2-1
- Upstream release 1.2.2.GA
- Cleanup in spec file
- Relocated jars to _javadir

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Marek Goldmann <mgoldman@redhat.com> 1.2.0-1
- Initial packaging


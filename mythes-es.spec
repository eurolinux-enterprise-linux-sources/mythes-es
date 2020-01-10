Name: mythes-es
Summary: Spanish thesaurus
%define upstreamid 20130102
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://openthes-es.berlios.de/download/OOo2-thes_es_ES.tar.bz2
Group: Applications/Text
URL: http://openthes-es.berlios.de
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
Requires: mythes

%description
Spanish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_es_ES_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_es_ES_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
es_ES_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_ES_aliases; do
        ln -s th_es_ES_v2.dat "th_"$lang"_v2.dat"
        ln -s th_es_ES_v2.idx "th_"$lang"_v2.idx"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_es_ES_v2.txt COPYING
%{_datadir}/mythes/*

%changelog
* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20130102-1
- Resolves: rhbz#905972 latest version

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120902-1
- latest version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120602-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120602-1
- latest version

* Wed Apr 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120402-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20111002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20111002-1
- latest version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101002-1
- latest version

* Fri Sep 24 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100902-1
- latest version

* Fri Jul 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100701-1
- latest version

* Sat Jun 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100601-1
- latest version

* Tue Apr 06 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100401-3
- add COPYING to doc

* Sat Apr 03 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100401-2
- mythes now owns /usr/share/mythes

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100401-1
- latest version

* Mon Mar 01 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100301-1
- latest version

* Tue Feb 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100201-1
- latest version

* Thu Dec 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091217-1
- latest version

* Tue Nov 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091117-1
- latest version

* Tue Sep 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090908-1
- latest version

* Sat Aug 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090808-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090708-2
- tidy spec

* Wed Jul 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Mon Apr 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090406-1
- latest version

* Fri Mar 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090306-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090206-1
- initial version

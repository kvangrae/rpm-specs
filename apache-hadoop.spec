Name: apache-hadoop
Version: 0.20.2
Release: el5
Summary: Apache Hadoop
License: Apache License Version 2.0
Group: Networking/Daemons
URL: http://hadoop.apache.org
Source0: http://apache.cs.utah.edu//hadoop/common/hadoop-%{version}/hadoop-%{version}.tar.gz
Source1: http://mirror.nyi.net/apache//hadoop/common/hadoop-%{version}/hadoop-%{version}.tar.gz
Source2: http://www.reverse.net/pub/apache//hadoop/common/hadoop-%{version}/hadoop-%{version}.tar.gz
Requires: ssh, rsync
AutoReq: yes
AutoProv: yes
BuildArch: noarch

%description
The Apache™ Hadoop™ project develops open-source software for reliable, scalable, distributed computing.

The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using a simple programming model. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-avaiability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-availabile service on top of a cluster of computers, each of which may be prone to failures.

%prep
%setup -q -n hadoop-0.20.2
exit 0

%build
exit 0

%install
install -d %{_rpmdir}/noarch
install -d %{_srcrpmdir}/noarch

# /etc/hadoop
install -d $RPM_BUILD_ROOT/etc
mv $RPM_BUILD_DIR/hadoop-%{version}/conf $RPM_BUILD_ROOT/etc/hadoop

# /usr/bin
install -d $RPM_BUILD_ROOT/usr/bin
cp $RPM_BUILD_DIR/hadoop-%{version}/bin/hadoop $RPM_BUILD_ROOT/usr/bin/

# /usr/share/hadoop-%{version}
install -d $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_DIR/hadoop-%{version} $RPM_BUILD_ROOT/usr/share/hadoop-%{version}

# /var/log/hadoop
install -d $RPM_BUILD_ROOT/var/log/hadoop
exit 0

%files
%defattr(0400,hadoop,hadoop,0500)
%attr(600,hadoop,hadoop) %config(noreplace) /etc/hadoop/*
%attr(500,hadoop,hadoop) /usr/bin/hadoop
%attr(500,hadoop,hadoop) /usr/share/hadoop-%{version}/bin/*
/usr/share/hadoop-%{version}/c++
/usr/share/hadoop-%{version}/contrib
/usr/share/hadoop-%{version}/ivy
/usr/share/hadoop-%{version}/lib
/usr/share/hadoop-%{version}/librecordio
/usr/share/hadoop-%{version}/src
/usr/share/hadoop-%{version}/webapps
/usr/share/hadoop-%{version}/*.xml
/usr/share/hadoop-%{version}/*.jar
%doc /usr/share/hadoop-%{version}/*.txt
%doc /usr/share/hadoop-%{version}/docs
%attr(700,hadoop,hadoop) /var/log/hadoop

%clean
rm -rf $RPM_BUILD_ROOT
exit 0

%pre
getent passwd hadoop > /dev/null || useradd -r -d /usr/share/hadoop hadoop
getent group hadoop > /dev/null || groupadd -r hadoop

%post
ln -s /usr/share/hadoop-%{version} /usr/share/hadoop
ln -s /etc/hadoop /usr/share/hadoop-%{version}/conf
ln -s /var/log/hadoop /usr/share/hadoop-%{version}/logs

%preun
rm /usr/share/hadoop
rm /usr/share/hadoop-%{version}/conf
rm /usr/share/hadoop-%{version}/logs

%postun

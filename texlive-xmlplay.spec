# revision 15878
# category Package
# catalog-ctan undef
# catalog-date 2006-12-16 17:11:43 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-xmlplay
Version:	20061216
Release:	5
Summary:	Typeset Shakespeare's plays as marked up by Bosak
Group:		Publishing
URL:		http://tug.org/texlive
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmlplay.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmlplay.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmlplay.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an xmltex package for typsetting the plays of
Shakespeare, as marked up by Jon Bosak.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xmltex/xmlplay/play.xmt
%doc %{_texmfdistdir}/doc/otherformats/xmltex/xmlplay/readme
#- source
%doc %{_texmfdistdir}/source/xmltex/xmlplay/play.dtd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061216-2
+ Revision: 757663
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061216-1
+ Revision: 719944
- texlive-xmlplay
- texlive-xmlplay
- texlive-xmlplay


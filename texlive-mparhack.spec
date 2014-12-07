# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mparhack
# catalog-date 2006-10-22 16:45:29 +0200
# catalog-license gpl
# catalog-version 1.4
Name:		texlive-mparhack
Version:	1.4
Release:	9
Summary:	A workaround for a LaTeX bug in marginpars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mparhack
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Implements a workaround for the LaTeX bug that marginpars will
sometimes come out at the wrong margin.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mparhack/mparhack.sty
%doc %{_texmfdistdir}/doc/latex/mparhack/README
%doc %{_texmfdistdir}/doc/latex/mparhack/mparhack.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mparhack/mparhack.dtx
%doc %{_texmfdistdir}/source/latex/mparhack/mparhack.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 754113
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 719067
- texlive-mparhack
- texlive-mparhack
- texlive-mparhack
- texlive-mparhack


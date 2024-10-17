Name:		texlive-mparhack
Version:	59066
Release:	2
Summary:	A workaround for a LaTeX bug in marginpars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mparhack
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/mparhack
%doc %{_texmfdistdir}/doc/latex/mparhack
#- source
%doc %{_texmfdistdir}/source/latex/mparhack

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

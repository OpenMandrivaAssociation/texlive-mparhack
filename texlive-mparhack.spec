%global tl_name mparhack
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Work around a LaTeX bug in marginpars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mparhack
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mparhack.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Works around the LaTeX bug that marginpars will sometimes come out at
the wrong margin.


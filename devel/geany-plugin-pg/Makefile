# $FreeBSD$

PORTNAME=	geany-plugin-pg
PORTVERSION=	${GEANY_VER}
PORTREVISION=	2
CATEGORIES=	devel

MAINTAINER=	makc@FreeBSD.org
COMMENT=	Geany plugin: ${${GEANY_PLUGIN}_DESC}

LIB_DEPENDS=	libgpgme.so:${PORTSDIR}/security/gpgme
RUN_DEPENDS=	gpg2:${PORTSDIR}/security/gnupg

.include "${.CURDIR}/../geany-plugins/files/Makefile.common"
.include <bsd.port.mk>

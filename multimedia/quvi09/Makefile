# Created by: Toni Gundogdu <legatvs@gmail.com>
# $FreeBSD$

PORTNAME=	quvi
PORTVERSION=	0.9.5
CATEGORIES=	multimedia devel
MASTER_SITES=	SF/${PORTNAME}/${PORTVERSION:R}/${PORTNAME}/ \
		GOOGLE_CODE
PKGNAMESUFFIX=	09

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Command line tool for parsing flash media stream URLs

LICENSE=	AGPLv3

BUILD_DEPENDS=	libquvi09>=0.9:${PORTSDIR}/multimedia/libquvi09
LIB_DEPENDS=	libcurl.so:${PORTSDIR}/ftp/curl
RUN_DEPENDS:=	${BUILD_DEPENDS}

CONFIGURE_ARGS=	--program-suffix=${PKGNAMESUFFIX}
GNU_CONFIGURE=	yes
USES=		pkgconfig tar:xz

PLIST_SUB=	PKGNAMESUFFIX=${PKGNAMESUFFIX}

.include <bsd.port.mk>

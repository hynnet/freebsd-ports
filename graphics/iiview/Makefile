# Created by: Martin Sugioarto <martin.sugioarto@udo.edu>
# $FreeBSD$

PORTNAME=	iiview
PORTVERSION=	0.31
CATEGORIES=	graphics
MASTER_SITES=	https://github.com/${GH_ACCOUNT}/${PORTNAME}/archive/
DISTNAME=	v${PORTVERSION}
DIST_SUBDIR=	${PORTNAME}

MAINTAINER=	martin.sugioarto@udo.edu
COMMENT=	Thumb viewer application

LICENSE=	BSD2CLAUSE

BUILD_DEPENDS=	${LOCALBASE}/lib/libpng.a:${PORTSDIR}/graphics/png \
		${LOCALBASE}/lib/libtiff.a:${PORTSDIR}/graphics/tiff \
		${LOCALBASE}/lib/libjpeg.a:${PORTSDIR}/graphics/jpeg

USE_XORG=	xpm x11

GH_ACCOUNT=	nakal
WRKSRC=		${WRKDIR}/iiview-${PORTVERSION}

PLIST_FILES=	bin/iiview man/man1/iiview.1.gz

MAKE_JOBS_UNSAFE=	yes

.include <bsd.port.mk>

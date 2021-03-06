# Created by: Denis Barov <dindin@dindin.ru>
# $FreeBSD$

PORTNAME=	lensfun
PORTVERSION=	0.2.8
PORTREVISION=	1
CATEGORIES=	graphics
MASTER_SITES=	SF/${PORTNAME}/${PORTVERSION}

MAINTAINER=	danfe@FreeBSD.org
COMMENT=	Library for fixing lens geometry distortions

LICENSE=	LGPL3

LIB_DEPENDS=	libpng.so:${PORTSDIR}/graphics/png

USES=		gmake pkgconfig python:build tar:bzip2
USE_GNOME=	glib20
USE_LDCONFIG=	yes

HAS_CONFIGURE=	yes
CONFIGURE_ENV=	LD="${CXX}" AR="${AR}"
CONFIGURE_ARGS=	--prefix=${PREFIX} --target=${TARGET} --vectorization=SSE
MAKE_ARGS=	V=1	# we want to know what's going on during the build
MAKEFILE=	GNUmakefile
LIBVERSION=	2

PLIST_SUB+=	LIBVERSION=${LIBVERSION}

post-patch: .SILENT
	${REINPLACE_CMD} -e '1s|#!/usr/bin/python|#!${PYTHON_CMD}|' \
		-e 's|make --version|g&|' -e '/DOXYGEN/d' \
		-e '/GNU Make/d' ${WRKSRC}/configure
	${REINPLACE_CMD} -e \
		's|CONF_LIBDIR)pkgconfig|CONF_LIBDIR)../libdata/pkgconfig|' \
			${WRKSRC}/build/tibs/compiler/pkgconfig.mak
	${REINPLACE_CMD} -e '/-s -O3/d' \
		${WRKSRC}/build/tibs/compiler/gcc.mak
	${REINPLACE_CMD} -e '/GROUPS/s| DOCS||' ${WRKSRC}/build/tibs/rules.mak

post-install:
	${LN} -sf lib${PORTNAME}.so \
		${STAGEDIR}${PREFIX}/lib/lib${PORTNAME}.so.${LIBVERSION}

.include <bsd.port.mk>

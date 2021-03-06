# Created by: Mikhail Teterin <mi@aldan.algebra.com>
# $FreeBSD$

PORTNAME=	lcms
PORTVERSION=	1.19
PORTREVISION=	5
PORTEPOCH=	1
CATEGORIES=	graphics
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${PORTVERSION} \
		http://www.littlecms.com/

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Light Color Management System -- a color management library

LICENSE=	MIT

OPTIONS_DEFINE=	DOCS JPEGICC TIFFICC
OPTIONS_DEFAULT=JPEGICC TIFFICC
OPTIONS_SUB=	yes
JPEGICC_DESC=	Build color profile applier for JPEG
TIFFICC_DESC=	Build color profile applier for TIFF

CPPFLAGS+=	-I${LOCALBASE}/include
GNU_CONFIGURE=	yes
INSTALL_TARGET=	install-strip
LDFLAGS+=	-L${LOCALBASE}/lib
USE_LDCONFIG=	yes
USES=		libtool:keepla pathfix

PORTDOCS=	*

JPEGICC_CONFIGURE_OFF=	--without-jpeg
JPEGICC_CONFIGURE_ON=	--with-jpeg=${LOCALBASE}
JPEGICC_LIB_DEPENDS=	libjpeg.so:${PORTSDIR}/graphics/jpeg
TIFFICC_CONFIGURE_OFF=	--without-tiff
TIFFICC_CONFIGURE_ON=	--with-tiff=${LOCALBASE}
TIFFICC_LIB_DEPENDS=	libtiff.so:${PORTSDIR}/graphics/tiff

post-patch:
	@${REINPLACE_CMD} -e '/^SUBDIRS = / s| python samples||' ${WRKSRC}/Makefile.in
	@${REINPLACE_CMD} -e '/^#ifdef __sgi/ s|__sgi|__unix__|; /^#include "sgidefs.h"/d' ${WRKSRC}/include/icc34.h.in
	@${REINPLACE_CMD} -e '/^testcms_LDFLAGS = / s|$$| -static|' ${WRKSRC}/testbed/Makefile.in

post-install:
	${MKDIR} ${STAGEDIR}${DOCSDIR}/
	cd ${WRKSRC}/ && ${INSTALL_DATA} doc/LCMSAPI.TXT doc/TUTORIAL.TXT tifficc/tifficc.c \
		jpegicc/jpegicc.c jpegicc/iccjpeg.c samples/wtpt.c samples/icctrans.c ${STAGEDIR}${DOCSDIR}/

regression-test test: build
	cd ${WRKSRC}/testbed/ && ${SETENV} ${MAKE_ENV} ${MAKE_CMD} check

.include <bsd.port.mk>

# Created by: Zach Zurflu <zach@pabst.bendnet.com>
# $FreeBSD$

PORTNAME=	libshout
PORTVERSION=	2.3.1
CATEGORIES=	audio net
MASTER_SITES=	http://downloads.xiph.org/releases/${PORTNAME}/ \
		LOCAL/sunpoet

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Connect and transmit data to an Icecast media streaming server

LICENSE=	LGPL20

LIB_DEPENDS=	libspeex.so:${PORTSDIR}/audio/speex \
		libtheora.so:${PORTSDIR}/multimedia/libtheora \
		libvorbis.so:${PORTSDIR}/audio/libvorbis

CONFLICTS=	libshout2-[0-9]*

OPTIONS_DEFINE=	DOCS

GNU_CONFIGURE=	yes
INSTALL_TARGET=	install-strip
USE_LDCONFIG=	yes
USES=		gmake libtool pathfix pkgconfig

PORTDOCS=	*

post-patch:
	@${REINPLACE_CMD} -e 's|-ffast-math||g' ${WRKSRC}/configure
	@${REINPLACE_CMD} -e 's|^Requires: |Requires.private: |' ${WRKSRC}/shout.pc.in
	@${REINPLACE_CMD} -e '/^AM_CPPFLAGS = / s|^\(.*\) \(@XIPH_CPPFLAGS@\) \(.*\)$$|\1 \3 \2|' ${WRKSRC}/examples/Makefile.in
	@${REINPLACE_CMD} -e 's|#ifdef IPV6_V6ONLY|#if defined(__BSD_VISIBLE) \&\& defined(IPV6_V6ONLY)|' ${WRKSRC}/src/net/sock.c

.include <bsd.port.mk>

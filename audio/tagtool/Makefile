# Created by: Anthony Ginepro <anthony.ginepro@laposte.net>
# $FreeBSD$
#    $MCom: ports/audio/tagtool/Makefile,v 1.1 2006/09/30 01:15:37 ahze Exp $

PORTNAME=	tagtool
PORTVERSION=	0.12.3
PORTREVISION=	12
CATEGORIES=	audio
MASTER_SITES=	SF

MAINTAINER=	ports@FreeBSD.org
COMMENT=	GNOME MP3/Ogg file tagger

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libid3.so:${PORTSDIR}/audio/id3lib \
		libvorbis.so:${PORTSDIR}/audio/libvorbis

USES=		tar:bzip2 gettext gmake pathfix pkgconfig
USE_GNOME=	intlhack libglade2
GNU_CONFIGURE=	yes
INSTALLS_ICONS=	yes

CPPFLAGS+=	-I${LOCALBASE}/include ${PTHREAD_CFLAGS}
LDFLAGS+=	-L${LOCALBASE}/lib ${PTHREAD_LIBS} -logg -lm

post-patch:
	@${FIND} ${WRKSRC} -name "Makefile.in" | ${XARGS} ${REINPLACE_CMD} -e \
		's|-Wno-pointer-sign||g'

.include <bsd.port.mk>

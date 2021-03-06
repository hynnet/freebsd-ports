# $FreeBSD$

PORTNAME=	libva
PORTVERSION=	1.5.0
CATEGORIES=	multimedia
MASTER_SITES=	http://cgit.freedesktop.org/${PORTNAME}/snapshot/

MAINTAINER=	madpilot@FreeBSD.org
COMMENT=	VAAPI wrapper and dummy driver

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	${LOCALBASE}/include/linux/videodev2.h:${PORTSDIR}/multimedia/v4l_compat
LIB_DEPENDS=	libdrm.so:${PORTSDIR}/graphics/libdrm

USES=		alias autoreconf gmake libtool pkgconfig tar:bzip2
USE_XORG=	glproto pciaccess xext xfixes
USE_GL=		gl
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--program-prefix=va
USE_LDCONFIG=	yes

LDFLAGS+=	-L${LOCALBASE}/lib
# prevent types conflict: videodev2.h vs. drm.h
CFLAGS+=	-I${LOCALBASE}/include -DHAVE_LINUX_INTEGER_TYPES

OPTIONS_DEFINE=	DEBUG

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MDEBUG}
CFLAGS+=	-D_DEBUG
.else
CFLAGS+=	-DNDEBUG
.endif

.include <bsd.port.pre.mk>

.if ${ARCH} == "sparc64"
BROKEN=		glXCreateContext fails during configure
.endif

.if defined(STRIP) && ${STRIP} != ""
INSTALL_TARGET=	install-strip
.endif

post-patch:	.SILENT
	${REINPLACE_CMD} -e 's|\($$libdir\)/dri|\1/va|' \
		-e 's|$${libdir}/\(pkgconfig\)|${PREFIX}/libdata/\1|' \
		${WRKSRC}/configure.ac
	${REINPLACE_CMD} -e 's/va\(info\)/\1/g' -e 's/info\.c/vainfo\.c/' \
		${WRKSRC}/test/vainfo/Makefile.am
	${REINPLACE_CMD} '/^export VA_HEADER_/d' \
		${WRKSRC}/doc/Makefile.am
	${REINPLACE_CMD} 's/-ldl//' ${WRKSRC}/va/Makefile.am

post-configure:	.SILENT
	${REINPLACE_CMD} 's/-lpthread/${PTHREAD_LIBS}/' \
		${WRKSRC}/test/putsurface/Makefile

.include <bsd.port.post.mk>

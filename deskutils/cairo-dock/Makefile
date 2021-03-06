# $FreeBSD$

PORTNAME=	cairo-dock
PORTVERSION=	3.4.0
CATEGORIES=	deskutils
DISTNAME=	${PORTNAME}-core-${PORTVERSION}.git20141115

MAINTAINER=	fidaj@ukr.net
COMMENT=	Cairo-Dock is a light and eye-candy dock

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libcairo.so:${PORTSDIR}/graphics/cairo \
		libcurl.so:${PORTSDIR}/ftp/curl \
		libdbus-glib-1.so:${PORTSDIR}/devel/dbus-glib \
		libgtkglext-x11-1.0.so:${PORTSDIR}/x11-toolkits/gtkglext
RUN_DEPENDS=	bash:${PORTSDIR}/shells/bash \
		sox:${PORTSDIR}/audio/sox

USE_GITHUB=	yes
GH_ACCOUNT=	Cairo-Dock
GH_PROJECT=	${PORTNAME}-core
GH_COMMIT=	18df440
GH_TAGNAME=	18df440

WRKSRC=		${WRKDIR}/${GH_ACCOUNT}-${PORTNAME}-core-${GH_COMMIT}

GNU_CONFIGURE=	yes
USE_GNOME=	glib20 gtk30 librsvg2 libxml2
USE_LDCONFIG=	yes
USE_XORG=	xrender xtst
USES=		cmake gettext pathfix pkgconfig
LDFLAGS+=	-L${LOCALBASE}/lib
CMAKE_ARGS+=	-Dinstall-pc-path:STRING="${LOCALBASE}/libdata/pkgconfig"
CMAKE_ARGS+=	-DROOT_PREFIX:PATH=${STAGEDIR}
CMAKE_ARGS+=	-DCMAKE_INSTALL_MANDIR:PATH=man

post-patch:
	@${FIND} ${WRKSRC} -type f -name "*" | ${XARGS} ${REINPLACE_CMD} -e \
	    's|/usr/share/pixmaps/|${LOCALBASE}/share/pixmaps/|g; \
	     s|/usr/bin/cairo-dock|${LOCALBASE}/bin/cairo-dock|g; \
	     s|/bin/bash|${LOCALBASE}/bin/bash|g; \
	     s|/usr/share/applications|${LOCALBASE}/share/applications|g; \
	     s|/usr/share/icons|${LOCALBASE}/share/icons|g; \
	     s|%%LOCALBASE%%|${LOCALBASE}|g;'

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/libgldi.so.3.4.0

.include <bsd.port.mk>

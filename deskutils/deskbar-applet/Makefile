# Created by: Michael Johnson <ahze@FreeBSD.org>
# $FreeBSD$
#   $MCom: ports/deskutils/deskbar-applet/Makefile,v 1.116 2010/09/27 19:36:13 kwm Exp $

PORTNAME=	deskbar-applet
PORTVERSION=	2.32.0
PORTREVISION=	6
CATEGORIES=	deskutils gnome
MASTER_SITES=	GNOME
DIST_SUBDIR=	gnome2

MAINTAINER=	gnome@FreeBSD.org
COMMENT=	Omnipresent versatile search interface

BROKEN=		Uses unknown GNOME components pygnomedesktop and evolutiondataserver

BUILD_DEPENDS=	${PYTHON_SITELIBDIR}/dbus/__init__.py:${PORTSDIR}/devel/py-dbus
RUN_DEPENDS=	${PYTHON_SITELIBDIR}/dbus/__init__.py:${PORTSDIR}/devel/py-dbus

USES=		gettext gmake libtool pathfix pkgconfig python tar:bzip2
USE_GNOME=	gnomeprefix pygnomedesktop intlhack
GNU_CONFIGURE=	yes
INSTALLS_ICONS=	yes
INSTALLS_OMF=	yes
INSTALL_TARGET=	install-strip
CPPFLAGS+=	-I${LOCALBASE}/include
LIBS+=		-L${LOCALBASE}/lib

GCONF_SCHEMAS=	deskbar-applet.schemas

OPTIONS_DEFINE=	EVO
OPTIONS_DEFAULT=EVO
EVO_DESC=	Enable evolution support

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MEVO}
USE_GNOME+=	evolutiondataserver
PLIST_SUB+=	EVO=""
.else
CONFIGURE_ARGS+=--disable-evolution
PLIST_SUB+=	EVO="@comment "
.endif

post-patch:
	@${REINPLACE_CMD} -e 's|/usr/local|${LOCALBASE}|g ; \
		s|%%LOCALBASE%%|${LOCALBASE}|g' \
		${WRKSRC}/deskbar/handlers/mozilla.py \
		${WRKSRC}/deskbar/core/Utils.py
	@${REINPLACE_CMD} -e 's|<glib/g.*\.h>|<glib.h>|g' \
		${WRKSRC}/deskbar/handlers/evolution/evolution.[ch]

.include <bsd.port.mk>

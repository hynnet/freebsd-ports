# Created by: James Earl <jdearl@telus.net>
# $FreeBSD$

PORTNAME=	xfce4-panel
PORTVERSION=	4.10.1
PORTREVISION=	3
CATEGORIES=	x11-wm xfce
MASTER_SITES=	${MASTER_SITE_XFCE}
MASTER_SITE_SUBDIR=	src/xfce/${PORTNAME}/${PORTVERSION:R}
DIST_SUBDIR=	xfce4

MAINTAINER=	xfce@FreeBSD.org
COMMENT=	Xfce's panel

LICENSE=	GPLv2 LGPL21
LICENSE_COMB=	multi
LICENSE_DISTFILES=	${WRKSRC}/COPYING \
	${WRKSRC}/COPYING.LIB

LIB_DEPENDS=	libcairo.so:${PORTSDIR}/graphics/cairo \
		libdbus-glib-1.so:${PORTSDIR}/devel/dbus-glib

USES=		desktop-file-utils gmake libtool:keepla pathfix perl5 \
		pkgconfig tar:bzip2
GNU_CONFIGURE=	yes
INSTALLS_ICONS=	yes
USE_GNOME=	glib20 gtk20 intltool intlhack libwnck
USE_LDCONFIG=	yes
USE_XFCE=	configenv garcon libexo libmenu libutil xfconf
USE_XORG=	x11 sm

CONFIGURE_ARGS+=--enable-gio-unix

OPTIONS_DEFINE=		NLS DOCS

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MNLS}
USES+=		gettext
CONFIGURE_ARGS+=--enable-nls
PLIST_SUB+=	NLS=""
.else
CONFIGURE_ARGS+=--disable-nls
PLIST_SUB+=	NLS="@comment "
.endif

.if ${PORT_OPTIONS:MDOCS}
CONFIGURE_ARGS+=--with-html-dir=${PREFIX}/share/gtk-doc/html
PLIST_SUB+=	APIDOCS=""
.else
CONFIGURE_ARGS+=--without-html-dir
PLIST_SUB+=	APIDOCS="@comment "
.endif

.include <bsd.port.mk>

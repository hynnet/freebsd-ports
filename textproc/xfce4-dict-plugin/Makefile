# Created by: Oliver Lehmann (oliver@FreeBSD.org)
# $FreeBSD$

PORTNAME=	xfce4-dict
PORTVERSION=	0.7.0
PORTREVISION=	1
CATEGORIES=	textproc xfce
MASTER_SITES=	${MASTER_SITE_XFCE}
MASTER_SITE_SUBDIR=	src/apps/${PORTNAME}/${PORTVERSION:R}
PKGNAMESUFFIX=	-plugin
DIST_SUBDIR=	xfce4

MAINTAINER=	xfce@FreeBSD.org
COMMENT=	Xfce4 plugin to query different dictionaries

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

GNU_CONFIGURE=	yes
INSTALLS_ICONS=	yes
USES=		gettext pkgconfig gmake libtool tar:bzip2
USE_GNOME=	glib20 gtk20 intltool intlhack
USE_XFCE=	configenv libmenu libutil panel
USE_XORG=	x11
USE_LDCONFIG=	yes

.include <bsd.port.mk>

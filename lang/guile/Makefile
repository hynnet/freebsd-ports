# Created by: jseger@FreeBSD.org
# $FreeBSD$
#    $MCom: ports/lang/guile/Makefile,v 1.1 2006/09/12 14:57:06 ahze Exp $

PORTNAME=	guile
PORTVERSION=	1.8.8
PORTREVISION=	2
CATEGORIES=	lang scheme
MASTER_SITES=	${MASTER_SITE_GNU}
MASTER_SITE_SUBDIR=	guile

MAINTAINER=	bofh@FreeBSD.org
COMMENT=	GNU Ubiquitous Intelligent Language for Extension

LICENSE=	LGPL21

LIB_DEPENDS=	libltdl.so:${PORTSDIR}/devel/libltdl \
		libgmp.so:${PORTSDIR}/math/gmp

CONFLICTS_INSTALL=	guile2-[0-9]*

USES=		gmake libtool makeinfo ncurses pathfix
USE_AUTOTOOLS=	autoheader
USE_LDCONFIG=	yes
GNU_CONFIGURE=	yes
CFLAGS+=	-fwrapv
CPPFLAGS+=	-I${LOCALBASE}/include
LIBS+=		-L${LOCALBASE}/lib
INSTALL_TARGET=	install-strip

PLIST_SUB=	GUILE_VER=${PORTVERSION:R}

REINPLACE_FILES=	libguile/smob.c libguile/filesys.c libguile/gc.c \
			libguile/mallocs.c libguile/eval.c libguile/gc-malloc.c \
			libguile/ports.c libguile/gc-mark.c libguile/gc_os_dep.c

INFO=		goops guile-tut guile r5rs

OPTIONS_DEFINE=	NLS
OPTIONS_SUB=	yes

NLS_CONFIGURE_ENABLE=	nls
NLS_USES=		gettext

post-extract:
	cd ${WRKSRC}; ${CHMOD} u+w ${REINPLACE_FILES}
	@${FIND} ${WRKSRC}/doc -name "*.info*" -delete

post-patch:
	@cd ${WRKSRC} ; \
	  ${REINPLACE_CMD} -e 's|<malloc\.h>|<stdlib.h>|g' ${REINPLACE_FILES}
	@${REINPLACE_CMD} -e 's|2.68|${AUTOCONF_VERSION}|g' ${WRKSRC}/aclocal.m4
	@${TOUCH} ${WRKSRC}/Makefile.in

.include <bsd.port.mk>

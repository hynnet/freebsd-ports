# Created by: Dirk-Willem van Gulik / dirkx@webweaving.org
# $FreeBSD$

PORTNAME=	widentd
PORTVERSION=	1.03
PORTREVISION=	2
CATEGORIES=	net ipv6
MASTER_SITES=	http://BSDforge.com/projects/source/net/widentd/

MAINTAINER=	dirkx@webweaving.org
COMMENT=	RFC1413 auth/identd daemon providing a fixed fake reply

LICENSE=	BSD3CLAUSE

USES=		uidfix tar:tgz
MAKE_ENV+=	BINDIR="${PREFIX}/sbin" MANDIR="${PREFIX}/man/man"

PLIST_FILES=	sbin/widentd \
		man/man8/widentd.8.gz
USE_RC_SUBR=	widentd

BROKEN_powerpc=		Does not compile on powerpc

.include <bsd.port.mk>
